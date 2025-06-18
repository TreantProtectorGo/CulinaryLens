from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSONB
import datetime

# Create a SQLAlchemy database instance
db = SQLAlchemy()

class Recipe(db.Model):
    # Define columns for the 'recipe' table
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    
    # Store the complex list data from the LLM directly as JSON.
    # This is flexible and makes it easy to add more fields later.
    recipe_ingredients = db.Column(JSONB, nullable=False)
    instructions = db.Column(JSONB, nullable=False)
    
    # New fields for enhanced recipe information
    cooking_time = db.Column(db.String(100), nullable=True)
    difficulty = db.Column(db.String(20), nullable=True)
    servings = db.Column(db.String(100), nullable=True)
    
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    # A helper method to convert the Recipe object to a dictionary
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'recipe_ingredients': self.recipe_ingredients,
            'instructions': self.instructions,
            'cooking_time': self.cooking_time,
            'difficulty': self.difficulty,
            'servings': self.servings,
            'created_at': self.created_at.isoformat()
        }