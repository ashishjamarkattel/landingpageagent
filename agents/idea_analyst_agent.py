from typing import Dict
from agents.baseAgent import BaseAgent

class IdeaAnalystAgent(BaseAgent):
    """Agent responsible for expanding and analyzing ideas"""
    
    def execute(self, inputs: Dict) -> Dict:
        idea = inputs.get("idea", "")
        
        prompt = f"""
        As a senior idea analyst, expand and analyze the following business idea comprehensively:
        
        Idea: {idea}
        
        Please provide:
        1. Market analysis and target audience
        2. Unique value proposition
        3. Key features and benefits
        4. Competitive advantages
        5. Business model suggestions
        6. Marketing angles
        
        Format your response as a detailed analysis that can be used to create compelling landing page content.
        Make it professional, engaging, and conversion-focused.
        """
        
        expanded_idea = self._generate_content(prompt)
        
        return {
            "expanded_idea": expanded_idea,
            "original_idea": idea
        }

    def generate_name(self, prompt: str) -> str:
        raise NotImplementedError("This agent does not support name generation.")
