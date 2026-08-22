// DOM Elements
const englishTextArea = document.getElementById('english-text');
const urduTranslationArea = document.getElementById('urdu-translation');
const analyzeBtn = document.getElementById('analyze-btn');
const newAnalysisBtn = document.getElementById('new-analysis-btn');
const resultsSection = document.getElementById('results-section');
const loadingIndicator = document.getElementById('loading-indicator');
const resultsContent = document.getElementById('results-content');
const errorMessageDiv = document.getElementById('error-message');

// Event Listeners
analyzeBtn.addEventListener('click', analyzeTranslation);
newAnalysisBtn.addEventListener('click', resetForm);

// Main Analysis Function
async function analyzeTranslation() {
    const englishText = englishTextArea.value.trim();
    const urduTranslation = urduTranslationArea.value.trim();

    // Validation
    if (!englishText || !urduTranslation) {
        showError('براہ مہربانی دونوں متن داخل کریں (Please enter both texts)');
        return;
    }

    // Show loading state
    resultsSection.style.display = 'grid';
    loadingIndicator.style.display = 'flex';
    resultsContent.style.display = 'none';
    errorMessageDiv.style.display = 'none';
    analyzeBtn.disabled = true;

    try {
        const response = await fetch('/api/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                english_text: englishText,
                translation: urduTranslation
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || 'تجزیہ میں خرابی');
        }

        // Process and display results
        displayResults(data.analysis);
        loadingIndicator.style.display = 'none';
        resultsContent.style.display = 'grid';

    } catch (error) {
        loadingIndicator.style.display = 'none';
        showError(error.message);
    } finally {
        analyzeBtn.disabled = false;
    }
}

// Display Results Function
function displayResults(analysis) {
    if (analysis.error) {
        showError('AI سے جواب حاصل نہیں ہو سکا: ' + analysis.error);
        return;
    }

    // Translation Type
    const typeName = document.getElementById('type-name');
    const typeDescription = document.getElementById('type-description');
    
    typeName.textContent = analysis.translation_type || 'نامعلوم';
    typeDescription.textContent = getTranslationTypeDescription(analysis.translation_type);

    // Scores
    updateScoreBar('accuracy-bar', analysis.accuracy_score);
    updateScoreBar('fluency-bar', analysis.fluency_score);
    document.getElementById('accuracy-score').textContent = `${analysis.accuracy_score}/100`;
    document.getElementById('fluency-score').textContent = `${analysis.fluency_score}/100`;

    // Cultural Adaptation
    const culturalAdapt = document.getElementById('cultural-adapt');
    culturalAdapt.textContent = analysis.cultural_adaptation === 'ہاں' ? '✓ ہاں' : '✗ نہیں';
    culturalAdapt.style.color = analysis.cultural_adaptation === 'ہاں' ? '#10b981' : '#ef4444';

    // Strengths
    populateList('strengths-list', analysis.strengths || []);

    // Weaknesses
    populateList('weaknesses-list', analysis.weaknesses || []);

    // Improvements
    populateList('improvements-list', analysis.improvements || []);

    // Detailed Analysis
    document.getElementById('detailed-analysis').textContent = analysis.detailed_analysis || '';

    // Word Choice Analysis
    document.getElementById('word-choice').textContent = analysis.word_choice_analysis || '';

    // Grammar Review
    document.getElementById('grammar-review').textContent = analysis.grammar_review || '';

    // Smooth scroll to results
    setTimeout(() => {
        resultsSection.scrollIntoView({ behavior: 'smooth' });
    }, 100);
}

// Update Score Bar Animation
function updateScoreBar(elementId, score) {
    const bar = document.getElementById(elementId);
    const percentage = Math.min(Math.max(score, 0), 100);
    
    bar.style.width = '0%';
    setTimeout(() => {
        bar.style.width = percentage + '%';
    }, 50);
}

// Populate List Items
function populateList(listId, items) {
    const list = document.getElementById(listId);
    list.innerHTML = '';
    
    if (items.length === 0) {
        list.innerHTML = '<li style="border: none; color: #999;">کوئی آئٹم نہیں</li>';
        return;
    }

    items.forEach(item => {
        const li = document.createElement('li');
        li.textContent = item;
        list.appendChild(li);
    });
}

// Get Translation Type Description
function getTranslationTypeDescription(type) {
    const descriptions = {
        'لفظی ترجمہ': 'لفظ بہ لفظ ترجمہ - براہ راست ترجمہ',
        'معنوی ترجمہ': 'معنیٰ کو محفوظ رکھتے ہوئے ترجمہ',
        'آزادانہ ترجمہ': 'روانی کو ترجیح دیتے ہوئے ترجمہ',
        'رشتہ دار ترجمہ': 'انداز اور تہذیب برقرار رکھتے ہوئے ترجمہ',
        'فارغ ترجمہ': 'بات چیت کے مقصد پر توجہ مرکوز'
    };

    return descriptions[type] || 'ترجمے کی قسم معلوم نہیں ہو سکی';
}

// Show Error Message
function showError(message) {
    errorMessageDiv.textContent = message;
    errorMessageDiv.style.display = 'block';
    resultsSection.style.display = 'none';
    errorMessageDiv.scrollIntoView({ behavior: 'smooth' });
}

// Reset Form
function resetForm() {
    englishTextArea.value = '';
    urduTranslationArea.value = '';
    resultsSection.style.display = 'none';
    errorMessageDiv.style.display = 'none';
    englishTextArea.focus();
}

// Keyboard Shortcuts
document.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
        e.preventDefault();
        analyzeTranslation();
    }
});

// Initialize
window.addEventListener('load', () => {
    englishTextArea.focus();
});