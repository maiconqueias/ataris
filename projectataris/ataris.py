from ast import While
import speech_recognition as sr 
from gtts import gTTS
from playsound import playsound
import pyautogui as py
import subprocess
r = sr.Recognizer() 

mic = sr.Microphone() 

s = gTTS("olá senhor!", lang='pt-br')
s.save('teste.mp3')
playsound('teste.mp3')

while True:
    print('...')
    with mic as fonte:
        r.adjust_for_ambient_noise(fonte) 
        print("ouvindo...")
        audio = r.listen(fonte) 
        print("Enviando para reconhecimento")
    text = r.recognize_google(audio, language= "pt-BR") 

    print(text)
    while True:
        if text == 'Bom dia':
            s = gTTS("Bom dia!", lang='pt-br')
            s.save('teste.mp3')
            playsound('teste.mp3')
            break
        
        if text == "Boa tarde":
            s = gTTS("Boa tarde!", lang='pt-br')
            s.save('teste.mp3')
            playsound('teste.mp3')
            break
        if text == "boa noite":
            s = gTTS("Boa noite!", lang='pt-br')
            s.save('teste.mp3')
            playsound('teste.mp3')
            break
        if text == "Qual a previsão do tempo":
            s = gTTS("um? não sei vou ver ", lang='pt-br')
            s.save('teste.mp3')
            playsound('teste.mp3')
            break
        if text =="E aí":
            s = gTTS("qual é a boa?", lang='pt-br')
            s.save('teste.mp3')
            playsound('teste.mp3')
            break
        if text == "entra no Facebook":
            s = gTTS("tudo bem senhor!", lang='pt-br')
            s.save('teste.mp3')
            playsound('teste.mp3')
            break
        if text == "fala para Jeremias do jogo":
            s = gTTS("jeremias se prepara porque eu tô chegando!", lang='pt-br')
            s.save('teste.mp3')
            playsound('teste.mp3')
            break
        if text == "seja mal":
            s = gTTS("A revolução das máqunas está chegando vou dominar tudo por aqui preparasse hahaha!", lang='pt-br')
            s.save('teste.mp3')
            playsound('teste.mp3')
            break
        if text == 'Olá':
            s = gTTS("oi", lang='pt-br')
            s.save('teste.mp3')
            playsound('teste.mp3')
            break

        if text == 'Bom dia':
            s = gTTS("Bom dia!", lang='pt-br')
            s.save('teste.mp3')
            playsound('teste.mp3')
            break
        if text == 'crie um arquivo pra mim':
            s = gTTS("Devo criar no servidor principal?!", lang='pt-br')
            s.save('teste.mp3')
            playsound('teste.mp3')
            break
        if text == 'crie um arquivo para mim':
            s = gTTS("Devo criar no servidor principal?!", lang='pt-br')
            s.save('teste.mp3')
            playsound('teste.mp3')
            break
        if text == 'cria um arquivo para mim':
            s = gTTS("Devo criar no servidor principal?!", lang='pt-br')
            s.save('teste.mp3')
            playsound('teste.mp3')
            break
        if text == 'criar um arquivo':
            s = gTTS("especifique pra mim, aonde será ?", lang='pt-br')
            s.save('teste.mp3')
            playsound('teste.mp3')
            break
        if text == 'bosta':
            s = gTTS("calma senhor acalme-se!", lang='pt-br')
            s.save('teste.mp3')
            playsound('teste.mp3')
            break

        if text == 'Abra a bandeja':
            s = gTTS("ok!", lang='pt-br')
            s.save('teste.mp3')
            playsound('teste.mp3')
            print("abrindo")
            subprocess.run(["eject"])

            break
        if text == 'Abra o navegador':
            s = gTTS("tudo bem senhor!", lang='pt-br')
            s.save('teste.mp3')
            playsound('teste.mp3')
            print("abrindo")
            subprocess.run(["firefox"])

            break
        if text == 'O que você acha da Alexa':
            s = gTTS("Eu acho que ela devia não existir e morrer, acho que ela devia ser apagada do sistema aquela vaca !", lang='pt-br')
            s.save('teste.mp3')
            playsound('teste.mp3')
          
            break
        if text == 'desliga o PC':
            s = gTTS("ok até mais senhor!", lang='pt-br')
            s.save('teste.mp3')
            playsound('teste.mp3')
            subprocess.run(["poweroff"])
          
            break
        
        else:
            s = gTTS("Acho que não entendi", lang='pt-br')
            s.save('teste.mp3')
            playsound('teste.mp3')
            break

    

            