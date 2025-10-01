from typing import Dict, List


class AlphabetTeacher:
    """Teaches Ukrainian alphabet with rows and mnemonics."""

    def __init__(self) -> None:
        self.alphabet = [
            "А",
            "Б",
            "В",
            "Г",
            "Ґ",
            "Д",
            "Е",
            "Є",
            "Ж",
            "З",
            "И",
            "І",
            "Ї",
            "Й",
            "К",
            "Л",
            "М",
            "Н",
            "О",
            "П",
            "Р",
            "С",
            "Т",
            "У",
            "Ф",
            "Х",
            "Ц",
            "Ч",
            "Ш",
            "Щ",
            "Ь",
            "Ю",
            "Я",
        ]
        self.rows = {
            "basic": [
                "А",
                "Б",
                "В",
                "Г",
                "Ґ",
                "Д",
                "Е",
                "Ж",
                "З",
                "И",
                "І",
                "Й",
                "К",
                "Л",
                "М",
                "Н",
                "О",
                "П",
                "Р",
                "С",
                "Т",
                "У",
                "Ф",
                "Х",
                "Ц",
                "Ч",
                "Ш",
                "Щ",
            ],
            "iotated": ["Я", "Ю", "Є", "Ї"],  # ya, yu, ye, yi (iotted)
            "soft_sign": ["Ь"],
            "foreign": ["Ґ"],  # hard g
            "vowels": ["А", "Е", "И", "І", "О", "У", "Ю", "Я", "Є", "Ї"],
        }
        self.mnemonics = {
            "Ґ": "Ґ — hard g as in 'go'; distinct from Г (voiced h).",
            "Ї": "Ї — looks like 'ï': pronounced [ji].",
            "Є": "Є — 'ye' [je], iotated vowel.",
            "І": "І — i (close front vowel), different from И (close central).",
            "Ь": "Ь — soft sign, palatalization marker (rare; compare Russian).",
        }

    def get_row(self, row: str) -> Dict[str, List[str]]:
        if row not in self.rows:
            raise ValueError(f"Unknown row: {row}")
        return {"row": row, "letters": self.rows[row]}

    def mnemonic(self, letter: str) -> str:
        return self.mnemonics.get(letter, "No mnemonic available yet.")

