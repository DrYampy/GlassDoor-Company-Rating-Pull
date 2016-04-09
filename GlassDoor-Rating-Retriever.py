from bs4 import BeautifulSoup
from selenium import webdriver
import time


## Get the GlassDoor Rating!
## REQUIRES FIREFOX!!
def GlassDoor():
    
    part=raw_input('Enter A company name: ')
    
    #The Search Query that gives results depends on the length of the search string
    length=len(part)
    url='https://www.glassdoor.com/Reviews/%s-reviews-SRCH_KE0,%s.htm' %(part,length)
    
    #Open Firefox
    driver = webdriver.Firefox()
    driver.get(url)
    
    #Wait for all the stuff to load
    time.sleep(10)
    presoup = driver.page_source
    soup = BeautifulSoup(presoup, "html.parser")
    
    #Pulls the rating of the first Search Result (Like Google's I'm Feeling Lucky!)
    #IS SUBJECT TO PULL THE WRONG RATING, Needs some sort of comparator
    ratings = soup.find_all('span', {'class' : 'bigRating strong margRtSm h1'})
    lines = [float(span.get_text()) for span in ratings]
    if len(lines)==0:
        ratings = soup.find_all('div', {'class' : 'notranslate ratingNum'})
        lines = [float(span.get_text()) for span in ratings]
    
    #Close the Browser and return the rating
    driver.quit()
    return lines[0]