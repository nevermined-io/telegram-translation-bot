
import os
import time
import logging
import requests
from dotenv import load_dotenv
import telebot
import threading

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Retrieve environment variables
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
AGENT_API_URL = os.environ.get('AGENT_API_URL')
AGENT_AUTH_TOKEN = os.environ.get('AGENT_AUTH_TOKEN')
AGENT_DID = os.getenv('AGENT_DID')

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    """
    Sends a welcome message when the /start or /hello command is issued.

    :param message: The message object containing the command.
    """
    bot.reply_to(message, "Welcome to the Translator Bot! Send me a message, and I will translate it to Spanish.")

@bot.message_handler(func=lambda msg: True)
def handle_message(message):
    """
    Handles incoming text messages and starts the translation process.

    :param message: The message object containing the user's text.
    """
    user_message = message.text
    chat_id = message.chat.id

    # Inform the user that the translation is in progress
    bot.send_message(chat_id, "Translating your message, please wait...")

    # Start a new thread to handle the translation
    translation_thread = threading.Thread(target=process_translation, args=(chat_id, user_message))
    translation_thread.start()

def process_translation(chat_id, text):
    """
    Processes the translation by creating a task and polling for the result.

    :param chat_id: The chat ID to send messages back to the user.
    :param text: The text to be translated.
    """
    # Create the translation task
    task_id = create_translation_task(text)
    if not task_id:
        bot.send_message(chat_id, "Failed to create a translation task.")
        return

    # Poll the agent's API to check the status of the task
    translated_text = get_translation_result(task_id)
    if translated_text:
        # Send the translated text back to the user
        bot.send_message(chat_id, translated_text)
    else:
        bot.send_message(chat_id, "Failed to retrieve the translation.")

def create_translation_task(text):
    """
    Creates a translation task with the agent's API.

    :param text: The text to be translated.
    :return: The task ID if successful, None otherwise.
    """
    headers = {
        'Authorization': f'Bearer {AGENT_AUTH_TOKEN}',
        'Content-Type': 'application/json',
    }
    data = {
        'query': text
    }
    agent_url = f"{AGENT_API_URL}/{AGENT_DID}/tasks/"

    try:
        response = requests.post(agent_url, json=data, headers=headers)
        response.raise_for_status()
        task_info = response.json()
        task_id = task_info['task']['task_id']
        logging.info(f"Created task with ID: {task_id}")
        return task_id
    except Exception as e:
        logging.error(f"Error creating translation task: {e}")
        return None

def get_translation_result(task_id):
    """
    Polls the agent's API to get the translation result.

    :param task_id: The ID of the translation task.
    :return: The translated text if successful, None otherwise.
    """
    headers = {
        'Authorization': f'Bearer {AGENT_AUTH_TOKEN}',
    }
    task_status_url = f"{AGENT_API_URL}/{AGENT_DID}/tasks/{task_id}"

    # Polling parameters
    max_attempts = 10
    sleep_interval = 2  # seconds

    for _ in range(max_attempts):
        try:
            response = requests.get(task_status_url, headers=headers)
            response.raise_for_status()
            task_info = response.json()
            task_status = task_info['task']['task_status']
            logging.info(f"Task {task_id} status: {task_status}")

            if task_status == 'Completed':
                translated_text = task_info['task']['output']
                return translated_text.strip()
            elif task_status == 'Failed':
                logging.error(f"Task {task_id} failed.")
                return None
            else:
                # Task is still in progress; wait and retry
                time.sleep(sleep_interval)
        except Exception as e:
            logging.error(f"Error fetching task status: {e}")
            return None

    # If max attempts reached without completion
    logging.error(f"Task {task_id} did not complete within the expected time.")
    return None

if __name__ == '__main__':
    bot.infinity_polling()