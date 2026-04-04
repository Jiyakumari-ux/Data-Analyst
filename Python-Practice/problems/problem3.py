import pyttsx3
import time
engine = pyttsx3.init()
lines = [
"I will speak this next line",
"I will become succesful",
"I will be a good human being"]
for line in lines:
 engine.say(lines)
engine.runAndWait()
time.sleep(2)