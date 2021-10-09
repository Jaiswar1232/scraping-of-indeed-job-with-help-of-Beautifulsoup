
from bs4 import BeautifulSoup as bs
import requests

link="https://in.indeed.com/jobs-in-Mumbai,-Maharashtra"
page=requests.get(link)
print(page)
soup=bs(page.content,'html.parser')
title=soup.find_all('h2',class_='jobTitle jobTitle-color-purple jobTitle-newJob')


review_title=[]
for i in range(0,len(title)):
    review_title.append(title[i].get_text())

review_title[:]=[titles.lstrip('new') for titles in review_title]
print(review_title)
print(len(review_title))
print(review_title[0])
print(review_title[1])
print(review_title[2])
print(review_title[3])
print(review_title[4])
print(review_title[5])

salary=soup.find_all('div',class_='metadata salary-snippet-container')
# print(salary)


review_salary=[]
for i in range(0,len(salary)):
    review_salary.append(salary[i].get_text())
print(review_salary)
print(len(review_salary))

print(review_salary[0])
print(review_salary[1])
print(review_salary[2])
print(review_salary[3])
print(review_salary[4])
print(review_salary[5])


location=soup.find_all('div',class_='companyLocation')
#print(location)

review_location=[]
for i in range(0,len(location)):
     review_location.append(location[i].get_text())
print(review_location)
print(len(review_location))

print(review_location[0])
print(review_location[1])
print(review_location[2])
print(review_location[3])
print(review_location[4])
print(review_location[5])
print(review_location[6])
print(review_location[7])
print(review_location[8])
print(review_location[9])
print(review_location[10])
print(review_location[11])
print(review_location[12])
print(review_location[13])
print(review_location[14])


Description=soup.find_all('div',class_='job-snippet')
Des=[]
for i in range(0,len(Description)):
     Des.append(Description[i].get_text())
print(Des)
print(len(Des))
print(Des[0])
print(Des[1])

company=soup.find_all('span',class_='companyName')
# print(company)


review_company=[]
for i in range(0,len(company)):
     review_company.append(company[i].get_text())
print(review_company)
print(len(review_company))

print(review_company[0])
print(review_company[1])
print(review_company[2])
print(review_company[3])
print(review_company[4])
print(review_company[5])
print(review_company[6])
print(review_company[7])
print(review_company[8])
print(review_company[9])
print(review_company[10])
print(review_company[11])
print(review_company[12])
print(review_company[13])
print(review_company[14])

responsive_employer=soup.find_all('td',class_='shelfItem responsiveEmployer')
# print(responsive_employer)

responsive_employer_list=[]
for i in range(0,len(responsive_employer)):
     responsive_employer_list.append(responsive_employer[i].get_text())
print(responsive_employer_list)
print(len(responsive_employer_list))

print(responsive_employer_list[0])
print(responsive_employer_list[1])
print(responsive_employer_list[2])



