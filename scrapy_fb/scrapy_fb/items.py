# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy




class FbaboutItem2(scrapy.Item):
    email = scrapy.Field()
    company = scrapy.Field()
    url = scrapy.Field()
    phone = scrapy.Field()
    city = scrapy.Field()
    industry = scrapy.Field()
    lead_source = scrapy.Field()
    email_drop = scrapy.Field()
    rvm_drop = scrapy.Field()
    date_of_pull = scrapy.Field()
    free_email = scrapy.Field()
    valid_email = scrapy.Field()
    phone_carrier = scrapy.Field()
    phone_type = scrapy.Field()
    rvm_lead_id = scrapy.Field()
    rvm_message = scrapy.Field()
    instagram = scrapy.Field()
    linkedin = scrapy.Field()
    twitter = scrapy.Field()
    facebook = scrapy.Field()
    otherlinks = scrapy.Field()
    yelp = scrapy.Field()
    ademail = scrapy.Field()
    adklentyapikey = scrapy.Field()
    adcadenceName = scrapy.Field()

