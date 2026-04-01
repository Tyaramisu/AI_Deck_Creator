import os
from dotenv import load_dotenv
import pandas as pd #Lets us import data, as seen in the previous TPs
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")

df = pd.read_excel("card_list.ods", engine="odf")
card_data_string = df.to_string() #This is so the AI can actually read the whole thing

print(f"Found {len(df)} cards.")
print(df.head(3)) #Just prints the first 3 cards, should be Arbok, Cloyster and Ekans

#This is a .txt file that we set up so the AI is given a clear context for what we are doing
with open("baseline.txt", "r", encoding="utf-8") as f:
    persona_content = f.read()

llm = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0,
    api_key=api_key
)

#Lets see if we can have a more prompt type loop
print("Type a deck you would like to make (ex: Make me a defensive Water type deck), (typing 'exit' will quit):")

while True:
    user_text = input("> ")

    if user_text.lower() == "exit":
        break

    message = [
        SystemMessage(content=f"{persona_content}\n\nDATABASE OF AVAILABLE CARDS:\n{card_data_string}"),
        HumanMessage(content=user_text)
    ]
    response = llm.invoke(message)

    print(response.content)
    print(response.usage_metadata)
    print("-" * 30)