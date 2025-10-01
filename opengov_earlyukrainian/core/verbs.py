from typing import Dict


class VerbConjugator:
    """Basic Ukrainian conjugation/aspect utilities (introductory)."""

    def aspect_pair(self, imperfective: str) -> str:
        """Heuristic: add prefix на-/по-/за- for a common perfective counterpart if known."""
        pairs = {
            "писати": "написати",
            "читати": "прочитати",
            "говорити": "сказати",  # suppletive
            "їсти": "з'їсти",
            "робити": "зробити",
        }
        return pairs.get(imperfective, f"по-{imperfective}")

    def conjugate(self, infinitive: str, tense: str = "present") -> Dict:
        """Conjugate common -ати, -ити; simplified patterns for demonstration."""
        if infinitive.endswith("ати"):
            stem = infinitive[:-3]
            if tense == "present":
                forms = {
                    "я": stem + "ю",
                    "ти": stem + "єш",
                    "він/вона/воно": stem + "є",
                    "ми": stem + "ємо",
                    "ви": stem + "єте",
                    "вони": stem + "ють",
                }
                # Example irregular spelling: читати → читаю (no apostrophe)
                return {"infinitive": infinitive, "tense": "present", "forms": forms}
        if infinitive.endswith("ити"):
            stem = infinitive[:-3]
            if tense == "present":
                forms = {
                    "я": stem + "у",
                    "ти": stem + "иш",
                    "він/вона/воно": stem + "ить",
                    "ми": stem + "имо",
                    "ви": stem + "ите",
                    "вони": stem
                    + "ать",  # many -ити verbs use -ять/-ать variants; simplified here
                }
                return {"infinitive": infinitive, "tense": "present", "forms": forms}

        if infinitive == "бути":
            if tense == "present":
                return {
                    "infinitive": "бути",
                    "tense": "present",
                    "forms": {
                        "я": "є",
                        "ти": "є",
                        "він/вона/воно": "є",
                        "ми": "є",
                        "ви": "є",
                        "вони": "є",
                    },
                }
            if tense == "past":
                return {
                    "infinitive": "бути",
                    "tense": "past",
                    "forms": {
                        "я (чол.)": "був",
                        "я (жін.)": "була",
                        "воно": "було",
                        "ми/ви/вони": "були",
                    },
                }

        return {"infinitive": infinitive, "tense": tense, "forms": {}}

