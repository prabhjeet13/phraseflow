from flask import Flask, request, send_file, render_template, jsonify
from TTSmodel import text_to_speech
import os
app = Flask(__name__)
app.secret_key = '131313' 
@app.route('/')
def homepage():
    return render_template('index.html')
@app.route('/tts', methods=['POST'])
def tts():
    try:
        data = request.json
        text = data.get('text')
        language = data.get('language')

        if not text or not language:
            return jsonify(error="Missing 'text' or 'language' in request"), 400

        output_file = 'output_audio.wav'
        
        # Call the TTS function
        text_to_speech(text, language, output_file)

        # Ensure the file exists before sending
        if not os.path.exists(output_file):
            return jsonify(error="Failed to generate the audio file"), 500

        return send_file(output_file, mimetype='audio/wav')

    except Exception as e:
        # Log the actual error
        print(f"Error: {str(e)}")
        return jsonify(error=f"An error occurred: {str(e)}"), 500
    # data = request.json
    # text = data.get('text')
    # language = data.get('language')
    
    # output_file = 'output_audio.wav'
    # text_to_speech(text, language,output_file)

    # return send_file(output_file, mimetype='audio/wav')



# Run Flask app
if __name__ == '__main__':
    app.run(port=5000, debug=True)