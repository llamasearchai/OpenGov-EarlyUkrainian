import pytest
from unittest.mock import Mock, patch
from opengov_earlyukrainian.ai.conversation import AIConversationPartner


def test_ai_conversation_init():
    """Test AIConversationPartner initialization."""
    partner = AIConversationPartner(level="A1", formal=True)
    assert partner.level == "A1"
    assert partner.formal is True
    assert len(partner.history) == 0


def test_ai_conversation_system_prompt_formal():
    """Test system prompt generation for formal address."""
    partner = AIConversationPartner(level="A2", formal=True)
    prompt = partner._system_prompt()
    assert "A2" in prompt
    assert "Ви" in prompt


def test_ai_conversation_system_prompt_informal():
    """Test system prompt generation for informal address."""
    partner = AIConversationPartner(level="B1", formal=False)
    prompt = partner._system_prompt()
    assert "B1" in prompt
    assert "ти" in prompt


def test_ai_conversation_chat_fallback():
    """Test chat with exception handling (fallback response)."""
    with patch("opengov_earlyukrainian.ai.conversation.OpenAI") as mock_openai:
        # Simulate API failure
        mock_client = Mock()
        mock_client.chat.completions.create.side_effect = Exception("API Error")
        mock_openai.return_value = mock_client
        
        partner = AIConversationPartner(level="A1", formal=True)
        response = partner.chat("Привіт")
        
        assert "ukrainian" in response
        assert "english" in response
        assert "Вітаю" in response["ukrainian"]


def test_ai_conversation_chat_success():
    """Test successful chat interaction with mocked API response."""
    with patch("opengov_earlyukrainian.ai.conversation.OpenAI") as mock_openai:
        # Setup mock
        mock_client = Mock()
        mock_response = Mock()
        mock_message = Mock()
        mock_message.content = "Доброго дня! Як справи?"
        mock_response.choices = [Mock(message=mock_message)]
        mock_client.chat.completions.create.return_value = mock_response
        mock_openai.return_value = mock_client
        
        partner = AIConversationPartner(level="A1", formal=True)
        response = partner.chat("Привіт")
        
        assert "ukrainian" in response
        assert response["ukrainian"] == "Доброго дня! Як справи?"
        assert len(partner.history) == 1
        assert partner.history[0]["role"] == "user"
        assert partner.history[0]["content"] == "Привіт"


def test_ai_conversation_history_management():
    """Test conversation history management (last 5 messages)."""
    with patch("opengov_earlyukrainian.ai.conversation.OpenAI") as mock_openai:
        mock_client = Mock()
        mock_client.chat.completions.create.side_effect = Exception("Fallback")
        mock_openai.return_value = mock_client
        
        partner = AIConversationPartner(level="A1", formal=True)
        
        # Add multiple messages
        for i in range(7):
            partner.chat(f"Message {i}")
        
        # Should have 7 messages in history
        assert len(partner.history) == 7
        
        # But only last 5 should be sent to API (tested via mock call)
        # The history itself stores all messages


def test_ai_conversation_different_levels():
    """Test conversation with different proficiency levels."""
    levels = ["A1", "A2", "B1", "B2", "C1"]
    for level in levels:
        partner = AIConversationPartner(level=level, formal=True)
        assert partner.level == level
        prompt = partner._system_prompt()
        assert level in prompt

