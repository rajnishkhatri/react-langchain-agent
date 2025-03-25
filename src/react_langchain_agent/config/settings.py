"""Configuration settings for the React LangChain Agent."""
import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings:
    """Application settings and configuration."""
    
    # OpenAI settings
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    
    # LLM settings
    TEMPERATURE: float = 0.0
    STOP_SEQUENCES: list[str] = ["\nObservation", "Observation"]
    
    @classmethod
    def validate(cls) -> list[str]:
        """Validate the settings and return a list of error messages."""
        errors = []
        if not cls.OPENAI_API_KEY:
            errors.append("OPENAI_API_KEY is not set in environment variables")
        return errors

# Global settings instance
settings = Settings() 