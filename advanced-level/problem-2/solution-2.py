import requests
from bs4 import BeautifulSoup

def get_h2_titles(url):
    # send HTTP GET request
    resp = requests.get(url)
    resp.raise_for_status()  # raise error for bad status codes

    # parse HTML
    soup = BeautifulSoup(resp.text, "html.parser")

    # find all <h2> tags
    h2_tags = soup.find_all("h2")
    print(h2_tags)

    # extract their text
    titles = [h2.get_text(strip=True) for h2 in h2_tags]
    return titles

if __name__ == "__main__":
    url = "https://medium.com/@noureldin_z3r0/how-to-write-the-perfect-blog-post-my-10-000-word-journey-7b5b38525848"
    titles = get_h2_titles(url)
    print("H2 titles found:")
    for idx, t in enumerate(titles, 1):
        print(f"{idx}. {t}")
