import telebot
from telebot import types
import xlwings as xw
print("Работяга в деле")
token = '5871621062:AAFnWEQ3Y1jE374qAm3ZoofNhX4HbNAPsoM'

bot = telebot.TeleBot(token)

#Кнопка назад
keyboard2 = types.InlineKeyboardMarkup()
callback_button1 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="*")
keyboard2.add(callback_button1)

#Назад с описания робототехника-бесплатно
p56 = types.InlineKeyboardMarkup()
m1 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="*****")
p56.add(m1)

#Назад с описания VR-бесплатно
p57 = types.InlineKeyboardMarkup()
m1 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="******")
p57.add(m1)

#Назад с описания java-бесплатно
p58 = types.InlineKeyboardMarkup()
m1 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="*******")
p58.add(m1)

#Назад с описания sis-бесплатно
p59 = types.InlineKeyboardMarkup()
m1 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="********")
p59.add(m1)

#Назад с описания mob-бесплатно
p60 = types.InlineKeyboardMarkup()
m1 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="*********")
p60.add(m1)

#Назад с описания python-бесплатно
p61 = types.InlineKeyboardMarkup()
m1 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="**********")
p61.add(m1)

#Назад с описания шахматы-бесплатно
p62 = types.InlineKeyboardMarkup()
m1 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="***********")
p62.add(m1)

#Назад с описания авио-бесплатно
p63 = types.InlineKeyboardMarkup()
m1 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="************")
p63.add(m1)

#Назад с описания robo-платно
p64 = types.InlineKeyboardMarkup()
m1 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="*************")
p64.add(m1)

#Назад с описания vr-платно
p65 = types.InlineKeyboardMarkup()
m1 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="**************")
p65.add(m1)

#Назад с описания java-платно
p66 = types.InlineKeyboardMarkup()
m1 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="***************")
p66.add(m1)

#Назад с описания python-платно
p67 = types.InlineKeyboardMarkup()
m1 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="****************")
p67.add(m1)

#Назад с описания shac-платно
p68 = types.InlineKeyboardMarkup()
m1 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="*****************")
p68.add(m1)


#Бесплатное
ngsfagfdng = types.InlineKeyboardMarkup(row_width=1)
n1 = types.InlineKeyboardButton(text='Программирование роботов', callback_data='rob')
n2 = types.InlineKeyboardButton(text='Разработка VR/AR-приложений', callback_data='vr')
n3 = types.InlineKeyboardButton(text='Программирование на JAVA', callback_data='java')
n4 = types.InlineKeyboardButton(text='Системное администрирование', callback_data='sis')
n5 = types.InlineKeyboardButton(text='Мобильная разработка', callback_data='mob')
n6 = types.InlineKeyboardButton(text='Программирование на Python', callback_data='python')
n7 = types.InlineKeyboardButton(text='Шахматы', callback_data='shah')
d8 = types.InlineKeyboardButton(text='Авиамоделирование', callback_data='avia')
back2 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="**")
ngsfagfdng.add(n1, n2, n3, n4, n5, n6, n7, d8, back2)

#Платное
wrehdghs = types.InlineKeyboardMarkup(row_width=1)
n8 = types.InlineKeyboardButton(text='Программирование роботов', callback_data='rob1')
n9 = types.InlineKeyboardButton(text='Разработка VR/AR-приложений', callback_data='vr1')
n10 = types.InlineKeyboardButton(text='Программирование на JAVA', callback_data='java1')
n11 = types.InlineKeyboardButton(text='Программирование на Python', callback_data='python1')
n12 = types.InlineKeyboardButton(text='Шахматы', callback_data='shah1')
back2 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="**")
wrehdghs.add(n8, n9, n10, n11, n12, back2)

#Робототехника
rob_besplanto = types.InlineKeyboardMarkup(row_width=1)
n13 = types.InlineKeyboardButton(text='Механика и Робототехника', callback_data='mech')
n14 = types.InlineKeyboardButton(text='Мобильная разработка на базе конструктора LEGO EV3', callback_data='mobil_lego')
n15 = types.InlineKeyboardButton(text='Основы программирования роботов', callback_data='rob_prog')
back3 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="***")
rob_besplanto.add(n13, n14, n15, back3)

#Vr
vr_besplanto = types.InlineKeyboardMarkup(row_width=1)
n16 = types.InlineKeyboardButton(text='VR/AR: моделирование, творчество, визуализация', callback_data='vr/ar')
n17 = types.InlineKeyboardButton(text='3D-моделирование: знакомство с миром объемных моделей', callback_data='3d')
n18 = types.InlineKeyboardButton(text='Основы инженерного 3D - моделирования', callback_data='insh_3d')
back3 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="***")
vr_besplanto.add(n16, n17, n18, back3)

#java
java_besplanto = types.InlineKeyboardMarkup(row_width=1)
n19 = types.InlineKeyboardButton(text='Визуальное программирование', callback_data='visual')
n20 = types.InlineKeyboardButton(text='Юный программист', callback_data='yniy')
n21 = types.InlineKeyboardButton(text='JAVA от А до Я', callback_data='baza_java')
back3 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="***")
java_besplanto.add(n19, n20, n21, back3)

#Sis
sis_besplanto = types.InlineKeyboardMarkup(row_width=1)
n22 = types.InlineKeyboardButton(text='Эникей', callback_data='enik')
n23 = types.InlineKeyboardButton(text='Сетевое администрирование', callback_data='set_ad')
n24 = types.InlineKeyboardButton(text='Системное администрирование', callback_data='sis_ad')
n25 = types.InlineKeyboardButton(text='Сетевой архитетктор', callback_data='arch')
back3 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="***")
sis_besplanto.add(n22, n23, n24, n25, back3)

#Mobil
mob_besplanto = types.InlineKeyboardMarkup(row_width=1)
n26 = types.InlineKeyboardButton(text='Создание приложений Android', callback_data='cos_mob')
n27 = types.InlineKeyboardButton(text='Разработка мобильных приложений под Android', callback_data='ras_mob')
back3 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="***")
mob_besplanto.add(n26, n27, back3)

#python
python_besplanto = types.InlineKeyboardMarkup(row_width=1)
n28 = types.InlineKeyboardButton(text='Основы видеомонтожа', callback_data='video')
n29 = types.InlineKeyboardButton(text='Основы программирования python', callback_data='osnovi_pyt')
n30 = types.InlineKeyboardButton(text='Web-дизайн', callback_data='web')
back3 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="***")
python_besplanto.add(n28, n29, n30, back3)

#Шахматы
schah_besplanto = types.InlineKeyboardMarkup(row_width=1)
n31 = types.InlineKeyboardButton(text='Шахматная гостиная', callback_data='gost')
n32 = types.InlineKeyboardButton(text='Шахматная гостиная(адаптированная)', callback_data='gost_up')
n33 = types.InlineKeyboardButton(text='Шахматная Академия', callback_data='shah_akad')
back3 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="***")
schah_besplanto.add(n31, n32, n33, back3)

#Авиомоделирование
avia_besplanto = types.InlineKeyboardMarkup(row_width=1)
n34 = types.InlineKeyboardButton(text='Юные инженеры-констуркторы', callback_data='insh-konst')
n35 = types.InlineKeyboardButton(text='Спортивный авиамоделизм', callback_data='sport_avia')
back3 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="***")
avia_besplanto.add(n34, n35, back3)

#Роботы-платно
rob_planto = types.InlineKeyboardMarkup(row_width=1)
h1 = types.InlineKeyboardButton(text='Соревновательная Робототехника', callback_data='sorev_robo')
h2 = types.InlineKeyboardButton(text='Лего-Знайки', callback_data='lego_znay')
back4 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="****")
rob_planto.add(h1, h2, back4)

#VR-платно
vr_planto = types.InlineKeyboardMarkup(row_width=1)
h3 = types.InlineKeyboardButton(text='Игродел', callback_data='igrodel')
back4 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="****")
vr_planto.add(h3, back4)

#JAVA-платно
java_planto = types.InlineKeyboardMarkup(row_width=1)
h4 = types.InlineKeyboardButton(text='Компьютерный гений', callback_data='geniy')
back4 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="****")
java_planto.add(h4, back4)

#Python-платно
python_planto = types.InlineKeyboardMarkup(row_width=1)
h5 = types.InlineKeyboardButton(text='Информатика (подготовка к ЕГЭ)', callback_data='ege_info')
h6 = types.InlineKeyboardButton(text='Математика (подготовка к ОГЭ)', callback_data='oge_math')
back4 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="****")
python_planto.add(h5, h6, back4)

#Шахматы-платно
schah_planto = types.InlineKeyboardMarkup(row_width=1)
h7 = types.InlineKeyboardButton(text='Соревновательные шахматы', callback_data='sorev_shah')
back4 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="****")
schah_planto.add(h7, back4)


# @bot.chat_join_request_handler()
# async def start1(update: types.ChatJoinRequest):
#     # тут мы принимаем юзера в канал
#     await update.approve()
#     # а тут отправляем сообщение
#     await bot.send_message(chat_id=update.from_user.id, text="👋 Привет, <b>{0.first_name}</b>! Я тестовый бот для IT-CUBE\n\n💻 Сервис осуществляет <b>поиск времени занятий детей</b> в режиме реального времени\n\n💬 Для того, чтобы начать, просто выбери, что хочешь".format(message.from_user), reply_markup=harb, parse_mode='html')

@bot.message_handler(commands=["start"])
def starting(message):
    harb = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button2 = types.KeyboardButton("🔍 Поиск ребенка")
    button3 = types.KeyboardButton("📄 О нас")
    button4 = types.KeyboardButton("❓ Частые вопросы")
    harb.add(button2,button3,button4)
    bot.send_message(message.chat.id, text="👋 Привет, <b>{0.first_name}</b>! Я тестовый бот для IT-CUBE\n\n💻 Сервис осуществляет <b>поиск времени занятий детей</b> в режиме реального времени\n\n💬 Для того, чтобы начать, просто выбери, что хочешь".format(message.from_user), reply_markup=harb, parse_mode='html')
    # bot.register_next_step_handler(a, returning)

@bot.message_handler(content_types=['text'])
def returning(message):
    if message.chat.type == 'private':
        if(message.text == "🔍 Поиск ребенка"):
            a = bot.send_message(message.chat.id, '🔐 Введите имя ребенка:')
            bot.register_next_step_handler(a, returning)
        elif(message.text == "📄 О нас"):
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("💡 VK", url='https://vk.com/itcubeugo')
            markup.add(button1)
            bot.send_message(message.chat.id, 'ℹ️ «IT-CUBE» — федеральный проект, реализуемый в рамках национального проекта «Образование» федерального проекта «Цифровая образовательная среда». Данный проект нацелен на популяризацию технических профессий, увеличение охвата учащихся IT-технологиями и направлен на раннюю профессиональную ориентацию.\n\n📞 тел.: 8 (35134) 4-22-81, 8 (35134) 4-37-13\n\n📧 эл.почта: itcubeugo@mail.ru', reply_markup=markup)
        elif(message.text == "❓ Частые вопросы"):
            markup_inline = types.InlineKeyboardMarkup(row_width=1)
            button2 = types.InlineKeyboardButton(text='Бесплатное ли обучение?', callback_data='obuchenie')
            button3 = types.InlineKeyboardButton(text='Какие есть направления?', callback_data='napravleniya')
            button7 = types.InlineKeyboardButton(text='Что нужно для поступления?', callback_data='dok')
            button8 = types.InlineKeyboardButton(text='Можно ли менять направления?', callback_data='smena')
            button9 = types.InlineKeyboardButton(text='Возраст поступления?', callback_data='age')
            markup_inline.add(button2,button3,button8,button7,button9)
            bot.send_message(message.chat.id, '📋 Выбирай:', reply_markup=markup_inline)

@bot.callback_query_handler(func = lambda call: True)
def answer(call):
    kk = types.InlineKeyboardMarkup(row_width=1)
    button2 = types.InlineKeyboardButton(text='Бесплатное ли обучение?', callback_data='obuchenie')
    button3 = types.InlineKeyboardButton(text='Какие есть направления?', callback_data='napravleniya')
    button7 = types.InlineKeyboardButton(text='Что нужно для поступления?', callback_data='dok')
    button8 = types.InlineKeyboardButton(text='Можно ли менять направления?', callback_data='smena')
    button9 = types.InlineKeyboardButton(text='Возраст поступления?', callback_data='age')
    kk.add(button2, button3, button8, button7, button9)
    
    ss = types.InlineKeyboardMarkup(row_width=1)
    b10 = types.InlineKeyboardButton(text='💥 Бесплатное', callback_data='nomoney')
    b11 = types.InlineKeyboardButton(text='💸 Платное', callback_data='money')
    callback_button1 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="*")
    ss.add(b10, b11, callback_button1)
    
    #Другие вопросы
    if call.data == 'napravleniya':
        bot.edit_message_text('📌 Что хочешь?', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=ss)
    elif call.data == 'obuchenie':
        bot.edit_message_text('📌 В нашем учереждении присутствует, как платное, так и бесплатное обучение.', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=keyboard2)
    elif call.data == 'dok':
        bot.edit_message_text('🗂 Паспорт/Свидетельство о рождении, черная/синяя ручка, один из родителей и хорошее настроение.\n📞 Подробнее по тел.: 8 (35134) 4-22-81, 8 (35134) 4-37-13.', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=keyboard2)
    elif call.data == 'smena':
        bot.edit_message_text('🔄 Да, только сначало нужно поговорить с преподавателем.', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=keyboard2)
    elif call.data == 'age':
        bot.edit_message_text('❗ Возраст поступления колеблется <b>от 3 до 18 лет!!!</b>', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=keyboard2, parse_mode='html')

    #Назад-другое
    elif call.data == '*':
        bot.edit_message_text('📋 Выбирай:', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=kk)
    elif call.data == '**':
        bot.edit_message_text('📌 Что хочешь?', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=ss)
    elif call.data == "***":
        bot.edit_message_text('📌 Что хочешь?', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=ngsfagfdng)
    elif call.data == "****":
        bot.edit_message_text('📌 Что хочешь?', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=wrehdghs)
    
    #назад-бесплатно
    elif call.data == "*****":
        bot.edit_message_text('Программирование роботов', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=rob_besplanto)
    elif call.data == "******":
        bot.edit_message_text('VR/AR', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=vr_besplanto)
    elif call.data == "*******":
        bot.edit_message_text('JAVA', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=java_besplanto)
    elif call.data == "********":
        bot.edit_message_text('Системное администрирование', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=sis_besplanto) 
    elif call.data == "*********":
        bot.edit_message_text('Мобильная разработка', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=mob_besplanto)
    elif call.data == "**********":
        bot.edit_message_text('Программирование на PYTHON', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=python_besplanto)
    elif call.data == "***********":
        bot.edit_message_text('Шахматная гостиная', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=schah_besplanto) 
    elif call.data == "************":
        bot.edit_message_text('Авиамоделирование', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=avia_besplanto)
    
    #назад-платно
    elif call.data == "*************":
        bot.edit_message_text('Программирование роботов', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=rob_planto) 
    elif call.data == "**************":
        bot.edit_message_text('VR/AR', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=vr_planto)
    elif call.data == "***************":
        bot.edit_message_text('Программирование на JAVA', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=java_planto)
    elif call.data == "****************":
        bot.edit_message_text('Программирование на PYTHON', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=python_planto) 
    elif call.data == "*****************":
        bot.edit_message_text('Шахматная гостиная', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=schah_planto)
    
    #Виды направлений
    elif call.data == 'nomoney':
        bot.edit_message_text('Бесплатное', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=ngsfagfdng)
    elif call.data == 'money':
        bot.edit_message_text('Платное', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=wrehdghs)
    
    #Бесплатыне направления
    elif call.data == 'rob':
        bot.edit_message_text('Программирование роботов', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=rob_besplanto)
    elif call.data == 'vr':
        bot.edit_message_text('VR/AR', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=vr_besplanto)
    elif call.data == 'java':
        bot.edit_message_text('JAVA', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=java_besplanto)
    elif call.data == 'sis':
        bot.edit_message_text('Системное администрирование', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=sis_besplanto)
    elif call.data == 'mob':
        bot.edit_message_text('Мобильная разработка', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=mob_besplanto)
    elif call.data == 'python':
        bot.edit_message_text('Программирование на PYTHON', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=python_besplanto)
    elif call.data == 'shah':
        bot.edit_message_text('Шахматная гостиная', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=schah_besplanto)
    elif call.data == 'avia':
        bot.edit_message_text('Авиамоделирование', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=avia_besplanto)

    #Платные направления    
    elif call.data == 'rob1':
        bot.edit_message_text('Программирование роботов', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=rob_planto)
    elif call.data == 'vr1':
        bot.edit_message_text('VR/AR', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=vr_planto)
    elif call.data == 'java1':
        bot.edit_message_text('Программирование на JAVA', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=java_planto)
    elif call.data == 'python1':
        bot.edit_message_text('Программирование на PYTHON', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=python_planto)
    elif call.data == 'shah1':
        bot.edit_message_text('Шахматная гостиная', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=schah_planto)

    #Описание робототехника-бесплатно
    elif call.data == 'mech':
        bot.edit_message_text('⚠️ В РАЗРАБОТКЕ', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=p56)
    elif call.data == 'mobil_lego':
        bot.edit_message_text('⚠️ В РАЗРАБОТКЕ', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=p56)
    elif call.data == 'rob_prog':
        bot.edit_message_text('⚠️ В РАЗРАБОТКЕ', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=p56)

    #Описание VR-бесплатно
    elif call.data == 'vr/ar':
        bot.edit_message_text('Дополнительная образовательная программа «VR/AR МОДЕЛИРОВАНИЕ, ТВОРЧЕСТВОВИЗУАЛИЗАЦИЯ» рассчитана на 108 часов (1 год обучения), возрастная категория обучающихся 11-15 лет. Занятия проводятся 2 раза в неделю.', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=p57)
    elif call.data == '3d':
        bot.edit_message_text('Дополнительная общеобразовательная программа «3D-моделирование знакомство с миром объемных моделей» технической направленности направленна на овладение инструментами компьютерных программ для моделирования и проектирования объемных моделей. Дополнительная образовательная программа «3D моделирование:» рассчитана на 108 часов (1 год обучения), возрастная категория обучающихся 12-16 лет. Занятия проводятся 2 раза в неделю.', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=p57)
    elif call.data == 'insh_3d':
        bot.edit_message_text('Дополнительная образовательная программа «Основы инженерного 3D-моделирования» рассчитана на 108 часов (1 год обучения), возрастная категория обучающихся 14-17 лет. КОМПАС-3D — это система трехмерного моделирования позволяет создавать объемные модели и чертежи. Программа предполагает освоение системы КОМПАС, применяемой при проектировании изделий и выполнении чертежей. ', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=p57) 

    #Описание JAVA-бесплатно
    elif call.data == 'visual':
        bot.edit_message_text('⚠️ В РАЗРАБОТКЕ', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=p58)
    elif call.data == 'yniy':
        bot.edit_message_text('Дополнительная общеобразовательная общеразвивающая программа «Юный программист» предназначена для обучающихся в возрасте 6-8 лет, занятия проходят 2 раза в неделю. На занятиях дети учатся простому программированию, собирая блоки программ из разноцветных кирпичиков, также как собираются конструкторы ЛЕГО. В этой среде можно создавать собственные истории, мультфильмы, игры персонажей, различные объекты, видоизменять их, перемещать по экрану, озвучивать. Обучаясь по программе, ребенок получает разнообразие возможностей для самовыражения и развития способностей. В программе предусмотрен промежуточный и итоговый контроль, которые проходят в виде защиты проектов.', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=p58)
    elif call.data == 'baza_java':
        bot.edit_message_text('Дополнительная общеобразовательная общеразвивающая программа «Java от А до Я» предназначена для обучающихся в возрасте 14-17 лет, занятия проходят 2 раза в неделю. Обучающиеся получат базовые знания и умения работы с объектно-ориентированным языком программирования, работающий на миллиардах устройств по всему миру. На Java работают приложения, операционные системы для смартфонов и многие известные программы. Java – один из самых востребованных языков программирования в мире и один из двух официальных языков программирования, используемых в разработке Android. Разработчики, знакомые с Java, весьма востребованы и способны создавать широкий спектр различных приложений, игр и инструментов. Обучающиеся научаться писать программы В программе предусмотрен промежуточный и итоговый контроль, которые проходят в виде защиты проектов. ', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=p58)

    #Описание sis-бесплатно
    elif call.data == 'enik':
        bot.edit_message_text('⚠️ В РАЗРАБОТКЕ', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=p59)
    elif call.data == 'set_ad':
        bot.edit_message_text('⚠️ В РАЗРАБОТКЕ', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=p59)
    elif call.data == 'sis_ad':
        bot.edit_message_text('⚠️ В РАЗРАБОТКЕ', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=p59)
    elif call.data == 'arch':
        bot.edit_message_text('⚠️ В РАЗРАБОТКЕ', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=p59)
    
    #Описание мобил-бесплатно
    elif call.data == 'cos_mob':
        bot.edit_message_text('⚠️ В РАЗРАБОТКЕ', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=p60)
    elif call.data == 'ras_mob':
        bot.edit_message_text('Дополнительная общеобразовательная общеразвивающая программа «Разработка мобильных приложений под Android» предназначена для обучающихся в возрасте 14-16 лет, занятия проходят 2 раза в неделю. На занятиях обучающиеся будут изучать основы создания приложений для операционной системы Android. В качестве среды разработки для обучения будет использоваться Android Studio, а в качестве языка программирования JAVA. В программе предусмотрен промежуточный и итоговый контроль, которые проходят в виде защиты проектов.', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=p60)
    
    #Описание python-бесплатно
    elif call.data == 'video':
        bot.edit_message_text('Программа предусматривает развитие технических и творческих способностей. Задачи ставятся так, чтобы подростки могли анализировать сценическую и техническую ситуации, делать выводы, проявлять находчивость, самостоятельно принимать технические решения и полученный опыт, использовать в работе с последующими творческими проектами. Курс видеомонтажа нужен тем, кто хочет больше развиваться в творческом плане. В курсе много практических заданий и кейсов, ориентированных на творческое развитие детей. В техническом плане они освоят программу видеомонтажа, познакомятся с её инструментами. Первое полугодие посвящено развитию навыков работы в программе. Второе полугодие ориентировано на изучение правил: как снимать, как ставить кадр, как писать сценарии к видео или фильмам и т.д. Программа рассчитана на возраст 12-17 лет, занятия проходят один раз в неделю по 2 часа, группы по 12 человек. В завершении обучения необходимо разработать совместный проект и защитить его на итоговой аттестации.', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=p61)
    elif call.data == 'osnovi_pyt':
        bot.edit_message_text('Программа рассчитана на возраст 13-17 лет, курс предназначен для тех, кто хочет связать свою жизнь с программированием. Только с 13 лет! Рекомендуется только для детей, которые сами хотят этим заниматься и интересуются компьютерными технологиями, программированием. Занятия проводятся 2 раза в неделю по 2 часа. В завершении обучения необходимо разработать совместный проект и защитить его на итоговой аттестации. Содержание программы способствует развитию навыка программирования на базовом уровне.', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=p61)
    elif call.data == 'web':
        bot.edit_message_text('Основная цель программы: способствовать формированию творческой личности, Закончив курс, обучающийся будет способен обладать информационными компетенциями, владеть базовыми навыками в области Web-дизайна, уметь разрабатывать эффективные алгоритмы и реализовывать их в виде кода, написанного на HTML и CSS.\n\nПервое полугодие будет посвящено наполнению сайта и добавление на веб-страницу разного контента. Во втором полугодии дети научатся красиво оформлять контент, который они добавили на веб-страницу. В конечно итоге дети научатся делать простые, но красивые сайты- визитки с функционалом.\n\nПрограмма рассчитана на возраст 12-16 лет, занятия два раза в неделю, группы по 12 человек. В завершении обучения необходимо разработать совместный проект и защитить его на итоговой аттестации.', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=p61)

    #Описание шахматы-бесплатно
    elif call.data == 'gost':
        bot.edit_message_text('⚠️ В РАЗРАБОТКЕ', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=p62)
    elif call.data == 'gost_up':
        bot.edit_message_text('⚠️ В РАЗРАБОТКЕ', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=p62)
    elif call.data == 'shah_akad':
        bot.edit_message_text('⚠️ В РАЗРАБОТКЕ', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=p62)
    
    #Описание авио-бесплатно
    elif call.data == 'insh-konst':
        bot.edit_message_text('⚠️ В РАЗРАБОТКЕ', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=p63)
    elif call.data == 'sport_avia':
        bot.edit_message_text('⚠️ В РАЗРАБОТКЕ', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=p63)
    elif call.data == 'rob_prog':
        bot.edit_message_text('⚠️ В РАЗРАБОТКЕ', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=p63)
    
    #Описание rob-платное
    elif call.data == 'sorev_robo':
        bot.edit_message_text('⚠️ В РАЗРАБОТКЕ', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=p64)
    elif call.data == 'lego_znay':
        bot.edit_message_text('⚠️ В РАЗРАБОТКЕ', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=p64)

    #Описание vr-платное
    elif call.data == 'igrodel':
        bot.edit_message_text('⚠️ В РАЗРАБОТКЕ', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=p65)
    
    #Описание java-платное
    elif call.data == 'geniy':
        bot.edit_message_text('⚠️ В РАЗРАБОТКЕ', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=p66)  

    #Описание pyth-платное
    elif call.data == 'ege_info':
        bot.edit_message_text('Программа подготовки к ЕГЭ по информатике. Возраст обучающихся – 16-17 лет, одно занятие в неделю по 2 часа. Обучение на платной основе.', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=p67)
    elif call.data == 'oge_math':
        bot.edit_message_text('Программа подготовки к ОГЭ по математике. Возраст обучающихся – 14-15 лет, одно занятие в неделю по 2 часа. Обучение на платной основе.', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=p67)

    #Описание шах-платное
    elif call.data == 'sorev_shah':
        bot.edit_message_text('⚠️ В РАЗРАБОТКЕ', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=p68)

#Поиск учителя
@bot.message_handler(content_types=['text'])
def returning(message):
    if message.chat.type == 'private':
        name = message.text
        i = 1
        j = 1
        wb = xw.Book('february.xlsx')
        sheet = wb.sheets['Sheet1']
        while sheet.range((i, 1)).value:
            if name == sheet.range((i, 1)).value:
                while sheet.range((j, 5)).value:
                    if sheet.range((j, 5)).value == sheet.range((i, 2)).value:
                        if sheet.range((j, 6)).value == '-':
                            return bot.send_message(message.chat.id, '🔑 ' + f"{sheet.range((i, 2)).value}: {sheet.range((i, 3)).value}. Занятий не будет")
                        else:
                            return bot.send_message(message.chat.id, '🔑 ' + f"{sheet.range((i, 2)).value}: {sheet.range((i, 3)).value}")
                    j += 1
            i += 1
        else:
            bot.send_message(message.chat.id, '❌ Такого ребенка нет')

#Поиск препода
# @bot.message_handler(content_types=['text'])
# def repurning(message):
#     if(message.text == "🔍 Поиск препода"):
#         b = bot.send_message(message.chat.id, 'Введите имя препода:')
#         bot.register_next_step_handler(b, returning)
# @bot.message_handler(content_types=['text'])
# def repurning(message):
#     i = 1
#     wb = xw.Book('february.xlsx')
#     sheet2 = wb.sheets['Sheet2']
#     while sheet2.range((i, 1)).value:
#         if work == sheet2.range((i, 1)).value:
#             return bot.send_message(message.chat.id, f'Педагог: {sheet2.range((i, 2)).value}, Описание: {sheet2.range((i, 3)).value}')
#         i += 1
#     else:
#         bot.send_message(message.chat.id, 'Такого препода нет')

if __name__ == '__main__':
    bot.polling(none_stop=True)

    # button4 = types.InlineKeyboardButton(text='Разработка VR/AR-приложений', callback_data='vr')
    # button5 = types.InlineKeyboardButton(text='Программирования на JAVA', callback_data='java')
    # b1 = types.InlineKeyboardButton(text='Мобильная разработка', callback_data='mobil')
    # b2 = types.InlineKeyboardButton(text='Программирование на Python', callback_data='python')
    # b3 = types.InlineKeyboardButton(text='Системное администрирование', callback_data='sis')
    # b4 = types.InlineKeyboardButton(text='Робототехника', callback_data='rob')
    # b5 = types.InlineKeyboardButton(text='Шахматы', callback_data='shah')