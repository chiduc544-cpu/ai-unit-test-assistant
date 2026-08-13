"""OpenAI API Handler Module"""

import logging
from typing import Optional
from openai import OpenAI, APIError, RateLimitError, APIConnectionError
from config.settings import OPENAI_API_KEY, OPENAI_MODEL, OPENAI_TEMPERATURE, OPENAI_MAX_TOKENS

logger = logging.getLogger(__name__)


class OpenAIHandler:
    """Handler for OpenAI API interactions"""

    def __init__(self):
        """Initialize OpenAI client"""
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = OPENAI_MODEL
        self.temperature = OPENAI_TEMPERATURE
        self.max_tokens = OPENAI_MAX_TOKENS
        logger.info(f"OpenAI Handler initialized with model: {self.model}")

    def call_api(self, messages: list, temperature: Optional[float] = None, 
                 max_tokens: Optional[int] = None) -> str:
        """Call OpenAI API with error handling
        
        Args:
            messages: List of message dictionaries
            temperature: Optional temperature override
            max_tokens: Optional max tokens override
            
        Returns:
            str: API response content
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature or self.temperature,
                max_tokens=max_tokens or self.max_tokens
            )
            
            content = response.choices[0].message.content
            logger.info(f"API call successful. Tokens used: {response.usage.total_tokens}")
            return content
            
        except RateLimitError as e:
            logger.error(f"Rate limit exceeded: {str(e)}")
            raise Exception("API rate limit exceeded. Please try again later.")
        except APIConnectionError as e:
            logger.error(f"API connection error: {str(e)}")
            raise Exception("Failed to connect to OpenAI API. Check your internet connection.")
        except APIError as e:
            logger.error(f"OpenAI API error: {str(e)}")
            raise Exception(f"OpenAI API error: {str(e)}")
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            raise

    def generate_response(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """Generate a response from OpenAI
        
        Args:
            prompt: User prompt/question
            system_prompt: Optional system message
            
        Returns:
            str: Generated response
        """
        messages = []
        
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        
        messages.append({"role": "user", "content": prompt})
        
        return self.call_api(messages)
