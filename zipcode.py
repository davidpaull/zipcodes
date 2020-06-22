#!/usr/bin/env python3

import csv
import time

zip_file = 'full-zips.csv'

def read_csv_iter(file_name=zip_file):
    if not file_name:
        return False

    #csv.field_size_limit(sys.maxsize)
    with open(file_name, 'r') as cf:
        csv_iter = csv.DictReader(cf)
        for row in csv_iter:
            yield row

def get_all_data(zipcode):
    for line in read_csv_iter(zip_file):
        if line['Zip'] == zipcode:
            return(line)

def coords_from_zip(zipcode):
    for line in read_csv_iter(zip_file):
        if line['Zip'] == zipcode:
            return(line['Latitude'], line['Longitude'])

if __name__ == '__main__':
    zip_to_get = input('enter zip: ')
    start_time = time.time()

    print()
    print('Retrieving lat, lon')
    lat, lon = coords_from_zip(zip_to_get)
    print('Retrieved lat, lon in [{}] sec.'.format(round(time.time() - start_time, 3)))
    print(lat, lon)
    print()

    print('Retrieving all data...')
    start_time = time.time()
    zip_data = get_all_data(zip_to_get)
    print('Retrieved all zipcode data in [{}] sec.'.format(round(time.time() - start_time, 3)))
    for k, v in zip_data.items():
        print(k, ':', v)
    print()
    print('SUCCESS. Exit')
