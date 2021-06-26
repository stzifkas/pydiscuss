from gtts import gTTS
import speech_recognition as sr
import pyglet
from utilities import config

LANGUAGE = config.LANGUAGE
DEBUG = False

def mic_to_text():
    global DEBUG
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source, phrase_time_limit=5)
        try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
            message = recognizer.recognize_google(audio)
            if DEBUG:
                print(f"Recognized: {message}")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return message

def text_to_speech(**kwargs):
    text = kwargs["text"]
    myobj = gTTS(text=text, lang=LANGUAGE, slow=False)
    myobj.save("speech.mp3")
    music = pyglet.resource.media('speech.mp3',streaming=False)
    music.play()
    pyglet.app.event_loop.run()
    pyglet.app.event_loop.exit()
    return True

def main():
    testing_text = "This is me testing"
    text_to_speech(text=testing_text)

if __name__ == "__main__":
    main()