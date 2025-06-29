import os
from typing import List, Dict
from model.content import GeneratedContent
import re


class LandingPageAssembler:
    """Assembles individual components into a complete landing page"""
    
    def __init__(self, output_dir: str = "output"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def assemble(self, content_list: List[GeneratedContent], template_config: Dict) -> str:
        """Assemble components into a complete HTML page, removing unwanted characters and images."""
        html_template = """
        <!DOCTYPE html>
        <html lang=\"en\">
        <head>
            <meta charset=\"UTF-8\">
            <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
            <title>Generated Landing Page</title>
            <meta name=\"description\" content=\"A high-converting, AI-generated landing page.\">
            <meta property=\"og:title\" content=\"Generated Landing Page\">
            <meta property=\"og:description\" content=\"A high-converting, AI-generated landing page.\">
            <meta property=\"og:type\" content=\"website\">
            <meta property=\"og:image\" content=\"https://placehold.co/1200x630\">
            <link rel=\"icon\" href=\"https://www.svgrepo.com/show/303388/web.svg\" type=\"image/svg+xml\">
            <script src=\"https://cdn.tailwindcss.com\"></script>
            <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css\">
        </head>
        <body class=\"bg-gray-50\">
            {content}
        </body>
        </html>
        """
        # Combine all component content
        combined_content = "\n".join([item.content for item in content_list])
        # Remove markdown code block markers and unwanted characters
        cleaned_content = re.sub(r"```[a-zA-Z]*", "", combined_content)
        # Remove all <img ...> tags
        cleaned_content = re.sub(r"<img[^>]*>", "", cleaned_content)
        # Remove any stray </img> closing tags
        cleaned_content = re.sub(r"</img>", "", cleaned_content)
        # Remove duplicate <!DOCTYPE html> and <html>... wrappers if present
        cleaned_content = re.sub(r"<!DOCTYPE html>.*?<body[^>]*>(.*?)</body>.*?</html>", r"\1", cleaned_content, flags=re.DOTALL)
        # Remove any remaining <html>, </html>, <head>, </head>, <body>, </body> tags
        cleaned_content = re.sub(r"</?(html|head|body)[^>]*>", "", cleaned_content, flags=re.IGNORECASE)
        # Remove leading/trailing whitespace
        cleaned_content = cleaned_content.strip()
        # Generate complete HTML
        complete_html = html_template.format(content=cleaned_content)
        # Save to file
        output_path = os.path.join(self.output_dir, "landingpage.html")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(complete_html)
        return output_path
