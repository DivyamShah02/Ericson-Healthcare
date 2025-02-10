import boto3
import base64
from botocore.exceptions import NoCredentialsError
import os

def decrypt(b64_text):
    # Decode the Base64 string back to bytes, then to text
    return base64.b64decode(b64_text.encode()).decode()


def upload_to_s3(file_path, file_name):
    """
    Uploads a file to S3 and returns the URL.
    :param file_path: Local path to file
    :param file_name: Name for the uploaded file in S3
    :param bucket: S3 bucket name
    :return: Public URL of the uploaded file
    """

    # AWS Credentials
    AWS_ACCESS_KEY = decrypt("QUtJQTRUNE9DTTU2TENMUUdTNlA=")
    AWS_SECRET_KEY = decrypt("TzRzQmlWK0NvcWdBM2Q1aGhPMXJkeGV0c1YyaWdibjR6YXhrbTRqMA==")
    BUCKET_NAME = "ehunt"

    try:
        s3 = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY
        )
        
        # Upload file to S3
        s3.upload_file(file_path, BUCKET_NAME, file_name)
        # ExtraArgs={'ACL': 'public-read'}
        
        # Generate public URL
        file_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{file_name}"
        return file_url

    except NoCredentialsError:
        return "AWS Credentials not found!"

# Example Usage
file_url = upload_to_s3(r"C:\Users\Divyam Shah\OneDrive\Desktop\Dynamic Labz\Clients\Clients\Ericson Healthcare\Ericson-Healthcare\EricsonHealthcare\static\logo.png", "uploads/logo.png")
print("File uploaded to:", file_url)



def upload_file_to_s3(uploaded_file):
    """Uploads a file to AWS S3, renaming it if a file with the same name exists."""
    region_name = "eu-north-1"
    s3_client = boto3.client(
        "s3",
        aws_access_key_id = decrypt("QUtJQTRUNE9DTTU2TENMUUdTNlA="),
        aws_secret_access_key = decrypt("TzRzQmlWK0NvcWdBM2Q1aGhPMXJkeGV0c1YyaWdibjR6YXhrbTRqMA=="),
        region_name = region_name
    )
    
    bucket_name = "ehunt"
    base_name, extension = os.path.splitext(uploaded_file.name)
    file_name = uploaded_file.name
    s3_key = f"uploads/{file_name}"
    counter = 1

    # Check if file exists and rename if necessary
    while True:
        try:
            s3_client.head_object(Bucket=bucket_name, Key=s3_key)
            # If file exists, update the filename
            file_name = f"{base_name}({counter}){extension}"
            s3_key = f"uploads/{file_name}"
            counter += 1
        except s3_client.exceptions.ClientError:
            break  # File does not exist, proceed with upload

    # Upload file
    s3_client.upload_fileobj(uploaded_file, bucket_name, s3_key)

    # Generate file URL
    file_url = f"https://{bucket_name}.s3.{region_name}.amazonaws.com/{s3_key}"

    return file_url
