import os
import pandas as pd

shops = pd.read_csv('shops.csv')
shop_list = {}

for i in range(len(shops)):
    shop_list[shops['shop_name'][i]] = shops['href'][i]

for k,v in shop_list.items():
    r = requests.get(v+"images/hero_large.jpg")
    if r.status_code == 200:
        open('photos\%s.jpg'%k,'wb').write(r.content)
        print('%s店的图片下好啦'%k)
        