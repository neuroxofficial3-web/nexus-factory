import os
api_key = os.getenv("LLAMA_API_KEY")

def start_factory():
    if api_key:
        print("✅ Nexus Factory: Llama 4 Brain Connected!")
    else:
        print("❌ Error: API Key missing in Secrets.")

if __name__ == "__main__":
    start_factory()
