import pyttsx3

if __name__ == "__main__":
    print("Welcome to robospeaker application created by Abhishek")

    while(True):

        x = input("Enter what has to be said: ")

        if(x == 'bye' or
           x == 'BYE' or
           x == 'Bye'):
            print("Bye!")
            command.say("Bye!")
            command.runAndWait()
            break
    

        #initialise the text to speech engine

        command = pyttsx3.init()

        #setting up properties in this case delay time

        command.setProperty("rate",150)

        #speak the input

        command.say(x)

        #run and wait operation

        command.runAndWait()