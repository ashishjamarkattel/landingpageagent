from abc import ABC, abstractmethod
import google.generativeai as genai
from typing import Dict, List, Optional

class BaseAgent(ABC):
    """Base class for all agents"""
    
    def __init__(self, api_key: str, model_name: str = "gemini-1.5-flash"):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)
        
    @abstractmethod
    def execute(self, inputs: Dict) -> Dict:
        """Execute the agent's main task"""
        pass
    
    def _generate_content(self, prompt: str) -> str:
        """Generate content using Gemini API"""
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error generating content: {e}")
            return ""

    @abstractmethod
    def generate_name(self, prompt: str) -> str:
        """Generate a name for the app or product from a prompt"""
        pass