import requests
from bs4 import BeautifulSoup
import csv
import time

def check_keywords(url):
    res = requests.get(f'http://iucn.ekoo.se/iucn/species_view/{url}')
    soup = BeautifulSoup(res.text, 'html.parser')
    text = soup.get_text()

    if 'edible' in text or 'commercial value' in text:
        return True
    else:
        return False

def get_iucn_status(url):
    res = requests.get(f'http://iucn.ekoo.se/iucn/species_view/{url}')
    soup = BeautifulSoup(res.text, 'html.parser')
    iucn_span = soup.find('span', {'class': 'label label-important'})

    if iucn_span is not None:
        iucn_status = iucn_span.get_text().strip()
    else:
        iucn_status = 'Not available'

    return iucn_status

urls = ['1000150', '1000235', '237034', '468177', '536518', '129700', '1000152', '1000151', '292441', '1000221', '443201', '359389', '103036', '160404', '1000251', '126302', '1000294', '283356', '514222', '468168', '412475', '308761', '362917', '1000224', '1000262', '358472', '1000158', '309397', '118428', '1000215', '378392', '271947', '249137', '831344', '356388', '451311', '252809', '412595', '100148', '450666','1000214', '209589', '487732', '327206', '1000236', '1000004', '107455', '561174', '130817', '103124', '800901', '818087', '803641', '443255', '803642', '561703', '374376', '487598', '369490', '154126', '514142', '108801', '295832', '412851', '1000202', '536180', '329096', '152271', '312143', '814401', '837446', '1000233', '133113', '332166', '332176', '1000196', '1000197', '812887', '104164', '277905', '519378', '463376', '508765', '221900', '515675', '199506', '109497', '313765', '438319', '197289', '109506', '1000187', '467601', '314169', '1000301', '511815', '1000188', '286567', '286574', '344422', '1000194', '1000193', '515528', '1000288', '298076', '445931', '315034', '552101', '113802', '437684', '437685', '100807', '332085', '100891', '100892', '332130', '298656', '438463', '136388', '287109', '298666', '437688', '1000198', '438468', '287111', '104324', '356817', '298676', '414579', '332199', '315409', '279613', '103453', '357512', '446558', '1000237', '252780', '415013', '1000191', '510757', '1000250', '1000268', '1000238', '1000156', '333109', '316492', '474726', '316609', '342491', '515366', '1000289', '521388', '1000356', '488418', '317299', '131519', '317455', '1000232', '107007', '501275','436829', '158191', '1000216', '102290', '364182', '335082', '414578', '415895', '318730', '504340', '827918', '260139', '319542', '319553', '136398', '283605', '820923', '464902', '1000264', '127486', '150169', '100829', '506902', '521537', '414472', '354929', '463649', '1000160', '289990', '1000281', '304476', '532164', '111880', '135188', '322276', '132942', '338666', '450960', '454332', '1000205','305493', '466458', '134031', '134054', '339684', '489466', '510885', '511916', '510884', '1000310', '511917', '820117', '1000274', '183615', '193656', '257064', '357102', '307044', '307073', '340464', '1000263', '538392', '354924', '325198', '427890', '1000253', '265741', '307495', '325522', '443729', '541867', '415337']

x = 0
with open('results.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['URL', 'Title', 'IUCN Red List Category', 'Contains Keywords'])

    for url in urls:
        res = requests.get(f'http://iucn.ekoo.se/iucn/species_view/{url}')
        soup = BeautifulSoup(res.text, 'html.parser')
        title = soup.title.string.strip()
        iucn_status = get_iucn_status(url)
        keywords = 'Yes' if check_keywords(url) else 'No'
        x = x + 1
        time.sleep(2)
        try:
            writer.writerow([f'http://iucn.ekoo.se/iucn/species_view/{url}', title, iucn_status, keywords])
        except UnicodeEncodeError:
            print(f"Error writing row for URL {url}: could not encode characters in title or keywords.")
        else:
            print(f"Wrote row for URL {url} to CSV." + " That makes " + str(x) + " recorded.")

print('Results saved to results.csv')
