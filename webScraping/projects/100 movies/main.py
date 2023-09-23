import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}


URL = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/", headers=headers)

# Write your code below this line 👇
def MustWatch100():

    movie_list = []
    soup = BeautifulSoup(URL.text, 'lxml')
    #Looks for all sections which contains h3 tag that contains movie titles
    div_tag = soup.find_all('section')
    
    # loops div_tag for each movie title
    for tag in div_tag:
        h3_tag = tag.find('h3').text
        
        movie_list.append(h3_tag)
        
    
    reversed_list = movie_list[::-1]
    with open('/Users/jun/Documents/Python-webScraping/Python-Learning-webScraping/webScraping/projects/100 movies/movieList.txt', 'w') as f:
        for movie in reversed_list:
            f.write(f"{movie}\n")
            
        
    
    
    
    
        
MustWatch100()