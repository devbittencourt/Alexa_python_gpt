import pyperclip
import pyttsx3
import speech_recognition as sr
import keyboard
import time

keyboard.send('windows')

time.sleep(3)

keyboard.write('chrome')

time.sleep(3)

keyboard.send('enter')

time.sleep(4)

site = 'https://chat.openai.com/'

keyboard.write(site)

time.sleep(2)

keyboard.send('enter')

time.sleep(2)

# Cria um objeto de sintetização de voz
engine = pyttsx3.init()
r = sr.Recognizer()
mic = sr.Microphone()

# Define a voz a ser usada
voices = engine.getProperty('voices')

# Verifica se há vozes disponíveis
if voices:
    engine.setProperty('voice', voices[0].id)
else:
    print("Nenhuma voz encontrada")

# Define a taxa de fala
rate = engine.getProperty('rate')
engine.setProperty('rate', 200)

engine.setProperty('volume', 2.0)


# Função que reproduz a voz
def speak(text):
    engine.say(text)
    engine.runAndWait()


while True:
    try:
        # Recebe a entrada do usuário
        with sr.Microphone() as source:
            speak("Diga alguma coisa!")
            audio = r.listen(source, timeout=7)
            text = ''

        # Transcreve o áudio para texto
        try:
            text = r.recognize_google(audio, language='pt-BR')
            print(text)

            # Se a palavra 'chat' estiver no texto
            if 'chat' in text.lower():
                texto = text
                # Escreve o texto na tela usando o teclado
                keyboard.write(texto)

                time.sleep(1)
                keyboard.send('enter')
                time.sleep(1)

                # Aguarda 10 segundos
                time.sleep(10)

                # Pressiona Shift + Tab 4 vezes
                for i in range(4):
                    keyboard.send('shift+tab')
                    time.sleep(0.2)

                # Pressiona Enter copiando a mensagem
                time.sleep(1)
                keyboard.send('enter')
                time.sleep(1)

                # Salva o texto da área de transferência na variável 'fala'
                fala = pyperclip.paste()
                time.sleep(1)

                # Reproduz a variável 'fala' como áudio
                speak(fala)

                # Pressiona Tab 5 vezes retornando a caixa de dialogo
                for i in range(5):
                    keyboard.send('tab')
                    time.sleep(0.2)

        except sr.UnknownValueError:
            print("Não foi possível reconhecer a fala")
    except sr.WaitTimeoutError:
        print("Timeout! Não foi detectada nenhuma fala.")
