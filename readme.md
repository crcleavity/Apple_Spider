## Apple店数据采集

目标网站：https://www.apple.com.cn/retail/storelist/   

1. 网站分析  
    静态网站，直接进去，解析response，提取信息即可。

2. 网站response获得  
    直接get，status200，成果获得。  
 
3. 网站xpath解析  
    整体数据块获得：response.xpath('//*[@id="cnstores"]/div/div/div/div/ul').getall()  
    店铺名：response.xpath('//*[@id="cnstores"]/div/div/div/div/ul/li[1]/a/text()').getall()  
    店铺地址：response.xpath('//*[@id="cnstores"]/div/div/div/div/ul/li[2]/text()').extract()
    店铺电话：re.findall(r'400-\d{3}-\d{4}', response.text)
    店铺链接  response.xpath('//*[@id="cnstores"]/div/div/div/div/ul/li[1]/a/@href').getall()

直接scrapy shell后代码：

import pandas as pd

doodle = pd.DataFrame(columns = ['shop_name','address','contact','href'])

shop_name = response.xpath('//*[@id="cnstores"]/div/div/div/div/ul/li[1]/a/text()').getall()  

address = response.xpath('//*[@id="cnstores"]/div/div/div/div/ul/li[2]/text()').getall()

contact = re.findall(r'400-\d{3}-\d{4}', response.text)
del contact[-1]

href = response.xpath('//*[@id="cnstores"]/div/div/div/div/ul/li[1]/a/@href').getall()



doodle['shop_name'] = shop_name
doodle['address'] = address
doodle['contact'] = contact
doodle['href'] = href
doodle.to_csv('C:/Users/a/OneDrive - arvmontessori.org/桌面/tmp.csv', encoding = 'utf_8_sig)

