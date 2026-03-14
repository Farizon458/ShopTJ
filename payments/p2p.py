# payments/p2p.py
import uuid
from django.utils import timezone

def process_p2p_payment(order):
    """
    Заглушка для P2P перевода. В реальном проекте здесь будет интеграция с API банка
    или платёжного агрегатора (например, Payme или Click).

    Алгоритм:
    1. Создать уникальный идентификатор транзакции.
    2. Отправить запрос в API банка с реквизитами получателя и суммой.
    3. Получить статус перевода и сохранить его в объекте `Payment`.
    4. Обновить статус заказа в зависимости от ответа.
    """
    tx_id = str(uuid.uuid4())  # уникальный идентификатор
    # вызов API банка (псевдокод)
    # response = bank_api.transfer(from_card=..., to_card=..., amount=order.total_amount)
    success = True  # предположим, что ответ успешный
    payment = order.payment
    payment.transaction_id = tx_id
    payment.is_confirmed = success
    payment.confirmed_at = timezone.now() if success else None
    payment.save()
    if success:
        order.status = OrderStatus.PAID
        order.save()
    return success
