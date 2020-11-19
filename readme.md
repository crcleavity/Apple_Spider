
## 新增：
- 将数据进行采集后自动储存在服务器mysql数据库中
- 引用可视化软件tableau连接mysql数据库进行可视化分析
![门店区域图](visual\pic1.jpg)
![门店区域图](visual\pic2.jpg)
![门店分布图](visual\pic3.jpg)


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
#### 实现方式
- 直接scrapy shell后代码：

``` 
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
```

4. 获得数据后制成表格，输出至shops中  
5. 对各店数据图片进行采集  
6. 通过对网站解析，得知图片在https://www.apple.com.cn/retail/{shop_name}/images/hero_large.jpg地址中
7. 对图片进行下载并保存到本地

#### 实现代码

```import os
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
```