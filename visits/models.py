from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Outlet(models.Model):
    title = models.CharField(max_length=255)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name="outlets")

    def __str__(self):
        return self.title


class Visit(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    outlet = models.ForeignKey(Outlet, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.outlet.title} / {self.datetime}"
