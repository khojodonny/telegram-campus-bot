#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Campus Landmark Descriptions - Core Data Only

landmark_data = {
    "Main Gate": "Primary entrance to the campus",
    "Administration Block": "Beside the main gate. Opposite Mechanical & Electrical Dept. Green and white.",
    "Lecture Hall": "First building from third gate. One-storey, green and white, metal gates.",
    "Library": "After lecture hall via third gate, with a garage in between. Opposite the auditorium. Dark brown and beige.",
    "Auditorium": "In the middle of campus. Opposite the library. Large forecourt with three statues.",
    "FIMMS": "Behind the auditorium, ~30m away. Three-storey, beige and dark brown.",
    "Mining and Mineral Technology Faculty": "Right behind FIMMS. Very close.",
    "Old FIMMS": "Opposite Mining Dept, separated by the main road.",
    "Clinic": "Beside the Old FIMMS building.",
    "Mathematics Department": "Behind the clinic. Has a forecourt with two tents.",
    "Old Mining Block": "Beside Math Dept forecourt. Stretches toward the library.",
    "School Field": "Adjacent to KT Hall. Accessible from Mechanical & Electrical Dept.",
    "KT Hall": "5-minute walk from auditorium. Reachable from Mechanical & Electrical Dept or via bridge route.",
    "Chamber of Mines": "Next to KT Hall on the right when facing KT. Also called Traditional Hall.",
    "Mechanical and Electrical Engineering Department": "Opposite Administration Block. Leads to School Field and KT Hall."
}

def get_landmark_description(landmark_name):
    """Returns the description for a given landmark"""
    return landmark_data.get(landmark_name, "Landmark not found")

# Example usage:
if __name__ == "__main__":
    print("Available Landmarks:")
    for name in sorted(landmark_data.keys()):
        print(f"- {name}")
    
    landmark = input("\nEnter a landmark name: ").title()
    print(f"\n{landmark}: {get_landmark_description(landmark)}")


# In[ ]:


get_ipython().system('pip install python-telegram-bot')


# In[6]:


# Cell 1: Install required package
get_ipython().system('pip install python-telegram-bot')


# In[13]:


# Cell 1: Install required package
get_ipython().system('pip install python-telegram-bot nest_asyncio')
import nest_asyncio
nest_asyncio.apply()  # This fixes the event loop conflict


# In[14]:


# Cell 2: Import libraries and define landmarks
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import asyncio

LANDMARKS = {
    "Main Gate": "Primary entrance to the campus",
    "Administration Block": "Beside the main gate. Opposite Mechanical & Electrical Dept.",
    "Lecture Hall": "First building from third gate. Green and white.",
    "Library": "Opposite auditorium. Dark brown and beige.",
    "Auditorium": "Center of campus with three statues.",
    "FIMMS": "Behind auditorium. 3-storey beige building.",
    "Mining Faculty": "Right behind FIMMS.",
    "Old FIMMS": "Opposite Mining Dept across main road.",
    "Clinic": "Beside Old FIMMS.",
    "Math Department": "Behind clinic with tented forecourt.",
    "Old Mining Block": "Beside Math Dept toward library.",
    "School Field": "Adjacent to KT Hall.",
    "KT Hall": "5-min walk from auditorium.",
    "Chamber of Mines": "Next to KT Hall (Traditional Hall).",
    "Mechanical & Electrical Dept": "Opposite Administration Block."
}


# In[15]:


# Cell 3: Bot handlers setup
landmark_keys = [[landmark] for landmark in sorted(LANDMARKS.keys())]
reply_markup = ReplyKeyboardMarkup(landmark_keys, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to Campus Navigator Bot\n\n"
        "Send /landmarks to see all available locations\n"
        "Or type/select any landmark name to get its description",
        reply_markup=reply_markup
    )

async def list_landmarks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Available Landmarks:\n\n" + "\n".join(f"- {loc}" for loc in sorted(LANDMARKS)),
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    if text in LANDMARKS:
        await update.message.reply_text(
            f"{text}:\n{LANDMARKS[text]}",
            reply_markup=reply_markup
        )
    else:
        await update.message.reply_text(
            "Landmark not found. Send /landmarks to see available options",
            reply_markup=reply_markup
        )


# In[16]:


# Cell 4: Create and run the bot
bot_token = "7619324978:AAF_S2_jp_f-wI8JPq-TX55rlPfrmgQHOBI"  # Your token here

async def main():
    application = Application.builder().token(bot_token).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("landmarks", list_landmarks))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    
    # Keep the bot running
    while True:
        await asyncio.sleep(1)

# Start the bot
import asyncio
asyncio.create_task(main())


# In[ ]:


# 1. Save this as 'bot.py' on your computer
from telegram.ext import ApplicationBuilder

application = ApplicationBuilder().token("7619324978:AAF_S2_jp_f-wI8JPq-TX55rlPfrmgQHOBI").build()

# Add your handlers (start, landmarks, etc) here
# Use the same code from the working Jupyter version

application.run_polling()


# In[ ]:




