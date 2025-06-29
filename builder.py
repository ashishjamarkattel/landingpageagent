import os
from dotenv import load_dotenv
from agents.landing_page_agent import LandingPageGenerator
load_dotenv()




def main():
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Please set GEMINI_API_KEY in your environment variables")
        return
    
    # Create the generator
    generator = LandingPageGenerator(api_key)
    
    # Example ideas to test
    test_ideas = [
        "A platform for connecting freelancers with small businesses",
    ]
    
    # Generate landing page for the first idea
    idea = test_ideas[0]
    output_path = generator.generate(idea)
    
    print(f" Generated landing page saved to: {output_path}")
    print("Open the HTML file in your browser to view the result!")

if __name__ == "__main__":
    main()