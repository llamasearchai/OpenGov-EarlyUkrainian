from typing import Dict


class Transliterator:
    """Simple Latin → Ukrainian transliteration (approximate, BGN/PCGN-inspired)."""

    LAT2UKR: Dict[str, str] = {
        "shch": "щ",
        "zh": "ж",
        "kh": "х",
        "ts": "ц",
        "ch": "ч",
        "sh": "ш",
        "yi": "ї",
        "ye": "є",
        "yu": "ю",
        "ya": "я",
        "yo": "йо",
        "a": "а",
        "b": "б",
        "v": "в",
        "h": "г",
        "g": "ґ",
        "d": "д",
        "e": "е",
        "z": "з",
        "y": "и",
        "i": "і",
        "j": "й",
        "k": "к",
        "l": "л",
        "m": "м",
        "n": "н",
        "o": "о",
        "p": "п",
        "r": "р",
        "s": "с",
        "t": "т",
        "u": "у",
        "f": "ф",
        # Apostrophe handling: represented with apostrophe if needed; omitted in simple map
        "'": "ʼ",
    }

    def to_ukrainian(self, text: str) -> str:
        s = text

        # Lowercase processing; then restore capitalization per token
        def tr_token(tok: str) -> str:
            low = tok.lower()
            out = ""
            i = 0
            while i < len(low):
                matched = False
                for length in [4, 3, 2, 1]:
                    if i + length <= len(low) and low[i : i + length] in self.LAT2UKR:
                        # Special case: "i" after "y" should become "ї" not "і"
                        # This handles cases like "Kyiv" → "Київ" (К-и-ї-в)
                        if low[i : i + length] == "i" and len(out) > 0 and out[-1] == "и":
                            # Convert "i" after "y" (now "и") to "ї"
                            uk = "ї"
                        else:
                            uk = self.LAT2UKR[low[i : i + length]]
                        
                        if tok[i : i + length].istitle():
                            uk = uk[0].upper() + uk[1:]
                        elif tok[i : i + length].isupper():
                            uk = uk.upper()
                        out += uk
                        i += length
                        matched = True
                        break
                if not matched:
                    out += tok[i]
                    i += 1
            return out

        return " ".join(tr_token(t) for t in s.split(" "))

