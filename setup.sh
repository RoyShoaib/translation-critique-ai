#!/bin/bash

# Translation Critique AI - Setup Script

echo "🌐 ترجمے کی تنقیدی جائزہ - سیٹ اپ شروع ہو رہا ہے..."
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 نہیں ہے۔ براہ مہربانی Python 3.8+ انسٹال کریں"
    exit 1
fi

echo "✅ Python3 موجود ہے"

# Create virtual environment
echo "📦 Virtual Environment بنا رہے ہیں..."
python3 -m venv venv

# Activate virtual environment
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

echo "✅ Virtual Environment فعال ہو گیا"

# Install dependencies
echo "📚 Dependencies انسٹال کر رہے ہیں..."
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ تمام Dependencies انسٹال ہو گئے"

# Check .env file
if [ ! -f .env ]; then
    echo "⚠️  .env فائل نہیں ہے"
    echo "📝 .env فائل بنا رہے ہیں..."
    cp .env.example .env
    echo "💡 براہ مہربانی .env میں اپنی Google API Key داخل کریں"
else
    echo "✅ .env فائل موجود ہے"
fi

echo ""
echo "🎉 سیٹ اپ مکمل ہو گیا!"
echo ""
echo "📍 ایپلیکیشن چلانے کے لیے:"
echo "   python app.py"
echo ""
echo "🌐 پھر براؤزر میں کھولیں:"
echo "   http://localhost:5000"
echo ""
