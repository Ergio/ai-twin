from pyrogram import Client, filters
from dotenv import load_dotenv
import os

from llm_workflow.main_chat_workflow import MainChatWorkflow


load_dotenv()

app = Client(
    "my_account",
    api_id=os.getenv('API_ID'),
    api_hash=os.getenv('API_HASH')
)


@app.on_message(filters.text & filters.private)
def start_command(client, message):
    main_wf = MainChatWorkflow()

    import uuid
    thread_id = str(uuid.uuid4())
    result = main_wf.chat_to_ai(message.text, thread_id=thread_id)
    ai_message = result['messages'][-1].content
    message.reply_text(ai_message)

if __name__ == "__main__":
    app.run()