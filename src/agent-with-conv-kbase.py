
import boto3
import json


# Initialize the Bedrock Kbase client
bedrock_client = boto3.client('bedrock')

def upload_and_vectorize_document(document_path, kbase_id):
    # Read the document
    with open(document_path, 'r') as file:
        document_content = file.read()

    # Upload the document to Kbase
    response = bedrock_client.upload_document(
        KnowledgeBaseId=kbase_id,
        DocumentContent=document_content
    )

    # Vectorize the document
    vector_response = bedrock_client.vectorize_document(
        KnowledgeBaseId=kbase_id,
        DocumentId=response['DocumentId']
    )

    return vector_response

# Example usage
document_path = r'..\docs\money-basics-guide-savings-checking-accounts.pdf'
kbase_id = 'YPBPTXCV3V'
vector_response = upload_and_vectorize_document(document_path, kbase_id)
print(json.dumps(vector_response, indent=2))