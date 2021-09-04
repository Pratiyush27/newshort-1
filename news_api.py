import requests
from bs4 import BeautifulSoup

def fetch_news(api_key:str, category:str):

    url = "https://bing-news-search1.p.rapidapi.com/news"

    querystring = {"category":category,"cc":"in","safeSearch":"Off","textFormat":"Raw"}

    headers = {
        'x-bingapis-sdk': "true",
        'x-rapidapi-host': "bing-news-search1.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    api_response = requests.request("GET", url, headers=headers, params=querystring)

    articles = api_response.json()["value"]

    result_articles = []

    for art in articles:
        art_url = art["url"]
        art_title = art["name"]
        art_date = art["datePublished"]

        art_content = get_article_text(art_url)

        result_articles.append({
            "title": art_title,
            "content": art_content,
            "category": category,
            "date": art_date
        })


    return result_articles

def get_article_text(url:str):

    news_html = requests.get(url).text

    soup = BeautifulSoup(news_html, 'html.parser')
    # print([0].get_text())

    news_content = ""
    elements = soup.find_all('p')
    for e in elements:
        news_content += e.get_text() 
        news_content += " "

    return news_content

