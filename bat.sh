#!/bin/bash
# Переходим в папку проекта, чтобы относительные пути (например, к .env) работали
cd /home/vladimiregorov/PycharmProjects/Clock/

# Запускаем python напрямую из папки .venv
# Это автоматически подтянет все установленные в окружение библиотеки
/home/vladimiregorov/PycharmProjects/Clock/.venv/bin/python3 /home/vladimiregorov/PycharmProjects/Clock/main1_checkBox.py
