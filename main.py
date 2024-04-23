#Code written by Jianping
#Credits: MerlinAI, ChatGPT, HuggingFace
#Main.py scraps your messages in telegram and put them in the excel file, do read the DOCS for telegram API 
#unsure if you can use BotFather.
#I dun fully understand just guessing


#Importing libraries
from pyrogram import Client
from dotenv import load_dotenv
import os
import pandas as pd

#Create a .env file to get your keys, keep them a secret
load_dotenv()

#idk what this means but it just stores your Keys in a map?? or a dict?
CONFIG = {
    "telegram_api_id": int(os.getenv("TG_API_ID")),
    "telegram_hash": os.getenv("TG_API_HASH"),
}

#I assume this connects your account? where generally client means you
app = Client("my_account", CONFIG["telegram_api_id"], CONFIG["telegram_hash"])

#import your chatid here, this can be found telegram.com 
chat_id = "#input your chat id here" 

message_limit = 100  # you can set how many messages you wish to scrap from

#make sure its async(asynchronus?)
async def main():
    messages_data = []  # List to store message data
    async with app:
        async for message in app.get_chat_history(chat_id, limit=message_limit):
            messages_data.append({"Message": message.text})  #with every text scraped put in an array/list

    df = pd.DataFrame(messages_data)

    # Save to an Excel file
    excel_filename = f"{chat_id}.xlsx" #this thing determines the file name using a fstring to make my life easier, you can change to be dynamic if uw 
    df.to_excel(excel_filename, index=False)
    print(f"Messages saved to {excel_filename}")

app.run(main())

