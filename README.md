### Backend Requirements
- Python 3.8+
- PostgreSQL database
- Google AI API Key

### Frontend Requirements
- Flutter 3.8.1+
- Dart SDK

## Installation & Setup

### 1. Clone the Project

```bash
git clone <your-repository-url>
cd CulinaryLens
```

### 2. Backend Setup

#### 2.1 Navigate to Backend Directory
```bash
cd backend
```

#### 2.2 Create Virtual Environment
```bash
python -m venv venv

# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

#### 2.3 Install Dependencies
```bash
pip install -r requirements.txt
```

#### 2.4 Setup Environment Variables
Create a `.env` file in the project root directory:

```env
# Database connection
DATABASE_URL=postgresql://username:password@localhost:5432/culinarylens

# Google AI API Key
GOOGLE_API_KEY=your_google_ai_api_key_here
```

#### 2.5 Setup PostgreSQL Database
```bash
# Install PostgreSQL (macOS with Homebrew)
brew install postgresql
brew services start postgresql

# Create database
createdb culinarylens
```

#### 2.6 Start Backend Service
```bash
python app.py
```

The backend service will run on `http://localhost:5000`

### 3. Frontend Setup

#### 3.1 Navigate to Frontend Directory
```bash
cd frontend
```

#### 3.2 Install Flutter Dependencies
```bash
flutter pub get
```

#### 3.3 Run Frontend Application

**Web version:**
```bash
flutter run -d chrome
```

**iOS Simulator:**
```bash
flutter run -d ios
```

**Android Emulator:**
```bash
flutter run -d android
```

**Desktop (macOS):**
```bash
flutter run -d macos
```

## API Documentation

### Generate Recipe

**Endpoint:** `POST /api/recipe/generate`

**Request Format:** `multipart/form-data`

**Parameters:**
- `image` (required): Ingredient photo file
- `cooking_style` (optional): Cooking style (e.g., "Chinese", "Japanese", "Western")

**Response:**
```json
{
  "id": 1,
  "title": "Scrambled Eggs with Tomato",
  "description": "Classic home-style dish, nutritious and delicious",
  "recipe_ingredients": [
    {"name": "Eggs", "quantity": "3 pieces"},
    {"name": "Tomatoes", "quantity": "2 pieces"}
  ],
  "instructions": [
    "Beat the eggs and add a little salt for seasoning",
    "Cut tomatoes into chunks and set aside"
  ],
  "cooking_time": "15 minutes",
  "difficulty": "Easy",
  "servings": "2 servings",
  "created_at": "2024-01-01T12:00:00.000000"
}
```

## Development Tools

### Database Management
```bash
# Enter Flask shell
cd backend
python -c "from app import app, db; app.app_context().push(); db.create_all()"
```

### Test Images
The project includes test images in the `test_images/` directory:
- `test_ingredients.jpg`
- `test_ingredients2.jpg`

## Deployment

### Backend Deployment (Heroku Example)
```bash
# Install Heroku CLI
# Login to Heroku
heroku login

# Create application
heroku create your-app-name

# Set environment variables
heroku config:set DATABASE_URL=your_postgresql_url
heroku config:set GOOGLE_API_KEY=your_api_key

# Deploy
git push heroku main
```

### Frontend Deployment
```bash
# Web deployment
flutter build web

# Android APK
flutter build apk

# iOS
flutter build ios
```

## Troubleshooting

### Common Issues

1. **Backend won't start**
   - Check if PostgreSQL is running
   - Verify `.env` file is configured correctly
   - Check if Python virtual environment is activated

2. **AI generation fails**
   - Verify Google AI API Key is valid
   - Check if API quota is sufficient

3. **Frontend can't connect to backend**
   - Verify backend service is running on correct port
   - Check API endpoint configuration in frontend

## Contributing

Issues and Pull Requests are welcome!

## License

This project is licensed under the MIT License. 