"""
ترجمے کی تنقیدی جائزہ - Testing Script
Translation Critique AI - Test File
"""

import json

# Test data
test_cases = [
    {
        "english": "Hello, how are you?",
        "urdu": "السلام علیکم، آپ کیسے ہیں؟"
    },
    {
        "english": "The beautiful sunset took my breath away.",
        "urdu": "خوبصورت غروب آفتاب نے میرا دم نکال دیا۔"
    },
    {
        "english": "Innovation is the key to success.",
        "urdu": "نوآوری کامیابی کی کلید ہے۔"
    }
]

# Expected response format
expected_response = {
    "translation_type": "معنوی ترجمہ",
    "accuracy_score": 85,
    "fluency_score": 90,
    "cultural_adaptation": "ہاں",
    "strengths": ["طاقت 1"],
    "weaknesses": ["کمزوری 1"],
    "improvements": ["بہتری 1"],
    "detailed_analysis": "تفصیلی تنقیدی جائزہ",
    "word_choice_analysis": "الفاظ کی تفصیل",
    "grammar_review": "گرائمر کے مسائل"
}

if __name__ == "__main__":
    print("=" * 60)
    print("🌐 ترجمے کی تنقیدی جائزہ - ٹیسٹ فائل")
    print("=" * 60)
    print()
    
    print("📝 ٹیسٹ کیسز:")
    print()
    
    for i, test in enumerate(test_cases, 1):
        print(f"{i}. English: {test['english']}")
        print(f"   Urdu: {test['urdu']}")
        print()
    
    print("=" * 60)
    print("Expected Response Format:")
    print("=" * 60)
    print(json.dumps(expected_response, ensure_ascii=False, indent=2))
    print()
    
    print("🚀 API Endpoint: POST /api/analyze")
    print("Request Format:")
    request_format = {
        "english_text": "sample english text",
        "translation": "sample urdu translation"
    }
    print(json.dumps(request_format, ensure_ascii=False, indent=2))
