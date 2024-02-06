from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup






# ниже кнопки

button_1 = KeyboardButton('❓Как пользоваться')
button_2 = KeyboardButton('🎯Найти лекарство')
button_3 = KeyboardButton('👍🏻Поддержка')

# кнопки для раскрытия информации о веществе
inline_btn_bal1 = InlineKeyboardButton(f'Название лекарства', callback_data='button1')
inline_bal1 = InlineKeyboardMarkup().add(inline_btn_bal1)

inline_btn_bal2 = InlineKeyboardButton(f'Активное в-во', callback_data='button2')
inline_bal2 = InlineKeyboardMarkup().add(inline_btn_bal2)

inline_btn_bal3 = InlineKeyboardButton(f'ATH', callback_data='button3') # СПЕЦ
inline_bal3 = InlineKeyboardMarkup().add(inline_btn_bal3)

inline_btn_bal4 = InlineKeyboardButton(f'Фармакологическая группа', callback_data='button4')
inline_bal4 = InlineKeyboardMarkup().add(inline_btn_bal4)

inline_btn_bal5 = InlineKeyboardButton(f'Состав', callback_data='button5')
inline_bal5 = InlineKeyboardMarkup().add(inline_btn_bal5)

inline_btn_bal6 = InlineKeyboardButton(f'Описание', callback_data='button6')
inline_bal6 = InlineKeyboardMarkup().add(inline_btn_bal6)

inline_btn_bal7 = InlineKeyboardButton(f'Фармакологическое действие', callback_data='button7')
inline_bal7 = InlineKeyboardMarkup().add(inline_btn_bal7)

inline_btn_bal8 = InlineKeyboardButton(f'Фармакодинамика', callback_data='button8')  # СПЕЦ
inline_bal8 = InlineKeyboardMarkup().add(inline_btn_bal8)

inline_btn_bal9 = InlineKeyboardButton(f'Фармакокинетика', callback_data='button9')  # СПЕЦ
inline_bal9 = InlineKeyboardMarkup().add(inline_btn_bal9)

inline_btn_bal10 = InlineKeyboardButton(f'Показания', callback_data='button10')
inline_bal10 = InlineKeyboardMarkup().add(inline_btn_bal10)

inline_btn_bal11 = InlineKeyboardButton(f'Противопоказания', callback_data='button11')
inline_bal11 = InlineKeyboardMarkup().add(inline_btn_bal11)

inline_btn_bal12 = InlineKeyboardButton(f'Применение при беременности и кормлении грудью', callback_data='button12')
inline_bal12 = InlineKeyboardMarkup().add(inline_btn_bal12)

inline_btn_bal13 = InlineKeyboardButton(f'Побочные действия', callback_data='button13')
inline_bal13 = InlineKeyboardMarkup().add(inline_btn_bal13)

inline_btn_bal14 = InlineKeyboardButton(f'Взаимодействие', callback_data='button14') # СПЕЦ
inline_bal14 = InlineKeyboardMarkup().add(inline_btn_bal14)

inline_btn_bal15 = InlineKeyboardButton(f'Способ применения и дозы', callback_data='button15')
inline_bal15 = InlineKeyboardMarkup().add(inline_btn_bal15)

inline_btn_bal16 = InlineKeyboardButton(f'Передозировка', callback_data='button16')
inline_bal16 = InlineKeyboardMarkup().add(inline_btn_bal16)

inline_btn_bal17 = InlineKeyboardButton(f'Особые указания', callback_data='button17')
inline_bal17 = InlineKeyboardMarkup().add(inline_btn_bal17)

inline_btn_bal18 = InlineKeyboardButton(f'Форма выпуска', callback_data='button18')
inline_bal18 = InlineKeyboardMarkup().add(inline_btn_bal18)

inline_btn_bal19 = InlineKeyboardButton(f'Производитель', callback_data='button19') # СПЕЦ
inline_bal19 = InlineKeyboardMarkup().add(inline_btn_bal19)

inline_btn_bal20 = InlineKeyboardButton(f'Условия отпуска из аптек', callback_data='button20') # СПЕЦ
inline_bal20 = InlineKeyboardMarkup().add(inline_btn_bal20)

inline_btn_bal21 = InlineKeyboardButton(f'Условия хранения', callback_data='button21') # СПЕЦ
inline_bal21 = InlineKeyboardMarkup().add(inline_btn_bal21)

inline_btn_bal22 = InlineKeyboardButton(f'Ссылка на препарат', callback_data='button22') # СПЕЦ
inline_bal22 = InlineKeyboardMarkup().add(inline_btn_bal22)


# общее меню из кнопок
inline_btn_ez_info = InlineKeyboardMarkup(row_width=2).add(inline_btn_bal1, inline_btn_bal2, inline_btn_bal4, inline_btn_bal5, inline_btn_bal6, inline_btn_bal7, inline_btn_bal10, inline_btn_bal11, inline_btn_bal12, inline_btn_bal13, inline_btn_bal15, inline_btn_bal16, inline_btn_bal17, inline_btn_bal18)

# markup = InlineKeyboardMarkup # разделил кнопки поменьше
# markup.row_width = 2

inline_btn_hard_info = InlineKeyboardMarkup(row_width=2).add(inline_btn_bal3, inline_btn_bal8, inline_btn_bal9, inline_btn_bal14, inline_btn_bal19, inline_btn_bal20, inline_btn_bal21, inline_btn_bal22)


# markup = InlineKeyboardMarkup
# markup.row_width = 2

# всплывающая кнопка
#inline_btn_1 = InlineKeyboardButton('Реферальная система', callback_data='button6')
#inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

# кнопки аккаунтов
#inline_btn_bal1 = InlineKeyboardButton(f'💰Баланс: {balance1}  💵Цена:{price1}', callback_data='button7')
#inline_bal1 = InlineKeyboardMarkup().add(inline_btn_bal1)

# общее меню из кнопок

#inline_btn_full123.add(inline_btn_bal1, inline_btn_bal2, inline_btn_bal3)
#inline_btn_full123.row(inline_btn_bal1, inline_btn_bal2, inline_btn_bal3)



mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(button_1, button_2, button_3)