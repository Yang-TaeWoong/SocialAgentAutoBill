import scrapy
from companycrawler.items import CompanycrawlerItem


class companycrawler_spiders(scrapy.Spider):
    name = "companycrawler"
    allowed_domains = "https://www.epost.go.kr/"
    start_urls = "https://www.epost.go.kr/"
    user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
    
    
    def start_requests(self):
        headers = {'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 'DNT': '1',
        'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36', 'Sec-Fetch-User': '?1', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        }
        arr = ("0318", "0224", "0225", "0122", "0601", "0121")
        for tail4 in range(7511, 7515):
            for middle4 in arr:
                yield scrapy.Request("https://service.epost.go.kr/trace.RetrieveDomRigiTraceList.comm?ems_gubun=E&sid1={0}&POST_CODE=&mgbn=trace&traceselect=1&target_command=&JspURI=&postNum={0}".format("14917"+middle4 + str(tail4).zfill(4)),callback = self.parse)

    def parse(self, response):
        item = CompanycrawlerItem()
        item['postnum'] = response.xpath("//*[@id=\"print\"]/table/tbody/tr/th").get()
        item['sender'] = response.xpath("//*[@id=\"print\"]/table/tbody/tr/td[1]/text()").get()
        item['receiver'] = response.xpath("//*[@id=\"print\"]/table/tbody/tr/td[2]/text()").get()
        item['result'] = response.xpath("//*[@id=\"print\"]/table/tbody/tr/td[4]/text()").get()
        print(item)