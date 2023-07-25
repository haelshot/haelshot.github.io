from django.shortcuts import render
from django.http import JsonResponse
from .models import CrimeData
import csv
import io
from .forms import UploadCrimeDataForm
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'index.html')

def get_country_crime(request, country_name):
    try:
        country = CrimeData.objects.get(country=country_name)
        data = {
            'country_name': country.country,
            'crime_rate': float(country.crime_rate),
            'safety_rate': float(country.safety_rate)
        }
        return render(request, 'statsPage.html')
    except CrimeData.DoesNotExist:
        return JsonResponse({'error': 'Country not found'}, status=404)

def map_page(request):
    return render(request, 'map-page.html')

def statsPage(request):
    return render(request, 'statsPage.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def stats(request):
    return render(request, 'stats.html')

def process_csv_file(csv_file):
    try:
        decoded_file = csv_file.read().decode('utf-8')
        io_string = io.StringIO(decoded_file)
        next(io_string)  
        next(io_string)
        for row in csv.reader(io_string, delimiter=','):
            # try:
            #     cityAndCountry = row[1].split(',')
            #     if len(cityAndCountry) > 2:
            #         country = cityAndCountry[-1].lower().replace(" ", "")
            #         city = cityAndCountry[0]
            #     else:
            #         country = cityAndCountry[-1].lower().replace(" ", "")
            #         city = cityAndCountry[0]
            # except:
            #     country = row[1].lower().replace(" ", "")
            #     city = 'Null'  
            # crime_rate = float(row[2])
            # safety_rate = float(row[3])
        # with open('homicide_data.csv', 'r') as csvfile:
                    # reader = csv.reader(csvfile)
                    # next(reader)  # Skip the header row

                # for row in reader:
            country_name = row[1].lower().replace(" ", "")
            year = int(row[2])
            data_type = row[3]
            value = float(row[4].replace(",",""))

                    # Get or create the Country instance
            country, _ = Country.objects.get_or_create(name=country_name)

            if data_type == 'Intentional homicide rates per 100,000':
                homicide_rate_instance = HomicideRate(country=country, year=year, homicide_rate=value)
                homicide_rate_instance.save()
            else:
                gender = 'Male' if data_type == 'Percentage of male and female intentional homicide victims, Male' else 'Female'
                homicide_percentage_instance = HomicidePercentage(country=country, year=year, gender=gender, percentage=value)
                homicide_percentage_instance.save()
            # Create a new CrimeData object and save it to the database
            # CrimeData.objects.create(country=country,city=city, crime_rate=crime_rate, safety_rate=safety_rate)
    except:
        return JsonResponse("error: functionality for anonymous data upload isnt incuded yet", 404)

def upload_dataset_view(request):
    if request.method == 'POST':
        form = UploadCrimeDataForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            # Process the CSV file and save data to the database
            process_csv_file(csv_file)
    else:
        form = UploadCrimeDataForm()
    return render(request, 'upload_dataset.html', {'form': form})

from django.http import JsonResponse
from .models import CrimeData
from django.db.models import Avg
from .models import Country, HomicideRate, HomicidePercentage


@csrf_exempt
def get_country_stats(request):
    if request.method == 'POST' and 'country_name' in request.POST:
        country_name = request.POST['country_name'].lower().replace(" ", "")

        # Retrieve the crime statistics for the country from the database
        try:
            country_stats = CrimeData.objects.filter(country=country_name)
            average_crime_rate = country_stats.aggregate(Avg('crime_rate'))['crime_rate__avg']
            average_saftey_Index = country_stats.aggregate(Avg('safety_rate'))['safety_rate__avg']
            crime_stats = {
                'country_name': country_name,
                'average_crime_rate': average_crime_rate,
                'average_safety_Index': average_saftey_Index,
                # Add other crime statistics fields as needed
            }

            # Pass the crime_stats data to the template
            return render(request, 'stats.html', context=crime_stats)
        except CrimeData.DoesNotExist:
           return JsonResponse(f'error: No recent stats for {country_name}', 404)
            
    return render(request, 'statsPage.html')



def stats_page_view(request):
    countries = Country.objects.all()
    return render(request, 'statsPage.html', {'countries': countries})


# views.py

def get_country(request, country_id):
    # Retrieve the country based on the country_id
    try:
        country = Country.objects.get(pk=country_id)
    except Country.DoesNotExist:
        return JsonResponse({'error': 'Country not found'}, status=404)

    # Query the homicide percentages data for the selected country
    homicides = HomicidePercentage.objects.filter(country=country)

    # Organize the data for the chart
    data = {
        'years': list(set(homicides.values_list('year', flat=True))),
        'male_percentages': [],
        'female_percentages': [],
    }

    # Populate the male and female percentages lists for each year
    for year in data['years']:
        male_percentage = homicides.filter(year=year, gender='Male').first()
        female_percentage = homicides.filter(year=year, gender='Female').first()

        data['male_percentages'].append(male_percentage.value if male_percentage else None)
        data['female_percentages'].append(female_percentage.value if female_percentage else None)

    return JsonResponse(data)

def report(request):
    return render(request, 'report.html')

