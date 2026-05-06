from flask import Flask, request, jsonify
import google.generativeai as genai
import time
from datetime import datetime

app = Flask(__name__)

# ==========================================
# 🔑 Yahan aapki official Google API Key hai
# ==========================================
GEMINI_API_KEY = "AIzaSyDZ_Hsgq5Oi_XxNUmgVXUCp1H269TZGHUQ" 

# Gemini API ko configure karna
genai.configure(api_key=GEMINI_API_KEY)

# 'gemini-1.5-flash' Google ka latest aur sabse fast model hai
model = genai.GenerativeModel('gemini-1.5-flash')

def chat_with_gemini(prompt):
    start_time = time.time()
    try:
        # Official API se generate_content call karna
        response = model.generate_content(prompt)
        end_time = time.time()
        
        if response.text:
            return {
                'success': True,
                'response': response.text,
                'metadata': {
                    'response_time': f'{round(end_time - start_time, 2)}s',
                    'timestamp': datetime.utcnow().isoformat() + 'Z',
                    'model': 'gemini-1.5-flash',
                    'character_count': len(response.text),
                    'word_count': len(response.text.split())
                }
            }
        else:
            return {
                'success': False,
                'error': 'Empty response from Gemini API.'
            }
            
    except Exception as e:
        # Agar koi API error aaye
        return {
            'success': False,
            'error': str(e)
        }

@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "Official Gemini API is running perfectly!",
        "developer": "@AmmarDevx",
        "api": {
            "name": "Google Gemini Official API",
            "version": "2.0.0" # Version update kar diya
        },
        "endpoints":[
            {
                "path": "/api/ask",
                "method": "GET",
                "description": "Ask anything to Gemini AI",
                "parameters":[
                    {
                        "name": "prompt",
                        "type": "string",
                        "required": True,
                        "description": "Your question or message"
                    }
                ],
                "example": "/api/ask?prompt=Explain how AI works in a few words"
            }
        ]
    })

@app.route('/api/ask', methods=['GET'])
def ask_gemini():
    prompt = request.args.get('prompt')
    
    if not prompt:
        return jsonify({
            'success': False,
            'error': 'Missing required parameter: prompt',
            'api_dev': '@AmmarDevx',
            'usage': {
                'endpoint': '/api/ask',
                'method': 'GET',
                'parameters': {
                    'prompt': 'Your question or message (required)'
                },
                'example': '/api/ask?prompt=Hello, how are you?'
            }
        }), 400
    
    if len(prompt.strip()) == 0:
        return jsonify({
            'success': False,
            'error': 'Prompt cannot be empty',
            'api_dev': '@AmmarDevx'
        }), 400
    
    # Gemini se chat function call karein
    result = chat_with_gemini(prompt)
    
    # Apni branding add karein
    result['api_dev'] = '@AmmarDevx'
    result['prompt'] = prompt
    
    if result['success']:
        return jsonify(result), 200
    else:
        # HTTP 500 status code for error
        return jsonify(result), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'error': 'Endpoint not found',
        'api_dev': '@AmmarDevx',
        'available_endpoints': ['/', '/api/ask']
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'success': False,
        'error': 'Internal server error',
        'api_dev': '@AmmarDevx'
    }), 500

if __name__ == '__main__':
    print('=' * 60)
    print('🚀 Gemini AI Flask API (OFFICIAL VERSION)')
    print('👨‍💻 Developer: AmmarDevx')
    print('🔑 Status: Using Official Google AI Studio Key')
    print('=' * 60)
    print('\nAPI Endpoints:')
    print('  GET  /           - API Information')
    print('  GET  /api/ask    - Ask Gemini AI')
    print('\nExample Usage:')
    print('  http://localhost:5000/api/ask?prompt=Hello, how are you?')
    print('=' * 60)
    print('\nStarting server...\n')
    
    app.run(debug=True, host='0.0.0.0', port=5000)
