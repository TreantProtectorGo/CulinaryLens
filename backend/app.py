import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from models import db, Recipe
from services import generate_recipe_from_image

# Load environment variables from the .env file
# Assumes the .env file is in the project root, one level above 'backend'
load_dotenv(dotenv_path='../.env') 

# Create the Flask application instance
app = Flask(__name__)

# --- Database Configuration ---
# Read the database connection URL from environment variables
# Example URL: "postgresql://user:password@host:port/database"
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

# --- API Routes (Endpoints) ---
@app.route('/api/recipe/generate', methods=['POST'])
def generate_recipe_endpoint():
    # 1. Check if the request contains an image file
    if 'image' not in request.files:
        return jsonify({'error': 'No image file found in the request'}), 400
    
    image_file = request.files['image']
    
    # 2. Get cooking style from form data (optional)
    cooking_style = request.form.get('cooking_style', None)
    
    # 2.5. Get source information (optional)
    source = request.form.get('source', 'direct_upload')
    
    # 3. Call the service layer to generate the recipe
    recipe_data = generate_recipe_from_image(image_file, cooking_style)
    
    if not recipe_data:
        return jsonify({'error': 'Failed to generate recipe, please try again later.'}), 500
        
    # 4. Save the generated recipe to the database
    try:
        # Log different behavior based on source
        if source == 'n8n_automation':
            print(f"📧 n8n Automation: Generated and saving recipe '{recipe_data['title']}'")
        elif source == 'flutter_app':
            print(f"📱 Flutter App: Generated and saving recipe '{recipe_data['title']}'")
        else:
            print(f"🖼️ Direct Upload: Generated and saving recipe '{recipe_data['title']}'")
            
        new_recipe = Recipe(
            title=recipe_data['title'],
            description=recipe_data['description'],
            recipe_ingredients=recipe_data['recipe_ingredients'],
            instructions=recipe_data['instructions'],
            cooking_time=recipe_data.get('cooking_time'),
            difficulty=recipe_data.get('difficulty'),
            servings=recipe_data.get('servings')
        )
        db.session.add(new_recipe)
        db.session.commit()
        
        # 5. Return the newly created recipe to the client
        return jsonify(new_recipe.to_dict()), 201
        
    except Exception as e:
        db.session.rollback() # Rollback the transaction in case of an error
        print(f"Database save error: {e}")
        return jsonify({'error': 'Internal error while saving the recipe'}), 500

@app.route('/api/recipes', methods=['GET'])
def get_all_recipes():
    """
    Get all recipes from the database - for checking if data is saved
    """
    try:
        recipes = Recipe.query.order_by(Recipe.created_at.desc()).all()
        recipe_list = [recipe.to_dict() for recipe in recipes]
        
        return jsonify({
            'total_recipes': len(recipe_list),
            'recipes': recipe_list
        }), 200
        
    except Exception as e:
        print(f"Error fetching recipes: {e}")
        return jsonify({'error': 'Failed to fetch recipes'}), 500

@app.route('/api/recipes/latest', methods=['GET'])
def get_latest_recipe():
    """
    Get the most recent recipe - useful for quick verification
    """
    try:
        latest_recipe = Recipe.query.order_by(Recipe.created_at.desc()).first()
        
        if latest_recipe:
            return jsonify({
                'message': 'Latest recipe found',
                'recipe': latest_recipe.to_dict()
            }), 200
        else:
            return jsonify({
                'message': 'No recipes found in database'
            }), 404
            
    except Exception as e:
        print(f"Error fetching latest recipe: {e}")
        return jsonify({'error': 'Failed to fetch latest recipe'}), 500

if __name__ == '__main__':
    # This block ensures that database tables are created before the app runs for the first time.
    with app.app_context():
        db.create_all()
    app.run(debug=True)