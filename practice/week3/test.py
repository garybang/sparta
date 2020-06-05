import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://terms.naver.com/entry.nhn?docId=5702597&cid=59153&categoryId=59153',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
contents = soup.select('#size_ct > p')

# movies (tr들) 의 반복문을 돌리기
for content in contents:
    # movie 안에 a 가 있으면,
    book = content.select_one('strong > a')
    if book is not None:
        bookTitle = book.text                                  # a 태그 사이의 텍스트를 가져오기
        print(bookTitle)

        #size_ct > p:nth-child(33) > strong > a
        #size_ct > p:nth-child(45) > strong > a