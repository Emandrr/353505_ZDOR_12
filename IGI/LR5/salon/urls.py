from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.home, name="homepage"),
    re_path(r'^home/?$', views.home, name="homepage"),
    re_path(r'^about/?$', views.about, name="about"),
    re_path(r'^news/$', views.list_of_news, name='news_list'),
    re_path(r'^news/(?P<pk>\d+)/$', views.detailed_news, name='news_detail'),
    re_path(r'^faq/?$', views.list_of_faq, name="faq"),
    re_path(r'^vacancies/?$', views.list_of_vacancies, name="vacancy"),
    re_path(r'^privacy_policy/?$', views.confi_policy, name="confidential"),
    re_path(r'^promocodes/?$', views.list_of_promocodes, name="promo"),
    re_path(r'^register/?$', views.register, name='register'),
    re_path(r'^login/?$', views.login_c, name='login'),
    re_path(r'^logout/?$', views.logout_c, name='logout'),
    re_path(r'^employes/?$', views.list_of_empl, name='employes'),
    re_path(r'^reviews/?$', views.reviews_list, name='reviews_list'),
    re_path(r'^reviews/add/?$', views.add_review, name='add_review'),
    re_path(r'^car_list/?$', views.car_list, name='car_list'),
    re_path(r'^car_list/(?P<pk>\d+)/$', views.car_detail, name='car_view'),
    re_path(r'^car_list/(?P<pk>\d+)/buy_car$', views.car_buy, name='buy_car'),
    re_path(r'^my-cars/?$', views.my_purchased_cars, name='my_purchased_cars'),
    re_path(r'^manage_purchase/(?P<pk>\d+)/?$', views.manage_purchase, name='manage_purchase'),
    re_path(r'^my-clients/', views.my_clients, name='my_clients'),
    re_path(r'^statistics/?', views.car_stats_view, name='car_stats'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
