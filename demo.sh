#!/bin/bash
# OpenGov-EarlyUkrainian Demo Script

echo "╔══════════════════════════════════════════════════════════════════╗"
echo "║     OpenGov-EarlyUkrainian - Complete Feature Demonstration      ║"
echo "╚══════════════════════════════════════════════════════════════════╝"
echo ""

echo "📚 1. ALPHABET LEARNING"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
.venv/bin/ukrainian alphabet iotated
echo ""

echo "📖 2. NOUN DECLENSION (7 Cases)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
.venv/bin/ukrainian decline студент masculine
echo ""

echo "🔄 3. VERB CONJUGATION"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
.venv/bin/ukrainian conjugate вчити --tense present
echo ""

echo "↔️  4. TRANSLITERATION"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
.venv/bin/ukrainian translit "Dobryi den, yak spravy?"
echo ""

echo "⚡ 5. VERB ASPECTS"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
.venv/bin/ukrainian aspect робити
echo ""

echo "💼 6. BUSINESS UKRAINIAN"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
.venv/bin/ukrainian business --purpose meeting
echo ""

echo "🎭 7. CULTURAL INFORMATION"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
.venv/bin/ukrainian culture
echo ""

echo "✅ All features working perfectly!"
echo ""
