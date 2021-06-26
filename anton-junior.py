import speech_recognition as sr
import pyttsx3
import sys
import pywhatkit
import datetime as clock
import wikipedia

r = sr.Recognizer()
anton = pyttsx3.init()
ai_pmt = "[Anton.Jr] : "
speaker_pmt = "[Speaker] : "

def speak(text):
    anton.say(text)
    anton.runAndWait()

def song_play(song):
    global listen_loop
    song = song.replace("anton", '')
    song = song.replace("hey anton", '')
    song = song.replace("play", '')
    speak("playing" + song)
    pywhatkit.playonyt(song)

def present_time():
    time = clock.datetime.now().strftime('%I:%M %p')
    speak_time = time.replace(":", " ")
    print(ai_pmt + "Time is " + time)
    speak("time is" + speak_time)

def wiki_search(parameter):
    print(parameter)
    info = wikipedia.summary(parameter, 1)
    print(ai_pmt + info)
    speak(info)

def listen_loop():
    global command
    try:
        with sr.Microphone() as source:
            print(ai_pmt + " listening...")
            input_command = r.listen(source)
            command = r.recognize_google(input_command)
            print(speaker_pmt, end=" ")
            print(command)
            if "play" in command:
                song_play(command)
            elif "time" in command:
                present_time()
            elif ("who is" or "what is") in command:
                command = command.replace("who is", '')
                command = command.replace("what is", '')
                wiki_search(command)
            else:
                print(ai_pmt + "I didnt get you, can you rephrase it please")
                speak("I didnt get you, can you rephrase it please")
    except:
        print(sys.exc_info())

while True:
    listen_loop()


    
    
