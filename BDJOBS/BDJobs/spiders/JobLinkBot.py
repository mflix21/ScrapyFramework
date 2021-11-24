import scrapy
from ..items import BdjobsLink
import csv


class JoblinkbotSpider(scrapy.Spider):
    name = 'JobLinkBot'
    allowed_domains = ['www.bdjobs.com']

    links = []
    with open('E:\mywork\environments\BDJOBS\Files\links.csv', mode='r', encoding='UTF-8') as f:
        reader = csv.reader(f, delimiter='|')
        for row in reader:
            links.append(row[1])
    start_urls = links[1:]

    # start_urls = ['https://jobs.bdjobs.com/jobsearch.asp?fcatId=1&icatId=']

    def parse(self, response):
        texts = response.xpath(r'//*[@id="jobList"]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/div/a/text()').getall() 
        links = response.xpath(r'//*[@id="jobList"]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/div/a/@href').getall()
    
        
        obj  = BdjobsLink()
        for index in range(len(texts)):
            obj['title']=texts[index].strip()
            obj['link']='https://jobs.bdjobs.com/'+links[index]
            
            yield obj

        
        

    



