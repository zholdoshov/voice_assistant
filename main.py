import os
import random
from email.mime import audio
from logging.config import listen
import sys
import datetime
import speech_recognition
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 120)

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

commands_dict = {
    'commands': {
        'greeting': ['hello', 'hi', 'good morning', 'hey', 'good day', 'heyo', "what's up"],
        'create_task': ['create a note', 'create a task', 'task', 'note', 'new note'],
        'play_music': ['play music', 'play song', 'music', 'song'],
        'exit': ['bye', 'exit', 'stop', 'i want to quit', 'i have to go'],
        'time': ['what time is it', 'what is time', 'time'],
        'date': ['what is the date today', "today's date", 'date']
    }
}


"""The function will return the recognized command"""
def listen_command():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio).lower()

            return query
    except speech_recognition.UnknownValueError:
        engine.say("Damn... Something went wrong! Try again!")
        engine.runAndWait()


"""Greeting function"""
def greeting():

    engine.say("Hello Mr. Nurulla, how can I help you?")
    engine.runAndWait()

    return listen_command()


"""Create a todo task"""
def create_task():

    engine.say("What should I add?")
    engine.runAndWait()

    query = listen_command()

    with open('todo-list.txt', 'a') as file:
        file.write(f'- {query}\n')

    engine.say(f'Task {query} added to the list!')
    engine.runAndWait()
    return listen_command()


"""Play a random mp3 file"""
def play_music():

    files = os.listdir('E:\\Nurullah\\Music\\NUR')
    random_file = f'E:\\Nurullah\\Music\\NUR\\{random.choice(files)}'
    os.system(f'start {random_file}')

    bslash = '\\'
    print(f'Dance to {random_file.split(bslash)[-1]} music')


"""The function that returns current time"""
def time():
    engine.say(f'The time is: {datetime.datetime.now().time().strftime(("%H:%M"))}')
    engine.runAndWait
    return listen_command()


"""The function that returns current date"""
def date():
    engine.say(f'Today is: {datetime.date.today().strftime("%B %d, %Y")}')
    engine.runAndWait
    return listen_command()


"""stop communicating"""
def exit():
    engine.say('Bye, good luck!')
    engine.runAndWait
    sys.exit(0)


"""main function"""
def main():
    while True:
        query = listen_command()
        for k, v in commands_dict['commands'].items():
            if query in v:
                print(globals()[k]())

if __name__ == '__main__':
    main()