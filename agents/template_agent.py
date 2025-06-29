from typing import Dict, List
import json
from agents.baseAgent import BaseAgent

class TemplateAgent(BaseAgent):
    """Agent responsible for selecting and customizing templates"""
    
    def __init__(self, api_key: str, templates_dir: str = "templates"):
        super().__init__(api_key)
        self.templates_dir = templates_dir
        self.available_templates = self._load_available_templates()
    
    def _load_available_templates(self) -> List[Dict]:
        """Load available template configurations"""
        return [
            {
                "id": "startup",
                "name": "Startup Landing Page",
                "components": ["hero", "features", "testimonials", "cta", "footer"],
                "description": "Modern startup-focused design with hero section"
            },
            {
                "id": "saas",
                "name": "SaaS Product Page",
                "components": ["hero", "features", "pricing", "testimonials", "faq", "cta"],
                "description": "SaaS-focused with pricing and feature comparison"
            },
            {
                "id": "ecommerce",
                "name": "E-commerce Landing",
                "components": ["hero", "products", "benefits", "reviews", "cta"],
                "description": "Product-focused e-commerce landing page"
            },
            {
                "id": "service",
                "name": "Service Business",
                "components": ["hero", "services", "about", "testimonials", "contact"],
                "description": "Service-based business landing page"
            }
        ]
    
    def execute(self, inputs: Dict) -> Dict:
        expanded_idea = inputs.get("expanded_idea", "")
        
        prompt = f"""
        Based on the following business idea analysis, recommend the most suitable landing page template and components:
        
        Analysis: {expanded_idea}
        
        Available templates:
        {json.dumps(self.available_templates, indent=2)}
        
        Please:
        1. Select the most appropriate template
        2. Recommend specific components to include
        3. Suggest any customizations needed
        
        Return your response as a JSON object with:
        - selected_template: template id
        - components: list of component names
        - customizations: list of suggested modifications
        """
        
        template_response = self._generate_content(prompt)
        
        try:
            # Extract JSON from response
            start = template_response.find('{')
            end = template_response.rfind('}') + 1
            template_config = json.loads(template_response[start:end])
        except:
            # Fallback to default template
            template_config = {
                "selected_template": "startup",
                "components": ["hero", "features", "testimonials", "cta"],
                "customizations": []
            }
        
        return template_config

    def generate_name(self, prompt: str) -> str:
        raise NotImplementedError("This agent does not support name generation.")