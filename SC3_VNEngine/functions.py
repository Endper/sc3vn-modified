from collections import deque

#Define variables
prevImage = []

#Displays an image accordingly in a tidy display
def print_image(image : list):
    global prevImage
    if (len(image) == 15 or (image == "null")):
        for i in range(0,15):
            #Check if an Image was inputted
            if not (image == "null") :
                #If there was an Image, print it out
                print(f"[{image[i]}]")
            else:
                #Otherwise, print the previous Image if there was one
                if not (not prevImage):
                    print(f"[{prevImage[i]}]")
                else:
                    print(f"[{' ' * 60}]")

    #Set the variable prevImage to the most recently printed image
    if (image != "null"):
        prevImage = image

#Displays the text that was provided
def print_text(text : str, lineAmount : int = "null"):
    #Declare variables
    toPrint = ""
    complete = False
    #Make a list of all words in the text
    words = deque(text.split(" "))
    lines = 0
    
    while not complete:
        #Clear the previous values from buffer
        toPrint = ""

        #Repeat until there are no more words
        while len(words) > 0:
            if (len(toPrint) + len(words[0])) <= 60:
                #If there is space for the next word, add it to the buffer and remove it from the list
                toPrint += words[0]
                words.popleft()
                if (len(toPrint)) < 60:
                    #If there is room for a space, add it to the buffer
                    toPrint += " "
            else:
                #If there isn't space for the next word, check if it is longer than 60 characters to prevent an infinite loop
                if len(words[0]) > 60:
                    print("[Error: Words cannot be longer than 60 characters!           ]")
                    complete = True
                #Exit the loop
                break
            
        #If there are no words left, it exits the loop
        if len(words) == 0:
            complete = True

        #Add spaces if necessary
        if not (len(toPrint) == 60):
            toPrint += " " * (60 - len(toPrint))
            

        #Print the buffer
        print(f"[{toPrint}]")
        lines += 1

    #Print remaining lines if necessary
    #If the line amount isn't specified:
    if (lineAmount == "null"):
        if lines < 4:
            for _ in range(4 - lines):
                print(f"[{' ' * 60}]")
    #If it is, print the specified amount
    else:
        for _ in range(lineAmount):
            print(f"[{' ' * 60}]")


#Displays the question with the image and answers that were provided
def ask_question(question : str, answers : list, image : list ="null"):
    #Add newlines, 49 so that it doesn't compress automatically
    print("\n" * 49)
    print(f"[{'=' * 60}]")
    #Print Image
    print_image(image)
    print(f"[{'=' * 60}]")
    #Ask Question
    print_text(question, 1)

    #Print out options
    for j, i in enumerate(answers, start=1):
        print_text(f"({j}). {i}", 1)

    #Add the bar at the bottom
    print(f"[              Press 1 to {len(answers)} to select an option              ]")
    print(f"[{'=' * 60}]")


# These are the main functions that will be 
# used by the user throughout the library

#One of the main functions for questioning the user on their choice
def ask_prompt(question : str, answers : list, image : list ="null"):
    #Get input
    while True:
        ask_question(question, answers, image)
        choice = input("")
        
        if int(choice) <= len(answers) and int(choice) > 0:
            break
    
    return choice

#The other main functions for displaying dialogue
def create_dialogue(text : str, image : list ="null") :
        print("\n" * 49)
        print(f"[{'=' * 60}]")
        #Print the Image
        print_image(image)
        print(f"[{'=' * 60}]")
        #Write all the text
        print_text(text)
        print(f"[{'=' * 60}]")
        input("")
