# multimodal_llm
A flask app for custom-data finetuned llama3 for banking chat service.

This is a simple multimodal (handles speech and text) Flask application that uses the finetuned llama3. The 'finetuning' was done on custom-dataset created using LLMs itself. (So, basically I prompted LLMs to create prompts so I can finetune LLM to handle prompts. Make it make sense.) Anyhoo you can find the dataset on my [huggingface profile](https://huggingface.co/suDEEP101). The name might not be exact as I might change it later on but any dataset with 'bank' keyword should be the one! Also, you can download the GGUF file (i.e. our actual finetuned model) from my huggingface profile as well. Exact name might be different but you can use anyone that has 'bank' keyword to it. I'd suggest you to use the ~4GB GGUF file.

Note that there's no frontend for this application as of yet. You must use Postman for hitting the URLs to get a response from the model. The frontend part of the application is soon to follow! For running the application:

1. Create a folder and open a terminal as administrator in it.
2. Clone the github repository:
`git clone https://github.com/sudipsudip001/multimodal_llm.git`
3. Go into the 'multimodal_llm' folder using the command:
`cd multimodal_llm`
4. Open terminal at this folder and paste the following command:
`pip install -r requirements.txt`
5. Download the GGUF file from the link below:
`https://huggingface.co/suDEEP101/bank_newest/tree/main`
I'd suggest that you download the ~4GB GGUF. Then move this GGUF file inside the multimodal_llm folder where you've the app.py file.
6. Run the flask app by using the command below:
`flask --app app.py run`

If everything went well then your application should run on (`http://127.0.0.1:5000`). Then you can use Postman to hit the URLS i.e. `http://127.0.0.1:5000/text` to send text prompts and `http://127.0.0.1:5000/audio` to send audio prompts. You can check the demonstration in this [video]().
