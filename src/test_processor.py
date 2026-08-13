"""Unit Test Processing Module"""

import logging
import re
from typing import List, Dict, Optional
from src.api_handler import OpenAIHandler

logger = logging.getLogger(__name__)


class TestProcessor:
    """Process and analyze unit tests"""

    def __init__(self):
        """Initialize Test Processor"""
        self.api_handler = OpenAIHandler()
        logger.info("Test Processor initialized")

    def generate_unit_tests(self, code: str, language: str = "python") -> str:
        """Generate unit tests from code
        
        Args:
            code: Source code to generate tests for
            language: Programming language (default: python)
            
        Returns:
            str: Generated unit tests
        """
        system_prompt = f"""You are an expert {language} test engineer. 
Generate comprehensive unit tests using pytest framework.
Include:
- Normal cases
- Edge cases
- Error handling
- Assertions

Return only the test code without explanations."""

        user_prompt = f"""Generate unit tests for this {language} code:

```{language}
{code}
```

Return complete pytest code ready to run."""

        logger.info(f"Generating unit tests for {language} code")
        return self.api_handler.generate_response(user_prompt, system_prompt)

    def analyze_tests(self, test_code: str) -> Dict[str, any]:
        """Analyze test quality and coverage
        
        Args:
            test_code: Unit test code to analyze
            
        Returns:
            dict: Analysis results
        """
        system_prompt = """You are an expert test analyst. Analyze the given unit tests and provide:
1. Coverage assessment (functions/methods tested)
2. Quality score (0-100)
3. Missing test cases
4. Edge cases not covered
5. Recommendations

Provide structured analysis."""

        user_prompt = f"""Analyze these unit tests:

```python
{test_code}
```

Provide detailed analysis in JSON format."""

        logger.info("Analyzing unit tests")
        response = self.api_handler.generate_response(user_prompt, system_prompt)
        
        return {
            "analysis": response,
            "test_code": test_code
        }

    def optimize_tests(self, test_code: str) -> List[str]:
        """Get optimization suggestions for tests
        
        Args:
            test_code: Unit test code to optimize
            
        Returns:
            list: Optimization suggestions
        """
        system_prompt = """You are an expert in Python testing best practices.
Provide specific, actionable optimization suggestions for unit tests.
Focus on:
- Code clarity and readability
- Test efficiency
- Coverage improvement
- Performance
- Best practices

Format: numbered list"""

        user_prompt = f"""Provide optimization suggestions for these tests:

```python
{test_code}
```

List specific improvements."""

        logger.info("Optimizing tests")
        response = self.api_handler.generate_response(user_prompt, system_prompt)
        
        # Parse response into list
        suggestions = [line.strip() for line in response.split('\n') if line.strip()]
        return suggestions

    def debug_test(self, test_code: str, error_message: str) -> str:
        """Help debug failing tests
        
        Args:
            test_code: Failing test code
            error_message: Error message from test failure
            
        Returns:
            str: Debug suggestions and fixes
        """
        system_prompt = """You are an expert Python debugger.
Analyze failing tests and provide:
1. Root cause analysis
2. Step-by-step fix
3. Corrected code
4. Prevention tips

Be specific and actionable."""

        user_prompt = f"""Debug this failing test:

Test Code:
```python
{test_code}
```

Error Message:
{error_message}

Provide complete debugging analysis and corrected code."""

        logger.info("Debugging test failure")
        return self.api_handler.generate_response(user_prompt, system_prompt)

    def refactor_tests(self, test_code: str) -> str:
        """Refactor tests for better quality
        
        Args:
            test_code: Test code to refactor
            
        Returns:
            str: Refactored test code
        """
        system_prompt = """You are an expert Python test refactoring specialist.
Refactor the given tests to:
- Follow best practices
- Improve readability
- Eliminate duplication
- Enhance maintainability
- Use pytest idioms

Return only the refactored code."""

        user_prompt = f"""Refactor these tests:

```python
{test_code}
```

Return clean, well-organized refactored code."""

        logger.info("Refactoring tests")
        return self.api_handler.generate_response(user_prompt, system_prompt)

    def estimate_coverage(self, code: str, test_code: str) -> Dict[str, any]:
        """Estimate test coverage
        
        Args:
            code: Source code
            test_code: Test code
            
        Returns:
            dict: Coverage estimation
        """
        system_prompt = """You are a test coverage analyst.
Estimate test coverage by analyzing source and test code.
Provide:
1. Estimated coverage percentage
2. Covered functions/methods
3. Uncovered functions/methods
4. Coverage gaps
5. Recommendations

Format: JSON structure"""

        user_prompt = f"""Estimate coverage for:

Source Code:
```python
{code}
```

Test Code:
```python
{test_code}
```

Provide detailed coverage analysis."""

        logger.info("Estimating test coverage")
        response = self.api_handler.generate_response(user_prompt, system_prompt)
        
        return {
            "coverage_estimate": response,
            "source_code": code,
            "test_code": test_code
        }
