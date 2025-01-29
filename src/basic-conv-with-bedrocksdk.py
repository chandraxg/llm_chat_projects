#Calling Bedrock LLMs with Bedrock-client Sdk
import boto3
import json

# Initialize the Bedrock Runtime client
bedrock_runtime = boto3.client('bedrock-runtime', region_name='us-east-1')

# Specify the model ID (Claude 3 Haiku in this example)
model_id = "us.anthropic.claude-3-5-sonnet-20241022-v2:0"

# Initialize the conversation array
conversation = []

def chat(user_message):
    # Add user message to the conversation
    conversation.append (
        { "role": "user", "content": [{ "text": user_message}] }   
    )  

    try:
        # Send the conversation to the model
        response = bedrock_runtime.converse(
            modelId=model_id,
            messages=conversation,
            inferenceConfig={"maxTokens": 512, "temperature": 1, "topP": 0.9},
        )

        # Parse the AI's response
        print ("**********************************************************************")
        print (user_message)  
        print ()

        ai_response = json.dumps(response['output']['message']['content'][0]['text'])

        # Add AI response to the conversation
        conversation.append(
            { "role": "assistant", "content": [{ "text": ai_response}] }
        )

        return ai_response
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return "An error occurred while processing your request."

# Example usage
if __name__ == "__main__":
    print("Starting conversation with LLM. Type 'exit' to end.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = chat(user_input)
        print(f"LLM: {response}")

