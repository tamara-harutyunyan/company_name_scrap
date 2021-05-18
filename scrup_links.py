import requests
from bs4 import BeautifulSoup

GOOLE = 'https://www.google.com/search?q='
SEARCH = '&sxsrf=ALeKk00t8jfC4IlqYjnZxHUPo0EY637-IA%3A162116' \
         '9615000&source=hp&ei=zhWhYO-FO4LeavLMoMAB&iflsig=AINFCb' \
         'AAAAAYKEj3wK_TvlmNxDtD5DPzCFXT43iaukH&oq=&gs_lcp=Cgdnd3Mtd2l6EA' \
         'EYADIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCM' \
         'Q6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJ1AAWABgzVRoAnA' \
         'AeACAAQCIAQCSAQCYAQCqAQdnd3Mtd2l6sAEK&sclient=gws-wiz'


def company_name_extract():
    """
    This function takes the company's website URL and returns the company name
    """
    print("Please input the link:")
    url1 = input(str())
    seaching_company_link = url1.split('www.')[-1]
    general_link = GOOLE + seaching_company_link + SEARCH
    reqs = requests.get(general_link)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    for title in soup.find_all('h3'):
        print(f"Title of the website is: {title.get_text()}")
        break


if __name__ == "__main__":
    company_name_extract()
