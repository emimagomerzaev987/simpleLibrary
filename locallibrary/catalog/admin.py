from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

# Inline для BookInstance внутри Book
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0  # сколько пустых форм будет отображаться
    # ❗ list_filter и fieldsets не работают в Inline-классах
    # Они используются только в admin.ModelAdmin
    # Можно оставить только fields
    fields = ('id','status', 'due_back', 'imprint')  # 'book' и 'id' не нужны, т.к. задаются автоматически

# Кастомизация отображения Author
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# Кастомизация отображения Book с Inline-экземплярами
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

# Кастомизация BookInstance в админке
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('book', 'status', 'due_back', 'id')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

# Регистрация моделей
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Genre)
# BookInstance уже зарегистрирован через декоратор
