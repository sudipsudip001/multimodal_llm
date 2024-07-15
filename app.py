from flask import Flask, render_template, request, jsonify
from llama_cpp import Llama
import whisper
import pyttsx3

model = Llama(model_path="best_model.gguf", n_ctx=2048, n_threads=4)
whisper_model = whisper.load_model("base")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/text', methods=['POST'])
def generate():
    prompt = request.json['prompt']
    output = model(prompt, max_tokens=50)
    response_text = output['choices'][0]['text']

    return jsonify({"response" : response_text})

@app.route('/audio', methods=['POST'])
def audio_generate():
    audio = request.files['audio']
    audio.save('audios/recording.wav')

    result = whisper_model.transcribe("audios/recording.wav")
    result_text = result['text']

    prompt = result_text
    output = model(prompt, max_tokens=50)
    response_text = output['choices'][0]['text']

    engine = pyttsx3.init()
    engine.say(response_text)
    engine.runAndWait()

    return jsonify({"response" : 'audio outputted'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)