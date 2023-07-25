from django.db import models

class CountryCrime(models.Model):
    country_name = models.CharField(max_length=100)
    crime_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.country_name

    class Meta:
        app_label = 'crime_stats'  # Add the app label for the model


class CrimeData(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    crime_rate = models.FloatField()
    safety_rate = models.FloatField()

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class HomicideRate(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    homicide_rate = models.FloatField()

    def __str__(self):
        return f"{self.country.name} - {self.year}"



class HomicidePercentage(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    percentage = models.FloatField()
    chart_image = models.ImageField(upload_to='chart_images/', blank=True, null=True)


    def __str__(self):
        return f"{self.country.name} - {self.year} - {self.gender}"


