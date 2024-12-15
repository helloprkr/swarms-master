"""Models module for Swarms."""
from typing import Optional, Dict, Any

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
        self.openai_api_key = openai_api_key
        self.openai_api_base = openai_api_base
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.kwargs = kwargs 