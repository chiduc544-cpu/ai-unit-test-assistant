"""Main AI Assistant Module"""

import logging
from typing import Optional, Dict, List
from src.test_processor import TestProcessor
from src.api_handler import OpenAIHandler

logger = logging.getLogger(__name__)


class AITestAssistant:
    """Main AI Assistant for Unit Testing"""

    def __init__(self):
        """Initialize AI Test Assistant"""
        self.test_processor = TestProcessor()
        self.api_handler = OpenAIHandler()
        self.conversation_history = []
        logger.info("AI Test Assistant initialized")

    def generate_tests(self, code: str, language: str = "python") -> str:
        """Generate unit tests from code
        
        Args:
            code: Source code
            language: Programming language
            
        Returns:
            str: Generated tests
        """
        logger.info(f"Generating tests for {language} code")
        return self.test_processor.generate_unit_tests(code, language)

    def analyze_tests(self, test_code: str) -> Dict:
        """Analyze test quality
        
        Args:
            test_code: Test code to analyze
            
        Returns:
            dict: Analysis results
        """
        logger.info("Analyzing tests")
        return self.test_processor.analyze_tests(test_code)

    def optimize_tests(self, test_code: str) -> List[str]:
        """Get test optimization suggestions
        
        Args:
            test_code: Test code to optimize
            
        Returns:
            list: Optimization suggestions
        """
        logger.info("Optimizing tests")
        return self.test_processor.optimize_tests(test_code)

    def debug_test(self, test_code: str, error: str) -> str:
        """Debug failing tests
        
        Args:
            test_code: Failing test code
            error: Error message
            
        Returns:
            str: Debug information and fixes
        """
        logger.info("Debugging test")
        return self.test_processor.debug_test(test_code, error)

    def refactor_tests(self, test_code: str) -> str:
        """Refactor tests
        
        Args:
            test_code: Test code to refactor
            
        Returns:
            str: Refactored code
        """
        logger.info("Refactoring tests")
        return self.test_processor.refactor_tests(test_code)

    def estimate_coverage(self, code: str, test_code: str) -> Dict:
        """Estimate test coverage
        
        Args:
            code: Source code
            test_code: Test code
            
        Returns:
            dict: Coverage information
        """
        logger.info("Estimating coverage")
        return self.test_processor.estimate_coverage(code, test_code)

    def chat(self, user_message: str) -> str:
        """Chat with the assistant
        
        Args:
            user_message: User input message
            
        Returns:
            str: Assistant response
        """
        logger.info("Processing chat message")
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        system_prompt = """You are an expert Python testing assistant specialized in unit testing.
You help developers:
- Generate comprehensive unit tests
- Analyze test quality
- Debug failing tests
- Optimize test code
- Improve test coverage

Be helpful, specific, and provide actionable advice."""
        
        # For chat, we'll use limited history to avoid token overflow
        messages = [{"role": "system", "content": system_prompt}]
        messages.extend(self.conversation_history[-10:])  # Keep last 10 messages
        
        response = self.api_handler.call_api(messages)
        
        self.conversation_history.append({
            "role": "assistant",
            "content": response
        })
        
        return response

    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
        logger.info("Conversation history cleared")

    def get_help(self) -> str:
        """Get help on available commands
        
        Returns:
            str: Help information
        """
        help_text = """
╔══════════════════════════════════════════════════════════════╗
║        AI Unit Test Assistant - Available Commands           ║
╚══════════════════════════════════════════════════════════════╝

1. GENERATE TESTS
   Command: generate <code>
   Description: Generate unit tests from source code
   Example: generate def add(a, b): return a + b

2. ANALYZE TESTS
   Command: analyze <test_code>
   Description: Analyze test quality and coverage

3. OPTIMIZE TESTS
   Command: optimize <test_code>
   Description: Get optimization suggestions

4. DEBUG TEST
   Command: debug <test_code> <error_message>
   Description: Debug failing tests

5. REFACTOR TESTS
   Command: refactor <test_code>
   Description: Refactor tests for better quality

6. ESTIMATE COVERAGE
   Command: coverage <code> <test_code>
   Description: Estimate test coverage

7. CHAT
   Command: chat <message>
   Description: Ask any question about testing

8. CLEAR HISTORY
   Command: clear
   Description: Clear conversation history

9. HELP
   Command: help
   Description: Show this help message

10. EXIT
    Command: exit
    Description: Exit the application

═══════════════════════════════════════════════════════════════
        """
        return help_text
