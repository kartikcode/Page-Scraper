from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('org_info.csv','w')
csv_write = csv.writer(csv_file)
csv_write.writerow(['Student Name','Organisation','Project'])


for j in range(1,13):
    url = "https://summerofcode.withgoogle.com/archive/2019/projects/?page=" + str(j)
    source = requests.get(url).text
    #print(source)
    soup = BeautifulSoup(source,"lxml")
    #print(soup.prettify())
    orgs = soup.find('section',class_='lifted-section')
    #print(orgs)
    for i in orgs.find_all('li'):
        details = (i.div.text).splitlines()
        stud_name = details[2]
        project = details[4]
        org_name = (details[5].split(':'))[1][1:]
        print(stud_name)
        print(project)
        print(org_name)
        
        csv_write.writerow([stud_name,org_name,project])

csv_file.close()
