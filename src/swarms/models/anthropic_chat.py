"""Anthropic Chat model implementation."""
import os
from typing import Optional, Dict, Any
from anthropic import Anthropic, APIError, APIConnectionError, RateLimitError

class AnthropicChat:
    """Anthropic Chat model wrapper."""
    
    def __init__(
        self,
        model_name: str = "claude-2.1",
        anthropic_api_key: Optional[str] = None,
        max_tokens: int = 1000,
        temperature: float = 0.7,
        **kwargs: Dict[str, Any]
    ):
        self.model_name = model_name
        self.anthropic_api_key = anthropic_api_key or os.getenv("ANTHROPIC_API_KEY")
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.kwargs = kwargs
        
        if not self.anthropic_api_key:
            raise ValueError("Anthropic API key is required")
            
        # Initialize Anthropic client
        self.client = Anthropic(api_key=self.anthropic_api_key)

    def generate(self, prompt: str) -> str:
        """Generate a response using the Anthropic Chat model."""
        try:
            # Create the message
            message = self.client.messages.create(
                model=self.model_name,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
            
            # Extract and return the response text
            if message and message.content and len(message.content) > 0:
                return message.content[0].text
            return "No response generated"
            
        except APIError as e:
            print(f"Anthropic API Error: {e}")
            return f"Anthropic API Error: {str(e)}"
        except APIConnectionError as e:
            print(f"Anthropic API Connection Error: {e}")
            return f"Connection Error: {str(e)}"
        except RateLimitError as e:
            print(f"Anthropic Rate Limit Error: {e}")
            return f"Rate Limit Error: {str(e)}"
        except Exception as e:
            print(f"Unexpected error: {e}")
            return f"Error: {str(e)}" 