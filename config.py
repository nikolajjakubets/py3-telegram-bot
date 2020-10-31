#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

site_url=os.environ.get("WEBSITE_URL")

class main_cfg:
    apiToken = os.environ.get("BOT_API_TOKEN")
    welcome_pic=os.environ.get("BOT_WELCOME_PIC")
    heroku_link=os.environ.get("HEROKU_APP_URL")
    path = 'pyBot_dict.json'
    lvl = 0.7
