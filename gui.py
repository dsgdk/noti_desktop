# MIT License
# 
# Copyright (c) 2024 dsgdk
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIcon, QPixmap

class TelegramMonitor(QtWidgets.QWidget):
    new_message_signal = QtCore.pyqtSignal(str, str)  # Сигнал для оновлення повідомлень

    def __init__(self):
        super().__init__()
        self.initUI()
        self.new_message_signal.connect(self.update_textbox)  # Підключення сигналу до методу

        # Змінна для зберігання статусу відтворення звуку
        self.sound_playing = False

    def initUI(self):
        """Ініціалізація графічного інтерфейсу."""
        self.setWindowTitle('Telegram Monitor')
        self.setGeometry(100, 100, 400, 200)
        self.setStyleSheet("""
            background-color: #1e1e1e; 
            color: #ffffff; 
            font-family: 'Segoe UI', sans-serif;
            border-radius: 10px;
        """)

        # Налаштування текстового поля
        self.text_edit = QtWidgets.QTextEdit(self)
        self.text_edit.setStyleSheet("""
            background-color: #2b2b2b; 
            color: #ffffff; 
            border: none; 
            border-radius: 5px;
            padding: 10px;
            font-size: 14px;
        """)
        self.text_edit.setReadOnly(True)
        self.text_edit.setFixedHeight(100)  # Зменшення висоти текстового поля

        # Стиль кнопок
        button_style = """
            QPushButton {
                background-color: #FFFFFF;
                border: none;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #505050;
            }
            QPushButton:pressed {
                background-color: #6a6a6a;
            }
        """

        # Додання кнопки для зупинки звуку з вашою іконкою
        self.stop_button = QtWidgets.QPushButton(self)
        stop_icon = QIcon(QPixmap("icons/stop_white.png"))  # Ваша іконка
        self.stop_button.setIcon(stop_icon)
        self.stop_button.setIconSize(QtCore.QSize(24, 24))  # Розмір іконки
        self.stop_button.setFixedSize(30, 30)  # Зменшення розміру кнопки до розміру іконки
        self.stop_button.setStyleSheet(button_style)  # Застосування стилю
        self.stop_button.clicked.connect(self.stop_sound)  # Підключення кнопки до методу

        # Додання кнопки для очищення тексту з вашою іконкою
        self.clear_button = QtWidgets.QPushButton(self)
        clear_icon = QIcon(QPixmap("icons/clear_white.png"))  # Ваша іконка
        self.clear_button.setIcon(clear_icon)
        self.clear_button.setIconSize(QtCore.QSize(24, 24))  # Розмір іконки
        self.clear_button.setFixedSize(30, 30)  # Зменшення розміру кнопки до розміру іконки
        self.clear_button.setStyleSheet(button_style)  # Застосування стилю
        self.clear_button.clicked.connect(self.clear_text)  # Підключення кнопки до методу

        # Встановлення розташування кнопок по центру
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()  # Відступ зліва
        button_layout.addWidget(self.stop_button)
        button_layout.addWidget(self.clear_button)
        button_layout.addStretch()  # Відступ справа

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.text_edit)
        vbox.addLayout(button_layout)
        self.setLayout(vbox)

    def update_textbox(self, channel_name, message_text):
        """Оновлення текстового поля з новими повідомленнями."""
        self.text_edit.append(f"Канал: {channel_name}\nТекст повідомлення:\n{message_text}\n")
        self.play_sound()

    def play_sound(self):
        """Відтворення звукового сигналу."""
        if not self.sound_playing:
            self.sound_playing = True
            self.sound.play()

    def stop_sound(self):
        """Зупинка відтворення звукового сигналу."""
        if self.sound_playing:
            self.sound.stop()
            self.sound_playing = False

    def clear_text(self):
        """Очищення текстового поля."""
        self.text_edit.clear()
