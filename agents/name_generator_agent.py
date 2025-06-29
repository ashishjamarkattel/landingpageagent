from agents.baseAgent import BaseAgent

class NameGeneratorAgent(BaseAgent):
    """Agent responsible for generating a catchy, brandable app name from a prompt."""
    def execute(self, inputs):
        # Not used for this agent
        pass

    def generate_name(self, prompt: str) -> str:
        name_prompt = f"""
        Generate a short, catchy, and brandable app name for the following product or idea:
        {prompt}
        
        Requirements:
        - 1-3 words
        - Memorable and easy to pronounce
        - Suitable for a modern tech product
        - Do NOT include generic words like 'app', 'platform', or 'website' in the name
        - Return ONLY the name, nothing else
        """
        name = self._generate_content(name_prompt)
        # Take only the first line, strip whitespace and quotes
        return name.strip().split('\n')[0].replace('"', '').replace("'", "") 