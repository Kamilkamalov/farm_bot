from os import link
from pickle import NONE
from tkinter.tix import TEXT
from xml.dom.minidom import Element

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiohttp import Payload
import keyboards as nav
from random import randint
import logging

import sqlite3

import asyncio # асинхронка для поздних логов

from config import TOKEN

# рефералка
from aiogram.utils.deep_linking import get_start_link, decode_payload
from aiogram import types

# счетчик
from collections import Counter

import time

# для шрифта
from aiogram import types
from aiogram.utils.markdown import link

import os.path # пытаюсь указать абсолютный путь до базы данных с пользователями



# Пишу для логирования в терминале, чтобы понять где мои ебаные ошибки
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


#base = sqlite3.connect('data.db') # создание подключения
#cur = conn.cursor('') # cur для взаимодействия с бд
#cur.execute('CREATE TABLE users(user_id INTEGER, username TEXT)') # добавил строку
def sql_start():
    global base, cur
    base = sqlite3.connect('data.db')
    cur = base.cursor()
    if base:
        print('База данных существует или успешно создана')
        # Эти альтеры не дают юзать бд на vds
        # cur.execute("alter table users add column 'Last_Name' 'TEXT INTEGER'") # + колонка для фикса бага
        # cur.execute("alter table users add column 'Last_Link' 'TEXT INTEGER'") # + колонка для фикса бага
        # cur.execute("alter table users add column 'Last_Active' 'TEXT INTEGER'") # + колонка для фикса бага
        # cur.execute("alter table users add column 'Last_ATH' 'TEXT INTEGER'") # + колонка для фикса бага
        # cur.execute("alter table users add column 'Last_Farm_group' 'TEXT INTEGER'") # + колонка для фикса бага
        # cur.execute("alter table users add column 'Last_Sostav' 'TEXT INTEGER'") # + колонка для фикса бага
        # cur.execute("alter table users add column 'Last_Description' 'TEXT INTEGER'") # + колонка для фикса бага
        # cur.execute("alter table users add column 'Last_Farm_deystv' 'TEXT INTEGER'") # + колонка для фикса бага
        # cur.execute("alter table users add column 'Last_Farmakodinamika' 'TEXT INTEGER'") # + колонка для фикса бага
        # cur.execute("alter table users add column 'Last_Farmakokinetika' 'TEXT INTEGER'") # + колонка для фикса бага
        # cur.execute("alter table users add column 'Last_Pokazaniya' 'TEXT INTEGER'") # + колонка для фикса бага
        # cur.execute("alter table users add column 'Last_Protiv' 'TEXT INTEGER'") # + колонка для фикса бага
        # cur.execute("alter table users add column 'Last_lact' 'TEXT INTEGER'") # + колонка для фикса бага
        # cur.execute("alter table users add column 'Last_Bad' 'TEXT INTEGER'") # + колонка для фикса бага
        # cur.execute("alter table users add column 'Last_Interaction' 'TEXT INTEGER'") # + колонка для фикса бага
        # cur.execute("alter table users add column 'Last_Sposob' 'TEXT INTEGER'") # + колонка для фикса бага
        # cur.execute("alter table users add column 'Last_Peredoz' 'TEXT INTEGER'") # + колонка для фикса бага
        # cur.execute("alter table users add column 'Last_Osob_ukaz' 'TEXT INTEGER'") # + колонка для фикса бага
        # cur.execute("alter table users add column 'Last_Forma_vipuska' 'TEXT INTEGER'") # + колонка для фикса бага
        # cur.execute("alter table users add column 'Last_Proizvoditel' 'TEXT INTEGER'") # + колонка для фикса бага
        # cur.execute("alter table users add column 'Last_Recept' 'TEXT INTEGER'") # + колонка для фикса бага
        # cur.execute("alter table users add column 'Last_Save' 'TEXT INTEGER'") # + колонка для фикса бага
        # cur.execute("alter table users add column 'Last_Srok' 'TEXT INTEGER'") # + колонка для фикса бага

    else:
        print('База данных не существует')
    base.execute('CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY NOT NULL, link, ref_manager, referals, name, Last_Name, Last_Active, Last_ATH, Last_Farm_group, Last_Sostav, Last_Description, Last_Farm_deystv, Last_Farmakodinamika, Last_Farmakokinetika, Last_Pokazaniya, Last_Protiv, Last_lact, Last_Bad, Last_Interaction, Last_Sposob, Last_Peredoz, Last_Osob_ukaz, Last_Forma_vipuska, Last_Proizvoditel, Last_Recept, Last_Save, Last_Srok, Last_Link, Counter)')
    base.commit()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "data.db")
with sqlite3.connect(db_path) as db:
    sql_start() # запускаем функцию с БД

def farmdata_start():
    global base_farm, cur_farm
    base_farm = sqlite3.connect('farmdata.db')
    cur_farm = base_farm.cursor()
    if base_farm:
        print('База данных препаратов существует')
        #cur_farm.execute("alter table lekarstva add column 'Sposob' 'TEXT INTEGER'") # + колонка Способ
    else:
        print('База данных препаратов либо не существует, либо к ней невозможно подключиться')
    base_farm.execute('CREATE TABLE IF NOT EXISTS lekarstva(Remedy_id INTEGER PRIMARY KEY NOT NULL, Name_lp TEXT INTEGER, Active TEXT INTEGER, ATH TEXT INTEGER, Farm_group TEXT INTEGER, Sostav TEXT INTEGER, Description TEXT INTEGER, Farm_deystv TEXT INTEGER, Farmakodinamika TEXT INTEGER, Farmakokinetika TEXT INTEGER, Pokazaniya TEXT INTEGER, Protiv TEXT INTEGER, Pregnancy_lact TEXT INTEGER, Bad_effects TEXT INTEGER, Interaction TEXT INTEGER, Peredoz TEXT INTEGER, Osob_ukaz TEXT INTEGER, Forma_vipuska TEXT INTEGER, Proizvoditel TEXT INTEGER, Recept TEXT INTEGER, Save TEXT INTEGER, Srok TEXT INTEGER, Link TEXT INTEGER )')
    base_farm.commit()
farmdata_start() # запускам функцию с бд препаратов

# Для обновления строки в lower
# cur_farm.execute('SELECT Name_lp FROM "lekarstva"')
# Name_tuple = cur_farm.fetchall()
# for Name_lp in Name_tuple:
#     Name_lp, = Name_lp
#     Element_Name_lp = Name_lp.lower()
#     cur_farm.execute('UPDATE "lekarstva" SET Name_lp = ? WHERE Name_lp = ?', (Element_Name_lp, Name_lp)) # bars @headovich thx
#     #cur_farm.execute('UPDATE "lekarstva" SET Name_lp = ?', (Element_Name_lp, ))
#     print(Element_Name_lp)
#     base_farm.commit()

# добавляю юзера в бд при /start
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    
    ref_link = await get_start_link(str(message.from_user.id), encode=True) # создаю ссылку
    args = message.get_args() # тут содержится зашифрованный id, который является частью реферальной ссылки
    reference = decode_payload(args) # расшифровка id
    print(ref_link)
    print(args)
    print(len(args))

    await message.reply('{user}'.format(user=message.from_user.full_name) + ", добро пожаловать!\n💊Здесь вы можете быстро найти информацию о лекарствах\nВведите название лекарства и отправьте боту✅\n", reply_markup = nav.mainMenu)
    try:
        base = sqlite3.connect('data.db')
        cur = base.cursor()
        # НЕВЕРНЫЙ СИНТАКСИС НЕТ ВОПРОСОВ sql cur.execute(f'INSERT INTO "users" (user_id, link) VALUES ("{message.from_user.id}", "{ref_link}")')
        cur.execute('INSERT INTO "users" (user_id, link, name) VALUES (?, ?, ?)', (message.from_user.id, ref_link, message.from_user.full_name))
        
        base.commit()
    except Exception as e1:
        print(e1)
        base = sqlite3.connect('data.db')
        cur = base.cursor()
        cur.execute('INSERT INTO "users" (user_id, link) VALUES(?, ?, ?)', (message.from_user.id, ref_link, message.from_user.full_name))
        # добавил name 
        base.commit()    
    finally:
        # Проверка на наличие записи в ref_manager
        # НЕВЕРНЫЙ СИНТАКСИС НЕТ ВОПРОСОВ cur.execute(f'SELECT ref_manager FROM "users" WHERE user_id = "{message.from_user.id}"') # выбираю ref_manager и сравниваю значение с NULL
        cur.execute('SELECT ref_manager FROM "users" WHERE user_id = ?', (message.from_user.id,))  # выбираю ref_manager и сравниваю значение с NULL
        base.commit()
        is_ref_manager = cur.fetchone() # вытаскиваю реф мэнэджэра в виде листа
        clean_ref_manager = is_ref_manager[0] # беру первый элемент списка
        print(clean_ref_manager, " реф менеджер")
    # СЧЕТЧИК
    #    i = 0
        if len(args) > 0: # Если длина payload у /start больше 0, то есть существует
            cur.execute('SELECT ref_manager FROM "users" WHERE ref_manager')
            base.commit()
            is_all_ref_managers = cur.fetchall() # вытаскиваю всех реф менеджеров в виде tuple
            Counter_all_ref_managers = Counter(is_all_ref_managers) # получаю словарь с ключами
            
            #print(Counter_all_ref_managers) # смотрю словарь, полученный выше
            #How_ref_managers = len(Counter_all_ref_managers) # считаю сколько реферальных менеджеров в словаре
            #print(How_ref_managers, " Сколько реферальных менеджеров в словаре") # смотрю сколько реферальных менеджеров в словаре
            #Last_index = How_ref_managers - 1
            #print(Last_index, " Последний индекс словаря")
            # расшифровка словаря по ключ:значение
            
            # ИЗВЛЕК с помощью запятой ебаный кортеж!
            for key, value in Counter_all_ref_managers.items():
                key, = key
                print(key,':',value) # если использовать * перед key, то кортеж распаковывается
                # НЕВЕРНЫЙ СИНТАКСИС cur.execute(f'UPDATE "users" SET referals = "{value}" WHERE user_id = "{key}"')
                cur.execute('UPDATE "users" SET referals = ? WHERE user_id = ?', (value, key))
                base.commit()
 
        if clean_ref_manager == None:
            # НЕВЕРНЫЙ СИНТАКСИС cur.execute(f'UPDATE "users" SET ref_manager = "{reference}" WHERE user_id = "{message.from_user.id}"') # указываю кто пригласил 
            cur.execute('UPDATE "users" SET ref_manager = ? WHERE user_id = ?', (reference, message.from_user.id)) # указываю кто пригласил
            base.commit()
        else:
            print("Пользователь был приглашен другим реф менеджером или у /start нет параметра payload(нет реф менеджера)")


# работа кнопок у юзеров

@dp.message_handler()
async def bot_message(message: types.Message):
    
    if message.text == '❓Как пользоваться':
        await message.reply("Инструкция:\n1) Видите кнопки? Нажмите на кнопку '🎯Найти лекарство'\n2) Введите название искомого лекарства\n3) Нажмите на появившиеся кнопки в чате\n❌Не получается? Нажмите /start и повторите \n\nОбязательно вводите препарат правильно, иначе будет ошибка.\n\nМожете вводить название капсом или маленькими буквами\n\nПоиск по активному веществу пока что не работает\n\nПосле открытия ссылки листните немного выше или ниже")
    if message.text == '👍🏻Поддержка':
        await message.reply("👤Нашли баг или ошибку? Напишите мне: \n@creppoq \n👤Менеджер по связям с общественностью, провизор-технолог: \n@Son511777")
    if message.text == '🎯Найти лекарство':
        await message.reply('⚙️Введите название лекарственного препарата, которое хотите найти')
    if message.text != '❓Как пользоваться' and message.text != '👍🏻Поддержка' and message.text != '🎯Найти лекарство':
        await message.reply(f"💊Информация по запросу:", reply_markup=nav.inline_btn_ez_info)
#        await bot.send_message(message.chat.id, '---------------------------')
        await message.reply(f"🤓Информация по запросу для специалистов:", reply_markup=nav.inline_btn_hard_info)

# запрос на лекарства в бд
        message.text = message.text.lower()
        Name_for_user = message.text # фикс бага
        cur.execute('UPDATE "users" SET Last_Name = ? WHERE user_id = ?', (Name_for_user, message.from_user.id)) # фикс бага
        base.commit() # решает 

        cur_farm.execute('SELECT Name_lp FROM "lekarstva" WHERE Name_lp LIKE ?', (Name_for_user,)) #  Баг с отказом
        Name_lp = cur_farm.fetchone()
        Warn_msg = "ВНИМАНИЕ❗️❗️❗️ \nВы допустили орфографическую ошибку или препарата нет в базе.\nИНФОРМАЦИЯ В КНОПКАХ ВЫШЕ НЕ ОБНОВИЛАСЬ❗️\nПопробуйте еще раз..."
        if Name_lp is None: # извлек получается пустоту не распакованную?
            await message.reply(f'ВНИМАНИЕ❗️❗️❗️ \nВы допустили орфографическую ошибку или препарата нет в базе.\nИНФОРМАЦИЯ В КНОПКАХ ВЫШЕ НЕ ОБНОВИЛАСЬ❗️\nПопробуйте еще раз...')
            cur.execute('UPDATE "users" SET Last_Name = ? WHERE user_id = ?', (Warn_msg, message.from_user.id))
        base.commit() # решает

        cur_farm.execute('SELECT Active FROM "lekarstva" WHERE Name_lp LIKE ?', (Name_for_user,))
        Active, = cur_farm.fetchone()
        Active_for_user = Active #  фикс бага
        cur.execute('UPDATE "users" SET Last_Active = ? WHERE user_id = ?', (Active_for_user, message.from_user.id))

# Счетчик при вводе слова руками
        cur.execute('SELECT Counter FROM "users" WHERE user_id = ?', (message.from_user.id,))
        Counter, = cur.fetchone() # извлекаю кол-во нажатий?
        Counter_for_user = Counter
        if Counter_for_user is None: # если новый пользователь
            Counter_for_user = 0
            cur.execute('UPDATE "users" SET Counter = ? WHERE user_id = ?', (Counter_for_user, message.from_user.id)) # кладу нолик
        else: 
            Counter_for_user += 1 
            cur.execute('UPDATE "users" SET Counter = ? WHERE user_id = ?', (Counter_for_user, message.from_user.id))


        cur_farm.execute('SELECT ATH FROM "lekarstva" WHERE Name_lp LIKE ?', (Name_for_user,))
        ATH, = cur_farm.fetchone()
        ATH_for_user = ATH #  фикс бага
        cur.execute('UPDATE "users" SET Last_ATH = ? WHERE user_id = ?', (ATH_for_user, message.from_user.id)) # фикс бага

        cur_farm.execute('SELECT Farm_group FROM "lekarstva" WHERE Name_lp LIKE ?', (Name_for_user,))
        Farm_group, = cur_farm.fetchone()
        Farm_group_for_user = Farm_group #  фикс бага
        cur.execute('UPDATE "users" SET Last_Farm_group = ? WHERE user_id = ?', (Farm_group_for_user, message.from_user.id)) # фикс бага

        cur_farm.execute('SELECT Sostav FROM "lekarstva" WHERE Name_lp LIKE ?', (Name_for_user,))
        Sostav, = cur_farm.fetchone()
        Sostav_for_user = Sostav #  фикс бага
        cur.execute('UPDATE "users" SET Last_Sostav = ? WHERE user_id = ?', (Sostav_for_user, message.from_user.id)) # фикс бага

        cur_farm.execute('SELECT Description FROM "lekarstva" WHERE Name_lp LIKE ?', (Name_for_user,))
        Description, = cur_farm.fetchone()
        Description_for_user = Description #  фикс бага
        cur.execute('UPDATE "users" SET Last_Description = ? WHERE user_id = ?', (Description_for_user, message.from_user.id)) # фикс бага

        cur_farm.execute('SELECT Farm_deystv FROM "lekarstva" WHERE Name_lp LIKE ?', (Name_for_user,))
        Farm_deystv, = cur_farm.fetchone()
        Farm_deystv_for_user = Farm_deystv #  фикс бага
        cur.execute('UPDATE "users" SET Last_Farm_deystv = ? WHERE user_id = ?', (Farm_deystv_for_user, message.from_user.id)) # фикс бага

        cur_farm.execute('SELECT Farmakodinamika FROM "lekarstva" WHERE Name_lp LIKE ?', (Name_for_user,))
        Farmakodinamika, = cur_farm.fetchone()
        Farmakodinamika_for_user = Farmakodinamika #  фикс бага
        cur.execute('UPDATE "users" SET Last_Farmakodinamika = ? WHERE user_id = ?', (Farmakodinamika_for_user, message.from_user.id)) # фикс бага
        
        cur_farm.execute('SELECT Farmakokinetika FROM "lekarstva" WHERE Name_lp LIKE ?', (Name_for_user,))
        Farmakokinetika, = cur_farm.fetchone()
        Farmakokinetika_for_user = Farmakokinetika #  фикс бага
        cur.execute('UPDATE "users" SET Last_Farmakokinetika = ? WHERE user_id = ?', (Farmakokinetika_for_user, message.from_user.id)) # фикс бага

        cur_farm.execute('SELECT Pokazaniya FROM "lekarstva" WHERE Name_lp LIKE ?', (Name_for_user,))
        Pokazaniya, = cur_farm.fetchone()
        Pokazaniya_for_user = Pokazaniya #  фикс бага
        cur.execute('UPDATE "users" SET Last_Pokazaniya = ? WHERE user_id = ?', (Pokazaniya_for_user, message.from_user.id)) # фикс бага

        cur_farm.execute('SELECT Protiv FROM "lekarstva" WHERE Name_lp LIKE ?', (Name_for_user,))
        Protiv, = cur_farm.fetchone()
        Protiv_for_user = Protiv #  фикс бага
        cur.execute('UPDATE "users" SET Last_Protiv = ? WHERE user_id = ?', (Protiv_for_user, message.from_user.id)) # фикс бага

        cur_farm.execute('SELECT Pregnancy_lact FROM "lekarstva" WHERE Name_lp LIKE ?', (Name_for_user,))
        Pregnancy_lact, = cur_farm.fetchone()
        Pregnancy_lact_for_user = Pregnancy_lact #  фикс бага
        cur.execute('UPDATE "users" SET Last_lact = ? WHERE user_id = ?', (Pregnancy_lact_for_user, message.from_user.id)) # фикс бага

        cur_farm.execute('SELECT Bad_effects FROM "lekarstva" WHERE Name_lp LIKE ?', (Name_for_user,))
        Bad_effects, = cur_farm.fetchone()
        Bad_effects_for_user = Bad_effects #  фикс бага
        cur.execute('UPDATE "users" SET Last_Bad = ? WHERE user_id = ?', (Bad_effects_for_user, message.from_user.id)) # фикс бага

        cur_farm.execute('SELECT Interaction FROM "lekarstva" WHERE Name_lp LIKE ?', (Name_for_user,))
        Interaction, = cur_farm.fetchone()
        Interaction_for_user = Interaction #  фикс бага
        cur.execute('UPDATE "users" SET Last_Interaction = ? WHERE user_id = ?', (Interaction_for_user, message.from_user.id)) # фикс бага

        cur_farm.execute('SELECT Sposob FROM "lekarstva" WHERE Name_lp LIKE ?', (Name_for_user,))
        Sposob, = cur_farm.fetchone()
        Sposob_for_user = Sposob #  фикс бага
        cur.execute('UPDATE "users" SET Last_Sposob = ? WHERE user_id = ?', (Sposob_for_user, message.from_user.id)) # фикс бага

        cur_farm.execute('SELECT Peredoz FROM "lekarstva" WHERE Name_lp LIKE ?', (Name_for_user,))
        Peredoz, = cur_farm.fetchone()
        Peredoz_for_user = Peredoz #  фикс бага
        cur.execute('UPDATE "users" SET Last_Peredoz = ? WHERE user_id = ?', (Peredoz_for_user, message.from_user.id)) # фикс бага

        cur_farm.execute('SELECT Osob_ukaz FROM "lekarstva" WHERE Name_lp LIKE ?', (Name_for_user,))
        Osob_ukaz, = cur_farm.fetchone()
        Osob_ukaz_for_user = Osob_ukaz #  фикс бага
        cur.execute('UPDATE "users" SET Last_Osob_ukaz = ? WHERE user_id = ?', (Osob_ukaz_for_user, message.from_user.id)) # фикс бага

        cur_farm.execute('SELECT Forma_vipuska FROM "lekarstva" WHERE Name_lp LIKE ?', (Name_for_user,))
        Forma_vipuska, = cur_farm.fetchone()
        Forma_vipuska_for_user = Forma_vipuska #  фикс бага
        cur.execute('UPDATE "users" SET Last_Forma_vipuska = ? WHERE user_id = ?', (Forma_vipuska_for_user, message.from_user.id)) # фикс бага
        
        cur_farm.execute('SELECT Proizvoditel FROM "lekarstva" WHERE Name_lp LIKE ?', (Name_for_user,))
        Proizvoditel, = cur_farm.fetchone()
        Proizvoditel_for_user = Proizvoditel #  фикс бага
        cur.execute('UPDATE "users" SET Last_Proizvoditel = ? WHERE user_id = ?', (Proizvoditel_for_user, message.from_user.id)) # фикс бага

        cur_farm.execute('SELECT Recept FROM "lekarstva" WHERE Name_lp LIKE ?', (Name_for_user,))
        Recept, = cur_farm.fetchone()
        Recept_for_user = Recept #  фикс бага
        cur.execute('UPDATE "users" SET Last_Recept = ? WHERE user_id = ?', (Recept_for_user, message.from_user.id)) # фикс бага

        cur_farm.execute('SELECT Save FROM "lekarstva" WHERE Name_lp LIKE ?', (Name_for_user,))
        Save, = cur_farm.fetchone()
        Save_for_user = Save #  фикс бага
        cur.execute('UPDATE "users" SET Last_Save = ? WHERE user_id = ?', (Save_for_user, message.from_user.id)) # фикс бага

        cur_farm.execute('SELECT Srok FROM "lekarstva" WHERE Name_lp LIKE ?', (Name_for_user,))
        Srok, = cur_farm.fetchone()
        Srok_for_user = Srok #  фикс бага
        cur.execute('UPDATE "users" SET Last_Srok = ? WHERE user_id = ?', (Srok_for_user, message.from_user.id)) # фикс бага

        cur_farm.execute('SELECT Link FROM "lekarstva" WHERE Name_lp LIKE ?', (Name_for_user,))
        Link, = cur_farm.fetchone()
        Link = Link.strip() # пришлось обрезать пробелы, потому что пробел мешает образованию ссылки
        Link_for_user = Link #  фикс бага
        cur.execute('UPDATE "users" SET Last_Link = ? WHERE user_id = ?', (Link_for_user, message.from_user.id)) # фикс бага

        base.commit() # решает 


# РАБОТА ИНЛАЙН КНОПОК ПРО ЛЕКАРСТВА
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('button'))
async def process_callback_button1(callback_query: types.CallbackQuery):
    code = callback_query.data
    # получаю Last_Link
    cur.execute('SELECT Last_Link FROM "users" WHERE user_id LIKE ?', (callback_query.from_user.id,)) # раньше параметр был message.text. Чел лучший!
    Last_Link, = cur.fetchone() # БАГИ 
     # фикшу баг
    if code == 'button1':
        await bot.answer_callback_query(callback_query.id)
        cur.execute('SELECT Last_Name FROM "users" WHERE user_id LIKE ?', (callback_query.from_user.id,)) # раньше параметр был message.text. Чел лучший!
        Last_Name, = cur.fetchone() # БАГИ 
        await bot.send_message(callback_query.from_user.id, f'{Last_Name}  \n', parse_mode = "HTML")


# пораньше всунул ссылки, чтобы использовать переменную без глобала
    elif code == 'button22':
        await bot.answer_callback_query(callback_query.id)
        cur.execute('SELECT Last_Link FROM "users" WHERE user_id LIKE ?', (callback_query.from_user.id,)) # раньше параметр был message.text. Чел лучший!
        Last_Link, = cur.fetchone() # БАГИ 
        await bot.send_message(callback_query.from_user.id, f'<a href="{Last_Link}">Ссылка на лекарство в rlsnet</a>  \n', disable_web_page_preview=True, parse_mode = "HTML")

    elif code == 'button2':
        await bot.answer_callback_query(callback_query.id)
        cur.execute('SELECT Last_Active FROM "users" WHERE user_id LIKE ?', (callback_query.from_user.id,)) # раньше параметр был message.text. Чел лучший!
        Last_Active, = cur.fetchone() # БАГИ 
        await bot.send_message(callback_query.from_user.id, f'{Last_Active}   \n', parse_mode = "HTML")

    elif code == 'button3':
        await bot.answer_callback_query(callback_query.id)
        cur.execute('SELECT Last_ATH FROM "users" WHERE user_id LIKE ?', (callback_query.from_user.id,)) # раньше параметр был message.text. Чел лучший!
        Last_ATH, = cur.fetchone() # БАГИ 
        if Last_ATH != "Нет информации":
            await bot.send_message(callback_query.from_user.id, f'<a href="{Last_Link}{Last_ATH}">ATH</a>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        else:
            await bot.send_message(callback_query.from_user.id, f'<b>{Last_ATH}</b>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        
    elif code == 'button4':
        await bot.answer_callback_query(callback_query.id)
        cur.execute('SELECT Last_Farm_group FROM "users" WHERE user_id LIKE ?', (callback_query.from_user.id,)) # раньше параметр был message.text. Чел лучший!
        Last_Farm_group, = cur.fetchone() # БАГИ 
        if Last_Farm_group != "Нет информации":
            await bot.send_message(callback_query.from_user.id, f'<a href="{Last_Link}{Last_Farm_group}">Фармакологическая группа</a>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        else:
            await bot.send_message(callback_query.from_user.id, f'<b>{Last_Farm_group}</b>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        
    elif code == 'button5':
        await bot.answer_callback_query(callback_query.id)
        cur.execute('SELECT Last_Sostav FROM "users" WHERE user_id LIKE ?', (callback_query.from_user.id,)) # раньше параметр был message.text. Чел лучший!
        Last_Sostav, = cur.fetchone() # БАГИ 
        if Last_Sostav != "Нет информации": # тут еще уточнить
            await bot.send_message(callback_query.from_user.id, f'<a href="{Last_Link}{Last_Sostav}">Состав</a>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        else:
            await bot.send_message(callback_query.from_user.id, f'<a href="{Last_Link}#sostav">Состав</a>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        
    elif code == 'button6':
        await bot.answer_callback_query(callback_query.id)
        cur.execute('SELECT Last_Description FROM "users" WHERE user_id LIKE ?', (callback_query.from_user.id,)) # раньше параметр был message.text. Чел лучший!
        Last_Description, = cur.fetchone() # БАГИ 
        if Last_Description != "Нет информации":
            await bot.send_message(callback_query.from_user.id, f'<a href="{Last_Link}{Last_Description}">Описание лекарственной формы</a>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        else:
            await bot.send_message(callback_query.from_user.id, f'<b>{Last_Description}</b>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        
    elif code == 'button7':
        await bot.answer_callback_query(callback_query.id)
        cur.execute('SELECT Last_Farm_deystv FROM "users" WHERE user_id LIKE ?', (callback_query.from_user.id,)) # раньше параметр был message.text. Чел лучший!
        Last_Farm_deystv, = cur.fetchone() # БАГИ 
        if Last_Farm_deystv != "Нет информации":
            await bot.send_message(callback_query.from_user.id, f'<a href="{Last_Link}{Last_Farm_deystv}">Фармакологическое действие</a>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        else:
            await bot.send_message(callback_query.from_user.id, f'<b>{Last_Farm_deystv}</b>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        
    elif code == 'button8':
        await bot.answer_callback_query(callback_query.id)
        cur.execute('SELECT Last_Farmakodinamika FROM "users" WHERE user_id LIKE ?', (callback_query.from_user.id,)) # раньше параметр был message.text. Чел лучший!
        Last_Farmakodinamika, = cur.fetchone() # БАГИ 
        if Last_Farmakodinamika != "Нет информации":
            await bot.send_message(callback_query.from_user.id, f'<a href="{Last_Link}{Last_Farmakodinamika}">Фармакодинамика</a>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        else:
            await bot.send_message(callback_query.from_user.id, f'<b>{Last_Farmakodinamika}</b>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        
    elif code == 'button9':
        await bot.answer_callback_query(callback_query.id)
        cur.execute('SELECT Last_Farmakokinetika FROM "users" WHERE user_id LIKE ?', (callback_query.from_user.id,)) # раньше параметр был message.text. Чел лучший!
        Last_Farmakokinetika, = cur.fetchone() # БАГИ 
        if Last_Farmakokinetika != "Нет информации":
            await bot.send_message(callback_query.from_user.id, f'<a href="{Last_Link}{Last_Farmakokinetika}">Фармакокинетика</a>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        else:
            await bot.send_message(callback_query.from_user.id, f'<b>{Last_Farmakokinetika}</b>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        
    elif code == 'button10':
        await bot.answer_callback_query(callback_query.id)
        cur.execute('SELECT Last_Pokazaniya FROM "users" WHERE user_id LIKE ?', (callback_query.from_user.id,)) # раньше параметр был message.text. Чел лучший!
        Last_Pokazaniya, = cur.fetchone() # БАГИ 
        if Last_Pokazaniya != "Нет информации":
            await bot.send_message(callback_query.from_user.id, f'<a href="{Last_Link}{Last_Pokazaniya}">Показания</a>  \n', disable_web_page_preview=True, parse_mode = "HTML") 
        else:
            await bot.send_message(callback_query.from_user.id, f'<b>{Last_Pokazaniya}</b>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        
    elif code == 'button11':
        await bot.answer_callback_query(callback_query.id)
        cur.execute('SELECT Last_Protiv FROM "users" WHERE user_id LIKE ?', (callback_query.from_user.id,)) # раньше параметр был message.text. Чел лучший!
        Last_Protiv, = cur.fetchone() # БАГИ 
        if Last_Protiv != "Нет информации":
            await bot.send_message(callback_query.from_user.id, f'<a href="{Last_Link}{Last_Protiv}">Противопоказания</a>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        else:
            await bot.send_message(callback_query.from_user.id, f'<b>{Last_Protiv}</b>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        
    elif code == 'button12':
        await bot.answer_callback_query(callback_query.id)
        cur.execute('SELECT Last_lact FROM "users" WHERE user_id LIKE ?', (callback_query.from_user.id,)) # раньше параметр был message.text. Чел лучший!
        Last_lact, = cur.fetchone() # БАГИ 
        if Last_lact != "Нет информации":
            await bot.send_message(callback_query.from_user.id, f'<a href="{Last_Link}{Last_lact}">Применение при беременности и кормлении грудью</a>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        else:
            await bot.send_message(callback_query.from_user.id, f'<b>{Last_lact}</b>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        
    elif code == 'button13':
        await bot.answer_callback_query(callback_query.id)
        cur.execute('SELECT Last_Bad FROM "users" WHERE user_id LIKE ?', (callback_query.from_user.id,)) # раньше параметр был message.text. Чел лучший!
        Last_Bad, = cur.fetchone() # БАГИ 
        if Last_Bad != "Нет информации":
            await bot.send_message(callback_query.from_user.id, f'<a href="{Last_Link}{Last_Bad}">Побочные действия</a>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        else:
            await bot.send_message(callback_query.from_user.id, f'<b>{Last_Bad}</b>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        
    elif code == 'button14':
        await bot.answer_callback_query(callback_query.id)
        cur.execute('SELECT Last_Interaction FROM "users" WHERE user_id LIKE ?', (callback_query.from_user.id,)) # раньше параметр был message.text. Чел лучший!
        Last_Interaction, = cur.fetchone() # БАГИ 
        if Last_Interaction != "Нет информации":
            await bot.send_message(callback_query.from_user.id, f'<a href="{Last_Link}{Last_Interaction}">Взаимодействие</a>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        else:
            await bot.send_message(callback_query.from_user.id, f'<b>{Last_Interaction}</b>  \n', disable_web_page_preview=True, parse_mode = "HTML")
    
    elif code == 'button15':
        await bot.answer_callback_query(callback_query.id)
        cur.execute('SELECT Last_Sposob FROM "users" WHERE user_id LIKE ?', (callback_query.from_user.id,)) # раньше параметр был message.text. Чел лучший!
        Last_Sposob, = cur.fetchone() # БАГИ 
        if Last_Sposob != "Нет информации":
            await bot.send_message(callback_query.from_user.id, f'<a href="{Last_Link}{Last_Sposob}">Способ применения и дозы</a>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        else:
            await bot.send_message(callback_query.from_user.id, f'<b>{Last_Sposob}</b>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        
    elif code == 'button16':
        await bot.answer_callback_query(callback_query.id)
        cur.execute('SELECT Last_Peredoz FROM "users" WHERE user_id LIKE ?', (callback_query.from_user.id,)) # раньше параметр был message.text. Чел лучший!
        Last_Peredoz, = cur.fetchone() # БАГИ 
        if Last_Peredoz != "Нет информации":
            await bot.send_message(callback_query.from_user.id, f'<a href="{Last_Link}{Last_Peredoz}">Передозировка</a>  \n', disable_web_page_preview=True, parse_mode = "HTML") 
        else:
            await bot.send_message(callback_query.from_user.id, f'<b>{Last_Peredoz}</b>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        
    elif code == 'button17':
        await bot.answer_callback_query(callback_query.id)
        cur.execute('SELECT Last_Osob_ukaz FROM "users" WHERE user_id LIKE ?', (callback_query.from_user.id,)) # раньше параметр был message.text. Чел лучший!
        Last_Osob_ukaz, = cur.fetchone() # БАГИ 
        if Last_Osob_ukaz != "Нет информации":
            await bot.send_message(callback_query.from_user.id, f'<a href="{Last_Link}{Last_Osob_ukaz}">Особые указания</a>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        else:
            await bot.send_message(callback_query.from_user.id, f'<b>{Last_Osob_ukaz}</b>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        
    elif code == 'button18':
        await bot.answer_callback_query(callback_query.id)
        cur.execute('SELECT Last_Forma_vipuska FROM "users" WHERE user_id LIKE ?', (callback_query.from_user.id,)) # раньше параметр был message.text. Чел лучший!
        Last_Forma_vipuska, = cur.fetchone() # БАГИ 
        if Last_Forma_vipuska != "Нет информации":
            await bot.send_message(callback_query.from_user.id, f'<a href="{Last_Link}{Last_Forma_vipuska}">Форма выпуска</a>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        else:
            await bot.send_message(callback_query.from_user.id, f'<b>{Last_Forma_vipuska}</b>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        
    elif code == 'button19':
        await bot.answer_callback_query(callback_query.id)
        cur.execute('SELECT Last_Proizvoditel FROM "users" WHERE user_id LIKE ?', (callback_query.from_user.id,)) # раньше параметр был message.text. Чел лучший!
        Last_Proizvoditel, = cur.fetchone() # БАГИ 
        if Last_Proizvoditel != "Нет информации":
            await bot.send_message(callback_query.from_user.id, f'<a href="{Last_Link}{Last_Proizvoditel}">Производитель</a>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        else:
            await bot.send_message(callback_query.from_user.id, f'<b>{Last_Proizvoditel}</b>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        
    elif code == 'button20':
        await bot.answer_callback_query(callback_query.id)
        cur.execute('SELECT Last_Recept FROM "users" WHERE user_id LIKE ?', (callback_query.from_user.id,)) # раньше параметр был message.text. Чел лучший!
        Last_Recept, = cur.fetchone() # БАГИ 
        if Last_Recept != "Нет информации":
            await bot.send_message(callback_query.from_user.id, f'<a href="{Last_Link}{Last_Recept}">Условия отпуска из аптек</a>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        else:
            await bot.send_message(callback_query.from_user.id, f'<b>{Last_Recept}</b>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        
    elif code == 'button21':
        await bot.answer_callback_query(callback_query.id)
        cur.execute('SELECT Last_Save FROM "users" WHERE user_id LIKE ?', (callback_query.from_user.id,)) # раньше параметр был message.text. Чел лучший!
        Last_Save, = cur.fetchone() # БАГИ 
        if Last_Save != "Нет информации":
            await bot.send_message(callback_query.from_user.id, f'<a href="{Last_Link}{Last_Save}">Условия хранения</a>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        else:
            await bot.send_message(callback_query.from_user.id, f'<b>{Last_Save}</b>  \n', disable_web_page_preview=True, parse_mode = "HTML")
        
    

# хендлер для создания ссылок 
#@dp.message_handler(commands=["ref"])
#async def get_ref(message: types.Message):
#   link = await get_start_link(str(message.from_user.username), encode=True)
#   result: 'https://t.me/MyBot?start='
#   после знака = будет закодированный никнейм юзера, который создал реф ссылку, вместо него можно вставить и его id 
#   await message.answer(f"Ваша реферальная ссылка {link}")


# хендлер для расшифровки ссылки
#@dp.message_handler(commands=["start"])
#async def handler(message: types.Message):
#    args = message.get_args()
#    reference = decode_payload(args)
#    await message.answer(f"Вас пригласил {reference}") #здесь в  reference должен быть юзернейм, того кто создал ссылку




#  поллинг = опрашиваю сервера телеграм о новых сообщениях?
if __name__ == '__main__':
    executor.start_polling(dp)