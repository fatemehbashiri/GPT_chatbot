import openai

from environs import Env

env = Env()

env.read_env()

openai.api_key = env("OPENAI_APIKEY")

def getreply(text):
    model = "text-davinci-003"
    prompt = "please answer this question in simple and short way :" + text
    completion = openai.Completion.create(engine = model ,
                                          prompt = prompt,
                                          n=3,
                                          temperature = 0.7)
    response = completion.choices
    return response

response =[]

while True:
    message = input("\n ask me any thing... type \"Exit\" to exit. ")

    if message == "Exit":
        break
    if message == "Regenerate":
        print(response[1].text)
    response = getreply (message)
    print (response[0].text)


