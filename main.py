#!/usr/bin/env python3
import json
import requests
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description='Download metadata and products about a brand featured on sephora.com')
parser.add_argument('brand', metavar='brand',
                    help='The slug brand name such as "givenchy" or "guerlain"')
args = parser.parse_args()

BASE_URL = 'https://www.sephora.com'
r = requests.get(BASE_URL+'/brand/'+args.brand+'/all?pageSize=3000')

def has_type_ld_json(tag):
    return tag.has_attr('type') and not tag.has_attr('id')

soup = BeautifulSoup(r.text, 'html.parser')
s = soup.find_all("script", attrs={"type": "application/ld+json"})

if len(s) != 2:
    raise Exception('This crawler is not compatible with this  version of Sephora. Expected LD+JSON scripts: 2. Found '+str(len(s))+'.')

brand = json.loads(s[0].get_text())
print('Brand name:', brand['itemListElement'][1]['item']['name'])
print('Brand URL:', brand['itemListElement'][1]['item']['@id'])

s = soup.find("script", attrs={"id": "linkJSON"})
data = json.loads(s.get_text())
TopBar = next(x for x in data if x['path'] == 'TopBar')
Logo = next(x for x in data if x['path'] == 'Logo')
LovesListBtn = next(x for x in data if x['path'] == 'LovesListBtn')
TopNav = next(x for x in data if x['path'] == 'TopNav')
PersistentBanner = next(x for x in data if x['path'] == 'PersistentBanner')
CatalogPage = next(x for x in data if x['path'] == 'CatalogPage')
Footer = next(x for x in data if x['path'] == 'Footer')

# Print Banner
print('Current offer in banner:', PersistentBanner['props']['bannerData']['text'])

# print Products
products = CatalogPage['props']['products']
print('Number of products:', len(products))
size = min(10, len(products))
print('Listing first', size, 'products:')
for p in products[:size]:
    print(' -', p['displayName'], '('+p['productId']+')', BASE_URL+p['targetUrl'])
