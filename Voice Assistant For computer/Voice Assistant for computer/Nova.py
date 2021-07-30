from tkinter import *
from PIL import Image, ImageTk
import cv2
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import requests
import pyjokes
from newsapi import NewsApiClient




def get_location():
    """ Function To Print GeoIP Latitude & Longitude """
    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    my_ip = ip_request.json()['ip']
    geo_request = requests.get('https://get.geojs.io/v1/ip/geo/' +my_ip + '.json')
    geo_data = geo_request.json()
    geo = geo_data['city']
    return geo

a = {'pratik':'pratiknalwar@gmail.com'}                 #replace with valid name and email id
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

window = Tk()

global var
global var1

var = StringVar()
var1 = StringVar()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('pratiknalwar@gmail.com', 'Swaminath')            #replace with master/sender email id and app-password generated from email provider
    server.sendmail('jyotikhed6901@gmail.com', to, content)
    server.close()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        var.set("Good Morning Sir") 
        window.update()
        speak("Good Morning Sir!")
    elif hour >= 12 and hour <= 18:
        var.set("Good Afternoon Sir!")
        window.update()
        speak("Good Afternoon Sir!")
    else:
        var.set("Good Evening Sir")
        window.update()
        speak("Good Evening Sir!")
    speak("Myself Nova! How may I help you sir")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        return "None"
    var1.set(query)
    window.update()
    return query

def play():
    btn2['state'] = 'disabled'
    btn0['state'] = 'disabled'
    btn1.configure(bg = 'orange')
    wishme()
    while True:
        btn1.configure(bg = 'orange')
        city=get_location()
        if city=="Solapur":
            var.set("You are in Solapur")
            window.update()

            continue
        query = takeCommand().lower()
        if 'exit' in query:
            var.set("Bye sir")
            btn1.configure(bg = '#5C85FB')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            window.update()
            speak("Bye sir")
            break

        elif 'change voice to female' in query:
            engine = pyttsx3.init('sapi5')
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            var.set('Hello, Myself Ruby')
            window.update()
            speak('Hello, Myself Ruby')

        elif 'change voice to male' in query:
            engine = pyttsx3.init('sapi5')
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            var.set('Hello, Myself Nova')
            window.update()
            speak('Hello, Myself Nova')

        elif 'wikipedia' in query:
            if 'open wikipedia' in query:
                webbrowser.open('wikipedia.com')
            else:
                try:
                    speak("searching wikipedia")
                    query = query.replace("according to wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to wikipedia")
                    var.set(query)
                    window.update()
                    speak(results)
                except Exception as e:
                    var.set('sorry sir could not find any results')
                    window.update()
                    speak('sorry sir could not find any results')

        elif 'open youtube' in query:
            var.set('opening Youtube')
            window.update()
            speak('opening Youtube')
            webbrowser.open("youtube.com")

        elif 'open website' in query:
            speak("which website")
            command = takeCommand()
            webbrowser.open(command+".com")
            var.set("opening " + command)
            window.update()
            speak("opening " + command)

        elif 'open coursera' in query:
            var.set('opening coursera')
            window.update()
            speak('opening coursera')
            webbrowser.open("coursera.com")

        elif 'open google' in query:
            var.set('opening google')
            window.update()
            speak('opening google')
            webbrowser.open("google.com")

        elif 'open gmail' in query:
            var.set('opening gmail')
            window.update()
            speak('opening gmail')
            webbrowser.open("gmail.com")

        elif 'say hello' in query:
            var.set('Hello Everyone! My self Nova')
            window.update()
            speak('Hello Everyone! My self Nova')

        elif 'hello' in query:
            var.set('Hello Sir')
            window.update()
            speak("Hello Sir")

        elif 'joke' in query:
            y = pyjokes.get_joke()
            var.set(y)
            window.update()
            speak(y)

        elif "covid" in query:
            r = requests.get('https://coronavirus-19-api.herokuapp.com/all').json()
            a= f'Confirmed Cases: {r["cases"]} \nDeaths: {r["deaths"]} \nRecovered {r["recovered"]}'
            var.set(a)
            window.update()
            speak(a)

        # elif 'change background' in query:
        #     ctypes.windll.user32.SystemParametersInfoW(20,10,"Location of wallpaper",0)
        #     speak("Background changed succesfully")

        elif "news" in query:
            newsapi = NewsApiClient(api_key='5840b303fbf949c9985f0e1016fc1155')
            speak("What topic you need the news about")
            topic = takeCommand()
            data = newsapi.get_top_headlines(
                q=topic, language="en", page_size=3)
            newsData = data["articles"]
            for y in newsData:
                var.set(y["description"])
                window.update()                
                speak(y["description"])
			
        elif 'open stack overflow' in query:
            var.set('opening stackoverflow')
            window.update()
            speak('opening stackoverflow')
            webbrowser.open('stackoverflow.com')

        elif ('play music' in query) or ('change music' in query):
            var.set('Here are your favorites')
            window.update()
            speak('Here are your favorites')
            music_dir = 'D:\songs'                                #enter valid path to songs folder
            songs = os.listdir(music_dir)
            n = random.randint(0,3)
            os.startfile(os.path.join(music_dir, songs[n]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            var.set("Sir the time is %s" % strtime)
            window.update()
            speak("Sir the time is %s" %strtime)

        elif 'the date' in query:
            strdate = datetime.datetime.today().strftime("%d %m %y")
            var.set("Sir today's date is %s" %strdate)
            window.update()
            speak("Sir today's date is %s" %strdate) 

        elif 'thank you' in query:
            var.set("Welcome Sir")
            window.update()
            speak("Welcome Sir")

        elif 'can you do for me' in query:
            var.set('I can do multiple tasks for you sir.\n tell me whatever you want to perform sir')
            window.update()
            speak('I can do multiple tasks for you sir. tell me whatever you want to perform sir')

        elif 'old are you' in query:
            var.set("I am a little baby sir")
            window.update()
            speak("I am a little baby sir")

        elif 'open media player' in query:
            var.set("opening VLC media Player")  
            window.update()
            speak("opening V L C media player")
            path = "D:\\vlc"                                       #Enter valid path for vlc.exe
            os.startfile(path)

        elif 'your name' in query:
            var.set("Myself Nova Sir")
            window.update()
            speak('myself Nova sir')

        elif 'who created you' in query:
            var.set('My Creator, My God, is Pratik')
            window.update()
            speak('My Creator, My God, is Pratik')


        elif 'weather' in query:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak(get_location())
            var.set(get_location())
            window.update()
            city_name = get_location()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                temperature = current_temperature - 273.15
                format_float = "{:.2f}".format(temperature)
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                var.set(" Temperature in kelvin unit = " +
                        str(current_temperature) + "\n Temperature in Celcius = " +
                        str(format_float) +
                        "\n humidity (in percentage) = " +
                        str(current_humidiy) +
                        "\n description = " +
                        str(weather_description))
                window.update()
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) + "\n Temperature in Celcius = " +
                        str(format_float) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))


            else:
                speak(" City Not Found ")



        elif 'email to' in query:
            try:
                query = query.replace("email to", "")
                query = query.replace(" ", "")
                print(query)
                var.set("What should I say")
                window.update()
                speak('what should I say')
                content = takeCommand()
                to = a[query]
                sendemail(to, content)
                var.set('Email has been sent!')
                window.update()
                speak('Email has been sent!')

            except Exception as e:
                print(e)
                var.set("Sorry Sir! I was not able to send this email")
                window.update()
                speak('Sorry Sir! I was not able to send this email')
		
        elif 'open code blocks' in query:
            var.set('Opening Codeblocks')
            window.update()
            speak('opening Codeblocks')
            os.startfile("D:\\CodeBlocks") 

        elif 'open anaconda' in query:
            var.set('Opening Anaconda')
            window.update()
            speak('opening anaconda')
            os.startfile("path-to\\Anaconda Navigator (Anaconda3)")

        elif 'click photo' in query:
            speak("Say Cheese")
            stream = cv2.VideoCapture(0)
            grabbed, frame = stream.read()
            if grabbed:
                cv2.imshow('pic', frame)
                cv2.imwrite('pic.jpg',frame)
                
            stream.release()

        elif 'record video' in query:
            cap = cv2.VideoCapture(0)
            out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*"MJPG"), 30,(640,480))
            while(cap.isOpened()):
                ret, frame = cap.read()
                if ret:
                    
                    out.write(frame)

                    cv2.imshow('frame',frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                else:
                    break
            cap.release()
            out.release()
            cv2.destroyAllWindows()
              
def update(ind):
    frame = frames[(ind)%5]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)

label2 = Label(window, textvariable = var1, bg = '#FAB60C')
label2.config(font=("Courier", 20))
var1.set('User Said:')
label2.pack()

label1 = Label(window, textvariable = var, bg = '#ADD8E6')
label1.config(font=("Courier", 20))
var.set('Welcome')
label1.pack()

frames = [PhotoImage(file='tenor.gif',format = 'gif -index %i' %(i)) for i in range(5)]
window.title('NOVA')

label = Label(window, width = 500, height = 500)
label.pack()
window.after(0, update, 0)

btn0 = Button(text = 'WISH ME',width = 20, command = wishme, bg = '#5C85FB')
btn0.config(font=("Courier", 12))
btn0.pack()
btn1 = Button(text = 'START',width = 20,command = play, bg = '#5C85FB')
btn1.config(font=("Courier", 12))
btn1.pack()
btn2 = Button(text = 'EXIT',width = 20, command = window.destroy, bg = '#5C85FB')
btn2.config(font=("Courier", 12))
btn2.pack()


window.mainloop()
