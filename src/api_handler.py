"""Google Gemini API Handler Module"""

import logging
from typing import Optional
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted, InvalidArgument
from config.settings import GEMINI_API_KEY, GEMINI_MODEL, GEMINI_TEMPERATURE, GEMINI_MAX_OUTPUT_TOKENS

logger = logging.getLogger(__name__)


class GeminiHandler:
    """Handler for Google Gemini API interactions"""

    def __init__(self):
        """Initialize Gemini client"""
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = GEMINI_MODEL
        self.temperature = GEMINI_TEMPERATURE
        self.max_output_tokens = GEMINI_MAX_OUTPUT_TOKENS
        logger.info(f"Gemini Handler initialized with model: {self.model}")

    def call_api(self, messages: list, temperature: Optional[float] = None, 
                 max_tokens: Optional[int] = None) -> str:
        """Call Gemini API with error handling
        
        Args:
            messages: List of message dictionaries with 'role' and 'content'
            temperature: Optional temperature override
            max_tokens: Optional max tokens override
            
        Returns:
            str: API response content
        """
        try:
            # Initialize the model
            model = genai.GenerativeModel(self.model)
            
            # Convert messages format for Gemini
            chat_history = []
            for msg in messages[:-1]:  # All but last message
                chat_history.append({
                    "role": "user" if msg["role"] == "user" else "model",
                    "parts": [msg["content"]]
                })
            
            # Create chat session
            chat = model.start_chat(history=chat_history)
            
            # Send the last message
            response = chat.send_message(
                messages[-1]["content"],
                generation_config=genai.types.GenerationConfig(
                    temperature=temperature or self.temperature,
                    max_output_tokens=max_tokens or self.max_output_tokens
                )
            )
            
            content = response.text
            logger.info(f"API call successful")
            return content
            
        except ResourceExhausted as e:
            logger.error(f"Rate limit exceeded: {str(e)}")
            raise Exception("API rate limit exceeded. Please try again later.")
        except InvalidArgument as e:
            logger.error(f"Invalid argument: {str(e)}")
            raise Exception(f"Invalid API request: {str(e)}")
        except Exception as e:
            logger.error(f"Gemini API error: {str(e)}")
            raise Exception(f"Gemini API error: {str(e)}")

    def generate_response(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """Generate a response from Gemini
        
        Args:
            prompt: User prompt/question
            system_prompt: Optional system message
            
        Returns:
            str: Generated response
        """
        messages = []
        
        # Combine system prompt with user prompt
        if system_prompt:
            combined_prompt = f"{system_prompt}\n\n{prompt}"
        else:
            combined_prompt = prompt
        
        messages.append({"role": "user", "content": combined_prompt})
        
        return self.call_api(messages)
