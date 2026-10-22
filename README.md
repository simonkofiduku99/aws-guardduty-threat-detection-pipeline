# AWS GuardDuty Automated Threat Detection Pipeline

Automated SOC pipeline that detects, routes, and alerts on AWS threats in real-time.

## Architecture
**GuardDuty (480 sample findings) -> EventBridge Rule (Enabled) -> Lambda `guardduty-response-function` + SNS -> Gmail + S3 Archiving**

- **Region:** us-east-1
- **Account:** 954328706940 (verified in logs)
- **Buckets:** `guardduty-logs-project5-954328706940-us-east-1-an`, `aws-cloudtrail-logs-...`

## Components
1. **GuardDuty** - Enabled, generated 480 sample findings (Trojan etc.)
2. **EventBridge** - Rule: `source: aws.guardduty`, `detail-type: GuardDuty Finding`, State: ENABLED
3. **Lambda** - `lambda_function.py` parses `detail.type`, `severity`, publishes to SNS
4. **SNS/Email** - Alert with finding JSON delivered to Gmail
5. **S3** - Archival bucket for logs

## Files
- `lambda_function.py` - Core processing logic
- `Eventbridge-rule.json` - Event pattern

## Screenshots
See `/screenshots` folder (or add them here) - Summary, Findings, EventBridge, Lambda, Email, S3

## Cost Control
Disabled GuardDuty detector after proof. Lambda, SNS, S3 free tier = $0.

Built: Oct 21, 2026
