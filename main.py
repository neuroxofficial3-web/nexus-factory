import os
import requests
import json
import logging

# Logging set ചെയ്യുന്നു
logging.basicConfig(level=logging.INFO, format='%(message)s')

class NexusEliteFactory:
    def __init__(self):
        self.api_key = os.getenv("LLAMA_API_KEY")
        self.url = "https://api.groq.com/openai/v1/chat/completions"

    def _call_api(self, role, task, temperature=0.2):
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {"role": "system", "content": f"You are a {role}. Provide professional results for Mufadul Ajlan."},
                {"role": "user", "content": task}
            ],
            "temperature": temperature
        }
        try:
            response = requests.post(self.url, headers=headers, json=payload, timeout=60)
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            logging.error(f"❌ API Error: {e}")
            return None

    def _extract_code(self, text):
        if "```python" in text:
            return text.split("```python")[1].split("```")[0].strip()
        elif "```text" in text:
            return text.split("```text")[1].split("```")[0].strip()
        elif "```" in text:
            return text.split("```")[1].split("```")[0].strip()
        return text

    def save_output(self, filename, content):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        logging.info(f"📂 Saved: {filename}")

    def start_production(self, user_idea):
        logging.info(f"🚀 Nexus Elite Factory: Production started for Mufadul Ajlan...")

        # PHASE 1: LOGIC ARCHITECTS
        logging.info("🧠 Phase 1: Creating High-End Blueprints...")
        blueprint = self._call_api("Group of 5 Senior Architects", f"Design a fail-proof logic for: {user_idea}")
        if blueprint: self.save_output("blueprint.md", blueprint)

        # PHASE 2: LEAD DEVELOPERS
        logging.info("💻 Phase 2: Generating Professional Code...")
        raw_code = self._call_api("Group of 5 Lead Developers", f"Write full Python/Kivy code based on this blueprint: {blueprint}")

        # PHASE 3: QA & LOGIC VALIDATION
        logging.info("🔍 Phase 3: Cross-referencing Code with Blueprint...")
        audit_task = f"Verify this code against blueprint and fix issues. Return ONLY the final code in a ```python block. Blueprint: {blueprint}\nCode: {raw_code}"
        audit_response = self._call_api("Senior QA Engineer", audit_task, temperature=0.1)
        
        final_extracted_code = self._extract_code(audit_response)
        self.save_output("main_final.py", final_extracted_code)

        # PHASE 4: REQUIREMENTS GENERATION
        logging.info("📝 Phase 4: Generating requirements.txt...")
        reqs_task = f"Analyze code and list ONLY necessary libraries in a ```text block. Code: {final_extracted_code}"
        reqs_response = self._call_api("DevOps Specialist", reqs_task)
        
        if reqs_response:
            clean_reqs = self._extract_code(reqs_response)
            self.save_output("requirements.txt", clean_reqs)

        logging.info("\n✅ PRODUCTION COMPLETE. Files ready for APK Build.")

if __name__ == "__main__":
    factory = NexusEliteFactory()
    # App idea ivide nalkunnu
    factory.start_production("Professional AI Finance Manager with Voice Commands")
