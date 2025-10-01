# OpenGov-EarlyUkrainian

AI-powered Ukrainian language learning platform featuring interactive lessons, cultural immersion, Business Ukrainian, and personalized learning paths.

## Features

- Ukrainian Alphabet & Pronunciation:
  - Full Cyrillic alphabet with ґ, ї, є, і
  - Iotated vowels: я, ю, є, ї
  - Apostrophe ʼ usage to block palatalization (об'єкт, п'ять)
  - Stress awareness and vowel reduction patterns (limited vs Russian)

- Grammar Mastery:
  - 7 cases + vocative: називний, родовий, давальний, знахідний, орудний, місцевий, кличний
  - Gender (masc/fem/neut), animacy in accusative
  - Verb aspect (perfective/imperfective) and conjugations
  - Tenses (past, present, future synthetic/compound), imperative, conditional (б + past)

- Conversational Practice:
  - AI conversation partner (OpenAI)
  - Formal vs informal (Ви/ти), politeness strategies
  - Real-life scenarios and feedback

- Business Ukrainian:
  - Email templates, meeting language, negotiation, industry vocabulary

- Cultural Context:
  - Regions, holidays, cuisine, etiquette, contemporary culture

- Tools:
  - Transliteration (Latin ↔ Ukrainian), SRS for vocab/grammar, progress tracking

## Quick Start

```bash
# Install uv (optional)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone & install
git clone https://github.com/opengov/earlyukrainian.git
cd OpenGov-EarlyUkrainian
uv sync

# Environment
cp .env.example .env
# Set OPENAI_API_KEY=...

# Run tests & server
uv run pytest
uv run uvicorn opengov_earlyukrainian.api.main:app --reload
```

## CLI Usage

```bash
# Alphabet lessons
ukrainian alphabet iotated

# Decline nouns
ukrainian decline книга feminine

# Conjugate verbs
ukrainian conjugate читати present

# Transliterate
ukrainian translit "Kyiv, Hryhoryi Skovoroda"
```

## API Examples

Start server:
```bash
uv run uvicorn opengov_earlyukrainian.api.main:app --reload
```

Sample API calls:
```bash
# Health check
curl http://localhost:8000/health

# Declension
curl -X POST http://localhost:8000/decline \
  -H "Content-Type: application/json" \
  -d '{"noun":"книга","gender":"feminine"}'

# Conjugation
curl -X POST http://localhost:8000/conjugate \
  -H "Content-Type: application/json" \
  -d '{"verb":"читати","tense":"present"}'

# Transliteration
curl -X POST http://localhost:8000/transliterate \
  -H "Content-Type: application/json" \
  -d '{"text":"Hryhoryi Skovoroda"}'

# Chat
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"utterance":"Вітаю!","level":"A1","formal":true}'
```

## Development

```bash
# Install dev dependencies
uv sync --extra dev

# Install hooks and run tox
uv run pre-commit install
uv run tox

# Format and lint
uv run black opengov_earlyukrainian tests
uv run ruff check opengov_earlyukrainian tests

# Type check
uv run mypy opengov_earlyukrainian tests

# Run tests with coverage
uv run pytest --cov=opengov_earlyukrainian --cov-report=term-missing
```

## Docker

```bash
# Build and run
docker-compose up --build

# Test health
curl http://localhost:8000/health
```

## License

MIT

## Author

Nik Jois <nikjois@llamasearch.ai>

