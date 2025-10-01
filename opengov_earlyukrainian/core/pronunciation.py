from typing import Dict, List


class PronunciationCoach:
    """Pronunciation coach for Ukrainian specifics."""

    def __init__(self) -> None:
        self.features = {
            "iotated": {
                "letters": {"я": "[ja/~a]", "ю": "[ju/~u]", "є": "[je/~e]", "ї": "[ji]"},
                "note": "Iotated vowels add [j] before or soften preceding consonant; at word start after vowel/apostrophe they surface as [jV].",
            },
            "apostrophe": {
                "char": "ʼ",
                "rule": "Blocks palatalization: об'єкт, п'ять; write apostrophe between prefix and iotated vowel.",
            },
            "hard_g": {
                "Ґ": "[g]",
                "Г": "[ɦ]",
                "note": "Ґ is hard g. Г is a voiced h.",
            },
            "stress": {
                "rule": "Stress can be mobile; dictionary lookup recommended. No vowel reduction as in Russian, but allophones vary.",
            },
        }

    def get_feature(self, key: str) -> Dict:
        if key not in self.features:
            raise ValueError("Unknown feature key")
        return self.features[key]

    def sample_pairs(self) -> Dict[str, List[str]]:
        return {
            "Г vs Ґ": ["Ганна [ɦanna]", "ґанок [ganok]"],
            "Iotated": ["яма [jama]", "ємність [jemnistʲ]", "їжа [jiʒa]"],
            "Apostrophe": ["п'ять", "об'єкт", "з'їсти"],
        }

