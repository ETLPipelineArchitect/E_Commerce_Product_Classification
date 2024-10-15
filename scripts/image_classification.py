import boto3
import json

def classify_image(bucket, key):
    client = boto3.client('rekognition')
    response = client.detect_labels(Image={'S3Object': {'Bucket': bucket, 'Name': key}}, MaxLabels=10)
    return json.dumps(response['Labels'])

if __name__ == '__main__':
    bucket_name = 'your-bucket-name'
    image_file_name = 'your-image-file.jpg'
    print(classify_image(bucket_name, image_file_name))
