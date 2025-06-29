from typing import Dict, List
from model.content import GeneratedContent
from agents.baseAgent import BaseAgent
import re


class ContentGeneratorAgent(BaseAgent):
    """Agent responsible for generating content for each component"""
    
    def execute(self, inputs: Dict) -> List[GeneratedContent]:
        expanded_idea = inputs.get("expanded_idea", "")
        components = inputs.get("components", [])
        template_id = inputs.get("selected_template", "startup")
        app_name = inputs.get("app_name", "FitGenius")
        
        generated_content = []
        
        for component in components:
            content = self._generate_component_content(expanded_idea, component, template_id, app_name)
            generated_content.append(content)
        
        return generated_content
    
    def _generate_component_content(self, idea: str, component: str, template_id: str, app_name: str = None) -> GeneratedContent:
        """Generate content for a specific component, replacing [App Name] and removing instructional text."""
        if not app_name:
            app_name = ""
        component_prompts = {
            "hero": f"""
            Create ONLY the HTML for a hero section for a {template_id} landing page based on:
            {idea}
            
            Include:
            - Catchy headline (under 10 words)
            - Compelling subheadline (under 25 words)
            - Primary CTA button text
            - Brief value proposition
            
            Format as HTML with Tailwind CSS classes. For light backgrounds (bg-white, bg-gray-100), use text-gray-900 for headings and text-gray-700 for body text. For dark or colored backgrounds (e.g., bg-blue-500, bg-gradient-to-r), use text-white for all text. DO NOT include <html>, <head>, or <body> tags. Only return the section HTML.
            """,
            
            "features": f"""
            Create ONLY the HTML for a features section highlighting key benefits based on:
            {idea}
            
            Include:
            - 3-6 key features
            - Each feature should have a title, description, and icon suggestion
            - Focus on benefits, not just features
            
            Format as HTML with Tailwind CSS classes. For light backgrounds (bg-white, bg-gray-100), use text-gray-900 for headings and text-gray-700 for body text. For dark or colored backgrounds, use text-white. DO NOT include <html>, <head>, or <body> tags. Only return the section HTML.
            """,
            
            "testimonials": f"""
            Create ONLY the HTML for a testimonials section for:
            {idea}
            
            Include:
            - 3 customer testimonials
            - Customer names and titles/companies
            - Specific benefits mentioned
            - Star ratings
            
            Format as HTML with Tailwind CSS classes. For light backgrounds (bg-white, bg-gray-100), use text-gray-900 for headings and text-gray-700 for body text. For dark or colored backgrounds, use text-white. DO NOT include <html>, <head>, or <body> tags. Only return the section HTML.
            """,
            
            "cta": f"""
            Create ONLY the HTML for a call-to-action section for:
            {idea}
            
            Include:
            - Urgency-driven headline
            - Brief benefit statement
            - Primary action button
            - Secondary action (if applicable)
            
            Format as HTML with Tailwind CSS classes. For dark or colored backgrounds (e.g., bg-blue-500, bg-gradient-to-r), use text-white for all text. For light backgrounds, use text-gray-900 for headings and text-gray-700 for body text. DO NOT include <html>, <head>, or <body> tags. Only return the section HTML.
            """,
            
            "pricing": f"""
            Create ONLY the HTML for a pricing section for:
            {idea}
            
            Include:
            - 2-3 pricing tiers
            - Feature comparisons
            - Recommended plan highlight
            - Clear pricing and billing terms
            
            Format as HTML with Tailwind CSS classes. For light backgrounds (bg-white, bg-gray-100), use text-gray-900 for headings and text-gray-700 for body text. For dark backgrounds, use text-white. DO NOT include <html>, <head>, or <body> tags. Only return the section HTML.
            """,
            
            "footer": f"""
            Create ONLY the HTML for a footer section for:
            {idea}
            
            Include:
            - Company/product name
            - Key navigation links
            - Social media placeholders
            - Contact information
            - Legal links
            
            Format as HTML with Tailwind CSS classes. For dark backgrounds, use text-white. For light backgrounds, use text-gray-900 for headings and text-gray-700 for body text. DO NOT include <html>, <head>, or <body> tags. Only return the section HTML.
            """,
            
            "faq": f"""
            Create ONLY the HTML for a frequently asked questions (FAQ) section for:
            {idea}
            
            Include:
            - 4-6 common questions and answers
            - Questions relevant to the product/service
            
            Format as HTML with Tailwind CSS classes. For light backgrounds (bg-white, bg-gray-100), use text-gray-900 for questions and text-gray-700 for answers. For dark backgrounds, use text-white. Use an accordion or collapsible style. DO NOT include <html>, <head>, or <body> tags. Only return the section HTML.
            """,
            
            "products": f"""
            Create ONLY the HTML for a products section for:
            {idea}
            
            Include:
            - 3-6 featured products
            - Each with name, image placeholder, description, and price
            
            Format as HTML with Tailwind CSS classes. For light backgrounds (bg-white, bg-gray-100), use text-gray-900 for product names and text-gray-700 for descriptions. For dark backgrounds, use text-white. Use a grid or card layout. DO NOT include <html>, <head>, or <body> tags. Only return the section HTML.
            """,
            
            "benefits": f"""
            Create ONLY the HTML for a benefits section for:
            {idea}
            
            Include:
            - 3-5 key benefits
            - Each benefit with a title, short description, and icon suggestion
            
            Format as HTML with Tailwind CSS classes. For light backgrounds (bg-white, bg-gray-100), use text-gray-900 for headings and text-gray-700 for body text. For dark backgrounds, use text-white. Use a visually engaging layout. DO NOT include <html>, <head>, or <body> tags. Only return the section HTML.
            """,
            
            "reviews": f"""
            Create ONLY the HTML for a customer reviews section for:
            {idea}
            
            Include:
            - 3-5 customer reviews
            - Reviewer names, star ratings, and specific feedback
            
            Format as HTML with Tailwind CSS classes. For light backgrounds (bg-white, bg-gray-100), use text-gray-900 for reviewer names and text-gray-700 for review text. For dark backgrounds, use text-white. Use a testimonial/review card style. DO NOT include <html>, <head>, or <body> tags. Only return the section HTML.
            """,
            
            "services": f"""
            Create ONLY the HTML for a services section for:
            {idea}
            
            Include:
            - 3-6 services offered
            - Each with a title, description, and icon suggestion
            
            Format as HTML with Tailwind CSS classes. For light backgrounds (bg-white, bg-gray-100), use text-gray-900 for headings and text-gray-700 for body text. For dark backgrounds, use text-white. Use a modern, clean layout. DO NOT include <html>, <head>, or <body> tags. Only return the section HTML.
            """,
            
            "about": f"""
            Create ONLY the HTML for an about section for:
            {idea}
            
            Include:
            - Company/brand story
            - Mission statement
            - Key team members (names and roles)
            
            Format as HTML with Tailwind CSS classes. For light backgrounds (bg-white, bg-gray-100), use text-gray-900 for headings and text-gray-700 for body text. For dark backgrounds, use text-white. Use a friendly, approachable style. DO NOT include <html>, <head>, or <body> tags. Only return the section HTML.
            """,
            
            "contact": f"""
            Create ONLY the HTML for a contact section for:
            {idea}
            
            Include:
            - Contact form (name, email, message)
            - Company address and phone (placeholder)
            - Map or location placeholder
            
            Format as HTML with Tailwind CSS classes. For light backgrounds (bg-white, bg-gray-100), use text-gray-900 for headings and text-gray-700 for body text. For dark backgrounds, use text-white. Use a clean, accessible layout. DO NOT include <html>, <head>, or <body> tags. Only return the section HTML.
            """
        }
        
        prompt = component_prompts.get(component, f"Create ONLY the HTML for a {component} section for: {idea}. DO NOT include <html>, <head>, or <body> tags. Only return the section HTML.")
        content = self._generate_content(prompt)
        # Replace [App Name] with the app name
        content = content.replace("[App Name]", app_name)
        # Remove instructional/breakdown text (e.g., lines starting with 'This HTML uses', 'Remember to replace', etc.)
        content = re.sub(r"(^|\n)(This HTML uses|Remember to replace|You can adjust|Here's a breakdown:|\*\*).*(\n|$)", "\n", content)
        # Remove any remaining markdown code block markers
        content = re.sub(r"```[a-zA-Z]*", "", content)
        return GeneratedContent(
            title=f"{component.title()} Section",
            content=content.strip(),
            component_type=component,
            file_path=f"components/{component}.html"
        )

    def generate_name(self, prompt: str) -> str:
        raise NotImplementedError("This agent does not support name generation.")
