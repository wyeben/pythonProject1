# import requests
# from bs4 import BeautifulSoup
#
#
# def scrape_website(url):
#     response = requests.get(url)
#     if response.status_code != 200:
#         print(f"Failed to fetch the page: {response.status_code}")
#         return
#
#     soup = BeautifulSoup(response.text, 'html.parser')
#
#     data = []
#     for item in soup.find_all('div', class_='item'):
#         title = item.find('h2').text.strip()
#         description = item.find('p').text.strip()
#         data.append({'title': title, 'description': description})
#
#     return data
#
#
# url = 'https://example.com'
# scraped_data = scrape_website(url)
# print(scraped_data)

with open('account.txt', mode='r') as my_file:
   print(my_file.read())

