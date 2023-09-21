from bs4 import BeautifulSoup
import requests
import time


headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}

print("input unfamiliar location")
unfamilair_loc = input(">")
print(f'Filtering out {unfamilair_loc}')

def find_job():
    url = requests.get('https://www.cv-library.co.uk/Software-Developer-jobs?s=105140&gclid=CjwKCAjw6p-oBhAYEiwAgg2PgrUrTZb9FzEL8U6tluwQTDkFZ_mzLbVVafPWhAVrREcmXSA1p9WCmBoCfEsQAvD_BwE', headers=headers)

    doc = BeautifulSoup(url.text, 'lxml')



    li_tag = doc.find_all('li', class_='results__item')
    for tag in li_tag:
        
        job_link = tag.find('a', attrs={'href' : True})['href']
        
        job = tag.find('a', {'data-job-title' : 'Software Developer'})
        # filter out tags that have the desired tags/content.
        # filters job titles to software devleoper and returns None if not
        if job is not None:
            job = job.text

        salary = tag.find('dd', class_="job__details-value salary")
        
        if salary is not None:
            salary = salary.text

        location = tag.find('span', class_="job__details-location")
        if location is not None:
            location = location.text.strip().split(',')
            #filters out user input for locations
            if unfamilair_loc in location:
                del location
            
        

        posted = tag.find('p', class_='job__posted-by').text.replace(' ', '')
        
            
        print(f"{job}\n{job_link}\n{salary}\n{location}\n{posted}")
        
        print("---------------------------")
        
        if __name__ == '__main__':
            while True:
                find_job()
                # Dynamic approach to start wait time
                time_wait = 10
                print(f"Waiting {time_wait} minutes")
                #Allows program to stop running for a destinated time(seconds)
                time.sleep(time_wait * 60)
            