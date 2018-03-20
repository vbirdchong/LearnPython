import scrapy
from scrapy.http import Request, FormRequest
import json
from PIL import Image
from io import BytesIO
import pytesseract
from scrapy.log import logger

class CaptchaLoginSpider(scrapy.spiders.Spider):
    name = 'captcha_login'
    allowed_domains = ['example.webscraping.com']
    start_urls = [
        'http://example.webscraping.com/user/profile'
    ]

    def parse(self, response):
        keys = response.css('table label::text').re('(.+):')
        valus = response.css('table tb.w2p_fw::text').extract()
        print(keys)
        print(valus)
        yield dict(zip(keys, valus))

    login_url = 'http://example.webscraping.com/places/default/user/login'
    user = 'liushuo@webscraping.com'
    password = '12345678'

    def start_requests(self):
        print("In loging, start requests")
        yield Request(self.login_url, callback=self.login, dont_filter=True)

    def login(self, response):
        login_reponse = response.meta.get('login_response')

        if not login_reponse:
            # step 1
            captchaUrl = response.css('label.field.prepend-icon img::attr(src)').extract_first()
            captchaUrl = response.urljoin(captchaUrl)
            yield Request(captchaUrl,
                            callback=self.login,
                            meta={'login_response':response},
                            dont_filter=True)
        else:
            # step 2
            formdata = {
                'email': self.user,
                'pass': self.password,
                'code': self.get_captcha_by_OCR(response.body),
            }
            yield FormRequest.from_response(login_reponse, 
                                            callback=self.parse_login,
                                            formdata=formdata,
                                            dont_filter=True)

    def parse_login(self, response):
        info = json.loads(response.text)
        if info['error'] == '0':
            logger.info('Login Success')
            return super().start_requests()
        
        logger.info('Login Fail')
        return self.start_requests()

    def get_captcha_by_OCR(self, data):
        img = Image.open(BytesIO(data))
        img = img.convert('L')
        captcha = pytesseract.image_to_string(img)
        img.close()

        return captcha