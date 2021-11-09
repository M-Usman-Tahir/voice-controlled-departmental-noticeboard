import speech_recognition as sr

def speak(engine):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            return r.recognize_google(audio)            
        except sr.UnknownValueError:
            engine.say("Google Speech Recognition could not understand audio")
            return ""
        except sr.RequestError as e:
            engine.say("Could not request results from Google Speech Recognition service; {0}".format(e))
            return ""
        except Exception as e:
            engine.say("Oooops, an error occurred: ")
            engine.say(str(e))
            print(e)
            return ""
        finally:
            engine.runAndWait()
            
def IfIn(words, text, opr="or"):
    if opr=="or":
        for word in words:
            if word in text:
                return True
        return False
    for word in words:
        if word in text:
            continue
        return False
    return True