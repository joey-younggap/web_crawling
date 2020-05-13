from bs4 import BeautifulSoup
import requests
import csv

csv_filename = "hot_chart100.csv"
csv_open = open(csv_filename, "w+", encoding='utf-8')
csv_writer = csv.writer(csv_open)
csv_writer.writerow( ('Rank', 'Song Title', 'Singer', ) )

req = requests.get('https://www.billboard.com/charts/hot-100')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

rank_list = soup.select('.chart-element__rank__number')
song_list = soup.select('.chart-element__information__song')
singer_list = soup.select('.chart-element__information__artist')

for i in range(0, 100):
    csv_writer.writerow( (rank_list[i].text, song_list[i].text, singer_list[i].text, ) )
    # print(rank_list[i].text, song_list[i].text, singer_list[i].text)

csv_open.close()
