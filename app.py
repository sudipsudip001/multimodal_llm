from flask import Flask, render_template, request, jsonify, send_file
from llama_cpp import Llama
import whisper
import pyttsx3
import os

model = Llama(model_path="bank_customer_support.gguf", n_ctx=2048, n_threads=4)  # change the name of the model according to the one you downloaded.
whisper_model = whisper.load_model("base")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/text', methods=['POST'])
def generate():
    prompt = request.json['prompt']
    customer_prompt = f"""Below is an instruction that describes a question from customer. Write the answer to 
    the question so that you answer in concise and polite.
    ### Instruction:
    {prompt}

    ### Input:
    
    ### Response
    """
    output = model(customer_prompt, max_tokens=150, stop=['###'])
    response_text = output['choices'][0]['text'].strip()
    return jsonify({"response" : response_text})

@app.route('/audio', methods=['POST'])
def audio_generate():
    audio = request.files['audio']
    audio.save('audios/recording.wav')

    result = whisper_model.transcribe("audios/recording.wav")
    os.remove('audios/recording.wav')
    result_text = result['text']

    customer_prompt = f"""Below is an instruction that describes a question from customer. Write the answer to 
    the question so that you answer in concise and polite.
    ### Instruction:
    {result_text}

    ### Input:
    
    ### Response
    """
    output = model(customer_prompt, max_tokens=150, stop=['###'])
    response_text = output['choices'][0]['text'].strip()

    #produce audio
    engine = pyttsx3.init()

    if os.path.exists('audios/output.mp3'):
        os.remove('audios/output.mp3')
    engine.save_to_file(response_text, 'audios/output.mp3')
    engine.runAndWait()

    return send_file('audios/output.mp3', mimetype='audio/mp3')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)