import os
from dotenv import load_dotenv, find_dotenv

# .envファイルを読み込む
_ = load_dotenv(find_dotenv())

# 環境変数の取得
api_key = os.environ.get("OPENAI_API_KEY")

if api_key:
    print("OpenAI API Key successfully loaded!")
    print("API Key (for test):", api_key)
else:
    print("OpenAI API Key not found. Please check .env file and .gitignore settings.")
