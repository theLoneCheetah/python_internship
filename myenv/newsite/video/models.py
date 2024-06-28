from django.db import models

# создание модели для базы данных
class RequestLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)   # автоматическое добавление даты и времени
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=255)
    remote_addr = models.CharField(max_length=50, blank=True)
    query_params = models.TextField(blank=True)

    def __str__(self):
        return f"{self.method} {self.path} at {self.timestamp}"
