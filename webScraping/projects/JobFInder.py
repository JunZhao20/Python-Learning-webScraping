from bs4 import BeautifulSoup
import requests
import time


headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}

print("input unfamiliar location")
unfamilair_loc = input(">").lower()
print(f'Filtering out {unfamilair_loc}')

def find_job():
    url = requests.get('https://www.cv-library.co.uk/Software-Developer-jobs?s=105140&gclid=CjwKCAjw6p-oBhAYEiwAgg2PgrUrTZb9FzEL8U6tluwQTDkFZ_mzLbVVafPWhAVrREcmXSA1p9WCmBoCfEsQAvD_BwE', headers=headers)

    doc = BeautifulSoup(url.text, 'lxml')

    li_tag = doc.find_all('li', class_='results__item')
    
    result = ''
    
    lst = []
    
    for tag in li_tag:
        
        
        location = tag.find('span', class_="job__details-location")
        if location is not None:
            location = location.text.lower().strip().split(',')
        else:
            location = ''
            
        job_link = tag.find('a', attrs={'href' : True})['href']
        
        job = tag.find('a', {'data-job-title' : 'Software Developer'})
        # filter out tags that have the desired tags/content.
        # filters job titles to software devleoper and returns None if not
        if job is not None:
            job = job.text
        else:
            job = ''
            
        salary = tag.find('dd', class_="job__details-value salary")
        
        if salary is not None:
            salary = salary.text
        else:
            salary = ''
        
        
        posted = tag.find('p', class_='job__posted-by').text.replace(' ', '')
        
        # creates a sublist of collection of tags of 1 job listing into a list
        lst.append([f"{job}\n",f"{job_link}\n",f"{salary}\n",f"{location}\n", f"{posted}\n"])
        
        #Filters out the location based on 'unfamiliar_loc' input.
        for i in lst:
            for elem in i:
                #checks is elem is a list which stores the location tag
                if type(elem) is list:
                    for x in elem:
                        # if condition to check if job location has 'unfamiliar_loc' input
                        if unfamilair_loc == x.strip():
                            lst.remove(i)
        
        for job_ in lst:
            result += f"{' '.join(job_)}\n"
        print(result)
        
    with open(f'/Users/jun/Documents/Python-webScraping/Python-Learning-webScraping/webScraping/projects/jobResults.txt', 'w') as f:
       f.write(f"{result}")
       
    

if __name__ == '__main__':
    #loops find_job scaper function
    while True:
        find_job()
        # Dynamic approach to start wait time
        time_wait = 10
        print(f"Waiting {time_wait} minutes")
        leave = input('Type '"y"' to quit, else then wait.').lower()
        if leave != 'y':
            #Allows program to stop running for a destinated time(seconds)
            time.sleep(time_wait * 60)
        else:
            exit()
        
        