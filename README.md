# AI Deck Creator

This project was made for the Machine Learning Course of UE7 | Masters 1 IOT

I have always been a fan of Trading Card Games, specifically the Pokémon one.
So, after learning the basics on how to use AI within a python code, I decided to make a quick Deck builder with it! cause why not, sometimes its cool to just be able to get given a random deck and test things out.

For example, you can ask it "Can I get a deck which is mainly defensive" and it'll give one to you
or you can ask "Can I get a deck that uses Poliwrath" and it will make a deck which is built around the function of the Poliwrath card

# But how does it work?!

First and foremost, you will need to give your own ChatMistralAI API key, simply put it in the same file as the .py code, in a file named .env
It must be written as such:
MISTRAL_API_KEY=[And then your API key here]

This project has 4 main components:

-A venv which is, well, the python virtual environment, to access it, simply do as you would do with any other python environments.

-A File I called "baseline.txt"
Basically, its a series of instruction that we give the ai as soon as it boots up, give it some context you know? so it stays in line and actually answers any question we really send it (Deck building wise of course, I'm sure if you force it to answer something else then it will go and answer that something else)

-card_list:
This is a file I will be updating from time to time, its basically just a list of cards the AI has direct access to, I did set it so the AI could look online real quick to try and find cards that could match any given task, but it will prioritize the cards found within this Class file

-deckbuild.py
As the name would imply, this is the regular Python code

# What is there left to do with this code?
I am not quite sure myself! of course, I will be continuing with adding more cards into the direct database, but I like, expected the project to be more indepth, but then it was like, already done haha

# Credits stuff
The Pokémon TCG is owned by | The Pokémon Company
The different Libraries used to make this application a reality goes to their respective creators