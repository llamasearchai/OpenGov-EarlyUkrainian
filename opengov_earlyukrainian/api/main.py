from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

from opengov_earlyukrainian.core.alphabet import AlphabetTeacher
from opengov_earlyukrainian.core.cases import CasesTeacher
from opengov_earlyukrainian.core.verbs import VerbConjugator
from opengov_earlyukrainian.core.transliteration import Transliterator
from opengov_earlyukrainian.ai.conversation import AIConversationPartner

app = FastAPI(title="OpenGov-EarlyUkrainian API", version="0.1.0")


@app.get("/health")
async def health() -> Dict[str, str]:
    return {"status": "healthy", "version": "0.1.0"}


class DeclineRequest(BaseModel):
    noun: str
    gender: str


@app.post("/decline")
async def decline(req: DeclineRequest) -> Dict[str, str]:
    return CasesTeacher().decline_noun(req.noun, req.gender)


class ConjugateRequest(BaseModel):
    verb: str
    tense: str = "present"


@app.post("/conjugate")
async def conjugate(req: ConjugateRequest) -> Dict:
    return VerbConjugator().conjugate(req.verb, req.tense)


class TranslitRequest(BaseModel):
    text: str


@app.post("/transliterate")
async def transliterate(req: TranslitRequest) -> Dict[str, str]:
    return {"ukrainian": Transliterator().to_ukrainian(req.text)}


class ChatRequest(BaseModel):
    utterance: str
    level: str = "A1"
    formal: bool = True


@app.post("/chat")
async def chat(req: ChatRequest) -> Dict:
    return AIConversationPartner(level=req.level, formal=req.formal).chat(req.utterance)


@app.get("/alphabet/{row}")
async def alphabet(row: str) -> Dict:
    return AlphabetTeacher().get_row(row)

