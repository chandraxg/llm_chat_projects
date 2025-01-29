
import boto3
import asyncio
from langchain_aws import ChatBedrockConverse


# Get the credentials
session = boto3.Session()
credentials = session.get_credentials().get_frozen_credentials()

def get_credentials():
    return {
        "aws_access_key_id": credentials.access_key,
        "aws_secret_access_key": credentials.secret_key,
        "aws_session_token": credentials.token
    }

# Initialize the Bedrock LLM (Claude model)
llm = ChatBedrockConverse(
    model_id="us.anthropic.claude-3-5-sonnet-20241022-v2:0",  # Specify the Claude model
        # Model parameters
    max_tokens = 512, 
    temperature = 0.5, 
    top_p = 0.9, 
    aws_access_key_id=credentials.access_key,
    aws_secret_access_key=credentials.secret_key,
    region_name="us-east-1",         # AWS region
    credentials_profile_name="default"  # AWS credentials profile (optional)
)

conversation = []

async def chat_with_llm (question):
    # Add user message to the conversation
    conversation.append (
        {"role": "user", "content": question}
    )  

    # Invoke the LLM with the conversation
    ai_response = llm.invoke (input = conversation)

    # Add AI response to the conversation
    conversation.append(
        { "role": "assistant", "content": ai_response.content }
    )
    return (ai_response.content)

# Example conversation
print("Starting conversation with LLM. Type 'exit' to end.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = asyncio.run (chat_with_llm(user_input))
    print(f"LLM: {response}")