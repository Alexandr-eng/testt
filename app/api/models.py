from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=255)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Visit(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    visit_time = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

