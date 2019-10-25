import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.ssa.gov/oact/babynames/'
result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')

table = soup.find('tbody')
records = []

for row in table.findAll('tr', attrs={'align': 'center'}):
    data = [td.text.strip() for td in row.select('td')]
    records.append(data)

fields = ['rank', 'male_name', 'female_name']
file_name = 'popular_names.csv'

with open(file_name, 'w') as csv_file:
    csv_writter = csv.writer(csv_file, delimiter=',')

    csv_writter.writerow(fields)
    csv_writter.writerows(records)


print('File created')
