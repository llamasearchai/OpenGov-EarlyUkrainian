from typing import Dict


class BusinessUkrainian:
    """Templates and phrases for business communication."""

    def email_template(self, purpose: str = "meeting") -> Dict[str, str]:
        templates = {
            "meeting": {
                "subject": "Запит щодо зустрічі",
                "body": "Доброго дня! Чи зручно Вам провести зустріч у {date} о {time}? З повагою, {name}.",
                "signoff": "З повагою,\n{name}\n{role}, {company}",
            },
            "follow_up": {
                "subject": "Нагадування про домовленості",
                "body": "Доброго дня! Нагадую про наші домовленості щодо {topic}. Чекаю на Вашу відповідь.",
                "signoff": "Щиро,\n{name}",
            },
        }
        return templates.get(purpose, templates["meeting"])

    def phone_phrases(self) -> Dict[str, str]:
        return {
            "intro": "Доброго дня! Мене звати {name}, я представляю {company}.",
            "ask_availability": "Чи зручно Вам зараз говорити?",
            "request": "Хотів(ла) би обговорити {topic}.",
            "closing": "Дякую за Ваш час! Гарного дня.",
        }

