# # import_data.py
# import os
# import csv
# import django
# import sys

# sys.path.append('C:\Users\Abdullah\Desktop\leafLet--Map\crime_statistics_backend')  # Replace with the path to your Django project folder
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crime_statistics_backend.settings')

# import django
# django.setup()

# # Import the models after setting up Django

# def import_data():
#     with open('homicide_data.csv', 'r') as csvfile:
#         reader = csv.reader(csvfile)
#         next(reader)  # Skip the header row

#         for row in reader:
#             country_name = row[1]
#             year = int(row[2])
#             data_type = row[3]
#             value = float(row[4])

#             # Get or create the Country instance
#             country, _ = Country.objects.get_or_create(name=country_name)

#             if data_type == 'Intentional homicide rates per 100,000':
#                 homicide_rate_instance = HomicideRate(country=country, year=year, homicide_rate=value)
#                 homicide_rate_instance.save()
#             else:
#                 gender = 'Male' if data_type == 'Percentage of male and female intentional homicide victims, Male' else 'Female'
#                 homicide_percentage_instance = HomicidePercentage(country=country, year=year, gender=gender, percentage=value)
#                 homicide_percentage_instance.save()

# if __name__ == "__main__":
#     import_data()
