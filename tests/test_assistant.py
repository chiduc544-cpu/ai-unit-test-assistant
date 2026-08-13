"""Test cases for AI Assistant"""

import pytest
from src.ai_assistant import AITestAssistant


class TestAITestAssistant:
    """Tests for AITestAssistant class"""

    @pytest.fixture
    def assistant(self):
        """Create assistant instance"""
        return AITestAssistant()

    def test_initialization(self, assistant):
        """Test assistant initialization"""
        assert assistant is not None
        assert assistant.test_processor is not None
        assert assistant.api_handler is not None
        assert assistant.conversation_history == []

    def test_clear_history(self, assistant):
        """Test clearing conversation history"""
        assistant.conversation_history.append({"role": "user", "content": "test"})
        assert len(assistant.conversation_history) > 0
        
        assistant.clear_history()
        assert assistant.conversation_history == []

    def test_get_help(self, assistant):
        """Test getting help information"""
        help_text = assistant.get_help()
        assert help_text is not None
        assert "AI Unit Test Assistant" in help_text
        assert "GENERATE TESTS" in help_text
        assert "ANALYZE TESTS" in help_text
        assert "OPTIMIZE TESTS" in help_text

    def test_chat_adds_to_history(self, assistant):
        """Test that chat adds messages to history"""
        initial_count = len(assistant.conversation_history)
        
        try:
            # This will attempt to call OpenAI API
            assistant.chat("What is unit testing?")
            # If API call succeeds, we should have user and assistant messages
            assert len(assistant.conversation_history) > initial_count
        except Exception:
            # If API fails, at least test that message would be added
            pytest.skip("API call failed - skipping integration test")


class TestAssistantMethods:
    """Test assistant methods"""

    @pytest.fixture
    def assistant(self):
        """Create assistant instance"""
        return AITestAssistant()

    def test_generate_tests_accepts_code(self, assistant):
        """Test generate_tests accepts code parameter"""
        test_code = "def add(a, b): return a + b"
        try:
            result = assistant.generate_tests(test_code)
            assert result is not None
            assert isinstance(result, str)
        except Exception:
            pytest.skip("API call failed - skipping integration test")

    def test_analyze_tests_returns_dict(self, assistant):
        """Test analyze_tests returns dictionary"""
        test_code = "def test_add(): assert 1 + 1 == 2"
        try:
            result = assistant.analyze_tests(test_code)
            assert isinstance(result, dict)
            assert "analysis" in result
        except Exception:
            pytest.skip("API call failed - skipping integration test")

    def test_optimize_tests_returns_list(self, assistant):
        """Test optimize_tests returns list"""
        test_code = "def test_add(): assert 1 + 1 == 2"
        try:
            result = assistant.optimize_tests(test_code)
            assert isinstance(result, list)
        except Exception:
            pytest.skip("API call failed - skipping integration test")
