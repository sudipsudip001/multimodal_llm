from flask import Flask, render_template, request, jsonify
from llama_cpp import Llama
import whisper
import pyttsx3

model = Llama(model_path="extended_bank_8bit.gguf", n_ctx=2048, n_threads=4)  # change the name of the model according to the one you downloaded.
whisper_model = whisper.load_model("base")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/text', methods=['POST'])
def generate():
    prompt = request.json['prompt']
    customer_prompt = f"""Below is an instruction that describes a question from customer. Write the answer to 
    the question so that you answer in exact, concise and polite.
    ### Instruction:
    {prompt}

    ### Input:
    
    ### Response
    """
    output = model(customer_prompt, max_tokens=100, stop=['###'])
    response_text = output['choices'][0]['text'].strip()
    return jsonify({"response" : response_text})

@app.route('/audio', methods=['POST'])
def audio_generate():
    audio = request.files['audio']
    audio.save('audios/recording.wav')

    result = whisper_model.transcribe("audios/recording.wav")
    result_text = result['text']

    customer_prompt = f"""Below is an instruction that describes a question from customer. Write the answer to 
    the question so that you answer in exact, concise and polite.
    ### Instruction:
    {result_text}

    ### Input:
    
    ### Response
    """
    output = model(customer_prompt, max_tokens=100, stop=['###'])
    response_text = output['choices'][0]['text'].strip()

    #produce audio
    engine = pyttsx3.init()
    engine.say(response_text)
    engine.runAndWait()

    return jsonify({"response" : 'audio outputted'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)