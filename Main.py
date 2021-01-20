import wolframalpha # Importing the Wolfram|Alpha library for Project.

AppID = "LRWVAL-77HYY7K9U6" # This is the AppID I got from Wolfram|Alpha for integration in my Project.
Client = wolframalpha.Client(AppID) # This gives the program my AppID telling it I am a Client.

while(1): # I used this to put my Program in while loop so that it doesn't stop just after giving a single output.
    Question = input("Enter the Word: ") # This takes the input for my Program.
    Client_Query = Client.query("What is the Meaning of " + Question + "?") # It forwards the input to my Program.
    Answer = next(Client_Query.results).text # This gets the Answer from Wolfram|Alpha using my Program
    print(Answer) # It prints the Result so that I can see Output.
    print("") # It is just to give a single-line spacing between the Previous Output and the New Word.