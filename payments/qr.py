# payments/qr.py
import qrcode
from io import BytesIO
import base64

def generate_qr_payment(order):
    """Генерирует QR‑код для оплаты заказа и возвращает base64‑строку."""
    # Строка для QR‑кода — в реальности формируется по регламенту платёжной системы.
    payload = f"PAY://order/{order.id}/amount/{order.total_amount}"  # пример
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(payload)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return {
        'qr_code_base64': img_str,
        'payload': payload
    }
