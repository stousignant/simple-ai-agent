import argparse
import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from constants import *
from prompts import *
from call_function import available_functions, call_function

def main():
    parser = argparse.ArgumentParser(description="AI Code Assistant")
    parser.add_argument("user_prompt", type=str, help="Prompt to send to Gemini")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")
    
    client = genai.Client(api_key=api_key)
    messages_in_conversation = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    if args.verbose:
        print(f"User prompt: {args.user_prompt}\n")

    generate_response(client, messages_in_conversation, args.verbose)

def call_model(client, messages_in_conversation, verbose):
    """Calls the Gemini model and returns the response."""
    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=messages_in_conversation,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt),
    )
    if not response.usage_metadata:
        raise RuntimeError("Gemini API response appears to be malformed")
    
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
    return response

def add_assistant_response_to_conversation(response, messages_in_conversation):
    """Adds the assistant's response (text and function calls) to the conversation."""
    assistant_parts = []
    if response.text:
        assistant_parts.append(types.Part(text=response.text))
    for function_call in response.function_calls:
        assistant_parts.append(types.Part(function_call=function_call))
    
    assistant_content = types.Content(
        role="model",
        parts=assistant_parts
    )
    messages_in_conversation.append(assistant_content)

def execute_function_calls(response, verbose):
    """Executes all function calls from the response and returns the function response parts."""
    function_responses = []
    for function_call in response.function_calls:
        result = call_function(function_call, verbose)
        if (
            not result.parts
            or not result.parts[0].function_response
            or not result.parts[0].function_response.response
        ):
            raise RuntimeError(f"Empty function response for {function_call.name}")
        if verbose:
            print(f"-> {result.parts[0].function_response.response}")
        function_responses.append(result.parts[0])
    return function_responses

def add_function_responses_to_conversation(function_responses, messages_in_conversation):
    """Adds function responses to the conversation."""
    tool_content = types.Content(
        role="tool",
        parts=function_responses
    )
    messages_in_conversation.append(tool_content)

def generate_response(client, messages_in_conversation, verbose):
    """Main loop that iterates until the agent produces a final response."""
    for iteration in range(MAX_ITERATIONS):
        response = call_model(client, messages_in_conversation, verbose)
        
        # Add all candidates to the conversation history
        if response.candidates:
            for candidate in response.candidates:
                if candidate.content:
                    messages_in_conversation.append(candidate.content)
        
        if not response.function_calls:
            print("Final response:")
            print(response.text)
            return

        add_assistant_response_to_conversation(response, messages_in_conversation)
        function_responses = execute_function_calls(response, verbose)
        # This ensures the model sees function call results in future iterations
        messages_in_conversation.append(types.Content(role="user", parts=function_responses))
    
    # If we've exhausted iterations, print an error and exit
    print("Error: Maximum iterations reached. The agent did not produce a final response.")
    print(f"The model made function calls in all {MAX_ITERATIONS} iterations and never returned a final answer.")
    sys.exit(1)


if __name__ == "__main__":
    main()

