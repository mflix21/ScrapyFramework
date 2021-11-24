import scrapy
from ..items import Job
import csv


class JobinfobotSpider(scrapy.Spider):
    name = 'JobInfoBot'
    allowed_domains = ['jobs.bdjobs.com']
    links = []
    with open('E:\mywork\environments\BDJOBS\BDJobs\JobLinks.csv', mode='r', encoding='UTF-8') as f:
        reader = csv.reader(f, delimiter='|')
        for row in reader:
            links.append(row[0])
    start_urls = links[1:]

    def parse(self, response):
        job = Job()

        job['title'] = response.xpath(r'//*[@id="job-preview"]/div[2]/div[1]/div/div/div[1]/div[1]/h2/text()').get()
        job['company'] = response.xpath(r'//*[@id="com_name"]/text()').get()
        job['vacancies'] = str(response.xpath(r'//*[@id="job-preview"]/div[2]/div[1]/div/div/div[3]/p/text()').get()).strip()
        j = response.xpath(r'//*[@id="job-preview"]/div[2]/div[1]/div/div/div[4]/ul/li/text()').getall()
        job['jobContext'] = '|'.join(j).replace('\r', '')
        jr = response.xpath(r'//*[@id="job-preview"]/div[2]/div[1]/div/div/div[5]/ul/li/text()').getall() 
        job['jobResposiblities'] = '|'.join(jr).replace('\r', '')
        job['jobType'] = str(response.xpath(r'//*[@id="job-preview"]/div[2]/div[1]/div/div/div[6]/p/text()').get()).strip()
        w = response.xpath(r'//*[@id="job-preview"]/div[2]/div[1]/div/div/div[7]/ul/li/text()').getall() 
        job['workplace'] = '|'.join(w).replace('\r', '')
        edu = response.xpath(r'//*[@id="job-preview"]/div[2]/div[1]/div/div/div[8]/ul/li/text()').getall()    
        job['education'] = '|'.join(edu).replace('\r', '')
        ex = response.xpath(r'//*[@id="job-preview"]/div[2]/div[1]/div/div/div[9]/ul/li/text()').getall()    
        job['experience'] = '|'.join(ex).replace('\r', '')
        ar = response.xpath(r'//*[@id="job-preview"]/div[2]/div[1]/div/div/div[10]/ul/li/text()').getall()    
        job['additionalRequirments'] = '|'.join(ar).replace('\r', '')
        job['joblocation'] = response.xpath(r'//*[@id="job-preview"]/div[2]/div[1]/div/div/div[11]/p/text()').get()
        job['salary'] = str(response.xpath(r'//*[@id="job-preview"]/div[2]/div[1]/div/div/div[12]/ul/li/text()').get()).strip()
        benefits = response.xpath(r'//*[@id="job-preview"]/div[2]/div[1]/div/div/div[13]/ul/li/text()').getall()
        job['benefits'] = '|'.join(benefits).replace('\r', '')
        job['source'] = response.xpath(r'//*[@id="job-preview"]/div[2]/div[1]/div/div/div[14]/p/text()').get()

        yield job
