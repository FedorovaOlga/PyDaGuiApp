import wolframalpha
import wikipedia
import pyttsx3
import speech_recognition as sr
import PySimpleGUI as sg

engine = pyttsx3.init()
image_micro ='./Mic.png'
app_id = "UKA9EQ-K954KLG7KU"
client = wolframalpha.Client(app_id)
r = sr.Recognizer()

sg.theme_button_color((sg.theme_background_color(), sg.theme_background_color())),
sg.theme('LightPurple')   
layout = [  [sg.Text('Q:'), sg.InputText(key='question'),sg.Button(image_filename=image_micro, image_size=(20, 20), image_subsample=2,  key='Mic')],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

window = sg.Window('Your Personal Asistant', layout)
# Event Loop to process "events" and get the "values" of the inputs

engine.say("Hi, Olga, how can I help you")
engine.runAndWait()
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        engine.say("Buy, Olga, see you soon")
        engine.runAndWait()
        break
    if event =='Mic':
        try:
            with sr.Microphone() as source:
                audio = r.listen(source, 10, 2)
            window['question'].update(r.recognize_google(audio))
            values['question'] = r.recognize_google(audio)
        except:
            print("Google Speech Recognition could not understand audio")
    try:
    	wolframres = client.query(values['question'])
    	res = next(wolframres.results).text
    except:
        try:
            res = wikipedia.summary(values['question'], sentences=3) 
        except:
            res ="Some error has occured, please try again"
    sg.PopupNonBlocking(res)
    engine.say(res)
    engine.runAndWait()    	
     

window.close()