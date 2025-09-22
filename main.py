import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if len(sys.argv) < 2:
        print("No prompt provided")
        sys.exit(1)

    prompt = sys.argv[1]

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    flag = ""
    if len(sys.argv) > 2:
        flag = sys.argv[2]

    verbose = False
    if flag == "--verbose":
        verbose = True

    client = genai.Client(api_key = api_key)
    response = client.models.generate_content(
            model='gemini-2.0-flash-001',
            contents= messages
            )
    
    if verbose: print("User prompt:", prompt)
    print("Response: " + response.text)
    if verbose: print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    if verbose: print("Response tokens:", response.usage_metadata.candidates_token_count)

if __name__ == "__main__":
    main()
