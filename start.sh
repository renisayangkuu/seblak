#!/bin/bash

# Initialize database and seed menu if not exists
if [ ! -f "umkm_bot.db" ]; then
    echo "Database not found. Creating and seeding..."
    python -c "from bot import init_database; init_database()"
    python seed_menu.py
else
    echo "Database exists. Checking if menu is empty..."
    MENU_COUNT=$(python -c "import sqlite3; conn = sqlite3.connect('umkm_bot.db'); cur = conn.cursor(); cur.execute('SELECT COUNT(*) FROM menu'); print(cur.fetchone()[0]); conn.close()")
    if [ "$MENU_COUNT" -eq "0" ]; then
        echo "Menu is empty. Seeding..."
        python seed_menu.py
    fi
fi

# Start the bot
echo "Starting bot..."
python bot.py
