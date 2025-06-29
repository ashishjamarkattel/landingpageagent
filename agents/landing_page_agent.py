from agents.baseAgent import BaseAgent
from agents.idea_analyst_agent import IdeaAnalystAgent
from agents.template_agent import TemplateAgent
from agents.content_generator_agent import ContentGeneratorAgent
from agents.landing_page_assembler import LandingPageAssembler
from agents.name_generator_agent import NameGeneratorAgent


class LandingPageGenerator:
    
    def __init__(self, gemini_api_key: str, output_dir: str = "output"):
        self.api_key = gemini_api_key
        self.output_dir = output_dir
        
        # Initialize agents
        self.name_generator = NameGeneratorAgent(gemini_api_key)
        self.idea_analyst = IdeaAnalystAgent(gemini_api_key)
        self.template_agent = TemplateAgent(gemini_api_key)
        self.content_generator = ContentGeneratorAgent(gemini_api_key)
        self.assembler = LandingPageAssembler(output_dir)
    
    def generate(self, idea: str) -> str:
        """
        Main function to generate a complete landing page from an idea
        
        Args:
            idea (str): The business idea or concept
            
        Returns:
            str: Path to the generated landing page HTML file
        """
        
        print(f"Starting landing page generation for: {idea}")
        
        # Step 0: Generate app name
        print("Generating app name...")
        app_name = self.name_generator.generate_name(idea)
        print(f"App name: {app_name}")
        
        print("Analyzing and expanding idea...")
        expanded_result = self.idea_analyst.execute({"idea": idea})
        
        print("Selecting template and components...")
        template_config = self.template_agent.execute(expanded_result)
        
        print("Generating content for components...")
        content_inputs = {
            **expanded_result,
            **template_config,
            "app_name": app_name
        }
        generated_content = self.content_generator.execute(content_inputs)
        print(" Assembling final landing page...")
        output_path = self.assembler.assemble(generated_content, template_config)
        
        print(f"Landing page generated successfully: {output_path}")
        return output_path
    
    def generate_with_feedback(self, idea: str, feedback: str = None) -> str:
        """
        Generate landing page with optional feedback for refinement
        
        Args:
            idea (str): The business idea
            feedback (str): Optional feedback for refinement
            
        Returns:
            str: Path to the generated landing page
        """
        
        if feedback:
            enhanced_idea = f"{idea}\n\nAdditional Requirements: {feedback}"
            return self.generate(enhanced_idea)
        else:
            return self.generate(idea)