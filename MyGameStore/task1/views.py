import os
from django.shortcuts import render
from .models import Buyer, Game
from decimal import Decimal


def platform(request):
    return render(request, 'task1/platform.html')


def games(request):
    games = Game.objects.all()
    return render(request, 'task1/games.html', {'games': games})


def cart(request):
    return render(request, 'task1/cart.html')


def register(request):
    error = ''
    message = ''

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        # Проверка существования пользователя
        existing_buyer = Buyer.objects.filter(name=username).exists()

        if existing_buyer:
            error = 'Пользователь с таким именем уже существует'
        elif password != repeat_password:
            error = 'Пароли не совпадают'
        elif len(password) < 8:
            error = 'Пароль должен содержать не менее 8 символов'
        else:
            # Создание нового покупателя
            Buyer.objects.create(
                name=username,
                balance=Decimal('0.00'),  # Начальный баланс
                age=int(age)
            )
            message = 'Регистрация успешно завершена!'

    return render(request, 'task1/registration_page.html', {
        'error': error,
        'message': message
    })