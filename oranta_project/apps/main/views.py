
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import InsuranceApplication, UploadedFile
from .forms import InsuranceApplicationForm
from .telegram_bot import send_to_telegram

# Файл: /home/oranta_django_project/oranta_project/apps/main/views.py

def home_view(request):
    return render(request, "main/home.html")

def contact_view(request):
    return render(request, "main/contacts.html")


def submit_insurance_form(request):
    if request.method == 'POST':
        form = InsuranceApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save()

            # Сохраняем техпаспорта
            for file in request.FILES.getlist('tech_passports'):
                UploadedFile.objects.create(file=file, application=application)

            # Сохраняем личные документы
            for file in request.FILES.getlist('personal_docs'):
                UploadedFile.objects.create(file=file, application=application)

            # Уведомление в Telegram
            message = (
                f"<b>Новая заявка</b>\n\n"
                f"<b>Код:</b> {application.unique_code}\n"
                f"<b>Телефон:</b> {application.phone_number}\n"
                f"<b>Адрес:</b> {application.registration_address}\n"
                f"<b>Франшиза:</b> {application.deductible}"
            )
            send_to_telegram(message)

            messages.success(request, "Ваша заявка успешно отправлена!")
            return redirect('home')
        else:
            messages.error(request, "Ошибка при отправке заявки!")
    else:
        form = InsuranceApplicationForm()

    return render(request, 'main/home.html', {'form': form})


