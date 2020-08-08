import os
import pyautogui
from time import sleep


#make sure to give permission to Terminal to control your computer under Accessibility

def auto_send_messages(message_input, number_of_times): #sends the message you typed
    #Don't change any of this
    sleep(0.5)
    for x in range(number_of_times):
        print("Loading message....")
        sleep(0.5)
        pyautogui.typewrite(message_input, interval=0.01) #interval is how fast the typing should be between each key stroke
        sleep(0.1)
        pyautogui.typewrite(['enter'], interval = 0.15) #makes sure the last sentence was/is sent
        print("Message sent.")     
    pyautogui.typewrite(['enter'], interval = 0.15) #makes sure the last sentence was/is sent

def auto_send_default_messages(): #sends messages from another file if user doesn't input a message
    #Don't change any of this
    file_name = "testTxt.txt"
    read_file = open(file_name, "r")
    print("Loading message....")
    sleep(1.5)
    for sentences in read_file:
        sleep(0.5)
        pyautogui.typewrite(sentences, interval=0.01) #interval is how fast the typing should be between each key stroke
    pyautogui.typewrite(['enter'], interval = 0.15) #makes sure the last sentence was/is sent
    pyautogui.typewrite(['enter'], interval = 0.15) 
    read_file.close()

def open_app():
    #Don't change any of this
    path = "Messages"
    os.system(f"open  -a {path}")
    print("{0} is open".format(path))

def open_testing_input_file_app():
    #Don't change any of this
    path = "inputTesting.txt"
    os.system(f"open {path}")
    print("{0} is open".format(path))
    
def end():
    #Don't change any of this
    print("All messages sent")
    print("End of program")