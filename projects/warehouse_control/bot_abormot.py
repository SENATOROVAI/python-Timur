import json
from  telebot import  types
token = "6961795957:AAECUWDdKeJSmpOgJXkfdy62T_kHQ4OCzBE"
import telebot
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(mess):
    bot.send_message(mess.chat.id, "Это бот для покупок на блубериз, вы можете посмотреть католог используя команду /look")


@bot.message_handler(commands=["look"])
def look(mess):
    message_beautiful = ""
    with open("data_base.json", "r") as file:
        data = json.load(file)
    for item in data:
        message_beautiful += f"*название:* {item[0]}\n"
        message_beautiful += f"*в наличии:* {item[1]}\n"
        message_beautiful += f"*ИП:* {item[2]}\n"
        message_beautiful += f"*цена:* {item[3]}\n"
        message_beautiful += f"*рейтинг:* {item[4]}\n"
        message_beautiful += "\n \n \n"
    bot.send_message(mess.chat.id, message_beautiful, parse_mode="Markdown")
@bot.message_handler(commands=["buy"])
def buy(mess):
    mesa = ""
    encounter = 1
    with open("data_base.json", "r") as file:
        data = json.load(file)
    for item in data:
        mesa += f"{encounter}-{item[0]}\n"
        encounter += 1
    ab = bot.send_message(mess.chat.id, mesa)
    bot.register_next_step_handler(ab, hand_buy)
def hand_buy (mess):
    with open("data_base.json", "r") as file:
        data = json.load(file)
        encounter = len(data)
    try:
        if len(data) >= int(mess.text):
            amamont = int(data[int(mess.text)-1][1])
    except:
        bot.send_message(mess.chat.id, "такого товара нет в списке")
    kb = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="я oплатил", callback_data="+")
    btn2 = types.InlineKeyboardButton(text="я передумал", callback_data="-")
    kb.add(btn1)
    kb.add(btn2)

    amogus = open('amogus.mp3', 'rb')
    with open("dataBot.json", "w") as file:
        dictinoari = {mess.chat.id:mess.text}
        json.dump(dictinoari, file, indent= 4)
    try:
        if int(mess.text) <= encounter:
            if amamont > 0:

                ab = bot.send_message(mess.chat.id, f"переведите {data[int(mess.text)-1][3]} на номер телефона +79534125001 и отправьте сюда чек", reply_markup=kb)
            else:
                bot.send_message(mess.chat.id, "товара нет на складе, попрорбуйте подождать пока он появится или закажите что то другое")
        else:

            bot.send_audio(mess.chat.id, amogus)
    except:

        bot.send_audio(mess.chat.id, amogus)

@bot.callback_query_handler(func=lambda call:True)
def hand_plus(call):
    if call.data == "+":
        ac = bot.send_message(call.message.chat.id, "Напишите ваш адрес чтобы мы могли доставить вам посылку")
        bot.register_next_step_handler(ac, hand_adress)
    elif call.data == "-":
        bot.send_message(call.message.chat.id, "Ну ладно так уж быть")
        amogus = open('amogus.mp3', 'rb')
        bot.send_audio(call.message.chat.id, amogus)
def hand_adress(mess):
    bot.send_message(mess.chat.id, f"Ожидайте доставку товара на адрес {mess.text} в течение 24 часов")
    with open("dataBot.json", "r") as file:
        datata = json.load(file)
        number = int(datata[str(mess.chat.id)])
    with open("data_base.json", "r") as file:
        data3 = json.load(file)
        data3[number-1][1] = str(int(data3[number-1][1]) - 1)

    with open("data_base.json", "w" ) as file:
        json.dump(data3,file,indent=5)

@bot.message_handler()
def chum_handler(mess):
    bot.send_message(mess.chat.id, "Я вас не понимаю хватит билибирду писать")
    bot.send_dice(mess.chat.id)

bot.polling()