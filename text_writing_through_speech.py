import speech_recognition as sr

import pyttsx3

r = sr.Recognizer()
def record_text():
    #loop in case of errors
    while(1):
        try:
            #use the microphone as source of input
            with sr.microphone() as source2:
                #prepare recognizer to recive input
                r.adjust_for_ambient_noise(source2,duration=0.2)
                #listens for the user's input
                audio2 = r.listen(source2)
                #using google to recognize audio
                MyText = r.recognize_google(audio2)

                return MyText



        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occurred")
    return

def output_text(text):
     f = open("output.txt","a")
     f.write(text)
     f.write("\n")
     f.close()
     return

while(1):
    text = record_text()
    output_text(text)

    print("Wrote text")
