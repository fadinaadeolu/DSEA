### Containerize Penguin Species Classification App

Penguin Classification Model was developed by [https://github.com/dataprofessor/code/tree/master/streamlit/part3]

To deploy app run the following commands:

- Build image

``` docker build -f Dockerfile -t app:latest . ```
or 
` make build `

- Deploy app

``` docker run -p 8501:8501 app:latest ```
or
` make run `

Go to ``` localhost:8501 ``` to view app
