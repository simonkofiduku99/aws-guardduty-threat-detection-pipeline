import json
import boto3
import os

sns_client = boto3.client('sns')
SNS_TOPIC_ARN = os.environ.get('SNS_TOPIC_ARN')

def lambda_handler(event, context):
    # EventBridge sends GuardDuty finding in event['detail']
    finding = event.get('detail', {})
    
    print(f"GuardDuty Finding ID: {finding.get('id')}")
    print(f"Type: {finding.get('type')}")
    print(f"Severity: {finding.get('severity')}")
    
    # Build alert message
    message = {
        "finding_type": finding.get('type'),
        "severity": finding.get('severity'),
        "account": event.get('account'),
        "region": event.get('region'),
        "description": finding.get('description')
    }
    
    # Send to SNS -> Email
    if SNS_TOPIC_ARN:
        sns_client.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject=f"GuardDuty Alert: {finding.get('type')}",
            Message=json.dumps(message, indent=2)
        )
    
    return {"statusCode": 200, "finding_processed": finding.get('id')}
