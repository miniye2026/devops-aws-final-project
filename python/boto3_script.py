import boto3

print(" AWS BASIC REPORT")

try:
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()['Buckets']
    print("S3 Buckets:", len(buckets))

    for bucket in buckets:
        print("-", bucket['Name'])

except Exception as e:
    print("S3 Error:", e)

try:
    ec2 = boto3.client('ec2')
    reservations = ec2.describe_instances()['Reservations']

    total = 0

    for r in reservations:
        for i in r['Instances']:
            total += 1

    print("EC2 Instances:", total)

except Exception as e:
    print("EC2 Error:", e)
