#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import os
from flask import Flask, request
import telebot
import re
import ui
import json
import re
from difflib import SequenceMatcher as SM
from config import main_cfg

kb = ui.keyboards
bot = telebot.TeleBot(main_cfg.apiToken)
server = Flask(__name__)


def reply_to(message, reply, kdb_type):
    if kdb_type != 'none' and kdb_type != 'address':
        bot.send_message(
            message.chat.id,
            reply,
            reply_markup=getattr(kb, kdb_type)
            )
    elif kdb_type == 'address':
        bot.send_message(message.chat.id, reply)
    else:
        bot.send_message(message.chat.id, reply)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_photo(
        message.chat.id,
        main_cfg.welcome_pic,
        "Приветствую, "+message.from_user.first_name+'! Я обучающийся бот!',
        reply_markup=kb.welcome_kbd
        )


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    ui = message.text.lower()
    q = re.sub(r"[#%!@*.]", '', ui)
    with open(main_cfg.path, 'r', encoding='utf-8') as jfr:
        data = json.loads(jfr.read())
        qf = [i['q'] for i in data[0]]
        qx = sorted(
            [SM(lambda x: x == ' ', q, i['q']).ratio() for i in data[0]],
            reverse=True
            )
        if qx[0] < main_cfg.lvl:
            reply_to(message, '...', 'none')
            return
        qt = sorted(qf, key=lambda x: SM(None, x, q).ratio(), reverse=True)
        rs = qt[0]
        for i in data[0]:
            if i['q'] == rs:
                res = i['a']
                kdb_type = i['x']
        if 'res' in locals():
            reply_to(message, res, kdb_type)
            return


@server.route('/' + main_cfg.apiToken, methods=['POST'])
def getMessage():
    bot.process_new_updates(
        [telebot.types.Update.de_json(request.stream.read().decode("utf-8"))]
        )
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=main_cfg.heroku_link + main_cfg.apiToken)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
