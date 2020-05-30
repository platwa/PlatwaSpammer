import ssl
import smtplib
import time as tm
from colorama import Fore, init, Style
from datetime import datetime, date, time

init()

print(Fore.YELLOW+"GmailSpammer by PLATWA сделано с любовью"+'\n'+Fore.WHITE)

context = ssl.create_default_context()
debug = 1
port = 465  # для SSL подключения
smtp_server = "smtp.gmail.com"
def acc():
	global sender_email
	global password
	sender_email = input("Введите gmail Бота. Оставьте поле пустым, чтобы использовать [Bot2Python@gmail.com]: ")
	if sender_email == '':
		sender_email = "Bot2Python@gmail.com"  # Ваш емайл
	password = input("Введите пароль Бота. Оставьте поле пустым, чтобы использовать пароль для [Bot2Python@gmail.com]: ")
	if password == '':
		password = 'te155735'
	try:
		print('\n'+Fore.BLACK+Style.BRIGHT+"Пробное подключение..."+Fore.WHITE+Style.DIM)
		with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
			server.login(sender_email, password)
		print(Fore.GREEN+"[V] Вход в аккаунт произошел успешно!"+Fore.WHITE)
	except:
		print(Fore.RED+"[X] Не удалось ввойти в аккаунт! Если логин и пароль правильный, тогда откройте доступ для небезопасных приложений в настройках аккаунта"+Fore.WHITE)
		acc()
acc()


receiver_email = input("Введите gmail получателя: ")  # Емайл получателя
msg = input("Введите текст сообщения: ")
while True:
	try:
		count = int(input("Введите кол-во сообщений: "))
		if count >=1 or debug == 1:
			break
		else:
			print(Fore.RED + "ОШИБКА! Введите число больше нуля" + Fore.WHITE)
	except ValueError:
		print(Fore.RED+'Неверный формат.'+Fore.WHITE)
while True:
	try:
		delay = float(input("Введите задержку. Например: 1.5: "))
		if delay >= 0 or debug == 1:
			break
		else:
			print(Fore.RED + "ОШИБКА! Введите положительное число" + Fore.WHITE)
	except ValueError:
		print(Fore.RED+'Неверный формат.'+Fore.WHITE)
a = 0
def func():
	global a
	while a == 0:
		try:
			print('\n'+Fore.BLACK+Style.BRIGHT+"Подключение..."+Fore.WHITE+Style.DIM)
			with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
				server.login(sender_email, password)
			print(Fore.GREEN+"[V] Вход в аккаунт произошел успешно!"+Fore.WHITE)
			a = 1
			break
		except:
			print(Fore.RED+"[X] Не удалось ввойти в аккаунт! "+Fore.WHITE)
			tm.sleep(1)
	try:
		with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
			server.login(sender_email, password)
			server.sendmail(sender_email, receiver_email, msg)
			print(Fore.GREEN+str(datetime.now())[11:-3]+" [V] Запрос на сообщение отправлен."+Fore.WHITE)
	except:
		print(Fore.RED+str(datetime.now())[11:-3]+" [X] Не удалось отправить запрос."+Fore.WHITE)
while True:
	func()
	tm.sleep(delay)
	count -= 1
	if count == 0:
		break