import requests
import os
from dotenv import load_dotenv
import logging
from typing import List, Dict

# Configure logger  
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

# Environment variable for API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY') 

API_URL = "https://api.openai.com/v1/engines/gpt-4-1106-preview/completions"

class OpenAIAPI:

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def analyze_writing(self, writing_samples: List[str]) -> Dict:
        """Analyze writing samples and return analysis."""
        prompt = self._build_prompt(writing_samples)
        response = self._generate_text(prompt, max_tokens=1000)
        return self._parse_response(response)

    def _build_prompt(self, writing_samples: List[str]) -> str:
        """Build prompt from writing samples."""
        return "Analyze these writing samples: " + " ".join(writing_samples)

    def _generate_text(self, prompt: str, max_tokens: int) -> dict:
        """Generate text from prompt using GPT-3."""
        
        # API request code
        
    def _parse_response(self, response: dict) -> dict: 
        """Extract analysis from API response."""
        
        # Parse response JSON
        
