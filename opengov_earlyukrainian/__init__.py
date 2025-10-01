"""OpenGov-EarlyUkrainian core exports."""
__version__ = "0.1.0"

from opengov_earlyukrainian.core.alphabet import AlphabetTeacher
from opengov_earlyukrainian.core.pronunciation import PronunciationCoach
from opengov_earlyukrainian.core.cases import CasesTeacher
from opengov_earlyukrainian.core.verbs import VerbConjugator
from opengov_earlyukrainian.core.transliteration import Transliterator
from opengov_earlyukrainian.ai.conversation import AIConversationPartner

__all__ = [
    "AlphabetTeacher",
    "PronunciationCoach",
    "CasesTeacher",
    "VerbConjugator",
    "Transliterator",
    "AIConversationPartner",
    "__version__",
]

