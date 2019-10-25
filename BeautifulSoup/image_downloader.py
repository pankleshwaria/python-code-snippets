import requests
from PIL import Image
from bs4 import BeautifulSoup
from io import BytesIO

search = str(input('Search for: '))
query = {'q': search}
url = 'http://www.bing.com/images/search/'

result = requests.get(url, params=query)
soup = BeautifulSoup(result.text, 'html.parser')

links = soup.findAll('a', {'class': 'thumb'}, limit=1)

for link in links:
    img_url = link.attrs['href']

    img_obj = requests.get(img_url)
    if img_obj.status_code != 200:
        print('Failed to load')
        break

    try:
        img = Image.open(BytesIO(img_obj.content))
        img.save('david.jpg')
    except (KeyError, IOError) as ex:
        print(ex.errors)
        print('Could not save image')
    else:
        print('Say Hello David')
