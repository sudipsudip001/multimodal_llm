# multimodal_llm
This is an upgrade to the main branch with frontend part included to it. I didn't want to upload this to the main branch. You can find the dataset on my [huggingface profile](https://huggingface.co/datasets/suDEEP101/bank_customer_support/tree/main). Also, you can download the GGUF file (i.e. our actual finetuned model) from [here](https://huggingface.co/suDEEP101/bank_customer_service/tree/main).

For running the application:

1. Create a folder and open a terminal as administrator in it.
2. Clone the github repository:<br>
`git clone --branch frontend_included https://github.com/sudipsudip001/multimodal_llm.git`
3. Go into the 'multimodal_llm' folder using the command:<br>
`cd multimodal_llm`
4. Download the GGUF file from the link below:<br>
`https://huggingface.co/suDEEP101/bank_newest/tree/main`
I'd suggest that you download the ~8GB GGUF. Move this downloaded GGUF file inside the multimodal_llm folder where you have the app.py file.
5. Handling the requirements might be a bit tricky. A detailed description of how to configure everything in anaconda is given at the bottom of this markdown. For now, let's assume we've activated the anaconda environment and installed all requirements for the program.
6. Open the terminal in your IDE and run the flask app by using the command below:<br>
`flask --app app.py run`

If everything went well, then your application should run on (`http://127.0.0.1:5000`). You can check the demonstration in this [video](https://youtu.be/EfZYrNmjcmU).

(For activating and running anaconda:
1. First, you've to install 'anaconda'. Basically, it helps create virtual environment for you to work on so you can separately create an environment to work with different versions of libraries for different projects. You've an easy option of virtualenv in python but I prefer anaconda.
2. Then open the anaconda terminal from your startup menu and type the following code to create a virtual environment in anaconda:<br>
   `conda create --new multimodal_env python=3.8 -y`
3. Activate the virtual environment:<br>
   `conda activate multimodal_env`
4. Install flask:<br>
   `pip install flask`
5. Install pyttsx3:<br>
   `pip install pyttsx3`
6. Install openai whisper:<br>
  `pip install -U openai-whisper`
8. Install llama-cpp-python (using pip causes problems here!!):<br>
   `conda install llama-cpp-python`
9. Open your IDE(in my case it's VS code. Make sure your IDE is running on the anaconda environment we just created.): <br>
    `code .`
)
