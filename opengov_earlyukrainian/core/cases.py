from typing import Dict

VOWEL = set("АЕЄИІЇОУЮЯаеєиіїоюя")


def ends_with_husher(word: str) -> bool:
    return word[-1].lower() in ["ж", "ч", "ш", "щ"]


class CasesTeacher:
    """Declension helper (introductory coverage; simplified rules)."""

    cases_order = [
        "називний",
        "родовий",
        "давальний",
        "знахідний",
        "орудний",
        "місцевий",
        "кличний",
    ]

    def decline_noun(self, lemma: str, gender: str) -> Dict[str, str]:
        """Return a basic declension table for common patterns (animate/inanimate not fully modeled)."""
        lemma = lemma.strip()
        g = gender.lower()
        table: Dict[str, str] = {}

        # Feminine -а/-я (e.g., книга → книги, книзі, книгу, книгою, (на) книзі, книго)
        if g == "feminine" and lemma.endswith(("а", "я")):
            base = lemma[:-1]
            a_is_ya = lemma.endswith("я")
            o_instr = "ею" if a_is_ya else "ою"
            i_loc = "і"
            gen = base + ("ї" if a_is_ya else "и")
            dat = base + ("ї" if a_is_ya else "і")
            acc = base + ("ю" if a_is_ya else "у")
            ins = base + o_instr
            loc = base + i_loc
            voc = base + ("є" if a_is_ya else "о")
            table = {
                "називний": lemma,
                "родовий": gen,
                "давальний": dat,
                "знахідний": acc,
                "орудний": ins,
                "місцевий": loc,
                "кличний": voc,
            }
            return table

        # Masculine hard-stem consonant (inanimate): стіл → стола, столу, стіл/стола, столом, (на) столі, столе
        if g == "masculine" and lemma[-1] not in VOWEL:
            base = lemma
            gen = base + "а"
            dat = base + "у"
            # accusative = nominative for inanimate
            acc = lemma
            ins = base + "ом"
            loc = base + "і"
            # vocative often adds -е or softens (simplified)
            voc = base + ("у" if ends_with_husher(lemma) else "е")
            return {
                "називний": lemma,
                "родовий": gen,
                "давальний": dat,
                "знахідний": acc,
                "орудний": ins,
                "місцевий": loc,
                "кличний": voc,
            }

        # Neuter -о/-е: місто → міста, місту, місто, містом, (у) місті, місто (voc=nom)
        if g == "neuter" and lemma.endswith(("о", "е")):
            base = lemma[:-1]
            gen = base + "а"
            dat = base + "у"
            acc = lemma
            ins = base + "ом"
            loc = base + "і"
            voc = lemma
            return {
                "називний": lemma,
                "родовий": gen,
                "давальний": dat,
                "знахідний": acc,
                "орудний": ins,
                "місцевий": loc,
                "кличний": voc,
            }

        # Fallback: return nominative only
        return {c: (lemma if c == "називний" else "?") for c in self.cases_order}

