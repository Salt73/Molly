import google.generativeai as genai
import speech_recognition as sr
import pyttsx3
import pygame
import time
from datetime import date, datetime
from openai import OpenAi

client = OpenAi()
pygame.mixer.init()

# Initialize TTS engine (pyttsx3)
engine = pyttsx3.init()
engine.setProperty('rate', 190)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 1 for female voice, 0 for male

# Initialize Gemini Pro model
model = genai.GenerativeModel('gemini-pro')
use_openai_tts = True  # Switch this to False to use pyttsx3 locally

def append2log(text):
    today = date.today().isoformat()
    timestamp = datetime.now().strftime("%H:%M:%S")
    fname = f'chatlog-{today}.txt'
    with open(fname, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {text}\n")

def speak(text):
    if use_openai_tts:
        response = client.audio.speech.create(
            model='tts-1',
            voice='nove',  # use 'alloy' for male voice if preferred
            input=text
        )
        fname = 'output.mp3'
        with open(fname, 'wb') as mp3file:
            response.write_to_file(mp3file)
        try:
            pygame.mixer.music.load(fname)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
            pygame.mixer.music.stop()
        except KeyboardInterrupt:
            pygame.mixer.music.stop()
    else:
        engine.say(text)
        engine.runAndWait()

def main():
    rec = sr.Recognizer()
    mic = sr.Microphone()
    rec.dynamic_energy_threshold = False
    rec.energy_threshold = 400
    sleeping = True
    talk = []

    print("Starting Molly AI Assistant. Say 'Molly' to wake me up.")

    while True:
        with mic as source:
            rec.adjust_for_ambient_noise(source, duration=0.5)
            print("Listening...")

            try:
                audio = rec.listen(source, timeout=10, phrase_time_limit=15)
                text = rec.recognize_google(audio)
                print(f"Recognized: {text}")

                lower_text = text.lower()

                if sleeping:
                    if "molly" in lower_text:
                        request = lower_text.split("molly", 1)[1].strip()
                        sleeping = False
                        append2log("_" * 40)
                        talk = []
                        if len(request) < 5:
                            speak("Hi, how can I help you?")
                            append2log("AI: Hi, how can I help you?")
                            continue
                    else:
                        continue
                else:
                    request = lower_text
                    if "that's all" in request or "goodbye" in request:
                        append2log(f"You: {request}")
                        speak("Goodbye!")
                        append2log("AI: Goodbye.")
                        print("Goodbye!")
                        sleeping = True
                        continue

                    if "molly" in request:
                        request = request.split("molly", 1)[1].strip()

                append2log(f"You: {request}")
                print(f"You: {request}\nAI: ", end='')

                talk.append({'role': 'user', 'parts': [request]})
                response = model.generate_content(talk, stream=True)

                full_response = ""
                for chunk in response:
                    print(chunk.text, end='')
                    full_response += chunk.text.replace("*", "")

                print('\n')
                speak(full_response)

                talk.append({'role': 'model', 'parts': [full_response]})
                append2log(f"AI: {full_response}")

            except Exception as e:
                print(f"Error: {e}")
                continue

if __name__ == "__main__":
    main()
