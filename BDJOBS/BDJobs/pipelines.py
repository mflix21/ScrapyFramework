# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3 as sq

class BdjobsPipeline:
    def __init__(self):
        self.connection = sq.connect("BDjobs.db")
        self.cursor = self.connection.cursor()
        self.create()

    def create(self):
        self.cursor.execute("""DROP TABLE IF EXISTS jobdetails""")
        self.cursor.execute("""CREATE TABLE jobdetails(
            title TEXT,
            company TEXT,
            vacancies INT,
            jobContext TEXT,
            jobResposiblities TEXT,
            jobType TEXT,
            workplace TEXT,
            education TEXT,
            experience TEXT,
            additionalRequirments TEXT,
            joblocation TEXT,
            salary TEXT,
            benefits TEXT,
            source TEXT
        )""")

    def process_item(self, item, spider):
        self.insert(item)
        return item

    def insert(self, item):
        self.cursor.execute("""INSERT INTO jobdetails VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (
            item['title'], item['company'], item['vacancies'], item['jobContext'],
            item['jobResposiblities'], item['jobType'], item['workplace'], item['education'],
            item['experience'], item['additionalRequirments'], item['joblocation'],
            item['salary'], item['benefits'], item['source']
        ))
        self.connection.commit()





class BdjobsCatWiseJobsPipeline:
    def __init__(self):
        self.connection = sq.connect("BDjobs.db")
        self.cursor = self.connection.cursor()
        self.create01()

    def create01(self):
        self.cursor.execute("""DROP TABLE IF EXISTS jobscategorydetails""")
        self.cursor.execute("""CREATE TABLE jobscategorydetails(
            title TEXT,
            link TEXT
        )""")

    def process_item(self, item, spider):
        self.insert01(item)
        return item

    def insert01(self, item):
        self.cursor.execute("""INSERT INTO jobscategorydetails VALUES(?,?)""", (
            item['title'], item['link']
        ))
        self.connection.commit()



class BdjobsCategoryJobsPipeline:
    def __init__(self):
        self.connection = sq.connect("BDjobs.db")
        self.cursor = self.connection.cursor()
        self.create02()

    def create02(self):
        self.cursor.execute("""DROP TABLE IF EXISTS jobscategory""")
        self.cursor.execute("""CREATE TABLE jobscategory(
            title TEXT,
            link TEXT
        )""")

    def process_item(self, item, spider):
        self.insert02(item)
        return item

    def insert02(self, item):
        self.cursor.execute("""INSERT INTO jobscategory VALUES(?,?)""", (
            item['title'], item['link']
        ))
        self.connection.commit()