from django.shortcuts import render

# Главная страница
def platform_view(request):
    return render(request, 'fourth_task/platform.html')

# Страница Магазин
def games_view(request):
    # Передаем список игр через контекст
    context = {
        'games': ['Atomic Heart', 'Cyberpunk 2077', 'The Witcher 3']
    }
    return render(request, 'fourth_task/games.html', context)

# Страница Корзина
def cart_view(request):
    return render(request, 'fourth_task/cart.html')
