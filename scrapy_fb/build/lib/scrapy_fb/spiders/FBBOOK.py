import datetime
import json
import os
# from .scrapyloop import ScrapyLoop
# ScrapyLoop().loop_crawl(FBBOOK)
import ssl
import time
from json import JSONDecodeError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from bson import ObjectId

import phonenumbers
import requests
# -*- coding: utf-8 -*-
import json
import itertools
import re

import pymongo
import scrapy

from ..items import FbaboutItem2


# '''
# CONCURRENT_REQUESTS_PER_DOMAIN = 100
# CONCURRENT_REQUESTS = 100
# CRAWLERA_URL = http://gravvisoft.crawlera.com
# CRAWLERA_APIKEY = c79ed6d3bb814597b4b26b17dfa299d5
# CRAWLERA_ENABLED = true
# CRAWLERA_DOWNLOAD_TIMEOUT = 200
#
#

class Fbbookinbound22(scrapy.Spider):
    name = 'FBBOOK'
    start_urls = ['https://scrapethissite.com/pages/simple/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapy_fb.pipelines.GRAVVISOFT_LEADSDB_Pipeline': 100,

        },
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy_crawlera.CrawleraMiddleware': 610,
        },
        # 'SPIDER_MIDDLEWARES': {
        #     'scrapy_deltafetch.DeltaFetch': 100,
        # },

        # 'DELTAFETCH_ENABLED': True,

        # "CONCURRENT_REQUESTS_PER_DOMAIN": 256,
        # "CONCURRENT_REQUESTS": 256,
        # "CRAWLERA_URL": "http://gravvisoft.crawlera.com",
        # "CRAWLERA_APIKEY": "c79ed6d3bb814597b4b26b17dfa299d5",
        # "CRAWLERA_ENABLED": True,
        # "CRAWLERA_DOWNLOAD_TIMEOUT": 30,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 32,
        "CONCURRENT_REQUESTS": 32,
        "CRAWLERA_URL": "http://gravvisoft.crawlera.com",
        "CRAWLERA_APIKEY": "c79ed6d3bb814597b4b26b17dfa299d5",
        "CRAWLERA_ENABLED": True,
        "CRAWLERA_DOWNLOAD_TIMEOUT": 200,
        # 'CONCURRENT_REQUESTS': 32,
        # 'CONCURRENT_REQUESTS_PER_DOMAIN': 32,
        #     'DOWNLOAD_TIMEOUT': 600,
        #     'CONCURRENT_REQUESTS': 256,
        #     'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
        #     'CONCURRENT_REQUESTS_PER_IP': 1,
        #
    }

    # def handle_error(self, failure):
    #     self.log("Error Handle: %s" % failure.request)
    #     self.log("Sleeping 60 seconds")
    #     time.sleep(60)
    #     url = 'https://scrapethissite.com/pages/simple/'
    #     yield scrapy.Request(url, self.parse, errback=self.handle_error, dont_filter=True)
    #

    def parse(self, response, **kwargs):

        global city, industry, cityyo, cityies

        indlist = []

        industrylist1 = getattr(self, "industrylist1", "")
        industrylist1_admin = getattr(self, "industrylist1_admin", "")
        industrylistwhatwhat = f'{industrylist1}{industrylist1_admin}'
        # print(industrylistwhatwhat)
        ind = industrylistwhatwhat.split("|")
        for indus in ind:
            if "" != indus:
                indlist.append(indus)
        # print(cit)

        indjoin = "|".join(indlist)
        industry = indjoin.split("|")

        stateies = getattr(self, "stateslist1", "")
        cityyo = getattr(self, "citylist1", "")
        citylist = []

        if stateies:
            cityyo = f"{cityyo}{stateies}"

        cit = cityyo.split("|")
        for c in cit:
            if "" != c:
                citylist.append(c)
        # print(cit)
        # print(citylist)

        cityjoin = "|".join(citylist)
        city = cityjoin.split("|")

        global link1
        link1 = []
        for ind in industry:
            for key in city:
                for n in range(0, 175):
                    link2 = f'https://www.google.com/search?q=site%3Afacebook.com+places+about+"{key}"+{n}+{ind}+&start=0&num=100'
                    link3 = f'https://www.google.com/search?q=site%3Afacebook.com+places+about+"{key}"+{ind}+{n}&start=0&num=100'
                    link4 = f'https://www.google.com/search?q=site%3Afacebook.com+places+about+"{ind}"+{key}+{n}+places+&start=0&num=100'
                    link5 = f'https://www.google.com/search?q=site%3Afacebook.com+places+about+"{key}"+{n}+{ind}+places+&start=0&num=100'
                    link6 = f'https://www.google.com/search?q=site%3Afacebook.com+places+about+"{key}"+{ind}+{n}+places+&start=0&num=100'
                    link7 = f'https://www.google.com/search?q=site%3Afacebook.com+places+about+places+{ind}+"{key}"+{n}+places+&start=0&num=100'

                    link1.append(link2)
                    link1.append(link3)
                    link1.append(link4)
                    link1.append(link5)
                    link1.append(link6)
                    link1.append(link7)

        for link in link1:
            yield scrapy.Request(url=link, callback=self.parse2)

    def parse2(self, response):
        item = FbaboutItem2()
        url = response.xpath('//a/@href').extract()
        for l in url:
            if "facebook.com" in l:
                l = l.replace("/url?q=", '')
                l = l.replace("reviews", "about~")
                l = l.replace("posts", "about~")
                l = l.replace("photos", "about~")
                l = l.replace("videos", "about~")
                l = l.replace("events", "about~")
                l = l.replace("marketplace", "about~")
                l = l.replace("community", "about~")
                l = l.replace("?referrer=services_landing_page", "about~")
                l = l.replace("directory", "~")
                l = l.replace("biz", "~")
                l = l.replace("+%22", "~")
                l = l.replace("facebook.com+", "facebook.com%2B")
                l = l.replace("%2B", "~")
                l = l.replace("biz", "~")
                l = l.replace("people", "~")
                l = l.replace("/?", "~")
                l = l.replace("&", "~")
                l = l.replace("+", "~")
                l = l.replace("%", "~")
                l = l.replace("groups", "~")
                l = l.replace(".php", "~")
                l = l.split("~")[0]
                if "facebook" in l:
                    l = l.split("facebook.com")[1]
                else:
                    pass
                l = f'https://m.facebook.com{l}'
                yield scrapy.Request(url=l, callback=self.parse_fb)

        pagination = response.xpath("//a[contains(text(),'Next')]/@href").extract()
        print(pagination)
        pagination = f'https://www.google.com{pagination}'
        if pagination:
            yield scrapy.Request(url=pagination, callback=self.parse2)

    def parse_fb(self, response):

        if "m." not in response.request.url:
            mobiledisplay = response.request.url.replace("www", "m")
            yield scrapy.Request(url=mobiledisplay, callback=self.parse_fb)

        item = FbaboutItem2()
        print("THIIIS IS TH EMOBILE PARESE")
        global cityies, datadebounce, email_found, phone_found, url_found

        companyfind = response.xpath('//title/text()').extract()
        companyfind1 = companyfind[0]
        company_found1 = companyfind1.replace(" - Home | Facebook", "")
        company_found = company_found1.replace("&amp;", "")
        print(company_found)
        item['company'] = company_found

        body = response.xpath('//*[@id="pages_msite_body_contents"]/*//text()').extract()
        print(body)

        matches = []
        for i in body:
            # print(i)
            find_ph_num = re.findall(
                "(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})", i)
            # print(find_ph_num)
            for p in find_ph_num:
                for match in phonenumbers.PhoneNumberMatcher(p, "US"):
                    phoneage = phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.NATIONAL)
                    if phoneage:
                        phone_found = phoneage
                        item['phone'] = phoneage
                        print(phone_found)
                    else:
                        phone_found = None
                        print(phone_found)

            email_regex = re.findall(
                "[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?",
                i)
            if email_regex:
                print(email_regex[0])
                item['email'] = email_regex[0]
                email_found = email_regex[0]
            else:
                email_found = None

            citylist = []
            # stateies = getattr(self, "stateslist1", "")
            cityies = getattr(self, "citylist1", "")

            # if stateies:
            #     cityies = f"{cityies}{stateies}"

            cit = cityies.split("|")
            for c in cit:
                if "" != c:
                    citylist.append(c)
            # print(cit)
            # print(citylist)

            citjoin = "|".join(citylist)
            # print(citjoin)

            cityies3 = citjoin.replace("|", r"\b|\b")

            citites4 = fr'\b{cityies3}\b'
            ad = " Oshkosh, WI, WI 54904"

            city_found = re.search(citites4, i)
            matches.append(city_found)
            print(city_found)

            if city_found is not None:
                print(city_found)
                item['city'] = i
                print(f'FOUND THE CITY: {i}')
                city_found1 = i
                body1 = response.xpath('//*[@id="pages_msite_body_contents"]/*//text()').extract()
                print(body1)
                for i1 in body1:

                    if "://" in i1:
                        url_found = i1
                        print(i1)

                    indlist = []

                    industrylist1 = getattr(self, "industrylist1", "")
                    industrylist1_admin = getattr(self, "industrylist1_admin", "")
                    industrylistwhatwhat = f'{industrylist1}{industrylist1_admin}'
                    # print(industrylistwhatwhat)
                    ind = industrylistwhatwhat.split("|")
                    for indus in ind:
                        if "" != indus:
                            indlist.append(indus)
                    # print(cit)

                    indjoin = "|".join(indlist)
                    # print(indjoin)

                    indies3 = indjoin.replace("|", r"\b|\b")

                    indtes4 = fr'\b{indies3}\b'

                    industry_found = re.search(indtes4, i1)
                    matches.append(industry_found)

                    if industry_found is not None:
                        item['industry'] = i1
                        industry_found1 = i1
                        print(industry_found)
                        print(f'FOUND THE INDUSTRY: {i1}')
                        conn = pymongo.MongoClient("mongodb+srv://benslow:Grannyboy1@cluster0.kuvzf.mongodb.net",
                                                   ssl_cert_reqs=ssl.CERT_NONE)
                        database = getattr(self, 'database', '')

                        db = conn[database]
                        collection = db['LEADS']
                        query2 = {'phone': phone_found}
                        doc_list2 = collection.find(query2)  # find all data
                        print(doc_list2)

                        phomeduplicate = True if len(list(doc_list2)) else False
                        if phomeduplicate is False or phone_found is None:
                            itemcity = {
                                "date_of_pull": str(datetime.date.today()),
                                'city': city_found1,
                                'company': item["company"],
                                'email': email_found,
                                'industry': industry_found1,
                                'lead_source': response.request.url,
                                'phone': phone_found,
                                "phone_carrier": "",
                                "phone_type": "",
                                'rvm_drop': "",
                                'email_drop': "",
                                "free_email": "",
                                "valid_email": "",
                                'url': url_found,
                                'dnc_email': "False",
                                'dnc_phone': "False",
                                'notes': "",
                                "tags": "",
                                "facebook": "",
                                "houzz": "",
                                "yelp": "",
                                "bbb": "",
                                "yp": "",
                                "instagram": "",
                                "linkedin": "",
                                "twitter": "",
                                "whatsapp": "",
                                "otherlinks": "",
                                "zillow": "",
                                "realtor": "",
                                "google": "",
                                "first_name": "",
                                "cadence_name": "",
                                "opens": "",
                                "clicks": "",
                                "replies": "",
                                "unsubscribes": "",
                                "rvm_sent": False,
                                "rvm_lead_id": "",
                                "rvm_message": "",

                            }
                            print(itemcity)

                            _id = collection.update(itemcity, itemcity, upsert=True)

                            if _id:
                                print(_id["upserted"])
                                if email_found:
                                    database = getattr(self, 'database', '')
                                    ademail = getattr(self, 'klentymail', '')
                                    adklentyapikey = getattr(self, 'klentyapikey', '')
                                    adcadenceName = getattr(self, 'klentyCadence', '')
                                    ### EMAIL API
                                    try:

                                        addprospect = requests.post(
                                            f"https://api.debounce.io/v1/?api=5f43170b7690e&email={email_found}")
                                        datadebounce = json.loads(addprospect.content)
                                    except JSONDecodeError:
                                        pass
                                    if datadebounce:
                                        print(datadebounce['debounce']['send_transactional'])
                                        processemail = datadebounce['debounce']['send_transactional']
                                        collection.find_one_and_update(
                                            {"_id": ObjectId(f'{_id["upserted"]}')},
                                            {'$set': {
                                                'free_email': datadebounce['debounce']['free_email'],
                                                'valid_email': datadebounce['debounce']['result']}})

                                        if processemail == "1":
                                            collection.find_one_and_update(
                                                {"_id": ObjectId(f'{_id["upserted"]}')},
                                                {'$set': {'email_drop': "Valid"}})

                                            addprospect = requests.post(
                                                f'https://app.klenty.com/apis/v1/user/{ademail}/prospects',
                                                json={"Email": f"{email_found}",
                                                      "Company": f"{company_found}",
                                                      "City": f"{city_found}",
                                                      "Department": f"{industry_found}",

                                                      "Phone": f"{phone_found}",
                                                      },
                                                headers={'x-api-key': adklentyapikey})
                                            try:
                                                data = json.loads(addprospect.content)
                                                print(data)
                                            except JSONDecodeError:
                                                pass
                                            addtocadence = requests.post(
                                                f'https://app.klenty.com/apis/v1/user/{ademail}/startcadence',
                                                json={"Email": f"{email_found}",
                                                      "cadenceName": adcadenceName},
                                                headers={'x-api-key': adklentyapikey})
                                            try:
                                                data2 = json.loads(addtocadence.content)
                                                print(data2)
                                            except JSONDecodeError:
                                                pass

                        conn.close()

