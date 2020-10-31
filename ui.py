#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from telebot import types
from config import site_url

class keyboards:

    welcome_kbd = types.ReplyKeyboardMarkup(resize_keyboard="True")
    support_btn = types.KeyboardButton('Поддержка')

    welcome_kbd.row(support_btn)

    website_kbd = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на сайт", url=site_url)
    website_kbd.add(url_button)
