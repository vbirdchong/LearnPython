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

### XPath的使用

1. 表达式

```
nodename    # 节点名
/           # 若在起始位置，则表明从根节点选取node；若不在起始位置，表明选取子节点,本意都是选取全部子节点
//          # 从任意位置选取node节点
@           # 选取属性
*           # 通配符
```

2. 谓语

```
[n]                  # 第n个
[last()]             # 最后一个
[position()<n]       # 第n个位置之前的全部指定节点
node[@attr]          # 拥有attr属性的节点
node[@attr='val']    # 属性attr的值为val的节点
node[contains(@class, 'val')]    # class属性中包含val的节点
```

3. 运算符

```
|          # 并集
+          # 加法
-          # 减法
*          # 乘法
div        # 除法
=          # 等于
!=         # 不等于
<          # 小于
<=         # 小于
>          # 大于
>=         # 大于等于
or         # 或
and        # 与
mod        # 取余
```

4. 具体使用

```
response.xpath('//dl[@class="table_day7 "])
选取class="table_day7 "的所有dl节点

response.xpath('//dl[@class="table_day7 "]|//dl[@class="table_day7 tbg"]')
选取class="table_day "和class="table_day tbg"的并集

week = sel.xpath('dd[@class="week"]/text()').extract()
取到class="week"的dd节点中的具体值内容

element_dom.xpath(“/div”)
# 选取根节点的子节点div（包含其全部后代节点）

element_dom.xpath("//p")
# 选取任意位置的p节点

element_dom.xpath("//div[@class='title']")
# 选取class值为title的div节点

element_dom.xpath("//div[@class='item_list']//li/a/@href")
# 选取任意位置的class为item_list的div节点 的全部子节点li 中a节点的href属性

element_dom.xpath("/div/@name")
# 选取div节点的name属性值

element_dom.xpath("/div/descendant::text()")
# 选取div节点全部后代节点的文本

element_dom.xpath("//div/p|//ul/li/a")
# 选取div节点的子节点pa 与 ul/li/a 的并集

element_dom.xpath("//div/p[2]")
# 选取div中名为p的子节点的第2个

element_dom.xpath("//div/*[id='name']")
# 选取div的子节点中id值为name的任意节点

element_dom.xpath("(//div//p)[1]")
# //div//p结果集中的第一个结果

```

#### 参考

[XPath笔记](https://segmentfault.com/n/1330000008635451)

### 自定义设置

默认设定在setting.py文件中，如果要修改其中的部分参数，我们可以直接在里面进行修改。还有一种方式就是通过custom_settings 属性来进行实现，这样可以为每个spider设定各自的配置值。

```
在spider中设置如下属性，与在setting.py文件中进行修改的效果是一样的

custom_settings = {
    'DOWNLOADER_MIDDLEWARES' : {'tianqi.middlewares.TianqiDownloaderMiddleware': 100,},
    'COOKIES_ENABLED' : False,
    'DEFAULT_REQUEST_HEADERS': {'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'}
}
```

### 注意事项

在自定义的 MySpider 类中，name 和 start_urls 必须填写正确



