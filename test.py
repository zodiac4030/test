#!/usr/bin/python
# -*- coding: utf-8 -*-
import telebot
import sys
import redis as r
import os
import re
import random
from random import randint as rand
import urllib2
import urllib
import requests
import requests as req
import json
from telebot import types
reload(sys)
session = requests.session()
sys.setdefaultencoding("utf-8")
redis = r.StrictRedis(host='localhost', port=6379, db=9)
TOKEN = '599655822:AAEL58MJxgP2hKsG2EIYKAOrzmGYRGIV9yQ' #Bot Token
bot = telebot.TeleBot(TOKEN)
sudo = [4091485] #Sudo Id
botid = bot.get_me().id
botu = bot.get_me().username
print bot.get_me().username


chtext = """
دوست عزیز من نوروزت مبارک😀
برای استفاده از ربات و حمایت از ما اول باید عضو کانال ما بشی👇
بعد از عضویت بیا دوباره بگو چی میخای📍
"""

natije2 = """
مجموع امتیازات شما : {} است😀

اگر مجموعه امتیازات شما بین 100-150 بود👇
📃 شما فردی دلسوز هستید که افراد به خاطر درون شما مجذوب می شوند.

اگر مجموع امتیازات شما بین 160-250 بود👇
📃 شما فردی دوست داشتنی هستید ولی دیگران این را درک نمیکنند و به خاطر ظاهر شما جذب میشوند.

اگر مجموع امتیازات شما بین 300-360 بود👇
📃 شما به راحتی عصبانی نمیشوید. شما دوست خوبی هستید و دیگران به خاطر خوبی و خونسردی شما مجذوب میشوند.
"""
natije = """
مجموع امتیازات شما : {} است


اگر مجموع امتیازات شما 350-400 بود سن عقلی شما بین 4 تا 9 سال میباشد👶
📃 این به این معناس که شما طبیعتی بچه گانه دارید و از هرچیز کوچک و ساده ای لذت میبرید و هیجان زده میشوید.

اگر مجموع امتیازات شما 300-340 بود سن عقلی شما بین 9 تا 16 سال میباشد👨
📃 این به این معنا است که سن عقلی یک نوجوان را دارا هستید شما نسبتا بالغ هستید و سرکش.شما شخصیتی دمدمی مزاج هستید.

اگر مجموع امتیازات شما 250-290 بود سن عقلی شما بین 16 تا 21 سال میباشد👦
📃 شما میدانید چه زمانی دست به عمل بزنید و چه زمانی برای تفریح مناسب است.شما میتوانید جدی باشید اگر بخواهید اما گاهی نابالغانه رفتار میکنید.

اگر مجموع امتیازات شما 200-240 بود سن عقلی شما بین 21 تا 29 سال میباشد👧
📃 به این معنی میباشد که شما سن عقلی یک جوان بالغ را دارید. شما اکثر اوقات عاقلانه رفتار میکنید و میدانید کِی جدی رفتار ونید. شما فردی باهوش و خود آگاه هستید

اگر مجموع امتیازات شما 150-190 بود سن عقلی شما بین 29 تا 55 سال میباشد👵
📃 یعنی شما سن عقلی یک فرد بالغ را دارید. شما فردی فروتن و نجیب میباشید. شما رفتاری خوب دارید و آداب معاشرت را خوب میدانید.

اگر مجموع امتیازات شما 100-140 بود سن عقلی شما +55 سال میباشد👨
📃 به این معنی میباشد که شما سن عقلی یک فرد مسن را دارا هستید. و قدردان ساده ترین چیزها در زندگی خود میباشید. میدانید چه میخواهید.
"""

starttext = """
سلام😁

دوس داری بدونی ضریب هوشیت چنده؟😳یا عقلت چند سالشه؟؟😳

پس اول تست خودتو انتخاب کن و به سوالاتی که بصورت کاملا علمی طراحی شده پاسخ دقیق بده😍😍

راستی از ویژگی های دیگه رباتم میتونی استفاده کنی خودت ببین...👇👇
"""

markups = types.ReplyKeyboardMarkup(resize_keyboard=True)
markups.row('سن عقلی من','تست جذابیت')
markups.row('فال حافظ')

#دریافت امار
@bot.message_handler(commands=["u"])
def usueu(m):
  bot.reply_to(m,redis.scard("uu"))
    
@bot.message_handler(commands=["send"])
def sendall(m):
     for all in redis.smembers('uu'):
      try:
       bot.send_message(all,m.text.replace('/send ',''))
      except:
       redis.srem('uu',all)
       
@bot.message_handler(commands=['start'])
def start(m):
    try:
        text = m.text.split()[1]
        if text:
            text2 = text.replace('id_', '')
            if int(text2) == m.from_user.id:
                bot.reply_to(m, 'ای کلک میخای با لینک خودت وارد ربات بشی😅')
            else:
                sts = redis.get('bot{}'.format(m.from_user.id))
                if redis.sismember("uu",m.from_user.id):
                    bot.send_message(m.chat.id, 'فقط کسایی که عضو ربات نیستن میتونن یک بار با لینک دوستشون وارد شوند❌')
                else:
                    oo = redis.get('ids{}{}'.format(m.from_user.id, text2))
                    if oo:
                        bot.reply_to(m, 'شما از قبل با لینک این کاربر وارد ربات شده اید😠')
                    else:
                        redis.set('ids{}{}'.format(m.from_user.id, text2), text2)
                        start2(m, m.from_user.id)
                        redis.sadd('add{}'.format(text2), m.from_user.id)
                        redis.sadd('uu',m.from_user.id)
                        bot.send_message(text2, 'یک نفر با لینک تو وارد ربات شد🌟')
    except Exception as e:
        print e
        if 'list index out of range' in str(e):
            start2(m, m.from_user.id)
        else:
            print('s')
    
def start2(m,u):
   redis.sadd("uu",u)
   bot.reply_to(m,starttext.format(m.from_user.first_name),reply_markup=markups)
   
markupch = types.InlineKeyboardMarkup()
markupch.add(types.InlineKeyboardButton('✌عضویت در‌کانال✌', url='telegram.me/sianol'))

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
      try:
        uid = call.from_user.id
        card = redis.scard('add'+str(uid))
        if call.data.startswith("fal") :
          link = call.data.replace("fal","")
          bot.send_audio(call.message.chat.id, link,title='SPEEDTEAM',caption='@HoshTestBot')
        if call.data.startswith("tabir") :
          text = call.data.replace("tabir","")
          tabir = redis.get('tabir{}'.format(text))
          bot.send_message(call.message.chat.id, tabir)
        if call.data == "startaql":
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('A', callback_data='numb'+str('20')),types.InlineKeyboardButton('B', callback_data='numb'+str('30')))
            markup.add(types.InlineKeyboardButton('C', callback_data='numb'+str('40')),types.InlineKeyboardButton('D', callback_data='numb'+str('10')))
            bot.send_photo(call.message.chat.id,'AgADBAAD9KwxGw0icVG7h_wGD6VwIDQSkRkABFKwocnUUZeOsVIAAgI',caption="📍سوال شماره یک:",reply_markup=markup)
        if call.data.startswith('numb'):
          num = call.data.replace("numb","")
          aql = redis.get('aql'+str(uid))
          tm = redis.get('aqlt'+str(uid))
          if int(aql) == int(1):
            bot.delete_message(call.message.chat.id,call.message.message_id)
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('A', callback_data='numb'+str('10')),types.InlineKeyboardButton('B', callback_data='numb'+str('30')))
            markup.add(types.InlineKeyboardButton('C', callback_data='numb'+str('40')),types.InlineKeyboardButton('D', callback_data='numb'+str('20')))
            bot.send_photo(call.message.chat.id,'AgADBAADUa0xGy19eVHNuRX8DEdE__N4jBoABPXn2m_E2OYplYsDAAEC',caption="📍سوال شماره دو:",reply_markup=markup)
            tes = int(tm) + int(num)
            redis.set('aqlt'+str(uid),tes)
            redis.set('aql'+str(uid),2)
          if int(aql) == int(2):
            bot.delete_message(call.message.chat.id,call.message.message_id)
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('A', callback_data='numb'+str('40')),types.InlineKeyboardButton('B', callback_data='numb'+str('20')))
            markup.add(types.InlineKeyboardButton('C', callback_data='numb'+str('10')),types.InlineKeyboardButton('D', callback_data='numb'+str('30')))
            bot.send_photo(call.message.chat.id,'AgADBAADE60xGw0ieVEuxfG9eDSgDxUFkRkABFz9nqsYoemO4FEAAgI',caption="📍سوال شماره سه:",reply_markup=markup)
            tes = int(tm) + int(num)
            redis.set('aqlt'+str(uid),tes)
            redis.set('aql'+str(uid),3)
          if int(aql) == int(3):
            bot.delete_message(call.message.chat.id,call.message.message_id)
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('A', callback_data='numb'+str('10')),types.InlineKeyboardButton('B', callback_data='numb'+str('40')))
            markup.add(types.InlineKeyboardButton('C', callback_data='numb'+str('30')),types.InlineKeyboardButton('D', callback_data='numb'+str('20')))
            bot.send_photo(call.message.chat.id,'AgADBAADFa0xGw0ieVEv90MCFpEsa4VbNBoABAg7in7PvQkAATJaAQABAg',caption="📍سوال شماره چهار:",reply_markup=markup)
            tes = int(tm) + int(num)
            redis.set('aqlt'+str(uid),tes)
            redis.set('aql'+str(uid),4)
          if int(aql) == int(4):
            bot.delete_message(call.message.chat.id,call.message.message_id)
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('A', callback_data='numb'+str('40')),types.InlineKeyboardButton('B', callback_data='numb'+str('30')))
            markup.add(types.InlineKeyboardButton('C', callback_data='numb'+str('20')),types.InlineKeyboardButton('D', callback_data='numb'+str('10')))
            bot.send_photo(call.message.chat.id,'AgADBAADFq0xGw0ieVGosV_s_6KC6aJfKRoABMs4cOnhApNDnGEFAAEC',caption="📍سوال شماره پنج:",reply_markup=markup)
            tes = int(tm) + int(num)
            redis.set('aqlt'+str(uid),tes)
            redis.set('aql'+str(uid),5)
          if int(aql) == int(5):
            bot.delete_message(call.message.chat.id,call.message.message_id)
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('A', callback_data='numb'+str('30')),types.InlineKeyboardButton('B', callback_data='numb'+str('20')))
            markup.add(types.InlineKeyboardButton('C', callback_data='numb'+str('40')),types.InlineKeyboardButton('D', callback_data='numb'+str('10')))
            bot.send_photo(call.message.chat.id,'AgADBAADF60xGw0ieVFe4OU4dmv0ZuhLNBoABPN5IM0GyJQAAXFbAQABAg',caption="📍سوال شماره شش:",reply_markup=markup)
            tes = int(tm) + int(num)
            redis.set('aqlt'+str(uid),tes)
            redis.set('aql'+str(uid),6)
          if int(aql) == int(6):
            bot.delete_message(call.message.chat.id,call.message.message_id)
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('A', callback_data='numb'+str('30')),types.InlineKeyboardButton('B', callback_data='numb'+str('40')))
            markup.add(types.InlineKeyboardButton('C', callback_data='numb'+str('10')),types.InlineKeyboardButton('D', callback_data='numb'+str('20')))
            bot.send_photo(call.message.chat.id,'AgADBAADGK0xGw0ieVF2RzeV64kr49j6jRoABPs0a2VQsvV44oUDAAEC',caption="📍سوال شماره هفت:",reply_markup=markup)
            tes = int(tm) + int(num)
            redis.set('aqlt'+str(uid),tes)
            redis.set('aql'+str(uid),7)
          if int(aql) == int(7):
            bot.delete_message(call.message.chat.id,call.message.message_id)
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('A', callback_data='numb'+str('10')),types.InlineKeyboardButton('B', callback_data='numb'+str('20')))
            markup.add(types.InlineKeyboardButton('C', callback_data='numb'+str('30')),types.InlineKeyboardButton('D', callback_data='numb'+str('40')))
            bot.send_photo(call.message.chat.id,'AgADBAADGa0xGw0ieVFeFxFVwyonsD_gkBkABAQ8xe94xgELvlUAAgI',caption="📍سوال شماره هشت:",reply_markup=markup)
            tes = int(tm) + int(num)
            redis.set('aqlt'+str(uid),tes)
            redis.set('aql'+str(uid),8)
          if int(aql) == int(8):
            bot.delete_message(call.message.chat.id,call.message.message_id)
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('A', callback_data='numb'+str('20')),types.InlineKeyboardButton('B', callback_data='numb'+str('40')))
            markup.add(types.InlineKeyboardButton('C', callback_data='numb'+str('10')),types.InlineKeyboardButton('D', callback_data='numb'+str('30')))
            bot.send_photo(call.message.chat.id,'AgADBAADGq0xGw0ieVGvbstUiPRDyTP6kBkABE8HbdOVzKPPJ1QAAgI',caption="📍سوال شماره نه:",reply_markup=markup)
            tes = int(tm) + int(num)
            redis.set('aqlt'+str(uid),tes)
            redis.set('aql'+str(uid),9)
          if int(aql) == int(9):
            bot.delete_message(call.message.chat.id,call.message.message_id)
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('A', callback_data='numb'+str('40')),types.InlineKeyboardButton('B', callback_data='numb'+str('30')))
            markup.add(types.InlineKeyboardButton('C', callback_data='numb'+str('20')),types.InlineKeyboardButton('D', callback_data='numb'+str('10')))
            bot.send_photo(call.message.chat.id,'AgADBAADG60xGw0ieVHDtWCPINbc5X18iRoABLKntH6mclh26qQDAAEC',caption="📍سوال شماره ده:",reply_markup=markup)
            tes = int(tm) + int(num)
            redis.set('aqlt'+str(uid),tes)
            redis.set('aql'+str(uid),'10')
          if int(aql) == int(10):
            bot.delete_message(call.message.chat.id,call.message.message_id)
            redis.delete('aql'+str(uid))
            t = redis.get('aqlt'+str(uid))
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('📍دریافت نتیجه بر اساس امتیاز📍', callback_data='natije'))
            tt = natije.format(t)
            redis.set('natijeaql'+str(uid),tt)
            redis.delete('aqlt'+str(uid))
            bot.send_message(call.message.chat.id,"برای دریافت نتیجه (سن عقلی شما و توضیحش) روی دکمه زیر کلیک کنید💡",reply_markup=markup)
        if call.data == "natije":
          card = redis.scard('add'+str(uid))
          text = redis.get("natijeaql"+str(uid))
          bot.send_message(call.message.chat.id,text)
        if call.data == "startjaz":
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('الف', callback_data='0numb2'+str('20')),types.InlineKeyboardButton('ب', callback_data='0numb2'+str('30')),types.InlineKeyboardButton('ج', callback_data='0numb2'+str('10')))
            bot.send_photo(call.message.chat.id,'AgADBAAD_asxG-UvgVE5ydocebP0GfRbjxoABKtyKyz4qjFxh4cDAAEC',caption="📍سوال شماره یک:",reply_markup=markup)
        if call.data.startswith('0numb2'):
          num = call.data.replace("0numb2","")
          aql = redis.get('jaz'+str(uid))
          tm = redis.get('jazt'+str(uid))
          if int(aql) == int(1):
            bot.delete_message(call.message.chat.id,call.message.message_id)
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('الف', callback_data='0numb2'+str('20')),types.InlineKeyboardButton('ب', callback_data='0numb2'+str('10')),types.InlineKeyboardButton('ج', callback_data='0numb2'+str('30')))
            bot.send_photo(call.message.chat.id,'AgADBAAD_qsxG-UvgVEqVRIssKB_MoVRJhoABIBIhQFciohUR_EEAAEC',caption="📍سوال شماره دو:",reply_markup=markup)
            tes = int(tm) + int(num)
            redis.set('jazt'+str(uid),tes)
            redis.set('jaz'+str(uid),2)
          if int(aql) == int(2):
            bot.delete_message(call.message.chat.id,call.message.message_id)
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('الف', callback_data='0numb2'+str('20')),types.InlineKeyboardButton('ب', callback_data='0numb2'+str('10')),types.InlineKeyboardButton('ج', callback_data='0numb2'+str('30')))
            bot.send_photo(call.message.chat.id,'AgADBAAD_6sxG-UvgVFodO14vAe-hT9eKRoABFaEwJ_7BuNU5WcFAAEC',caption="📍سوال شماره سه:",reply_markup=markup)
            tes = int(tm) + int(num)
            redis.set('jazt'+str(uid),tes)
            redis.set('jaz'+str(uid),3)
          if int(aql) == int(3):
            bot.delete_message(call.message.chat.id,call.message.message_id)
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('الف', callback_data='0numb2'+str('30')),types.InlineKeyboardButton('ب', callback_data='0numb2'+str('20')),types.InlineKeyboardButton('ج', callback_data='0numb2'+str('10')))
            bot.send_photo(call.message.chat.id,'AgADBAAErDEb5S-BUY6tCO4n1hP3_0wmGgAE9pYtbfotpUgtZwUAAQI',caption="📍سوال شماره چهار:",reply_markup=markup)
            tes = int(tm) + int(num)
            redis.set('jazt'+str(uid),tes)
            redis.set('jaz'+str(uid),4)
          if int(aql) == int(4):
            bot.delete_message(call.message.chat.id,call.message.message_id)
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('الف', callback_data='0numb2'+str('20')),types.InlineKeyboardButton('ب', callback_data='0numb2'+str('10')),types.InlineKeyboardButton('ج', callback_data='0numb2'+str('30')))
            bot.send_photo(call.message.chat.id,'AgADBAADAawxG-UvgVHPmKaBkxwP20kJjhoABNHOzWs-QompH4oDAAEC',caption="📍سوال شماره پنج:",reply_markup=markup)
            tes = int(tm) + int(num)
            redis.set('jazt'+str(uid),tes)
            redis.set('jaz'+str(uid),5)
          if int(aql) == int(5):
            bot.delete_message(call.message.chat.id,call.message.message_id)
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('الف', callback_data='0numb2'+str('30')),types.InlineKeyboardButton('ب', callback_data='0numb2'+str('10')),types.InlineKeyboardButton('ج', callback_data='0numb2'+str('20')))
            bot.send_photo(call.message.chat.id,'AgADBAADAqwxG-UvgVFZ8qoMr_i-zcFIJhoABDVD1v1HomtfU_MEAAEC',caption="📍سوال شماره شش:",reply_markup=markup)
            tes = int(tm) + int(num)
            redis.set('jazt'+str(uid),tes)
            redis.set('jaz'+str(uid),6)
          if int(aql) == int(6):
            bot.delete_message(call.message.chat.id,call.message.message_id)
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('الف', callback_data='0numb2'+str('10')),types.InlineKeyboardButton('ب', callback_data='0numb2'+str('20')),types.InlineKeyboardButton('ج', callback_data='0numb2'+str('30')))
            bot.send_photo(call.message.chat.id,'AgADBAADA6wxG-UvgVGdvBcQomC6QWN5iRoABB4SlhjiC6K0qagDAAEC',caption="📍سوال شماره هفت:",reply_markup=markup)
            tes = int(tm) + int(num)
            redis.set('jazt'+str(uid),tes)
            redis.set('jaz'+str(uid),7)
          if int(aql) == int(7):
            bot.delete_message(call.message.chat.id,call.message.message_id)
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('الف', callback_data='0numb2'+str('20')),types.InlineKeyboardButton('ب', callback_data='0numb2'+str('10')),types.InlineKeyboardButton('ج', callback_data='0numb2'+str('30')))
            bot.send_photo(call.message.chat.id,open("park.jpg"),caption="📍سوال شماره هشت:",reply_markup=markup)
            tes = int(tm) + int(num)
            redis.set('jazt'+str(uid),tes)
            redis.set('jaz'+str(uid),8)
          if int(aql) == int(8):
            bot.delete_message(call.message.chat.id,call.message.message_id)
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('الف', callback_data='0numb2'+str('10')),types.InlineKeyboardButton('ب', callback_data='0numb2'+str('20')),types.InlineKeyboardButton('ج', callback_data='0numb2'+str('30')))
            bot.send_photo(call.message.chat.id,"AgADBAADBqwxG-UvgVGxPncBtvD0GjXbkBkABKstBUzjbCMXXFkAAgI",caption="📍سوال شماره نه:",reply_markup=markup)
            tes = int(tm) + int(num)
            redis.set('jazt'+str(uid),tes)
            redis.set('jaz'+str(uid),9)
          if int(aql) == int(9):
            bot.delete_message(call.message.chat.id,call.message.message_id)
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('الف', callback_data='0numb2'+str('30')),types.InlineKeyboardButton('ب', callback_data='0numb2'+str('10')),types.InlineKeyboardButton('ج', callback_data='0numb2'+str('20')))
            bot.send_photo(call.message.chat.id,'AgADBAADB6wxG-UvgVFNWkjoOREs2KqQjBoABCifI-At4QLCt4oDAAEC',caption="📍سوال شماره ده:",reply_markup=markup)
            tes = int(tm) + int(num)
            redis.set('jazt'+str(uid),tes)
            redis.set('jaz'+str(uid),'10')
          if int(aql) == int(10):
            bot.delete_message(call.message.chat.id,call.message.message_id)
            redis.delete('jaz'+str(uid))
            t = redis.get('jazt'+str(uid))
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('📍دریافت نتیجه بر اساس امتیاز📍', callback_data='natije2'))
            tt = natije2.format(t)
            redis.set('natijejaz'+str(uid),tt)
            redis.delete('jazt'+str(uid))
            bot.send_message(call.message.chat.id,"برای دریافت نتیجه (سن عقلی شما و توضیحش) روی دکمه زیر کلیک کنید💡",reply_markup=markup)
        if call.data == "natije2":
          card = redis.scard('add'+str(uid))
          text = redis.get("natijejaz"+str(uid))
          if int(card) > int(4):
            bot.send_message(call.message.chat.id,text)
          else:
            bot.send_photo(call.message.chat.id,"AgADBAAD8KsxG-UvgVG9gBHm_xGx9GBBNBoABIhNYgABYxEfioZbAQABAg",caption='😎 تست جذابیت\n👾تست دریافت سن عقلی\n😌تست هوش\nدوست داری ببینی عقلت چندسالشه😀؟\nدوست داری بفهمی چقدر جذابیت داری😎؟\n\nt.me/{}?start={}'.format(botu,uid))
            bot.send_message(call.message.chat.id,"""
            همان طور که در قبل از تست گفته شد برای دریافت نتیجه تست ها یک راه وجود دارد. راه حل رایگان معرفی ربات به پنج نفر توسط لینک اختصاصی شما است که در عکس های بالا قرار دارد:

پس از دریافت زیرمجموعه‌ شما میتوانید جواب تست هارا بدون محدودیت دریافت کنید💡
تعداد زیرمجموعه های شما : {}
""".format(card))
      except Exception as e:
          print(e)

@bot.message_handler(content_types=['text', 'sticker', 'photo', 'voice'])
def text(m):
  rank = bot.get_chat_member('@Sianol',m.from_user.id).status
  if str(rank) == 'creator' or str(rank) == 'member' or str(rank) == 'administrator':
      uid = m.from_user.id
      if m.text == "فال حافظ":
                  fl = json.loads(urllib.urlopen("http://hafez.iteam-co.ir/api.php").read())
                  markup = types.InlineKeyboardMarkup()
                  markup.add(types.InlineKeyboardButton("دریافت فایل صوتی🎧", callback_data='fal'+fl['audio']))
                  num = random.randint(1, 99999)
                  redis.set('tabir{}'.format(num),fl['sonnet'][0]['phrase'])
                  markup.add(types.InlineKeyboardButton("دریافت تعبیر🌟", callback_data='tabir'+str(num)))
                  bot.send_photo(m.chat.id, fl['image'],reply_markup=markup,caption="@HoshTestBot")
      if m.text == "سن عقلی من":
        text = """
 شما باید به این ۱۰ سوال صادقانه پاسخ دهید.
 
  آماده اید؟"""
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('👾شروع تست سن عقلی👾', callback_data='startaql'))
        bot.reply_to(m,text,reply_markup=markup)
        redis.set('aql'+str(m.from_user.id),1)
        redis.set('aqlt'+str(m.from_user.id),0)
      if m.text == "تست جذابیت":
        text = """
 شما باید به این ۱۰ سوال صادقانه پاسخ دهید.
 
  آماده اید؟"""
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('😎شروع تست جذابیت😎', callback_data='startjaz'))
        bot.reply_to(m,text,reply_markup=markup)
        redis.set('jaz'+str(m.from_user.id),1)
        redis.set('jazt'+str(m.from_user.id),0)
  else:
    bot.send_message(m.chat.id,chtext,reply_markup=markupch)

  
#End
#By @Mrblack1
bot.polling(True)

