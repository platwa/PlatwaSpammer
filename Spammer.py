import ssl
import smtplib
import time as tm
from colorama import Fore, init, Style
from datetime import datetime, date, time

init()

print(Fore.YELLOW+"GmailSpammer by PLATWA сделано с любовью"+'\n'+Fore.WHITE)

logins = {
	'1':'Bot2Python@gmail.com',
	'2':'Bot3Python@gmail.com',
	'3':'Bot4Python@gmail.com',
	'4':'Bot5Python@gmail.com',
	'5':'Bot6Python@gmail.com',
	'6':'Bot7Python@gmail.com',
	'7':'Bot8Python@gmail.com',
	'8':'Bot9Python@gmail.com',
	'9':'Bot10Python@gmail.com',
	'10':'Bot11Python@gmail.com',
	'11':'Bot12Python@gmail.com',
	'12':'Bot13Python@gmail.com',
	'13':'Bot14Python@gmail.com',
	'14':'Bot15Python@gmail.com',
	'15':'Bot16Python@gmail.com',
	'16':'Bot17Python@gmail.com',
	'17':'Bot18Python@gmail.com',
	'18':'Bot19Python@gmail.com',
	'19':'Bot20Python@gmail.com',
	'20':'Bot21Python@gmail.com',
}
context = ssl.create_default_context()
debug = 1
port = 465  # для SSL подключения
smtp_server = "smtp.gmail.com"
def acc():
	global sender_email
	global password
	sender_email = input("Введите gmail Бота. Введите число от 1 до 20 (работают не все), чтобы использовать стандартных ботов: ")
	password = 'te155735'
	if sender_email == '1' or sender_email == '2' or sender_email == '3' or sender_email == '4' or sender_email == '5' or sender_email == '6' or sender_email == '7' or sender_email == '8' or sender_email == '9' or sender_email == '10' or sender_email == '11' or sender_email == '12' or sender_email == '13' or sender_email == '14' or sender_email == '15' or sender_email == '16' or sender_email == '17' or sender_email == '18' or sender_email == '19' or sender_email == '20':
		sender_email = logins[sender_email]
	else:
		password = input("Введите пароль вашего бота: ")
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