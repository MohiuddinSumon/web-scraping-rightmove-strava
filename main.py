import csv
import requests
from bs4 import BeautifulSoup

URL = 'https://www.strava.com/segments/631102'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
segment_details = []
segment_name = soup.find(class_='segment-name').text.strip()
segment_details.append([segment_name])
segment_location = soup.find(class_='location').text.strip().replace('\n', ' ')
segment_details.append([segment_location])
segment_states_list = soup.find(class_='inline-stats').findAll('li')
for segment_state in segment_states_list:
    segment_details.append([segment_state.text.strip()])


with open('output.csv', 'w+') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(segment_details)

response_table = soup.find(id='segment-leaderboard')
tables = soup.findAll('table')
output_rows = []
for table in tables:
    for table_row in table.findAll('tr', limit=11):
        columns = table_row.findAll('td')
        output_row = []
        for column in columns:
            if len(column.text) > 0:
                output_row.append(column.text.strip())
        output_rows.append(output_row)

with open('output.csv', 'a+') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(output_rows)
