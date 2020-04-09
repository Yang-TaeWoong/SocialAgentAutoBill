import scrapy
from companycrawler.items import CompanycrawlerItem
import re

class companycrawler_spiders(scrapy.Spider):
    name = "companycrawler"
    allowed_domains = "https://www.epost.go.kr/"
    start_urls = "https://www.epost.go.kr/"
    user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
    
    def start_requests(self):
        arr = ("0318", "0224", "0225", "0122", "0601", "0121")
        for tail4 in range(7511, 7515):
            for middle4 in arr:
                yield scrapy.Request("https://service.epost.go.kr/trace.RetrieveDomRigiTraceList.comm?ems_gubun=E&sid1={0}&POST_CODE=&mgbn=trace&traceselect=1&target_command=&JspURI=&postNum={0}".format("14917"+middle4 + str(tail4).zfill(4)),callback = self.parse)

    def parse(self, response):
        postnum = str(response.xpath("//*[@id=\"print\"]/table/tbody/tr/th").get())
        sender = response.xpath("//*[@id=\"print\"]/table/tbody/tr/td[1]/text()").get()
        receiver = response.xpath("//*[@id=\"print\"]/table/tbody/tr/td[2]/text()").get()
        result = response.xpath("//*[@id=\"print\"]/table/tbody/tr/td[4]/text()").get()

        item = CompanycrawlerItem()
        
        print(item)