# Aiogram 3 Template

This repository provides a template for quickly starting a Telegram bot using Aiogram 3 in Python, with PyCharm as the preferred IDE.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [PyCharm Setup](#pycharm-setup)
- [Commands](#commands)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Aiogram 3.x** – Built on the latest version of Aiogram for asynchronous Telegram bot development.
- **Modular Structure** – Organized project structure to manage modules easily.
- **PostgreSQL Integration** – Uses asyncpg for efficient asynchronous PostgreSQL database interactions.
- **Detailed Logging and Error Handling** – Comprehensive logging and error handling for better debugging and tracking.
- **Markdown V2 Support** – Sends Telegram messages with rich formatting using Markdown V2.

## Installation

### Clone the Repository
Open Terminal in PyCharm or any terminal on your system, and clone the repository:

```bash
git clone https://github.com/Karabaev1/aiogram3-template.git
cd aiogram3-template
```

### Create a Virtual Environment

#### In PyCharm:
1. Go to `File > Settings > Project > Python Interpreter`.
2. Click the gear icon > Add and select New environment to create a virtual environment.

#### Alternatively, you can create it via the terminal:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies
Once the virtual environment is activated, run the following to install dependencies:
```bash
pip install -r requirements.txt
```

### Set Up PostgreSQL Database
1. Install PostgreSQL if it's not already installed.
2. Create a database specifically for this bot.
3. Note the database URL, as it will be needed in the configuration step.

## Configuration

### Configure Environment Variables
Rename `.env.example` to `.env` and fill in your configuration values:
```dotenv
BOT_TOKEN=your_telegram_bot_token
DATABASE_URL=your_database_url
ADMINS=your_admin_telegram_id
```

Set `BOT_TOKEN` to your bot’s token, `DATABASE_URL` to the connection string for your PostgreSQL database, and `ADMINS` with the Telegram ID(s) of admins.

### Load Configuration in PyCharm
1. To ensure PyCharm recognizes the .env variables, install the Env File plugin.
2. Go to `Run > Edit Configurations...`.
3. Select Add new configuration > Python and add `app.py` as the script path.
4. Check `Enable EnvFile` and add the `.env` file path. This will load the environment variables automatically when running the script.

## Usage

### Run the Bot
In PyCharm, right-click `app.py` and choose `Run 'app'` or use the terminal:
```bash
python app.py
```

### Debugging
- Use PyCharm’s debugging tools, such as breakpoints and variable inspection, to debug.
- Logs are configured to help track errors and events in the console.

## Project Structure
Here’s a quick overview of the main directories and files:
```bash
.
├── app.py                  # Main entry point to run the bot
├── data/
│   ├── config.py           # Configuration file
│   └── db.py               # Database connection
├── handlers/
│   ├── __init__.py         # Imports all handlers
│   ├── users/              # User command handlers
│   └── admin/              # Admin command handlers
├── middlewares/            # Middlewares for handling requests
├── models/                 # Database models
├── services/               # Business logic and utility functions
├── .env.example            # Environment variables template file
└── README.md               # Project documentation
```

## PyCharm Setup

### Setting Up Code Style
1. Go to `File > Settings > Code Style > Python`.
2. Set up PEP8 or customize based on your project’s guidelines.

### Enable Virtual Environment in Terminal
1. Go to `File > Settings > Terminal`.
2. Set the Shell path to activate your virtual environment automatically.

### Using Git in PyCharm
1. Make sure Git is enabled in `File > Settings > Version Control > Git`.
2. Commit and push changes directly from PyCharm’s Git tab for streamlined workflow.

## Commands

### User Commands
- `/start` - Starts the bot and registers the user.
- `/help` - Shows help information and available commands.

### Admin Commands
- Notifications sent to admins for specific events like new user registration.

## Contributing
Contributions are welcome! Please fork the repository, create a new branch, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License.