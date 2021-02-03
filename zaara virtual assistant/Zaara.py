import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pw
import webbrowser
import os
import wikipedia as wp

r = sr.Recognizer()
speaker = pt.init()
voices = speaker.getProperty("voices")
speaker.setProperty("voice", voices[2].id)
a = 1


def opfold(fi, dri):
    c = 1
    while c != 0:
        try:
            os.startfile(dri+":\\"+fi)
            speaker.say("opening Folder"+fi)
            speaker.runAndWait()
            c = 0
            speaker.say("to stop virtual assistant say stop")
            speaker.runAndWait()
        except Exception as ex:
            speaker.say("Folder not found")
            speaker.runAndWait()
            speaker.say("please say again the name of Folder")
            speaker.runAndWait()
            fi = asist()
            fi = fi.lower()
            if "ok stop" in fi:
                c = 0
            print(ex)


def talk(tex):
    tex = str(tex)
    tex = tex.lower()
    if "name" in tex and "your" in tex:
        speaker.say("My name is zaara and i am a virtual assistant")
        speaker.runAndWait()
    elif "play" in tex:
        comd = tex.replace("play", "")
        pw.playonyt(comd)
        speaker.say("playing "+comd+"on Youtube")
        speaker.runAndWait()
        speaker.say("to stop virtual assistant say stop")
        speaker.runAndWait()
    elif "ayub" in tex:
        speaker.say("Ayub born 9 february 2001 in mumbai at sindhu kamble hospital ")
        speaker.say("he completed his schooling at shivaji vidiyalaya and then done his high school from R J college")
        speaker.say("currently he is doing Engineering from swami vivekanand anh he created me to")
        speaker.runAndWait()

    elif 'facebook' in tex:
        speaker.say("opening Facebook")
        webbrowser.open_new("www.facebook.com")
        speaker.say("to stop virtual assistant say stop")
        speaker.runAndWait()
    elif "search" in tex:
        comd = tex.replace("search", "")
        speaker.say("searching on Google")
        pw.search(comd)
        speaker.say("to stop virtual assistant say stop")
        speaker.runAndWait()

    elif "open" in tex:
        speaker.say("from which drive you want to open a folder c d e or f")
        speaker.runAndWait()
        lis = asist()
        lis = lis.lower()
        global a
        if "c" in lis and "not" not in lis:
            print(lis)
            speaker.say("from c which folder you want to open")
            speaker.runAndWait()
            dri = "c"
            fol = asist()
            fol = fol.lower()
            if "stop" in fol:
                a = 0
                return
            opfold(fol, dri)
        elif "d" in lis:
            speaker.say("from d which folder you want to open")
            speaker.runAndWait()
            dri = "d"
            fol = asist()
            fol = fol.lower()
            if "stop" in fol:
                a = 0
                return
            opfold(fol, dri)
        elif "e" in lis:
            speaker.say("from e which folder you want to open")
            speaker.runAndWait()
            dri = "e"
            fol = asist()
            fol = fol.lower()
            if "stop" in fol:
                a = 0
                return

            opfold(fol, dri)
        elif "f" in lis:
            speaker.say("from f which folder you want to open")
            speaker.runAndWait()
            dri = "f"
            fol = asist()
            fol = fol.lower()
            if "stop" in fol:
                a = 0
                return
            opfold(fol, dri)
        elif "stop" in lis:
            a = 0
        else:
            speaker.say("Please say again")
            speaker.runAndWait()
            talk("open")
    elif "who" in tex:
        tex = tex.replace("who is ", "")
        try:
            info = wp.summary(tex, 4)
            info = str(info)
            speaker.say(info)
            speaker.runAndWait()
            print(info)
        except:
            tex = "who is "+tex
            speaker.say("I don't "+tex)
            speaker.runAndWait()

    elif "what" in tex:
        tex = tex.replace("what is ", "")
        try:
            info = wp.summary(tex, 4)
            info = str(info)
            speaker.say(info)
            speaker.runAndWait()
            print(info)
        except:
            tex = "what is "+tex
            speaker.say("I don't "+tex)
            speaker.runAndWait()


    elif "stop" in tex:
        speaker.say("ok")
        speaker.runAndWait()
    else:
        speaker.say("Please say again")
        speaker.runAndWait()


def asist():
    try:
        with sr.Microphone() as source:
            print("listening...")
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
            com = r.recognize_google(audio)
            print(com)
            com = com.lower()
    except Exception as e:
        print("NOT RECOGNIZE", e)
        return "NOT RECOGNIZE"
    return com


speaker.say("hi")
speaker.say("My name is zaaraa what I can get for you ")
speaker.runAndWait()

while a != 0:
    text = asist()
    talk(text)
    if "stop" in text:
        a = 0

speaker.say("closing Virtual assistant zaaraa")
speaker.runAndWait()
exit(0)

