from django.core.mail import send_mail

def send_activation_code(email, activation_code):
    message = f"""
    Congratilation Вы зарегестрированы на нашем сайте. Пройдите активацию ващего аккаунта отправив нам код: {activation_code}"""

    send_mail(
        'Активация аккаунта',
        message,
        'test@gmail.com',
        [email]
    )