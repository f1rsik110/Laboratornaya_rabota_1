import requests
from bs4 import BeautifulSoup

def get_data(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }

    req = requests.get(url, headers)

    soup = BeautifulSoup(req.text, "lxml")
    ahrefs = soup.find_all("a", class_="css-xb5nz8 e1huvdhj1")

    projects_urls = []
    for ahref in ahrefs:
        project_url = ahref.get("href")
        projects_urls.append(project_url)

    spans = soup.find_all("div", class_="css-1dv8s3l eyvqki91")

    projects_prices = []
    for span in spans:
        project_price = span.find("span", class_="css-46itwz e162wx9x0").find("span").text
        project_price = str(project_price).replace("\xa0", "")
        projects_prices.append(project_price)

    names = soup.find_all("div", class_="css-17lk78h e3f4v4l2")

    projects_names = []
    for name in names:
        project_name = name.find("span").text
        projects_names.append(project_name)

    with open("info.txt", 'w', encoding='utf-8') as file:
        for i in range(20):
            file.write(projects_names[i] + " (" + projects_prices[i] + " руб.) url: " + projects_urls[i] + "\n")

get_data("https://auto.drom.ru/")