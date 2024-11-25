[![banner](https://raw.githubusercontent.com/nevermined-io/assets/main/images/logo/banner_logo.png)](https://nevermined.io)

Telegram Translation Bot using Nevermined's Payments API
========================================================

> Python Telegram bot that translates text messages into Spanish by interacting with an AI agent via Nevermined's Payments API.

> [nevermined.io](https://nevermined.io)

* * *

Introduction
------------

The **Telegram Translation Bot** is a Python application that allows users to translate text messages into Spanish. The bot interacts with an AI agent through Nevermined's Payments API to perform the translations. Users need to purchase a subscription from Nevermined to use this bot.

* * *

Prerequisites
-------------

*   **Python 3.7** or higher
*   **Telegram Bot Token** (`TELEGRAM_TOKEN`)
*   **Nevermined Subscription**
*   **Nevermined Agent DID** (`AGENT_DID`)
*   **Nevermined JWT Token** (`AGENT_AUTH_TOKEN`)
*   **Git**

* * *

Installation
------------

1.  **Clone the repository**
    
    ```bash
    git clone https://github.com/nevermined-io/translation_telegram_bot.git
    cd telegram-translation-bot
    ```
    
2.  **Create a virtual environment**
    
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
    
3.  **Install the dependencies**
    
    ```bash
    pip install -r requirements.txt
    ```
    

* * *

Configuring Environment Variables
---------------------------------

Before running the bot, you need to configure several environment variables in the `.env` file.

1.  **Purchase a Nevermined Subscription**
    
    *   Visit the following URL to purchase a subscription:
        
        [Nevermined Translation Agent Subscription](https://testing.nevermined.app/en/plan/did:nv:0fdae7c5c6f76ef47b3fa8d20a5f151589c48e5ba52052392c7d6074c0d749bd)
        
    *   Follow the instructions to complete the purchase.
        
2.  **Obtain the Agent DID and JWT Token**
    
    *   After purchasing the subscription, navigate to the **"Translation Agent"** asset on Nevermined.
    *   Go to the **"Integration Details"** tab.
    *   Copy the **Agent DID** and **JWT Token** provided.
3.  **Set Up the `.env` File**
    
    Create a `.env` file in your project's root directory and add the following variables:
    
    ```env
    TELEGRAM_TOKEN=your_telegram_bot_token
    AGENT_API_URL=https://testing.nevermined.app/api/v1/agents
    AGENT_AUTH_TOKEN=your_nevermined_jwt_token
    AGENT_DID=your_agent_did
    ```
    
    Replace the placeholders with your actual tokens and DID:
    
    *   `your_telegram_bot_token`: The token provided by @BotFather when you created your Telegram bot.
    *   `your_nevermined_jwt_token`: The JWT token obtained from the "Integration Details" tab.
    *   `your_agent_did`: The Agent DID obtained from the "Integration Details" tab.
    
    **Note:** Ensure that your `.env` file is included in your `.gitignore` to prevent sensitive information from being committed to version control.
    

* * *

Running the Bot
---------------

Activate your virtual environment if not already activated:

```bash
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Run the bot:

```bash
python bot.py
```

Now, open Telegram and send a message to your bot. The bot will translate your message into Spanish and send it back to you.

* * *

License
-------

```
Copyright 2024 Nevermined

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
