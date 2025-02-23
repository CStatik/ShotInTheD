#!/bin/bash

echo "🚀 AWS Test Setup for Key Search System"

INSTANCE_TYPE="g5.12xlarge"
SPOT_PRICE="3.50"
S3_BUCKET="test-keysearch-$(date +%s)"

INSTANCE_ID=$(aws ec2 run-instances \
    --instance-type $INSTANCE_TYPE \
    --key-name MyAWSKey \
    --image-id ami-08e4e35cccc6189f4 \
    --instance-market-options "MarketType=spot,SpotOptions={MaxPrice=$SPOT_PRICE}" \
    --block-device-mappings '[{"DeviceName":"/dev/sda1","Ebs":{"VolumeSize":500}}]' \
    --query 'Instances[0].InstanceId' --output text)

aws s3 mb s3://$S3_BUCKET
