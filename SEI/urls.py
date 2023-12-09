from django.urls import path
from app_cad_produto import views

urlpatterns = [
    # Cria Rota, views responsave, nome de referncia
    path('',views.home, name='home'),
    path('historico/',views.produto, name='historico')
]
