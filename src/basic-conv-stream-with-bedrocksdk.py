#Calling Bedrock LLMs with Bedrock client Sdk
import boto3
import json

# Initialize the Bedrock Runtime client
bedrock_runtime = boto3.client('bedrock-runtime', region_name='us-east-1')

# Specify the model ID (Claude 3 Haiku in this example)
model_id = "anthropic.claude-3-haiku-20240307-v1:0"

# Initialize the conversation array
conversation = []

def chat(user_message):
    # Add user message to the conversation
    #conversation.append({"role": "user", "content": [{"type": "text", "text": user_message}]})
    #conversation = []
    conversation.append (
        {
            "role": "user", 
            "content": [{ "text": user_message}]
        }   
    )  

    try:
        # Send the conversation to the model
        streaming_response = bedrock_runtime.converse_stream(
            modelId=model_id,
            #input=json.dumps({"messages": conversation})
            messages=conversation,
            inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9}
        )

        print ("**********************************************************************")
        print (user_message)  
        print ()

        for chunk in streaming_response["stream"]:
            if "contentBlockDelta" in chunk:
                llm_text = chunk["contentBlockDelta"]["delta"]["text"]
                print(llm_text, end="")
        

        print ()

        # ai_response = json.dumps(streaming_response['output']['message']['content'][0]['text'])
        # print (ai_response)

        # Add AI response to the conversation
        conversation.append(
            {
                "role": "assistant", 
                "content": [{ "text": llm_text}]
            }
        )

    except Exception as e:
        print(f"Error: {str(e)}")
        return "An error occurred while processing your request."


# Example usage
def run_conversation():
    chat("Hello! How are you today?")
    chat("What's the weather like?")
    chat("Tell me a joke.")

if __name__ == "__main__":
    run_conversation()