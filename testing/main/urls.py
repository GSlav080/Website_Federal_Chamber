from django.urls import path
from .views import *

# Отслеживаем переходы
urlpatterns = [
    path('', index, name='home'),
    path('register_right', register_right, name='register_right'),
    path('about', about_us, name='about'),
    path('contacts', contacts, name='contacts'),
    path('doing', doing, name='doing'),
    path('register', RegisterFormView.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', LogoutUser, name='logout'),
    path('mytask', MyTask, name='mytask'),

    path('form2', form2_v, name='form2'),
    path('form3', form3_v, name='form3'),
    path('form4', form4_v, name='form4'),
    path('form5', form5_v, name='form5'),
    path('form6', form6_v, name='form6'),
    path('update/<int:pk>', Update, name='update'),
    path('update2/<int:pk>', Update2, name='update2'),
    path('update3/<int:pk>', Update3, name='update3'),
    path('update4/<int:pk>', Update4, name='update4'),
    path('update5/<int:pk>', Update5, name='update5'),
    path('update6/<int:pk>', Update6, name='update6'),
    path('delit1/<int:pk>', DELIT1, name='delit1'),
    path('delit2/<int:pk>', DELIT2, name='delit2'),
    path('delit3/<int:pk>', DELIT3, name='delit3'),
    path('delit4/<int:pk>', DELIT4, name='delit4'),
    path('delit5/<int:pk>', DELIT5, name='delit5'),
    path('delit6/<int:pk>', DELIT6, name='delit6'),


    path('mytask', MyTask, name='mytask'),

]
