import requests
import json
from bs4 import BeautifulSoup


BASE_URL = 'https://www.aladin.co.kr/'

def get_page(page_url):
    """
    Get html inofrmation from page_url
    """
    page = requests.get(page_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return page, soup

def get_id(page_num=4):
    """
    Get id of bestseller
    """
    bestseller_id = []
    for i in range(1,page_num+1):
        bestseller_url = f'{BASE_URL}/shop/common/wbest.aspx?BestType=Bestseller&BranchType=1&CID=0&page={i}&cnt=1000&SortOrder=1'
        page_id, soup_id = get_page(bestseller_url)

        # Get the top value from the class bo3
        id_url = soup_id.select('.bo3')
        
        for d in id_url:
            d = d.get('href')
            #id값만 가져와 정수형으로 바꾸기
            # Get id value and convert into integer
            ids = int(d.split('=')[1])
            # Append id value to the list 
            bestseller_id.append(ids)
        
    return bestseller_id



def info(ItemId):
    """
    Get sales point, rating and genre using id of book
    """
    book_url = f'{BASE_URL}/shop/wproduct.aspx?ItemId={ItemId}'
    page_book, soup_book = get_page(book_url)
    
    # Get Sales Point, rating, genre
    sales_point = soup_book.find('div',style='display:inline-block;').find('strong').text
    rating = float(soup_book.find(class_='Ere_sub_pink Ere_fs16 Ere_str').text)
    genre = soup_book.select('#ulCategory>li>a')[1].text

    return [sales_point, rating, genre]







