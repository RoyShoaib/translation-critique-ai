# 🌐 ترجمے کی تنقیدی جائزہ AI

**Translation Critique AI** - Google Gemini کی مدد سے انگریزی متن اور اس کے اردو ترجمے کا تنقیدی جائزہ لینے والا ایک جدید ویب ایپلیکیشن۔

## ✨ خصوصیات

### 1. **ترجمے کی قسم کی شناخت**
   - لفظی ترجمہ (Literal Translation)
   - معنوی ترجمہ (Semantic Translation)
   - آزادانہ ترجمہ (Free Translation)
   - رشتہ دار ترجمہ (Relative Translation)
   - فارغ ترجمہ (Functional Translation)

### 2. **مکمل تنقیدی تجزیہ**
   - **درستگی کے نمرات** (0-100)
   - **روانی کے نمرات** (0-100)
   - **ثقافتی موافقت** کی شناخت
   - **الفاظ کے انتخاب** کی تفصیل
   - **گرائمر کے مسائل** کی نشاندہی

### 3. **تفصیلی رپورٹ**
   - طاقتیں اور کمزوریاں
   - بہتری کی تجاویز
   - تفصیلی تنقیدی جائزہ

### 4. **صارف دوست انٹرفیس**
   - جدید ڈیزائن
   - اردو میں مکمل سپورٹ
   - موبائل فرینڈلی
   - تیز اور قابل اعتماد

## 🚀 شروعات کریں

### ضروری چیزیں
- Python 3.8+
- pip (Python Package Manager)
- Google Gemini API Key

### Step 1: Repository Clone کریں
```bash
git clone https://github.com/RoyShoaib/translation-critique-ai.git
cd translation-critique-ai
```

### Step 2: Virtual Environment بنائیں
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Dependencies Install کریں
```bash
pip install -r requirements.txt
```

### Step 4: Environment Variables سیٹ کریں
```bash
# .env فائل بنائیں
cp .env.example .env
```

`.env` فائل میں Google API Key شامل کریں:
```
GOOGLE_API_KEY=your_google_gemini_api_key_here
FLASK_ENV=development
FLASK_PORT=5000
```

### Step 5: Google Gemini API Key حاصل کریں

1. [Google AI Studio](https://makersuite.google.com/app/apikey) پر جائیں
2. "Create API Key" پر کلک کریں
3. اپنی API Key کاپی کریں
4. `.env` فائل میں شامل کریں

### Step 6: ایپلیکیشن چلائیں
```bash
python app.py
```

### Step 7: کھولیں اور استعمال کریں
```
http://localhost:5000
```

## 📚 استعمال کی مثال

### انگریزی متن:
```
The quick brown fox jumps over the lazy dog.
```

### اردو ترجمہ:
```
تیز رفتار بھوری لومڑی سست کتے کے اوپر سے کود جاتی ہے۔
```

### نتیجہ:
- **قسم**: معنوی ترجمہ
- **درستگی**: 85/100
- **روانی**: 92/100
- **ثقافتی موافقت**: ہاں
- **طاقتیں**: بہترین معنوی ترجمہ، بہترین اردو روانی
- **بہتری**: کچھ الفاظ کو مزید رسمی بنایا جا سکتا ہے

## 🛠️ تکنیکی معلومات

### Architecture
```
translation-critique-ai/
├── app.py                 # Flask ایپلیکیشن
├── requirements.txt       # Python Dependencies
├── .env.example          # Environment Variables
├── templates/
│   └── index.html        # HTML انٹرفیس
└── static/
    ├── style.css         # CSS سٹائل
    └── script.js         # JavaScript کوڈ
```

### استعمال شدہ ٹیکنالوجی
- **Backend**: Flask (Python)
- **AI Model**: Google Gemini Pro
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **API**: Flask RESTful API

## 🔒 سیکیورٹی

- API Keys کو `.env` فائل میں محفوظ رکھیں
- `.env` فائل کو git میں شامل نہ کریں
- صرف HTTPS استعمال کریں (production میں)

## 📝 API Endpoints

### `/api/analyze` (POST)
ترجمے کا تنقیدی جائزہ لیں

**Request:**
```json
{
    "english_text": "Hello, how are you?",
    "translation": "السلام علیکم، آپ کیسے ہیں؟"
}
```

**Response:**
```json
{
    "success": true,
    "analysis": {
        "translation_type": "معنوی ترجمہ",
        "accuracy_score": 90,
        "fluency_score": 95,
        "cultural_adaptation": "ہاں",
        "strengths": [...],
        "weaknesses": [...],
        "improvements": [...]
    }
}
```

### `/api/translation-types` (GET)
تمام ترجمے کی اقسام حاصل کریں

## 🤝 شراکت

اگر آپ اس پروجیکٹ میں بہتری لانا چاہتے ہیں:

1. Repository Fork کریں
2. Feature Branch بنائیں (`git checkout -b feature/AmazingFeature`)
3. اپنی تبدیلیاں Commit کریں (`git commit -m 'Add some AmazingFeature'`)
4. Branch کو Push کریں (`git push origin feature/AmazingFeature`)
5. Pull Request کھولیں

## 📄 لائسنس

یہ پروجیکٹ MIT License کے تحت ہے۔

## 👨‍💻 ڈیولپر

**RoyShoaib**
- GitHub: [@RoyShoaib](https://github.com/RoyShoaib)

## 📞 رابطہ

اگر کوئی سوال یا تجویز ہے تو براہ مہربانی Issue بھیجیں۔

## 🙏 شکریہ

- Google Gemini AI
- Flask Community
- Open Source Contributors

---

**نوٹ**: یہ ٹول تعلیمی اور ترجمہ کاری کے مقاصد کے لیے ہے۔ اہم ترجموں کے لیے انسانی نگرانی ضروری ہے۔

**Note**: This tool is for educational and translation purposes. Human review is recommended for critical translations.
