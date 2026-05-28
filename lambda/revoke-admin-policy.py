```python
import boto3
import logging
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

iam = boto3.client('iam')

def lambda_handler(event, context):

    logger.info(f"FULL EVENT: {json.dumps(event)}")

    try:
        detail = event['detail']

        user_name = detail['requestParameters']['userName']
        policy_arn = detail['requestParameters']['policyArn']

        iam.detach_user_policy(
            UserName=user_name,
            PolicyArn=policy_arn
        )

        logger.info(f"Detached admin policy from user: {user_name}")

        return {
            'statusCode': 200,
            'body': f'Removed {policy_arn} from {user_name}'
        }

    except Exception as e:
        logger.error(str(e), exc_info=True)
        raise
```
