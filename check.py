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
        
        list1=name.split(' ')
        if(len(name.split(' '))<2):
            continue
        if set(name).difference(ascii_letters + " "):
            continue
        if(not(set(name).difference(ascii_lowercase + " "))):
            continue

        for person in file_j:
            list2 = person['n'].split('  ')

            list3 = person['n'].split(' ')
            
            if list1==list2 or list1==list3:
                print("Name: "+name)
                print("Roll No: "+person['i'])
                print("Branch: "+person['d'])
                print("Organisation: "+ line[1])
                print("Project: "+ line[2])  
                print()
                

