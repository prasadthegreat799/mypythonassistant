import speech_recognition as sr
import tkinter as tk
import pyttsx3



top=tk.Tk()
engine=pyttsx3.init()
r=sr.Recognizer()



def fun_speak(text):
    engine.say(text)
    engine.runAndWait()

def fun_listen():
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio=r.listen(source2)
            text=r.recognize_google(audio)
            text=text.lower()
            fun_speak(text)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError: 
        print("unknown error occured") 
         

          
frame = tk.Frame(top)
           
Btn_listen=tk.Button(frame,text="Click me",command=fun_listen)
Btn_listen.pack()
frame.pack() 

tk.mainloop()
            


