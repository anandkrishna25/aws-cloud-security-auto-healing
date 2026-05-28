# AWS Cloud Security Auto-Healing Platform

A cloud-native AWS security monitoring and automated remediation platform built using AWS Organizations, CloudTrail, AWS Config, EventBridge, Lambda, SNS, Security Hub, and CloudWatch.

---

# Features

* Real-time threat detection
* Automated remediation
* IAM privilege escalation protection
* Public S3 exposure auto-healing
* Security Hub aggregation
* CloudWatch dashboards
* SNS alerting
* Event-driven security operations

---

# Services Used

* AWS Organizations
* AWS Config
* CloudTrail
* EventBridge
* AWS Lambda
* Amazon SNS
* Amazon CloudWatch
* AWS Security Hub
* IAM Access Analyzer

---

# Security Monitoring Capabilities

## Threat Detection

The platform continuously monitors AWS infrastructure for:

* Root account logins
* IAM privilege escalation attempts
* Public S3 bucket exposure
* CloudTrail tampering attempts
* IAM policy modifications
* Compliance violations

---

# Automated Remediation

## Public S3 Exposure Auto-Healing

When a bucket becomes publicly accessible:

1. AWS Config detects NON_COMPLIANT state
2. EventBridge rule triggers automatically
3. Lambda remediation function executes
4. Public bucket policy is removed
5. S3 Public Access Block is enabled
6. SNS alert notification is sent
7. AWS Config re-evaluates compliance

---

## IAM Privilege Escalation Protection

When AdministratorAccess policy is attached:

1. CloudTrail logs AttachUserPolicy event
2. EventBridge detects privilege escalation
3. Lambda remediation function executes
4. Unauthorized AdministratorAccess policy is detached
5. SNS critical alert is delivered
6. CloudWatch logs record remediation activity

---

# Incident Simulations

The platform supports controlled security incident simulations:

* Public S3 bucket exposure simulation
* IAM AdministratorAccess escalation simulation
* Root account login monitoring
* Security Hub finding aggregation testing

---

# Auto-Remediation Outcomes

* Removes public S3 exposure automatically
* Revokes unauthorized AdministratorAccess policies automatically
* Sends real-time SNS notifications
* Restores AWS Config compliance automatically
* Logs remediation activity in CloudWatch

---

# Dashboard & Security Monitoring

## CloudWatch Security Operations Dashboard

![Dashboard](screenshots/Cloud-dashboard.png)

---

## Security Hub Findings

![Security Hub](screenshots/security-hub-findings.png)

---

## EventBridge Detection Rules

![EventBridge](screenshots/eventbridge-rules.png)

---

## Lambda Auto-Remediation Logs

![Lambda Logs](screenshots/lambda-remediation-logs.png)

---

## SNS Critical Alert Notifications

![SNS Alerts](screenshots/sns-alerts.png)

---

# Architecture Diagram
![aws_cloud_security_architecture](https://github.com/user-attachments/assets/31693c9f-a0b1-49a1-be5d-9afdbe725ffc)


---

# Architecture Flow

```text
CloudTrail / AWS Config / Security Hub
                ↓
           EventBridge
                ↓
        Detection Rules
                ↓
        Lambda Remediation
                ↓
         SNS Notifications
                ↓
      CloudWatch Dashboard
```

---

# Cloud Security Workflow

## Detection Layer

* Organization-wide CloudTrail logging
* AWS Config compliance monitoring
* Security Hub findings aggregation
* CloudWatch metric filters

## Automation Layer

* EventBridge event pattern matching
* Lambda-based remediation
* Serverless security operations

## Alerting Layer

* SNS critical and high-priority alerts
* Email notification delivery
* Real-time incident visibility

## Governance Layer

* IAM least-privilege enforcement
* AWS Config managed rules
* Security compliance monitoring

---

# Security Outcomes

* Automated remediation of public S3 bucket exposure
* Real-time IAM privilege escalation detection
* Root account activity monitoring
* Centralized security findings aggregation
* Event-driven serverless remediation architecture
* Mean Time To Remediation (MTTR) reduced to under 60 seconds
* Real-time CloudWatch operational dashboard visibility

---

# Technical Highlights

* Built event-driven security automation using AWS EventBridge
* Developed Python-based Lambda remediation functions
* Implemented real-time CloudWatch metric filters and alarms
* Integrated Security Hub with centralized findings monitoring
* Designed automated security response workflows
* Simulated and validated real-world cloud security incidents

---

# Future Enhancements

* Slack and PagerDuty integrations
* Multi-account AWS Organizations deployment
* Terraform Infrastructure-as-Code automation
* SIEM integrations
* Automated incident ticketing workflows
* GuardDuty malware detection pipelines
* AWS Step Functions remediation orchestration
* Security analytics and reporting automation

---

# Resume Project Summary

AWS Cloud Security Monitoring & Auto-Healing Platform implementing real-time threat detection, compliance monitoring, event-driven alerting, and automated remediation using AWS CloudTrail, AWS Config, EventBridge, Lambda, SNS, Security Hub, and CloudWatch.

The platform automatically detects and remediates public S3 exposure and IAM privilege escalation incidents within seconds using serverless automation and event-driven security workflows.
