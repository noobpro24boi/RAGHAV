import pyttsx3
ts=pyttsx3.init()
speech=input("what do you want to say:")
ts.say(speech)
ts.runAndWait()
