from django.contrib import admin
from .models import Game, Buyer

# Админ-класс для модели Game
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size')  # Отображаемые поля в списке
    list_filter = ('size', 'cost')  # Фильтрация по полям size и cost
    search_fields = ('title',)  # Поиск по полю title
    list_per_page = 20  # Ограничение количества записей на странице

# Админ-класс для модели Buyer
@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')  # Отображаемые поля в списке
    list_filter = ('balance', 'age')  # Фильтрация по полям balance и age
    search_fields = ('name',)  # Поиск по полю name
    list_per_page = 30  # Ограничение количества записей на странице
    readonly_fields = ('balance',)  # Поле balance доступно только для чтения