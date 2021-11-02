from bs4 import BeautifulSoup
import requests
import csv

source=requests.get('https://merojob.com/search/?q=python').text
soup=BeautifulSoup(source,'lxml')

csv_file=open('scrap.csv','a')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Job Title','Company','Skills Required'])

total_jobs_row=soup.find('div',class_="card mt-md-0 mt-3").div.div.h1.text

total_jobs_for_python=total_jobs_row.split(" ")[6]

for job_role in soup.find_all('div',class_="col-8 col-lg-9 col-md-9 pl-3 pl-md-0 text-left"):
    company=job_role.h3.text
    job_title=job_role.h1.text
    skills_required=job_role.find_all("span",class_="badge badge-pill badge-light rounded text-muted")
    skills=[]
    for item in skills_required:
        skill=item.text
        skills.append(skill) 
        
    csv_writer.writerow([job_title,company,skills])
    


csv_file.close()