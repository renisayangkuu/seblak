#!/bin/bash

# Check if database exists
if [ ! -f "umkm_bot.db" ]; then
    echo "Database not found. Creating and seeding..."
    python seed_menu.py
fi

# Start the bot
python bot.py
