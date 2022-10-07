from django.db import models


class Message(models.Model):
    name = models.CharField("Имя отправителя", max_length=20)  # max_length - максимальная длина текста
    message = models.TextField("Текст сообщений")

    def __str__(self):
        return str(self.name) + " " + str(self.message)

    class Meta:  # для руссификации в админке
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ['-id']  # для возможности отрицательной индексации
