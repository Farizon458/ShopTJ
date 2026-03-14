# payments/__init__.py
from .p2p import process_p2p_payment
from .telegram import process_telegram_payment
from .qr import generate_qr_payment

def handle_payment(order: Order):
    if order.payment_method == PaymentMethod.P2P:
        return process_p2p_payment(order)
    elif order.payment_method == PaymentMethod.TELEGRAM:
        return process_telegram_payment(order)
    elif order.payment_method == PaymentMethod.SBP_QR:
        return generate_qr_payment(order)
    else:
        raise ValueError("Unsupported payment method")
