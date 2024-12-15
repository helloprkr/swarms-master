"""OpenAI Chat model implementation."""
import os
from typing import Optional, Dict, Any
from openai import OpenAI

class OpenAIChat:
    """OpenAI Chat model wrapper."""
    
    def __init__(
        self,
        model_name: str = "gpt-4",
        openai_api_key: Optional[str] = None,
        openai_api_base: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 1000,
        **kwargs: Dict[str, Any]
    ):
        self.model_name = model_name
        self.openai_api_key = openai_api_key or os.getenv("OPENAI_API_KEY")
        self.openai_api_base = openai_api_base
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.kwargs = kwargs
        
        # Initialize OpenAI client
        self.client = OpenAI(
            api_key=self.openai_api_key,
            base_url=self.openai_api_base
        )

    def generate(self, prompt: str) -> str:
        """Generate a response using the OpenAI Chat model."""
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}],
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                **self.kwargs
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error generating response: {e}")
            return str(e) 