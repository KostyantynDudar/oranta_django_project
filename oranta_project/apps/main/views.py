from django.shortcuts import render, get_object_or_404
from apps.main.models import Article

def home_view(request):
    return render(request, "main/home.html")

def contact_view(request):
    return render(request, "main/contacts.html")

def submit_insurance_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        insurance_type = request.POST.get('insurance_type')
        message = request.POST.get('message')
        documents = request.FILES.getlist('documents')

        # Логика сохранения данных
        # Отправка уведомления на почту
        send_mail(
            f'Нова заявка на страхування: {insurance_type}',
            f'Ім’я: {name}\nЕлектронна пошта: {email}\nТелефон: {phone}\nТип страхування: {insurance_type}\nПовідомлення: {message}',
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
        )

        return HttpResponse('Дякуємо за вашу заявку! Ми зв’яжемося з вами найближчим часом.')

    return redirect('home')