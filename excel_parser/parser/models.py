from django.db import models


class Data(models.Model):
    DATATYPES = (
        ("0", "fact"),
        ("1", "forecast")
    )
    company_id = models.IntegerField(null=False, blank=False, verbose_name="ID компании")
    company_name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Наименование компании")
    date = models.DateField(null=False, blank=False, verbose_name="Дата")
    qliq = models.IntegerField(null=False, blank=False, verbose_name="Qliq")
    qoil = models.IntegerField(null=False, blank=False, verbose_name="Qoil")
    data_type = models.CharField(max_length=10, choices=DATATYPES, null=False, blank=False, verbose_name="Тип данных")

    class Meta:
        ordering = ["id"]
        unique_together = ["company_id", "date", "data_type"]

    def __str__(self):
        return f"Строка данных компании {self.company_name} №{self.id}"
