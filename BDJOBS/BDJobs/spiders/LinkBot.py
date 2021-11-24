import scrapy
from ..items import BdjobsCategoryLink
import csv

class LinkbotSpider(scrapy.Spider):
    name = 'LinkBot'
    allowed_domains = ['www.bdjobs.com']
    
    # links = []
    # with open('E:\mywork\environments\BDJOBS\Files\links.csv', mode='r', encoding='UTF-8') as f:
    #     reader = csv.reader(f, delimiter='|')
    #     for row in reader:
    #         links.append(row[1])
    # start_urls = links[1:]

    start_urls = ['https://www.bdjobs.com']

    def parse(self, response):
        # Get all titles and links
        titles = response.xpath(r'/html/body/div[10]/div/div/div[1]/div/div[3]/div/ul/li/a/@title').getall()
        links = response.xpath(r'/html/body/div[10]/div/div/div[1]/div/div[3]/div/ul/li/a/@href').getall()
        data =[[titles[index],'https:'+links[index]] for index in range(len(links))]

        obj  = BdjobsCategoryLink()
        for index in range(len(titles)):
            obj['title']=titles[index].strip()
            obj['link']='https://jobs.bdjobs.com/'+links[index]
            
            yield obj
        
        # Writing on CSV
        with open('E:\mywork\environments\BDJOBS\Files\links.csv', mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter='|')
            writer.writerow(['Category', 'Link'])
            writer.writerows(data)
