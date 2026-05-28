# AWS Cloud Security Auto-Healing Platform

A cloud-native AWS security monitoring and automated remediation platform built using AWS Organizations, CloudTrail, AWS Config, EventBridge, Lambda, SNS, Security Hub, and CloudWatch.

## Features

- Real-time threat detection
- Automated remediation
- IAM privilege escalation protection
- Public S3 exposure auto-healing
- Security Hub aggregation
- CloudWatch dashboards
- SNS alerting
- Event-driven security operations

## Services Used

- AWS Organizations
- AWS Config
- CloudTrail
- EventBridge
- Lambda
- SNS
- CloudWatch
- Security Hub
- IAM Access Analyzer

## Incident Simulations

- Public S3 bucket exposure
- IAM AdministratorAccess escalation

## Auto-Remediation

- Removes public S3 exposure automatically
- Revokes unauthorized AdministratorAccess policies automatically
