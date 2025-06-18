import os
import google.generativeai as genai
import PIL.Image
from dotenv import load_dotenv

load_dotenv()

print("腳本開始執行...")

try:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("錯誤：找不到 GOOGLE_API_KEY，請檢查您的 .env 檔案。")
    genai.configure(api_key=api_key)
    print("API 金鑰設定成功。")
except Exception as e:
    print(e)
    exit() 
try:
    image_path = "test_images/test_ingredients.jpg"
    img = PIL.Image.open(image_path)
    print(f"成功載入圖片：{image_path}")
except FileNotFoundError:
    print(f"錯誤：找不到圖片 {image_path}，請確認檔案路徑和名稱是否正確。")
    exit()

prompt = """
你是一位專業的世界級廚師。請仔細分析這張圖片中的所有可食用食材。
根據這些食材，設計一道美味、步驟簡單的家常食譜。

請嚴格遵循以下的 JSON 格式回傳，不要包含前後任何多餘的文字或 ```json 標記：
{
  "title": "食譜的創意標題",
  "description": "一句話的食譜誘人簡介",
  "identified_ingredients": [
    {"name": "圖片中辨識出的食材1"},
    {"name": "圖片中辨識出的食材2"}
  ],
  "recipe_ingredients": [
    {"name": "食譜所需的食材1", "quantity": "份量"},
    {"name": "食譜所需的食材2", "quantity": "份量"}
  ],
  "instructions": [
    "烹飪步驟一的詳細說明",
    "烹飪步驟二的詳細說明"
  ]
}
"""

model = genai.GenerativeModel('gemini-2.0-flash')

try:
    response = model.generate_content([prompt, img])
    
    # --- 步驟 5: 輸出結果 ---
    print("\n--- Gemini 模型回傳結果 ---")
    print(response.text)
    print("--- 腳本執行完畢 ---")

except Exception as e:
    print(f"\n呼叫 API 時發生錯誤：{e}")