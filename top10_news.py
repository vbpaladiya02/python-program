import requests
import json
i=1
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

url="http://newsapi.org/v2/top-headlines?country=in&apiKey="xxxxxxxxxxxxxxxxxxxxxxx"

nr=requests.get(url).text
news=json.loads(nr)
article=news['articles']

speak("top 10 news of india for today.. listen carefully")
for art in article:
    print(i,".")
    speak(f"{i} news is..")
    print(art['title'])
    speak(art['title'])
    print("\n")
    i+=1
    if i==11:
        break
    
speak("thank you for listening good bye....")

 