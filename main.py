import os
import sys
from dotenv import load_dotenv
from google import genai
from constants import *
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

is_verbose = False

def main():
    user_prompt = handle_args()
    generate_response(user_prompt)

def handle_args():
    global is_verbose

    if len(sys.argv) <= 1:
        print("Missing prompt argument.")
        sys.exit(1)

    user_prompt = sys.argv[1]

    for i in range(2, len(sys.argv)):
        if sys.argv[i] == "--verbose":
            is_verbose = True

    if is_verbose:
        print(f"User prompt: {user_prompt}")
    return user_prompt

def generate_response(user_prompt):
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    response = client.models.generate_content(model=GEMINI_MODEL, contents=messages)
    print(f"LLM response : {response.text}")
    if is_verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()

