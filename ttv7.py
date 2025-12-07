
import pyttsx3
import speech_recognition as ss
import google.generativeai as genai

api_key = "api key"
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")
chat = model.start_chat()
print("Chat with davis! type exit to end the chat.")

a = ss.Recognizer()

def speak_text(text):
    
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 25)
    engine.say(text)
    engine.runAndWait()

while True:
    with ss.Microphone() as source:
        print("Listening...")
        
        a.adjust_for_ambient_noise(source)
        audio = a.listen(source)

    try:
        user_input = a.recognize_google(audio)
        print("You said:", user_input)
    except ss.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        speak_text("Sorry, I could not understand the audio.")
        continue  
    except ss.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        continue  

    if user_input.lower() == "exit":
        break

    response = chat.send_message(user_input)
    print("davis:", response.text)
    
    
    speak_text(response.text)