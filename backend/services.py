import os
import google.generativeai as genai
import PIL.Image
import json

try:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("Error: GOOGLE_API_KEY not found. Please check your .env file.")
    genai.configure(api_key=api_key)
except Exception as e:
    print(f"Service initialization error: {e}")

# Select the model to use
MODEL_NAME = 'models/gemini-2.0-flash'
model = genai.GenerativeModel(MODEL_NAME)


def generate_recipe_from_image(image_file, cooking_style=None):
    """
    Takes an image file, calls the Gemini API, and returns the parsed recipe as a dictionary.
    """
    try:
        # Open the image file
        img = PIL.Image.open(image_file)

        # Build the base prompt
        base_prompt = """
        You are a professional world-class chef with extensive culinary experience. Carefully analyze all edible ingredients visible in this image.

        STRICT REQUIREMENTS:
        1. ONLY use ingredients that are clearly visible in the image
        2. DO NOT add ingredients that are not shown in the image
        3. For seasonings and basic cooking essentials (salt, pepper, oil, water), you may include them ONLY if they are essential for cooking the visible ingredients
        4. If you cannot create a complete recipe with only the visible ingredients, suggest what additional common household items might be needed
        5. Identify every ingredient in the image, including vegetables, meats, seasonings, spices, etc.
        6. Consider the freshness and cooking suitability of the ingredients
        7. Create a delicious, simple, home-style recipe based ONLY on the identified ingredients
        8. Provide precise quantity suggestions (based on common household portions)
        9. Cooking steps should be clear, understandable, and actionable"""

        # Add cooking style preference if specified
        if cooking_style:
            style_instruction = f"""
        6. IMPORTANT: Create the recipe in the {cooking_style} cooking style. Use traditional {cooking_style} cooking methods, seasonings, and flavor profiles."""
            base_prompt += style_instruction

        # Complete the prompt with JSON format requirements
        prompt = base_prompt + """

        Please respond STRICTLY in the following JSON format, without any extra text or ```json markers:
        {
          "title": "Creative recipe title",
          "description": "An enticing one-sentence summary of the recipe",
          "recipe_ingredients": [
            {"name": "Ingredient name", "quantity": "Specific amount (e.g., 200g, 2 pieces, to taste, etc.)"},
            {"name": "Ingredient name", "quantity": "Specific amount"}
          ],
          "instructions": [
            "Detailed cooking step 1 (include timing and heat level)",
            "Detailed cooking step 2 (include timing and heat level)"
          ],
          "cooking_time": "Estimated cooking time",
          "difficulty": "Easy/Medium/Hard",
          "servings": "Recommended servings"
        }
        """
        
        response = model.generate_content([prompt, img])
        
        # debugging: print the raw response from the model
        print(f"--- Gemini Raw Response ---\n{response.text}\n--- End of Raw Response ---")

        # Clean the response text to remove markdown code blocks if present
        response_text = response.text.strip()
        
        # Remove ```json at the beginning and ``` at the end if they exist
        if response_text.startswith('```json'):
            response_text = response_text[7:]  # Remove '```json'
        elif response_text.startswith('```'):
            response_text = response_text[3:]   # Remove '```'
            
        if response_text.endswith('```'):
            response_text = response_text[:-3]  # Remove trailing '```'

        # Parse the JSON string returned by the model
        recipe_dict = json.loads(response_text)
        return recipe_dict

    except Exception as e:
        print(f"An error occurred during recipe generation: {e}")
        return None