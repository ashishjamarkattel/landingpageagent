# AI Landing Page Builder

## Overview
This project is an AI-powered landing page builder that generates beautiful, conversion-focused landing pages for any business idea. It uses Google Gemini (Generative AI) to analyze your idea, select the best template, generate high-quality content for each section, and assemble everything into a single, production-ready HTML file.

## Features
- Uses Google Gemini API for all AI content generation
- Generates a catchy, brandable app name for your idea
- Supports multiple landing page sections (hero, features, testimonials, pricing, FAQ, about, contact, etc.)
- Ensures visually appealing, readable, and modern design (Tailwind CSS)
- Outputs a single `landingpage.html` file
- Fully customizable and extensible agent-based architecture

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd webbuilder
```

### 2. Install Python & Dependencies
- Python 3.8+
- Install dependencies:
```bash
pip install -r requirement.txt
```

### 3. Set Up Environment Variables
Create a `.env` file in the project root with your Gemini API key:
```
GEMINI_API_KEY=your_google_gemini_api_key_here
```

### 4. (Optional) Install Node.js (for Tailwind CSS CDN, not required for backend)

## How to Run
```bash
python builder.py
```
- The generated landing page will be saved as `output/landingpage.html`.
- Open this file in your browser to view the result.

## How It Works
1. **App Name Generation:** Uses Gemini to create a catchy app name from your idea.
2. **Idea Analysis:** Expands and analyzes your idea for market fit, features, and value.
3. **Template Selection:** Picks the best template and components for your idea.
4. **Content Generation:** Generates high-quality HTML for each section (no full HTML pages, only fragments).
5. **Assembly:** Combines all sections into a single, beautiful HTML file with proper meta tags and styling.

## Project Structure
```
webbuilder/
  agents/
    baseAgent.py              # Abstract base class for all agents
    name_generator_agent.py   # Generates app names
    idea_analyst_agent.py     # Expands and analyzes ideas
    template_agent.py         # Selects templates and components
    content_generator_agent.py# Generates HTML for each section
    landing_page_assembler.py # Assembles the final HTML file
  model/
    content.py                # Data class for generated content
  builder.py                  # Entry point for running the builder
  requirement.txt             # Python dependencies
  output/                     # Generated landing pages
```

## Customization
- **Add/Remove Sections:** Edit `agents/template_agent.py` and `agents/content_generator_agent.py` to change supported sections.
- **Change Styling:** Modify Tailwind CSS classes in the prompts in `content_generator_agent.py`.
- **Change App Name Logic:** See `name_generator_agent.py` for how names are generated.

## Example Usage
Edit `builder.py` to change the test idea:
```python
test_ideas = [
    "AI-powered fitness app that creates personalized workout plans",
]
```
Run the builder and check `output/landingpage.html`.

## Troubleshooting
- **Gemini API Key Error:** Make sure your `.env` file is set up and the key is valid.
- **No Output:** Check for errors in the terminal. Ensure all dependencies are installed.
- **Text Visibility Issues:** Prompts are tuned for readability, but you can further tweak Tailwind classes in the prompts.

## License
MIT License 