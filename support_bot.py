#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🤖 ПРОМЕТЕЙ ПОДДЕРЖКА — Бот для пожертвований
Просто показывает ссылки. Без автоматизации.
🔐 Создано: БАТЕНЬКА
"""
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# ▼▼▼ ТОКЕН ОТ @BotFather ▼▼▼
TOKEN = "8775685520:AAEkuvkXhCEAFO48fR1sOPwK0q9BivjFQws"
# ▲▲▲ ▲▲▲ ▲▲▲

# ▼▼▼ ССЫЛКИ ЮMONEY ▼▼▼
LINK_BASIC = "https://yoomoney.ru/fundraise/1GGC4QUKOLT.260314"
LINK_PRO = "https://yoomoney.ru/fundraise/1GGC6I8DLLH.260314"
# ▲▲▲ ▲▲▲ ▲▲▲

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🤖 Базовый", url=LINK_BASIC)],
        [InlineKeyboardButton("🤖 Профи", url=LINK_PRO)],
    ]
    
    await update.message.reply_text(
        "🤖 Прометей: Базовый\n"
        "💙 Поддержать проект: 3 000 ₽\n"
        "📦 После благодарности вы получите:\n"
        "   • Агент для работы с базами данных\n"
        "   • Оптимизация, поиск, резервное копирование\n"
        "   • Инструкция на 1 странице\n"
        "🔐 Создано: БАТЕНЬКА\n\n"
        "🤖 Прометей: Профи\n"
        "💙 Поддержать проект: 5 000 ₽\n"
        "📦 После благодарности вы получите:\n"
        "   • Агент для 2+ баз данных\n"
        "   • Слияние, сравнение, экспорт\n"
        "   • Инструкция на 1 странице\n"
        "🔐 Создано: БАТЕНЬКА",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Это бот поддержки проекта Prometheus Lab.\n"
        "Нажмите /start чтобы увидеть продукты."
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
