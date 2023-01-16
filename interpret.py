import matplotlib as plt
import csv

df = []
with open('filtered_stars.csv','r') as f:
  csvreader = csv.reader(f)
  for row in csvreader:
    if row != []:
      df.append(row)

headers = df[0] 
data = df[1:]
Name = []
Mass = []
Radius = []
Distance = []
Gravity = []

for i in data:
  Name.append(i[1])
  Distance.append(float(i[2].split(' ')))
  Mass.append(float(i[3].split(' ')))
  Radius.append(float(i[4].split(' ')))
  Gravity.append(float(i[5].split(' ')[0]))

plt.bar(Name, Mass)
plt.title('Name VS Mass')
plt.xlabel('Name')
plt.ylabel('Mass')
plt.show()

plt.bar(Name, Radius)
plt.title('Name VS Radius')
plt.xlabel('Name')
plt.ylabel('Radius')
plt.show()

plt.bar(Name, Distance)
plt.title('Name VS Distance')
plt.xlabel('Name')
plt.ylabel('Distance')
plt.show()

plt.bar(Name, Gravity)
plt.title('Name VS Gravity')
plt.xlabel('Name')
plt.ylabel('Gravity')
plt.show()