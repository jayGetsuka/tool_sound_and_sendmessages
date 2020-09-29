def music(*data):
        from gtts import gTTS
        from playsound import playsound

        audio = 'XXXXXX.mp3'
        language = data[0][1] # data[1] is a language
        clip = gTTS(text=data[0][0].strip(), lang=language, slow=False) #data[0] is messages
        clip.save(audio)
        playsound(audio)

def Sendmessages(*data):
    from twilio.rest import Client
    client = Client(data[0], data[1]) # account and token
    client.messages.create(from_= data[2], body= data[3].split(), to=data[4]) # 2 is numbers , 3 is messages, 4 is numbers telephone


print("""FUNCTION IN PROGRAM
[1.] >>> CREATE SOUND.
[2.] >>> SENDMESSAGES TO CLIENT.
[3. or other] >>> SHUT DOWN PROGRAM.
""")
while True:
    choose = int(input("Choose number : "))
    if choose == 1:
        message = input("INPUT MESSAGE AND LANGUAGE example( HELLO WORLD, en)  : ").split(",")
        music(message)
    elif choose == 2:
        print("IF YOU DON'T HAVE AN ACCOUNT YET, APPLY AT https://www.twilio.com/try-twilio")
        send = input("INPUT ACCOUNT_SID, AUTH_TOKEN, NUMBER TWILIO, MESSAGES TO CLIENT, NUMBERS CLIENT (+66XXXXXXXXX)").split(",")
        Sendmessages(send)
    else:
        print("SUCCESSFUL...")
        break
        
