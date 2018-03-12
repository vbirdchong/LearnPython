## Scrapy 框架使用记录

### 代理设置

#### 代码中设置

```
class DmozSpider(scrapy.spiders.Spider):
    name = "dmoz"
    allowed_domains = ["dmoztools.net"]
    start_urls = [
        "http://www.dmoztools.net/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoztools.net/Computers/Programming/Languages/Python/Resources/"
    ]

    def start_requests(self):
        meta_proxy = "http://10.144.1.10:8080"
        for url in self.start_urls:
            print("url = " + url)
            yield scrapy.Request(url = url, callback=self.parse, meta={'proxy':meta_proxy})

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, "wb") as f:
            f.write(response.body)
```


#### 使用中间件及配置文件

```
每个项目创建的时候，都会默认创建一个中间件 **middlewares.py**。我们的项目名称叫tutotial，所以在上述的文件中可以找到如的类
class TutorialDownloaderMiddleware(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = "http://10.144.1.10:8080"
        return None

在该类中修改对应的request处理，对代理进行设置。

同时，修改配置文件**setting.py**，默认该值为543，由于要用到代理，所以将其优先级提高到100

DOWNLOADER_MIDDLEWARES = {
   'tutorial.middlewares.TutorialDownloaderMiddleware': 100,
}
```