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
