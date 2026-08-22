from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv
import json

load_dotenv()

app = Flask(__name__)
CORS(app)

# Google Gemini API Configuration
api_key = os.getenv('GOOGLE_API_KEY')
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment variables")

genai.configure(api_key=api_key)

# Translation types in Urdu and English
TRANSLATION_TYPES = {
    "لفظی ترجمہ": "Literal Translation - Direct word-for-word translation",
    "معنوی ترجمہ": "Semantic Translation - Preserves meaning while adapting to target language",
    "آزادانہ ترجمہ": "Free Translation - Prioritizes fluency over literal accuracy",
    "رشتہ دار ترجمہ": "Relative Translation - Maintains stylistic and cultural elements",
    "فارغ ترجمہ": "Functional Translation - Focuses on communicative function"
}

def analyze_translation(english_text, translation):
    """
    Use Google Gemini to analyze translation and classify it
    """
    prompt = f"""
آپ ایک ترجمے کی تنقید کار ہیں۔ براہ مہربانی مندرجہ ذیل انگریزی متن اور اس کے اردو ترجمے کا تنقیدی جائزہ لیں:

انگریزی متن:
"{english_text}"

اردو ترجمہ:
"{translation}"

براہ مہربانی مندرجہ ذیل معلومات JSON فارمیٹ میں فراہم کریں:

{{
    "translation_type": "درج ذیل میں سے ایک - لفظی ترجمہ، معنوی ترجمہ، آزادانہ ترجمہ، رشتہ دار ترجمہ، یا فارغ ترجمہ",
    "accuracy_score": 0-100 (درستگی کا اسکور),
    "fluency_score": 0-100 (روانی کا اسکور),
    "cultural_adaptation": "ہاں/نہیں",
    "strengths": ["طاقت 1", "طاقت 2", "طاقت 3"],
    "weaknesses": ["کمزوری 1", "کمزوری 2"],
    "improvements": ["بہتری کی تجویز 1", "بہتری کی تجویز 2"],
    "detailed_analysis": "تفصیلی تنقیدی جائزہ اردو میں",
    "word_choice_analysis": "الفاظ کے انتخاب کی تفصیل",
    "grammar_review": "گرائمر کے مسائل اگر ہوں"
}}

براہ مہربانی صرف JSON جواب دیں، کوئی اور متن نہیں۔
"""
    
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        
        # Extract JSON from response
        response_text = response.text.strip()
        
        # If response contains markdown code block, extract it
        if "```json" in response_text:
            response_text = response_text.split("```json")[1].split("```")[0].strip()
        elif "```" in response_text:
            response_text = response_text.split("```")[1].split("```")[0].strip()
        
        analysis = json.loads(response_text)
        return analysis
    
    except json.JSONDecodeError as e:
        return {"error": f"JSON parsing error: {str(e)}", "raw_response": response_text}
    except Exception as e:
        return {"error": str(e)}

@app.route('/')
def index():
    """Render main page"""
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    """API endpoint for translation analysis"""
    try:
        data = request.json
        english_text = data.get('english_text', '').strip()
        translation = data.get('translation', '').strip()
        
        if not english_text or not translation:
            return jsonify({'error': 'دونوں متن ضروری ہیں (Both texts are required)'}), 400
        
        # Analyze translation
        analysis = analyze_translation(english_text, translation)
        
        return jsonify({
            'success': True,
            'english_text': english_text,
            'translation': translation,
            'analysis': analysis
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/translation-types', methods=['GET'])
def get_translation_types():
    """Get available translation types"""
    return jsonify(TRANSLATION_TYPES)

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Page not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    port = int(os.getenv('FLASK_PORT', 5000))
    app.run(debug=True, port=port, host='0.0.0.0')
