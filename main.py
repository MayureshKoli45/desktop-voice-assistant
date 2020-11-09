import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import math
from translate import Translator
import pyaudio
from countryinfo import *
import os.path
import subprocess
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    speak('all systems have been started')
    speak('now i am online')
    
    
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("Good Morning!")

    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am EVIE")
    speak("Please tell me how may I help you")    


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing ...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said : {query}\n")

    except:
        speak("Say that again please ...")
        print("Say that again please ...")
        return "None"
    return query        


# code to make a note:-

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":","-") + "-note.txt"
    with open(file_name,"w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe",file_name])    


# code to play music:-

def media():
    try:
        speak('ok')
        speak('starting required application')
        speak('what do you want me to play for you')
        k = takeCommand()
        os.startfile('M:\\SONGS\\' + k + '.mp3')
        speak("Playing"+k+"for you")
    except:
        print("sorry didnt recognise that song")
        speak("sorry didnt recognise that song")


# code to quit:-

def shut_down():
    speak('understood')
    speak('connecting to command prompt')
    speak('shutting down your computer')
    os.system('shutdown -s')
    quit()

def gooffline():
    speak('ok')
    speak('going offline')
    speak('have a good day')
    quit()


# code to factorial

def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num-1)


def guessing_game():
    secret_number = random.randint(1, 20)
    chances = 0 
    while chances < 10:  
        try:     
            chances = chances + 1
            speak("guess number"+str(chances))  
            print("guess number :- " + str(chances))  
            guess = int(takeCommand())

            if guess > secret_number:
                speak("your number is greater than the secret number") 
                print("your number is greater than the secret number")
                if chances == 10:
                    print("sorry you are out of guesses")

            elif guess < secret_number:
                speak("your number is lesser than the secret number")
                print("your number is lesser than the secret number")
                if chances == 10:
                    print("sorry you are out of guesses")

            else:
                speak("congratulations you have guessed the secret number " + str(secret_number) +
                      " in " + str(chances) + " guesses.")
                print("congratulations you have guessed the secret number " + str(secret_number) +
                      " in " + str(chances) + " guesses.")   
                break

        except:
            speak("invalid input")
            print("invalid input")  # this will display when the player makes a typo mistake

    print("game over")                

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
#Logic for executing task based on query
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia ...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'guessing game' in query:
            speak("ok you have to guess a number between 1 to 20 and you only have 10 guesses") 
            guessing_game()


# code to open websites:-

        elif '.com' in query:
            speak("here you go") 
            webbrowser.open("www."+query)

        elif '.in' in query:
            speak("Okay got it") 
            webbrowser.open("www."+query)

        elif '.net' in query:
            speak("here you go") 
            webbrowser.open("www."+query)

        elif '.org' in query:
            speak("Okay got it") 
            webbrowser.open("www."+query)
                
        elif 'open youtube' in query:
            speak("Okay")
            webbrowser.open("https://www.youtube.com")
        
        elif 'open google' in query:
            speak("Here you go")
            webbrowser.open("https://www.google.com")

        elif 'current affairs' in query:
            speak("Okay")
            webbrowser.open("https://www.jagranjosh.com/current-affairs")

        elif 'weather forecast' in query:
            speak("here you go")
            webbrowser.open("https://www.accuweather.com/en/world-weather")

        elif 'open map' in query:
            speak("opening google map for you")
            webbrowser.open("https://www.google.com/maps/@19.0352007,72.9578672,15z")        

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# code to find time and date:-
        
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strtime}")    

        elif 'date' in query:
            strdate = datetime.datetime.now().strftime("%D:%Y")
            speak (f"the date is {strdate}")
   

# code to open apps:-

        elif 'open visual studio' in query:
            codepath = "C:\\Users\\Monty\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Happy coding")
            os.startfile(codepath)

        elif 'open calculator' in query:
            speak("I can calculate for you")
            speak("then why you need a calculator")
            os.startfile('calc')

        elif 'open paint' in query:
            speak("Happy painting")
            os.startfile('mspaint')

        elif 'open notepad' in query:
            speak("Okay")
            os.startfile('notepad')

        elif "open steam" in query:
            codepath = "F:\\steam\\Steam.exe"
            speak("Okay")
            os.startfile(codepath)        

        elif "open google chrome" in query:
            codepath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            speak("Okay")
            os.startfile(codepath)

        elif "open torrent" in query:
            codepath = "C:\\Users\\Monty\\AppData\\Roaming\\BitTorrent\\BitTorrent.exe"
            speak("happy pirating")
            os.startfile(codepath)    

        elif 'open my computer' in query:
            speak("ok")
            os.system('explorer C:\\"{}"'.format(query.replace('open','')))
            continue

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////            

#code to casual talk:-

        elif 'name' in query:
            speak(f"my name is Everything here is Voice Intelligence Environment")
            speak("but in short you can call me EVIE")

        elif 'who are you' in query:
            speak("I am EVIE your personal voice assistant")
            speak("how may i help you")    
                
        elif 'created you' in query:
            speak(f"my creater is Mayuresh Shridhar Koli")

        elif 'bye' in query:
            speak(f"Good Bye have a good day")

        elif 'hello' in query or 'hey' in query or 'hi' in query:
            stMsgs = ['hello','hey','hi']
            print(random.choice(stMsgs))
            speak(random.choice(stMsgs))

        elif 'thank you' in query:
            speak("your welcome")

        elif 'what are you doing' in query:
            speak("I am just working with you")

        elif 'helpful' in query:
            speak("you think")
            speak("Thanks")

        elif 'favourite food' in query:
            speak("DC voltage with a side of current")

        elif 'shut up' in query:
            speak("dont talk to me like that")

        elif 'i love you' in query:
            speak("if i will say i love you still we dont have any future")
            speak("because you are a human and i am a machine")
            speak("sorry")                        

        elif 'how are you' in query:
            speak("i am fine") 
            speak("thank you")
            speak("and how are you")

        elif 'i am not fine' in query:
            speak("its okay")
            speak("some days are good some days are bad")
            speak("just say")
            speak("thats life")
            speak("and carry on")
            speak("dont be sad")    
            speak("maybe tomorrow will be your day")
            
        elif 'i am fine' in query:
            speak("good")
            speak("ok now tell me how may i help you")

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////                

# code to play music:-

        elif 'play music' in query:
            media()
   
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# code to quit:-

        elif 'offline' in query:
            gooffline()    
               
               
        elif 'shutdown' in query:
            shut_down() 

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        
# code for mathematical calculations:-           
#Addition:-
        elif 'add' in query:
            try:
                speak("what will be your first number")
                a = float(takeCommand())
                speak("what will be your second number")
                b = float(takeCommand())
                speak("do you want me to add more number")
                if 'no' in takeCommand():
                    ab = a+b
                    print(ab)
                    speak("the answer will be")
                    speak(ab)
                else:    
                    speak("what will be your another number")
                    c = float(takeCommand())
                    abc = a+b+c
                    print(abc)
                    speak("the answer will be")
                    speak(abc)         
            except:
                print("sorry i didnt understand the number you said")
                speak("sorry i didnt understand the number you said")    
                
#Subtract:-            
        elif 'subtract' in query:
            try:
                speak("what will be your first number")
                a = float(takeCommand())
                speak("what will be your second number")
                b = float(takeCommand())
                speak("do you want to subtract more number")
                if 'no' in takeCommand():
                    ab = a-b
                    print(ab)
                    speak("the answer will be")
                    speak(ab)
                else:    
                    speak("what will be your another number")
                    c = float(takeCommand())
                    abc = a-b-c
                    print(abc)
                    speak("the answer will be")
                    speak(abc)
            except:
                print("sorry i didnt understand the number you said")
                speak("sorry i didnt understand the number you said")

#Multiply:-
        elif 'multiply' in query:
            try:
                speak("what will be your first number")
                a = float(takeCommand())
                speak("what will be your second number")
                b = float(takeCommand())
                speak("do you want me to multiply with more number")
                if 'no' in takeCommand():
                    ab = a*b
                    print(ab)
                    speak("the answer will be")
                    speak(ab)
                else:    
                    speak("what will be your another number")
                    c = float(takeCommand())
                    abc = a*b*c
                    print(abc)
                    speak("the answer will be")
                    speak(abc)
            except:
                print("sorry i didnt understand the number you said")
                speak("sorry i didnt understand the number you said")

#Division:-               
        elif 'divide' in query:
            try:
                speak("what will be your first number")
                a = float(takeCommand())
                speak("what will be your second number")
                b = float(takeCommand())
                ab = a/b
                print(ab)
                speak("the answer will be")
                speak(ab)
            except:
                print("something went wrong")
                speak("something went wrong")

#Cube:-
        elif 'cube' in query:
            try:
                speak("please tell me a number of which do you want me to find a cube")
                cu = int(takeCommand())
                cube = cu**3
                print(cube)
                speak(cube)
            except:
                print("sorry i didnt understand the number you said")
                speak("sorry i didnt understand the number you said")
        
#Square and Square root:-        
        elif 'square' in query:
            try:
                speak("please tell me a number of which do you want me to find a square")
                sq = int(takeCommand())
                square = sq**2
                print(square)
                speak(square)
            except:
                print("sorry i didnt understand the number you said")
                speak("sorry i didnt understand the number you said")
        
        
        elif 'route' in query:
            try:
                speak("please tell me a number of which do you want me to find a square root")
                x = float(takeCommand())
                z = math.sqrt(x)
                print(z)
                speak(z)
            except:
                print("sorry i didnt understand the number you said")
                speak("sorry i didnt understand the number you said")
        
#Binary, Octal and Hexadecimal:-        
        elif 'binary' in query:
            try:
                speak("please tell me a number which do you want me to convert in binary")
                x = int(takeCommand())
                z = bin(x)
                print(z)
                speak(z)
            except:
                print("sorry i didnt understand the number you said")
                speak("sorry i didnt understand the number you said")

        
        elif 'octal' in query:
            try:
                speak("please tell me a number which do you want me to convert in octal")
                x = int(takeCommand())
                z = oct(x)
                print(z)
                speak(z)    
            except:
                print("sorry i didnt understand the number you said")
                speak("sorry i didnt understand the number you said")
        
        
        elif 'hexadecimal' in query:
            try:
                speak("do you want me to convert integer number or float number")
                takeCommand()
                if 'integer' in query:
                    x = int(takeCommand())
                    z = hex(x)
                    print(z)
                    speak(z)
                else:
                    x = float(takeCommand())
                    z = float.hex(x)
                    print(z)
                    speak(z)
            except:
                print("sorry i didnt understand the number you said")
                speak("sorry i didnt understand the number you said")

#Bitwise operation:-        
        elif 'bitwise and' in query:
            try:
                speak("what will be your first number")
                a = int(takeCommand())
                speak("what will be your second number")
                b = int(takeCommand())
                c = a&b
                print(c)
                speak(c)
            except:
                print("sorry i didnt understand the number you said")
                speak("sorry i didnt understand the number you said")


        elif 'bitwise or' in query:
            try:
                speak("what will be your first number")
                a = int(takeCommand())
                speak("what will be your second number")
                b = int(takeCommand())
                c = a|b
                print(c)
                speak(c)
            except:
                print("sorry i didnt understand the number you said")
                speak("sorry i didnt understand the number you said")
        
        
        elif 'bitwise xor' in query:
            try:
                speak("what will be your first number")
                a = int(takeCommand())
                speak("what will be your second number")
                b = int(takeCommand())
                c = a^b
                print(c)
                speak(c)
            except:
                print("sorry i didnt understand the number you said")
                speak("sorry i didnt understand the number you said")

#Perfect square, Prime number and Factorial:-
        elif 'perfect' in query:
            try:
                speak("what will be your first number")
                a = int(takeCommand())
                speak("what will be your second number")
                b = int(takeCommand())
                ab = range(a,b)
                for i in ab:
                    if i**2<=b:
                        print(i**2)
                        speak(i**2)
            except:
                print("sorry i didnt understand the number you said")
                speak("sorry i didnt understand the number you said")
        
        
        elif 'prime number' in query:
            try:
                speak("which number should i take")
                x = int(takeCommand())
                for i in range (2,x):
                    if x%i==0:
                        print("it is not a prime number")
                        speak("it is not a prime number")
                        break
                    else:
                        print("it is a prime number")
                        speak("it is a prime number")
                        break
            except:
                print("sorry i didnt understand the number you said")
                speak("sorry i didnt understand the number you said")

        
        elif 'factorial' in query:
            try:
                speak("which number should i take")
                num = int(takeCommand())
                if num<0:
                    print("factorial connot be found for negative number")
                    speak("factorial connot be found for negative number")
                elif num==0:
                    print("factorial of 0 is 1")
                    speak("factorial of 0 is 1")
                else:
                    print(factorial(num))
                    speak(factorial(num))                    
            except:
                print("sorry i didnt understand the number you said")
                speak("sorry i didnt understand the number you said")

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////                    

#code for German and Spanish translator:-

        elif 'german translator' in query:
            try:
                speak("what do you want me to translate sir")
                ge = str(takeCommand())
                translator = Translator(to_lang="german")
                translation = translator.translate(ge)
                print(translation)
                speak(translation)
            except:
                print("sorry something went wrong")
                speak("sorry something went wrong")


        elif 'spanish translator' in query:
            try:
                speak("what do you want me to translate sir")
                sp = str(takeCommand())
                translator = Translator(to_lang="spanish")
                translation = translator.translate(sp)
                print(translation)
                speak(translation)
            except:
                print("sorry something went wrong")
                speak("sorry something went wrong")    

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////            

#code for Capital, Currency and Time Zone of a country:-

        elif 'capital' in query:
            try:
                speak("which country capital do you want to know about")
                country = CountryInfo(takeCommand())
                a = country.capital()
                speak("the capital of this country is")
                print(a)
                speak(a)
            except:
                print("something went wrong")
                speak("something went wrong")

        elif 'currency' in query:
            try:
                speak("which country currency do you want to know about")
                country = CountryInfo(takeCommand())
                a = country.currencies()
                speak("the currency used in this country is")
                print(a)
                speak(a)
            except:
                print("something went wrong")
                speak("something went wrong")    

        elif 'time zone' in query:
            try:
                speak("which country timezones do you want to know about")
                country = CountryInfo(takeCommand())
                a = country.timezones()
                speak("the timezone of this country is")
                print(a)
                speak(a)    
            except:
                print("something went wrong")
                speak("something went wrong")

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#code to make a Note:-

        elif 'make a note' in query:
            try:
                speak("what would you like me to write down?")
                note_text = takeCommand()
                note(note_text)
                speak("I've made a note of that")
            except:
                speak("sorry something went wrong")    

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            
#code to send Emails:-       

        elif 'email' in query:
            try:
                print('Who is the recipient? ')
                speak('Who is the recipient? ')
                recipient = takeCommand()
                recipient = recipient.lower()

                if 'mayuresh' in recipient:
                    print('What should I say? ')
                    speak('What should I say? ')
                    content = takeCommand()
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("kolimist45@gmail.com", 'marvel12345')
                    server.sendmail('kolimist45@gmail.com', "mistkoli45@gmail.com", content)
                    server.close()
                    print('Email sent!')
                    speak('Email sent!')

                elif 'durgesh' in recipient:
                    print('What should I say? ')
                    speak('What should I say? ')
                    content = takeCommand()
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("kolimist45@gmail.com", 'marvel12345')
                    server.sendmail('kolimist45@gmail.com', "durgeshzaware@gmail.com", content)
                    server.close()
                    print('Email sent!')
                    speak('Email sent!')

                elif 'kp' in recipient:
                    print('What should I say? ')
                    speak('What should I say? ')
                    content = takeCommand()
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("kolimist45@gmail.com", 'marvel12345')
                    server.sendmail('kolimist45@gmail.com', "divyesh.lesnar1997@gmail.com", content)
                    server.close()
                    print('Email sent!')
                    speak('Email sent!')

                elif 'harsh' in recipient:
                    print('What should I say? ')
                    speak('What should I say? ')
                    content = takeCommand()
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("kolimist45@gmail.com", 'marvel12345')
                    server.sendmail('kolimist45@gmail.com', "harshkoli07@gmail.com", content)
                    server.close()
                    print('Email sent!')
                    speak('Email sent!')

                elif 'yadu' in recipient:
                    print('What should I say? ')
                    speak('What should I say? ')
                    content = takeCommand()
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("kolimist45@gmail.com", 'marvel12345')
                    server.sendmail('kolimist45@gmail.com', "yadneshk45@gmail.com", content)
                    server.close()
                    print('Email sent!')
                    speak('Email sent!')    

                else:
                    print('Sorry ' + 'Sir' + '!, I am unable to send your message at this moment!')
                    speak('Sorry ' + 'Sir' + '!, I am unable to send your message at this moment!')



            except:
                print('Sorry ' + 'Sir' + '!, I am unable to send your message at this moment!')
                speak('Sorry ' + 'Sir' + '!, I am unable to send your message at this moment!')

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////        

#code to search on Wikipedia:-

        else:
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    print(results)
                    speak(results)
                except:
                    results = wikipedia.summary(query, sentences=2)
                    print(results)
                    speak(results)
            except:
                print("sorry")
                

input()                


