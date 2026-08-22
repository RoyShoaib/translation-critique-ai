@echo off
REM Translation Critique AI - Setup Script for Windows

echo.
echo 🌐 ترجمے کی تنقیدی جائزہ - سیٹ اپ شروع ہو رہا ہے...
echo.

REM Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python نہیں ہے۔ براہ مہربانی Python 3.8+ انسٹال کریں
    exit /b 1
)

echo ✅ Python موجود ہے

REM Create virtual environment
echo 📦 Virtual Environment بنا رہے ہیں...
python -m venv venv

echo ✅ Virtual Environment بن گیا

REM Activate virtual environment
call venv\Scripts\activate.bat

echo ✅ Virtual Environment فعال ہو گیا

REM Install dependencies
echo 📚 Dependencies انسٹال کر رہے ہیں...
python -m pip install --upgrade pip
pip install -r requirements.txt

echo ✅ تمام Dependencies انسٹال ہو گئے

REM Check .env file
if not exist .env (
    echo ⚠️  .env فائل نہیں ہے
    echo 📝 .env فائل بنا رہے ہیں...
    copy .env.example .env
    echo 💡 براہ مہربانی .env میں اپنی Google API Key داخل کریں
) else (
    echo ✅ .env فائل موجود ہے
)

echo.
echo 🎉 سیٹ اپ مکمل ہو گیا!
echo.
echo 📍 ایپلیکیشن چلانے کے لیے:
echo    python app.py
echo.
echo 🌐 پھر براؤزر میں کھولیں:
echo    http://localhost:5000
echo.
pause
