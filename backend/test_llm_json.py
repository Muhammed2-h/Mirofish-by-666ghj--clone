import sys
import os
import time
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.utils.llm_client import LLMClient

def main():
    print("Testing chat_json...")
    try:
        client = LLMClient()
        print(f"URL: {client.base_url}, Model: {client.model}")
        start = time.time()
        res = client.chat_json([{"role": "system", "content": "You are a helpful assistant. Output a JSON object with a key 'message' containing the word 'hello'."}, {"role": "user", "content": "test"}])
        print("Response JSON:", res)
        print(f"Time taken: {time.time()-start:.2f}s")
    except Exception as e:
        print("Error!", type(e), str(e))

if __name__ == "__main__":
    main()
