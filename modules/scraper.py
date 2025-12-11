import requests
from bs4 import BeautifulSoup

def fetch_python_news():
    """
    Python.org 블로그에서 최신 글의 '제목', '링크', '본문'을 가져옴
    반환값: 딕셔너리 형태 {'title': ..., 'url': ..., 'content': ...}
    """
    base_url = "https://www.python.org/blogs/"
    
    try:
        # 1. 목록 페이지 접속
        res = requests.get(base_url)
        soup = BeautifulSoup(res.text, 'html.parser')
        
        # 최신 글 요소 찾기
        post_tag = soup.select_one(".list-recent-posts li h3 a")
        if not post_tag:
            return None
            
        title = post_tag.get_text().strip()
        link = post_tag['href']
        
        # 2. 상세 페이지 접속
        detail_res = requests.get(link)
        detail_soup = BeautifulSoup(detail_res.text, 'html.parser')
        
        # 3. 본문 추출
        content_tag = detail_soup.select_one(".item-page-content")
        
        if content_tag:
            content = content_tag.get_text().strip()
        else:
            paras = detail_soup.select("p")
            content = " ".join([p.get_text().strip() for p in paras if len(p.get_text()) > 30])
            
        return {
            "title": title,
            "url": link,
            "content": content
        }
        
    except Exception as e:
        print(f"[Scraper Error] {e}")
        return None

if __name__ == "__main__":
    data = fetch_python_news()
    if data:
        print(f"제목: {data['title']}")
        print(f"본문 길이: {len(data['content'])}자")
    else:
        print("크롤링 실패")