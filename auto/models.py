from django.db import models


class Car(models.Model):
    car_brand = models.CharField(max_length=255,
                                 verbose_name="Марка авто")
    model = models.CharField(max_length=255,
                             verbose_name="Модель авто")
    year_of_issue = models.IntegerField(verbose_name="Год выпуска")
    gear_box = models.SmallIntegerField(choices=[(1, 'МКПП'), (2, 'АКПП'), (3, 'Робот')],
                                        verbose_name="Тип КПП")
    color = models.CharField(max_length=255,
                             verbose_name="Цвет кузова")

    def __str__(self):
        return f'{self.car_brand} {self.model}'

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"
