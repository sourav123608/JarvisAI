import speech_recognition as sr
import os
import webbrowser
import openai
import datetime
import random
import smtplib
chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = "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"
    chatStr += f"User: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

def sendmail(to,contact):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("pandasourav823@gmail.com","@Sourav123")
    server.sendmail("pandasourav823@gmail.com",to,content)
    server.close()
def ai(prompt):
    openai.api_key = "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"
    text = f"OpenAI response for Prompt: {prompt} \n ********************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Write an email to my boss for resignation?",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/prompt- {random.randint(1, 23434343356)}", "w") as f:
        f.write(text)
def say(text):
    os.system(f"say {text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
       # r.pause_thresold = 1
        audio = r.listen(source)
        try:
            print("Recognizing..")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"

if __name__ == '__main__':
    print('pyCharm')
    say("Hello I am Jarvis A.I")
    while True:
        print("listening...")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia","https://www.wikipedia.com"], ["google","https://www.google.com"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
            if "what the time" in query:
                strfTime = datetime.datetime.now().strftime("%H:%M:%S")
                say(f"Sir the time is {strfTime}")
            if "open code" in query:
                os.system(f"open /Applications/Visual Studio Code.app")
            if "open facetime".lower() in query.lower():
                os.system(f"open /System/Applications/FaceTime.app")
            if "send email" in query:
                try:
                    say('whom to be sent')
                    to = takeCommand()
                    say('what to be sent')
                    content = takeCommand()
                    sendmail(to,content)
                    say('Email has been sent')
                except Exception as e:
                    print(e)
                    say('Sorry ! I am not able to sent Email')

            if "use ai".lower() in query.lower():
                ai(prompt=query)
            elif "Jarvis Quit".lower() in query.lower():
                exit()

            elif "reset chat".lower() in query.lower():
                chatStr = ""

            else:
                print("Chatting...")
                chat(query)

            # say(query)