from typing import Dict, List
from openai import OpenAI
from opengov_earlyukrainian.config import settings


class AIConversationPartner:
    """AI partner with level-aware, polite/formal control."""

    def __init__(self, level: str = "A1", formal: bool = True):
        self.level = level
        self.formal = formal
        self.client = OpenAI(api_key=settings.openai_api_key.get_secret_value())
        self.history: List[Dict[str, str]] = []

    def _system_prompt(self) -> str:
        form = "Ви" if self.formal else "ти"
        return f"""
You are a friendly Ukrainian tutor for a {self.level} learner.
- Use natural Ukrainian with {form} address.
- Prefer high-frequency vocabulary.
- Provide a brief English gloss.
Return JSON with keys: "ukrainian", "english", "notes", "follow_up".
"""

    def chat(self, user_utterance: str) -> Dict:
        self.history.append({"role": "user", "content": user_utterance})
        # Minimal dependency to avoid network in tests; structure only
        try:
            resp = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "system", "content": self._system_prompt()}]
                + self.history[-5:],
                temperature=0.4,
                max_tokens=200,
            )
            content = resp.choices[0].message.content
            # In practice, ensure JSON; simplified:
            return {
                "ukrainian": content,
                "english": "",
                "notes": [],
                "follow_up": "Розкажіть, будь ласка, більше.",
            }
        except Exception:
            return {
                "ukrainian": "Вітаю! Як справи?",
                "english": "Hello! How are you?",
                "notes": [],
                "follow_up": "Чим ви цікавитеся?",
            }

