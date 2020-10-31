#!/usr/bin/python
# -*- coding: utf-8 -*-

from difflib import SequenceMatcher as SM
import json
import re

path = 'pyBot_dict.json'
lvl = 0.7

print('\nБот запущен!')
print('--------------------------')
print('/q - завершить работу бота\n')


def speak():
    usrQuestion = input('> ')
    usrInput = usrQuestion.lower()
    if usrInput == '/q':
        return
    question = re.sub(r"[#%!@*.]", '', usrInput)
    with open(path, 'r', encoding='utf-8') as jfr:
        data = json.loads(jfr.read())
        qf = [i['q'] for i in data[0]]
        qx = sorted([SM(lambda x: x == ' ', question, i['q']).ratio()
                    for i in data[0]], reverse=True)
        if qx[0] < lvl:
            add(question)
        qt = sorted(qf, key=lambda x: SM(None, x, question).ratio(),
                    reverse=True)
        rs = qt[0]
        for i in data[0]:
            if i['q'] == rs:
                res = i['a']
    if 'res' in locals():
        print('@ ', res, '\n')
        speak()
    else:
        add(question)


def add(cq):
    print('\nБот не знает ответа. Напишите новый ответ!')
    newAnswer = input('Новый ответ > ')
    with open(path, 'r', encoding='utf-8') as jfr:
        jfr1 = json.load(jfr)
    with open(path, 'w', encoding='utf-8') as jfw:
        jfw1 = jfr1[0]
        entry = {'q': cq, 'a': newAnswer, 'x': 'none'}
        jfw1.append(entry)
        json.dump(jfr1, jfw, indent=2, ensure_ascii=False)
        print('В словарь добавлен новый ответ.\n')
    speak()

speak()

