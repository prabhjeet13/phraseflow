from flask import Flask, request, send_file, render_template
from TTSmodel import text_to_speech
app = Flask(__name__)
app.secret_key = '131313' 
@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/tts', methods=['POST'])
def tts():
    data = request.json
    text = data.get('text')
    language = data.get('language')
    
    output_file = 'output_audio.wav'
    text_to_speech(text, language,output_file)

    return send_file(output_file, mimetype='audio/wav')



# Run Flask app
if __name__ == '__main__':
    app.run(port=5000, debug=True)