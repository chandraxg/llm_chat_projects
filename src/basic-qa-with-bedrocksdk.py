#Calling Bedrock LLMs with Bedrock-client Sdk
import boto3
import json


# Create a Bedrock Runtime client
client = boto3.client('bedrock-runtime', region_name='us-east-1')

# Get the credentials
session = boto3.Session()
credentials = session.get_credentials().get_frozen_credentials()

# Print the security token
print(f"Access Key: {credentials.access_key}")
print(f"Secret Key: {credentials.secret_key}")
print(f"Session Token: {credentials.token}")

# Set the model ID (e.g., for Claude 3 Haiku)
model_id = 'anthropic.claude-3-haiku-20240307-v1:0'

# Define your input message
user_message = "What is the capital of France?."

# Prepare the request payload
request_payload = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 512,
    "temperature": 0.5,
    "messages": [
        {
            "role": "user",
            "content": [{"type": "text", "text": user_message}]
        }
    ]
}

# Invoke the model
try:
    response = client.invoke_model(
        modelId=model_id,
        body=json.dumps(request_payload)
    )
    
    # Process and print the response
    response_body = json.loads(response['body'].read())
    print(response_body['content'][0]['text'])

except Exception as e:
    print(f"An error occurred: {str(e)}")

