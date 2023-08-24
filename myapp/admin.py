from django.contrib import admin
from .models import UserProfile

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
# Crea una clase de administración para UserProfile
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'bio')  # Campos a mostrar en la lista de usuarios
    list_filter = ('age',)  # Opciones de filtro
    search_fields = ('user__username', 'age', 'bio')  # Campos de búsqueda

# Asegúrate de registrar la administración personalizada en tu modelo UserProfile
