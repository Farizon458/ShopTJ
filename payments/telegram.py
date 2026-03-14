# payments/telegram.py
from django.utils import timezone
import requests

def process_telegram_payment(order):
    """
    Отправляет администратору уведомление о заказе через Telegram‑бот.
    Администратор вручную подтверждает получение денег; бот отмечает заказ как оплачен.
    """
    # отправить сообщение через Telegram Bot API
    BOT_TOKEN = 'Ваш токен бота'
    ADMIN_CHAT_ID = 'id администратора'
    message = f"Новый заказ №{order.id} на сумму {order.total_amount} сомони. "\
              f"Платежный метод: оплата администратору. Подтвердите оплату."
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    params = {"chat_id": ADMIN_CHAT_ID, "text": message}
    requests.get(url, params=params)
    # возвращаем ссылку на заказ для фронтенда (можно показать пользователю статус)
    return {
        'status': 'waiting',
        'message': 'Ваш заказ ожидает подтверждения администратором.\n' \
                   'Мы свяжемся с вами после проверки.'
    }

# В другом месте нужно реализовать обработчик веб‑хука Telegram, который 
# отмечает платеж подтвержденным, когда администратор нажимает кнопку.
