```python
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client('s3')

def lambda_handler(event, context):

    logger.info(f"FULL EVENT: {event}")

    bucket = event['detail']['resourceId']

    try:
        # Remove public bucket policy if exists
        try:
            s3.delete_bucket_policy(Bucket=bucket)
            logger.info(f"Deleted bucket policy for: {bucket}")
        except Exception as e:
            logger.info(f"No bucket policy found or unable to delete: {str(e)}")

        # Enable S3 Public Access Block
        s3.put_public_access_block(
            Bucket=bucket,
            PublicAccessBlockConfiguration={
                'BlockPublicAcls': True,
                'IgnorePublicAcls': True,
                'BlockPublicPolicy': True,
                'RestrictPublicBuckets': True
            }
        )

        logger.info(f"Successfully remediated public access for bucket: {bucket}")

        return {
            'statusCode': 200,
            'body': f'Remediated bucket: {bucket}'
        }

    except Exception as e:
        logger.error(str(e), exc_info=True)
        raise
```
