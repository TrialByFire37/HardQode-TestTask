from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models

from courses.models import Course, Group


class CustomUser(AbstractUser):
    """Кастомная модель пользователя - студента."""

    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        max_length=250,
        unique=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = (
        'username',
        'first_name',
        'last_name',
        'password'
    )
    group_id = models.ForeignKey(
        Group,
        null=True,
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-id',)

    def __str__(self):
        return self.get_full_name()


class Balance(models.Model):
    """Модель баланса пользователя."""

    amount = models.IntegerField(
        default=1000,
        verbose_name='Счёт',
        validators=[MinValueValidator]
    )
    customuser_id = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Баланс'
        verbose_name_plural = 'Балансы'
        ordering = ('-id',)


class Subscription(models.Model):
    """Модель подписки пользователя на курс."""

    customuser_id = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE
    )
    course_id = models.OneToOneField(
        Course,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        ordering = ('-id',)

