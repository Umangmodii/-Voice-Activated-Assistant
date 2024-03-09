import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

while 1:
    print("Enter the Word : ")
    s1 = input()
    speaker.Speak(s1)