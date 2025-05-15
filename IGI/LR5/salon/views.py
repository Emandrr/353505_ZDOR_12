from decimal import Decimal
import pandas as pd
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, ReviewForm, CarForm
from .models import AutoCompany, News, FAQ, Vacancy, Promo, CustomUser, Review, Car, Buyer
import logging
import requests
from django.utils import timezone
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
import pytz
import calendar
from django.utils import timezone
from tzlocal import get_localzone
from datetime import datetime
from django.utils.safestring import mark_safe
logger = logging.getLogger(__name__)


def home(request):
    logger.info('Timezone: %s', timezone.get_current_timezone())

    utc_time = timezone.get_default_timezone()
    tz = get_localzone()
    user_time = datetime.now().astimezone(tz)
    utc_time = datetime.utcnow()
    cal = calendar.HTMLCalendar()
    current_month_cal = cal.formatmonth(datetime.utcnow().year, datetime.utcnow().month)
    response = requests.get(
        'https://api.openweathermap.org/data/2.5/weather?',
        params={
            'q': 'Minsk',
            'appid': '972c1f9056037ccde9a28fbc8aa5806c',
            'units': 'metric',
            'lang': 'ru'
        },
        timeout=5
    )
    weather_data = response.json()
    context = {
        'youtube_video_id': 'aUqrexu-d8U',
        'youtube_player_width': '100%',
        'youtube_player_height': '500',
        'youtube_autoplay': 0,
        'youtube_controls': 1,
        'weather': weather_data,
        'user_timezone': tz,
        'utc_timezone': 'UTC',
        'user_now': user_time,
        'utc_now': utc_time,
        'current_month_cal': mark_safe(current_month_cal),
    }
    return render(request, 'salon/index.html', context)


def about(request):
    auto_company = AutoCompany
    return render(request, 'salon/about.html', {'auto_company': auto_company})


def list_of_news(request):
    news_items = News.objects.all()
    return render(request, 'salon/news_list.html', {'news_items': news_items})


def detailed_news(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    return render(request, 'salon/news_detail.html', {'news_item': news_item})


def list_of_faq(request):
    faqs = FAQ.objects.all()
    return render(request, 'salon/faq.html', {'faqs': faqs})


def list_of_vacancies(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'salon/vacancy.html', {'vacancies': vacancies})


def confi_policy(request):
    return render(request, 'salon/confidential.html')


def list_of_promocodes(request):

    active_promocodes = Promo.objects.filter(pub_date_expire__gte=timezone.now())
    expired_promocodes = Promo.objects.filter(pub_date_expire__lt=timezone.now())
    logger.info(active_promocodes)
    return render(request, 'salon/promo.html', {'active_promocodes': active_promocodes,'expired_promocodes': expired_promocodes})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            #login(request, user)
            return redirect('/home')  # Замените на ваш URL
    else:
        form = RegisterForm()
    return render(request, 'salon/register.html', {'form': form})


def login_c(request):
    if request.user.is_authenticated:
        return redirect('/home')  # Перенаправляем если уже авторизован

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Добро пожаловать, {username}!")
                return redirect('/home')
        else:
            messages.error(request, "Неверное имя пользователя или пароль")
    else:
        form = AuthenticationForm()

    return render(request, 'salon/login.html', {'form': form})


def logout_c(request):
    if request.user.is_authenticated:
        messages.info(request, f"До свидания, {request.user.username}! Вы успешно вышли из системы.")
    logout(request)
    return redirect('/home')


def list_of_empl(request):
    empl = CustomUser.objects.all()
    return render(request, 'salon/employes.html', {'empl': empl})


def reviews_list(request):
    reviews = Review.objects.all().select_related('user')
    return render(request, 'salon/reviews_list.html', {'reviews': reviews})


@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('reviews_list')
    else:
        form = ReviewForm()

    return render(request, 'salon/review_add.html', {'form': form})


def car_list(request):
    sort_by = request.GET.get('sort', 'default')

    if sort_by == 'price':
        cars = Car.objects.order_by('price')
    elif sort_by == 'popular':
        cars = Car.objects.order_by('-purchases')
    else:
        cars = Car.objects.all()

    return render(request, 'salon/car_list.html', {'cars': cars, 'sort_by': sort_by})


def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'salon/car_view.html', {'car': car})


@login_required
@user_passes_test(lambda u: not u.is_staff)
def car_buy(request, pk):
    car = get_object_or_404(Car, pk=pk)
    sellers = CustomUser.objects.filter(is_staff=True, is_superuser=False)
    promos = Promo.objects.filter(pub_date_create__lte=timezone.now(), pub_date_expire__gte=timezone.now())
    if request.method == 'POST':
        selected_email = request.POST.get('seller_email')

        promo_id = request.POST.get('promo_code')
        buyer = Buyer.objects.create(user=request.user)
        buyer.email_admin = selected_email
        buyer.favorite_cars.add(car)
        buyer.real_value = car.price
        buyer.save()
        promo = None
        print(buyer)
        if promo_id:
            try:
                promo = Promo.objects.get(pk=promo_id)
                print(promo)
            except Promo.DoesNotExist:
                promo = None
                print(0)
        #car.purchases += 1
        if promo:
            discount = car.price * (Decimal(promo.discount_value) / Decimal('100'))
            final_price = car.price - discount
            buyer.real_value = final_price
            buyer.save()
        else:
            final_price = car.price

        car.save()
        car.purchases += 1
        car.save()

        messages.success(request, 'Поздравляем с успешной покупкой!')
        return redirect('/car_list')

    return render(request, 'salon/buy_car.html', {'car': car, 'sellers': sellers, 'promos': promos})


@login_required
@user_passes_test(lambda u: not u.is_staff)
def my_purchased_cars(request):
    buyers = Buyer.objects.filter(user=request.user)
    cars_with_prices = [(buyer.favorite_cars.first(), buyer.real_value) for buyer in buyers if buyer.favorite_cars.exists()]

    return render(request, 'salon/purchased_cars.html', {
        'cars_with_prices': cars_with_prices,
    })


@login_required
@user_passes_test(lambda u: not u.is_staff)
def manage_purchase(request, pk):
    car = get_object_or_404(Car, pk=pk)
    buyers = Buyer.objects.filter(user=request.user, favorite_cars=car)

    if not buyers.exists():
        return redirect('my_purchased_cars')  # защита от доступа к чужим записям

    buyer = buyers.first()

    staff_users = CustomUser.objects.filter(is_staff=True, is_superuser=False)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'change_staff':
            selected_email = request.POST.get('staff_email')
            buyer.email_admin = selected_email
            buyer.save()
            return redirect('my_purchased_cars')
        elif action == 'delete_car':
            buyer.favorite_cars.remove(car)
            car.purchases -= 1
            car.save()
            return redirect('my_purchased_cars')

    return render(request, 'salon/manage_purchase.html', {
        'car': car,
        'buyer': buyer,
        'staff_users': staff_users,
        'current_email': buyer.email_admin,
    })


@login_required
@user_passes_test(lambda u: u.is_staff)
def my_clients(request):
    buyers = Buyer.objects.filter(email_admin=request.user.email).filter(favorite_cars__isnull=False).distinct()
    return render(request, 'salon/my_clients.html', {'buyers': buyers})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def car_stats_view(request):
    cars = Car.objects.all().values()
    buyers = Buyer.objects.prefetch_related('favorite_cars').all()


    managers = {
        user.email: user.get_full_name() or user.username
        for user in CustomUser.objects.filter(is_staff=True)
    }

    car_df = pd.DataFrame(cars)
    buyer_data = []

    for buyer in buyers:
        manager_name = managers.get(buyer.email_admin, buyer.email_admin)
        for car in buyer.favorite_cars.all():
            buyer_data.append({
                'manager': manager_name,
                'car': f"{car.make} {car.model}",
                'price': float(car.price),
                'purchases': car.purchases,
                'mileage': car.mileage
            })

    buyer_df = pd.DataFrame(buyer_data)

    popularity = car_df.groupby(['make', 'model'])['purchases'].sum().sort_values(ascending=False)
    popular_labels = [f"{make} {model}" for make, model in popularity.index]
    popular_values = popularity.values.tolist()

    expensive = car_df.sort_values(by='price', ascending=False)
    expensive_labels = expensive['model'].tolist()
    expensive_prices = expensive['price'].astype(float).tolist()

    corr_df = car_df[['price', 'purchases']].dropna()
    correlation_data = [{'x': float(price), 'y': int(purchase)} for price, purchase in zip(corr_df['price'], corr_df['purchases'])]

    year_count = car_df.groupby('year').size()
    year_labels = year_count.index.tolist()
    year_values = year_count.values.tolist()

    mileage_data = car_df[['mileage', 'purchases']].dropna()
    mileage_scatter = [{'x': int(mileage), 'y': int(purchases)} for mileage, purchases in zip(mileage_data['mileage'], mileage_data['purchases'])]

    manager_sales = buyer_df.groupby('manager')['purchases'].sum().sort_values(ascending=False)
    top_manager = manager_sales.idxmax() if not manager_sales.empty else "Нет данных"
    top_manager_sales = manager_sales.max() if not manager_sales.empty else 0
    manager_labels = manager_sales.index.tolist()
    manager_values = manager_sales.values.tolist()

    context = {
        'popular_labels': popular_labels,
        'popular_values': popular_values,
        'expensive_labels': expensive_labels,
        'expensive_prices': expensive_prices,
        'correlation_data': correlation_data,
        'year_labels': year_labels,
        'year_values': year_values,
        'mileage_data': mileage_scatter,
        'manager_labels': manager_labels,
        'manager_values': manager_values,
        'top_manager': top_manager,
        'top_manager_sales': top_manager_sales,
    }

    return render(request, 'salon/car_stats.html', context)

