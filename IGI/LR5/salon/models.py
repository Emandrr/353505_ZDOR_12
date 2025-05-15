from django.db import models
from django.contrib.auth.models import AbstractUser, User, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    birth_date = models.DateField(null=True, verbose_name='Дата рождения')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(unique=True)
    additional_info = models.CharField(max_length=300, verbose_name='Доп информация', default="")
    image = models.ImageField(upload_to='user_images/', default="")
    selected_amount = models.IntegerField(default=0)
    selled_amount = models.IntegerField(default=0)
    objects = CustomUserManager()
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')


    def __str__(self):
        return self.username


class AutoCompany(models.Model):
    name = models.CharField(max_length=50, default="Premium Cars Minsk")
    description = models.TextField(default="This is a company witch can help you buy supercar. "
                                           "10 Years We are selling the best cars for best clients.")

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200, default="Title")
    short_content = models.CharField(max_length=300, default="Short description")
    full_content = models.TextField(verbose_name="Full text")
    image = models.ImageField(upload_to='news_images/', default="")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Publication date")

    def __str__(self):
        return self.title


class FAQ(models.Model):
    title = models.CharField(max_length=200, default="Title")
    full_content_question = models.TextField(verbose_name="Full text")
    full_content_answer = models.TextField(verbose_name="Full text")
    ans_date = models.DateTimeField(auto_now_add=True, verbose_name="Publication date")

    def __str__(self):
        return self.title


class Vacancy(models.Model):
    title = models.CharField(max_length=200, default="Title")
    short_content = models.CharField(max_length=300, default="Short description")
    full_content = models.TextField(verbose_name="Full text")


class Promo(models.Model):
    title = models.CharField(max_length=200, default="Title")
    full_content = models.TextField(verbose_name="Full text")
    discount_value = models.FloatField(default=0)
    pub_date_create = models.DateTimeField(verbose_name="Publication date")
    pub_date_expire = models.DateTimeField(verbose_name="Expired date")


class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 - Ужасно'),
        (2, '2 - Плохо'),
        (3, '3 - Удовлетворительно'),
        (4, '4 - Хорошо'),
        (5, '5 - Отлично'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    rating = models.IntegerField(choices=RATING_CHOICES, verbose_name='Оценка')
    text = models.TextField(verbose_name='Текст отзыва')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']

    def __str__(self):
        return f'Отзыв от {self.user.username} ({self.rating}/5)'


class Car(models.Model):
    make = models.CharField("Марка", max_length=100)
    model = models.CharField("Модель", max_length=100)
    year = models.PositiveIntegerField("Год выпуска")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    description = models.TextField("Описание", blank=True)
    mileage = models.PositiveIntegerField("Пробег (км)")
    purchases = models.PositiveIntegerField("Количество покупок", default=0)
    photo = models.ImageField("Фото", upload_to='car_photos/', blank=True, null=True)

    def __str__(self):
        return f'{self.make} {self.model} ({self.year})'


class Buyer(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    favorite_cars = models.ManyToManyField(
        Car,
        related_name='interested_buyers',
        verbose_name='Избранные автомобили',
    )
    real_value = models.IntegerField(default="0")
    email_admin = models.EmailField()


