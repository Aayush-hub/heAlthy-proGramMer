from datetime import date               #built-in module
from datetime import datetime           #built-in module
from time import time                   #built-in module
from plyer import notification          #pip install plyer

def speak(str):
    from win32com.client import Dispatch   #pip install pywin32
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    print("************HeAlth aLarm***********")
    
    print("hello world")
    print("Welcome to the Office")
    speak("Welcome to the Office")
    today = date.today()
    tme = datetime.now().time()
    print("Date: ",today)
    print(f"Time: {tme} seconds")
    speak(f"Today's date is {today} and time is {tme}seconds.. Lets begin")
    #taking the initial time
    init_water = time()
    init_exercise= time()
    init_eyes = time()
    watersecs = 40*60     #in seconds
    exercisesecs = 30*60   #in seconds
    eyessecs = 45*60    #in seconds
    while True:
        if time() - init_water > watersecs:
            notification.notify(
                title = "***Please Drink Water to be healthy***",
                message = "Drinking Water Helps Maintain the Balance of Body Fluids. ",
                app_icon = "c:/Users/anshul garg/Desktop/water_bottle.ico",    #ico file should be downloaded
                timeout = 6
            )
            speak("Water Drinking time. Enter 'zero' to stop the alarm.")
            inp = input("Enter code ")
            while inp == "0":
               break
            else:
                continue
            #printing the real time water has dranked
            print("Water drank at: ",datetime.now().time())
            init_water = time()
            
            

        if time() - init_eyes >eyessecs:
            notification.notify(
                title = "**Relax your eyes**",
                message = "Eye exercise, as well as a proper diet and rest, are all important to the long-term health of your eyes.",
                app_icon = "c:/Users/anshul garg/Desktop/eye.ico",    #ico file should be downloaded
                timeout = 6
            )
            speak("Eye exercise time. Enter 'zero' to stop the alarm.")
            inp = input("Enter code ")
            while inp == "0":
                break
            else:
                continue
           #printing the real time eye exercise has done
            print("Eye exercise done at: ",datetime.now().time())
            init_eyes = time()
            
            
               

        if time() - init_exercise > exercisesecs:
            notification.notify(
                title = "**Move back and relax**",
                message = "Regular Exercise can make You Feel Happier. It Can Help With Weight Loss. It Is Good for Your Muscles and Bones. It Can Increase Your Energy",
                app_icon = "c:/Users/anshul garg/Desktop/exercise.ico",     #ico file should be downloaded
                timeout = 6
            )
            speak("Physical Activity Time. Enter 'zero' to stop the alarm.")
            inp = input("Enter code ")
            while inp == "0":
                break
            else:
                continue
            #printing the real time exercise has done
            print("Physical exercise done at: ",datetime.now().time())
            init_exercise = time()
            
