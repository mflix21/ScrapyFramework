# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class BdjobsCategoryLink(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()

class BdjobsLink(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()

class Job(scrapy.Item):
    title = scrapy.Field()
    company = scrapy.Field()
    vacancies = scrapy.Field()
    jobContext = scrapy.Field()
    jobResposiblities = scrapy.Field()
    jobType = scrapy.Field()
    workplace = scrapy.Field()
    education = scrapy.Field()
    experience = scrapy.Field()
    additionalRequirments = scrapy.Field()
    joblocation = scrapy.Field()
    salary = scrapy.Field()
    benefits = scrapy.Field()
    source = scrapy.Field()
