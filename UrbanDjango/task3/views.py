from django.shortcuts import render

# Главная страница
def platform_view(request):
    return render(request, 'third_task/platform.html')

# Магазин
def games_view(request):
    games = {
        'Игра 1': '500 ₽',
        'Игра 2': '1000 ₽',
        'Игра 3': '1500 ₽',
    }
    return render(request, 'third_task/games.html', {'games': games})

# Корзина
def cart_view(request):
    return render(request, 'third_task/cart.html')
