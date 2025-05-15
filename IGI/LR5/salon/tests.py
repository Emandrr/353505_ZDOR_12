from decimal import Decimal

from django.test import TestCase, Client
from django.urls import reverse
from .models import *
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import News, FAQ, Vacancy, Promo


class CarStatsViewTests(TestCase):
    def setUp(self):
        self.client = Client()

        self.staff_user = CustomUser.objects.create_user(
            username='staffuser', email='staff@example.com', password='pass123', is_staff=True
        )

        self.car = Car.objects.create(
            make='Toyota', model='Camry', price=20000, purchases=5, mileage=50000, year=2021
        )

        self.buyer = CustomUser.objects.create_user(
            username='buyeruser', email='buyer@example.com', password='pass123', is_staff=False
        )
        self.buyer_entry = Buyer.objects.create(user=self.buyer, email_admin=self.staff_user.email, real_value=self.car.price)
        self.buyer_entry.favorite_cars.add(self.car)
        self.buyer_entry.save()

    def test_car_stats_view_staff_access(self):
        self.client.login(username='staffuser', password='pass123')
        response = self.client.get(reverse('car_stats'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'salon/car_stats.html')
        # Дополнительно проверим, что в контексте есть популярные метки, топ-менеджер и т.п.
        self.assertIn('popular_labels', response.context)
        self.assertIn('top_manager', response.context)
        self.assertEqual(response.context['top_manager'], self.staff_user.get_full_name() or self.staff_user.username)




class SimpleViewTests(TestCase):

    def test_list_of_news_view(self):
        news_item = News.objects.create(title='Test News', full_content='Test content')
        url = reverse('news_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, news_item.title)

    def test_detailed_news_view(self):
        news_item = News.objects.create(title='Detail News', full_content='Detail content')
        url = reverse('news_detail', args=[news_item.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, news_item.title)

    def test_list_of_faq_view(self):
        faq_item = FAQ.objects.create(
            title='Test?',
            full_content_question='Question text',
            full_content_answer='Answer text'
        )
        url = reverse('faq')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, faq_item.title)

    def test_list_of_vacancies_view(self):
        vacancy = Vacancy.objects.create(title='Vacancy 1', full_content='Desc')
        url = reverse('vacancy')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, vacancy.title)

    def test_list_of_promocodes_view(self):
        now = timezone.now()
        promo = Promo.objects.create(
            title='Promo 1',
            full_content='Promo description',
            discount_value=10.5,
            pub_date_create=now,
            pub_date_expire=now + timezone.timedelta(days=1)
        )
        url = reverse('promo')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, promo.title)

    def test_confidential_policy_view(self):
        url = reverse('confidential')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)




User = CustomUser

class UserFlowTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user_password = 'testpassword123'
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password=self.user_password
        )
        self.staff_user = CustomUser.objects.create_user(
            username='testuser1',
            email='testusse1r@example.com',
            password=self.user_password
        )
        self.car = Car.objects.create(
        make='TestMake',
        model='TestModel',
        year=2020,
        price=Decimal('10000.00'),
        mileage=50000,
        purchases=0
        )
        self.promo = Promo.objects.create(
            title='Promo1',
            full_content='Promo content',
            discount_value=10,
            pub_date_create=timezone.now(),
            pub_date_expire=timezone.now() + timezone.timedelta(days=1)
        )

    def test_register_view_get(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)

    def test_login_logout_flow(self):

        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)

        response = self.client.post(reverse('login'), {'username': self.user.username, 'password': self.user_password})
        self.assertRedirects(response, '/home')

        self.client.login(username=self.user.username, password=self.user_password)
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, '/home')

    def test_list_of_empl_view(self):
        self.client.login(username=self.user.username, password=self.user_password)
        response = self.client.get(reverse('employes'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.user, response.context['empl'])

    def test_add_review_view_get(self):
        self.client.login(username=self.user.username, password=self.user_password)
        response = self.client.get(reverse('add_review'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)

    def test_car_list_view(self):
        response = self.client.get(reverse('car_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.car, response.context['cars'])

    def test_car_detail_view(self):
        response = self.client.get(reverse('car_view', args=[self.car.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['car'], self.car)

    def test_car_buy_view_get(self):
        self.client.login(username=self.user.username, password=self.user_password)
        response = self.client.get(reverse('buy_car', args=[self.car.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertIn('car', response.context)
        self.assertIn('sellers', response.context)
        self.assertIn('promos', response.context)

    def test_car_buy_view_post_with_promo(self):
        self.client.login(username=self.user.username, password=self.user_password)
        sellers = User.objects.filter(is_staff=True, is_superuser=False)
        seller_email = sellers.first().email if sellers.exists() else ''
        response = self.client.post(reverse('buy_car', args=[self.car.pk]), {
            'seller_email': seller_email,
            'promo_code': self.promo.pk
        })
        self.assertRedirects(response, '/car_list')
        buyer = Buyer.objects.filter(user=self.user).last()
        self.assertIsNotNone(buyer)
        expected_price = self.car.price * (Decimal('1.0') - Decimal(self.promo.discount_value) / Decimal('100'))
        self.assertEqual(buyer.real_value, expected_price.quantize(Decimal('0.01')))

    def test_my_purchased_cars_view(self):
        self.client.login(username=self.user.username, password=self.user_password)
        buyer = Buyer.objects.create(user=self.user, real_value=Decimal('9000.00'))
        buyer.favorite_cars.add(self.car)
        response = self.client.get(reverse('my_purchased_cars'))
        self.assertEqual(response.status_code, 200)
        self.assertIn((self.car, buyer.real_value), response.context['cars_with_prices'])



