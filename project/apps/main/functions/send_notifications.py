import requests

from django.core.mail import EmailMessage

from settings import TG_TOKEN, TG_CHAT_ID, TG_API_URL

# from apps.main.models import Email


def send_tg_notification(message=''):
	requests.get('{}/bot{}/sendMessage?chat_id={}&text={}'.format(TG_API_URL, TG_TOKEN, TG_CHAT_ID, message))


def send_email_notification(message=''):
	emails = []

	# for item in Email.active_objects.all():
	# 	emails.append(item.email)

	msg = EmailMessage('Новая заявка!', message, to=emails)
	msg.send()
