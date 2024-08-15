# MIT License
# 
# Copyright (c) 2024 dsgdk
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

import sys
from PyQt5 import QtWidgets, QtCore
from gui import TelegramMonitor
from telegram_client import start_telegram_client, alert_sound

class TelegramThread(QtCore.QThread):
    def __init__(self, signal_emitter):
        super().__init__()
        self.signal_emitter = signal_emitter

    def run(self):
        """Запуск асинхронного клієнта Telegram у фоновому потоці."""
        import asyncio
        asyncio.run(start_telegram_client(self.signal_emitter))

def main():
    app = QtWidgets.QApplication(sys.argv)
    monitor = TelegramMonitor()
    monitor.sound = alert_sound  # Передача звукового об'єкта у GUI
    monitor.show()

    # Запуск клієнта Telegram у фоновому потоці
    telegram_thread = TelegramThread(monitor)
    telegram_thread.start()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
