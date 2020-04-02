import csv
import re
from string import ascii_letters, digits,ascii_lowercase
import json

file_j = json.loads(open('students.json').read())


with open('org_info.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    next(csv_reader)
    for line in csv_reader:
        name = line[0]
        flag=0
        if(len(name.split(' '))<2):
            continue
        if set(name).difference(ascii_letters + " "):
            continue
        if(not(set(name).difference(ascii_lowercase + " "))):
            continue

        for person in file_j:
            if(person['n']==name):
                print("Name: "+name)
                print("Roll No: "+person['i'])
                print("Branch: "+person['d'])
                print("Organisation: "+ line[1])
                print("Project: "+ line[2])  
                print()

