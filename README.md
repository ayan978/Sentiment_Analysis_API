# Sentiment_Analysis_API
To run this project, follow these steps:
1. Clone this repository.
2. Open the folder using any IDE.
3. Open terminal and run the command "cd Sentiment_Analysis_API"
4. In the terminal, run the command "pip install fastapi"
5. Then, run the command "pip install uvicorn"
6. Then, run the command "pip install setfit" to use the pretrained model.
7. A single endpoint at '/analyze' is created to accept post request and show the response using the pre-trained AI model.
8. By hitting the url '/docs#/analyze', an input string can be put inside the request body. The sentiment analysis result produced by the pretrained can be seen inside the response body.
