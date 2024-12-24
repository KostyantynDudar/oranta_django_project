from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from .models import Article, InsuranceApplication
from .telegram_bot import send_to_telegram  # Импорт функции для отправки в Telegram

# Файл: /home/oranta_django_project/oranta_project/apps/main/views.py

def home_view(request):
    return render(request, "main/home.html")

def contact_view(request):
    return render(request, "main/contacts.html")

def submit_insurance_form(request):
    if request.method == 'POST':
        try:
            # Извлечение данных из формы
            phone_number = request.POST.get('phone')
            tax_code = request.POST.get('tax_code')
            registration_address = request.POST.get('registration_address')
            deductible = request.POST.get('deductible')
            tech_passport = request.FILES.get('tech_passport')
            personal_docs = request.FILES.get('personal_docs')

            # Создание новой записи в базе данных
            application = InsuranceApplication(
                phone_number=phone_number,
                tax_code=tax_code,
                registration_address=registration_address,
                deductible=deductible,
                tech_passport=tech_passport,
                personal_docs=personal_docs,
            )
            application.save()

            # Формирование сообщения для Telegram
            message = (
                f"<b>Новая заявка</b>\n\n"
                f"<b>Код:</b> {application.unique_code}\n"
                f"<b>Телефон:</b> {application.phone_number}\n"
                f"<b>Адрес:</b> {application.registration_address}\n"
                f"<b>Франшиза:</b> {application.deductible}"
            )

            # Отправка в Telegram
            send_to_telegram(message)

            # Добавляем сообщение об успешной отправке
            messages.success(request, "Ваша заявка успешно отправлена! Мы свяжемся с вами в ближайшее время.")

            # Перенаправление после успешного сохранения
            return redirect('home')

        except Exception as e:
            # Обработка ошибок
            messages.error(request, f"Ошибка при обработке заявки: {e}")
            return render(request, 'main/home.html')

    return render(request, 'main/home.html')
