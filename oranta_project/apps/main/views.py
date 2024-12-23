from django.shortcuts import render, get_object_or_404
from apps.main.models import Article

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import InsuranceApplication
from django.contrib import messages

def home_view(request):
    return render(request, "main/home.html")

def contact_view(request):
    return render(request, "main/contacts.html")
# Файл: /home/oranta_django_project/oranta_project/apps/main/views.py


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

            # Добавляем сообщение об успешной отправке
            messages.success(request, "Ваша заявка успешно отправлена! Мы свяжемся с вами в ближайшее время.")

            # Перенаправление после успешного сохранения
            return redirect('home')

        except Exception as e:
            # Обработка ошибок
            messages.error(request, f"Ошибка при обработке заявки: {e}")
            return render(request, 'main/home.html')

    return render(request, 'main/home.html')
