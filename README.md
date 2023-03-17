# keylogger

### Introduction:
In this project, I have developed a keylogger that captures the users key logs and uploads the keystroke file to mega storage so that hacker can remotely access the keystrokes. This project has been developed in python. The application is able to bypass defender and able to run in background without user knowing about it.
<br>
<br>
### Project Description:
The project basically has two parts : One for capturing the user keylog  and another part to upload to mega repository for accessing the keylog file remotely . The keylogger monitors the keystrokes continuously and saves the file locally as log.txt. In the second part of the program, the file log.txt is uploaded to mega repo.
The program takes the keyboard input with the help of pynput.keyboard package.
