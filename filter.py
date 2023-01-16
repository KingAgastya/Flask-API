import pandas as pd
import matplotlib as plt
import csv

df = []
with open('main.csv','r') as f:
  csvreader = csv.reader(f)
  for i in csvreader:
    if i != []:
      df.append(i)

headers = df[0]
headers[0] = 'index'
data = df[1:]

comfortable_distance = []
for i in data:
  if float(i[2]) <= 100:
    comfortable_distance.append(i)
  else:
    pass

comfortable_gravity = []
for i in comfortable_distance:
    try:    
        if float(i[5].split(' ')[0]) > 150 and float(i[5].split(' ')[0]) < 350:
            comfortable_gravity.append(i)
    except:
        pass

print(f'number of stars with distance less than 100 lightyears: {len(comfortable_distance)}')
print(f'number of stars with gravity within 150-350 m/s2 : {len(comfortable_gravity)}')

with open('filtered_stars.csv','w') as f:
  csvWriter = csv.writer(f)
  csvWriter.writerow(headers)
  csvWriter.writerows(comfortable_gravity)