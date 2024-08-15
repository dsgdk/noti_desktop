# MIT License
# 
# Copyright (c) 2024 dsgdk
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

from telethon import TelegramClient, events
import asyncio
import configparser
import pygame
import os

# Завантаження конфігурації
config = configparser.ConfigParser()
config.read('config.ini')
api_id = config.get('telegram', 'api_id')
api_hash = config.get('telegram', 'api_hash')
channels = config.get('channels', 'channels').split(', ')
keywords = config.get('keywords', 'keywords').split(', ')
alert_sound_path = config.get('sounds', 'alert_sound')

client = TelegramClient('session_name', api_id, api_hash)

# Ініціалізація pygame для відтворення звуку
pygame.mixer.init()
alert_sound = pygame.mixer.Sound(alert_sound_path)

async def start_telegram_client(signal_emitter):
    """Запуск Telegram клієнта та обробка нових повідомлень."""
    await client.start()

    @client.on(events.NewMessage)
    async def handler(event):
        if event.chat.username in channels:
            if any(keyword.lower() in event.raw_text.lower() for keyword in keywords):
                channel_name = event.chat.title or event.chat.username
                message_text = event.raw_text
                print(f"Message found: {channel_name}, {message_text}")  # Діагностичний вивід
                
                # Відтворення звукового сигналу
                signal_emitter.new_message_signal.emit(channel_name, message_text)

    await client.run_until_disconnected()
