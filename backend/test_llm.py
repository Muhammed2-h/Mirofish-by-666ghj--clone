import sys
import os
import time
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.utils.llm_client import LLMClient
from openai import OpenAI

def main():
    print("Testing LLM Client...")
    try:
        client = LLMClient()
        # override client to have a short timeout
        client.client = OpenAI(
            api_key=client.api_key,
            base_url=client.base_url,
            timeout=10.0
        )
        print(f"URL: {client.base_url}, Model: {client.model}, API_KEY: {client.api_key[:10]}...")
        start = time.time()
        res = client.chat([{"role": "user", "content": "hi"}], max_tokens=10)
        print("Response:", res)
        print(f"Time taken: {time.time()-start:.2f}s")
    except Exception as e:
        print("Error!", type(e), str(e))

if __name__ == "__main__":
    main()
