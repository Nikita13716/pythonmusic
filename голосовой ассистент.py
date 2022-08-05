
from gtts import gTTS
import time
import speech_recognition as sr
import pyttsx3
import subprocess
import pyglet
import webbrowser
def listen_command():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Скажите вашу команду: ")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        our_speech = r.recognize_google(audio, language="en")
        print("Вы сказали: "+our_speech)
        return our_speech
    except sr.UnknownValueError:
        return "ошибка"
    except sr.RequestError:
        return "ошибка"

    #return input("Скажите вашу команду: ")

def do_this_command(message):
    message = message.lower()
    if "google" in message:
        subprocess.call("C:\Program Files\Google\Chrome\Application\chrome.exe")
    elif "list" in message:
        print('Google\ndead cells \nconstruct \nmusic \noff \nfl studio \nchill ') 
    elif "dead cells" in message:
        subprocess.call("C:\Program Files (x86)\Steam\steamapps\common\Dead Cells\deadcells.exe")
    elif "fl studio" in message:
        subprocess.call("C:\Program Files\Image-Line\FL Studio 20\FL64.exe")    
    elif "construct" in message:
        subprocess.call("D:\Construct 2\Construct2.exe")
    elif "chill" in message:
        webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe'))
        webbrowser.get('Chrome').open_new_tab('www.youtube.com/watch?v=jfKfPfyJRdk&ab_channel=LofiGirl')
    
    elif "music" in message:
        webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe'))
        webbrowser.get('Chrome').open_new_tab('https://vk.com/audios333772498')
    elif "off" in message:
        print("Off")
        engine = pyttsx3.init()
        engine.say("пока")
        engine.runAndWait()
        exit()
if __name__ == '__main__':
    while True:
        command = listen_command()
        do_this_command(command)


