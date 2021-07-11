import pyttsx3
import speech_recognition as sr
import pyaudio


r = sr.Recognizer()
engine = pyttsx3.init()

introduction = " Hi, myself siri a chatbot"
engine.say(introduction)
engine.runAndWait()


def take_command():

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_thresh1old = 1
        print("listening....")

        audio=r.listen(source)
        ans=r.recognize_google(audio)
        print(ans)

        try:
            if ans == "hello":
                print(" hello ,how shall i help you")
                engine.say("hello ,how shall i help you")
                engine.runAndWait()


            elif ans == "how are you":
                print("i am fine , what about you?")
                engine.say("i am fine , what about you?")
                engine.runAndWait()
                return take_command()

            elif ans == "i am also fine ":
                print("  that's great ")
                engine.say(" that's great")
                engine.runAndWait()
                return take_command()

            elif ans == " who is your creator? ":
                print(" mananya gaur is my creator")
                engine.say("mananya gaur is my creator ")
                engine.runAndWait()
                return take_command()

            elif ans == "thanks ":
                print(" welcome ")
                engine.say(" welcome ")
                engine.runAndWait()
                return take_command()







        except:
             engine.say("sorry, Try again")
             print(": sorry try again")
             return take_command()
take_command()


