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
from scrapy import FormRequest

from scrapinghub import ScrapinghubClient
import hashlib
import phonenumbers
import requests
# -*- coding: utf-8 -*-
import json
import itertools
import re

import pymongo
import scrapy
# scrapy crawl FBBOOK -a citylist1="Grayslake,-IL|Barrington,-IL|Cary,-IL|Lake-Villa,-IL|Mchenry,-IL|Park-Ridge,-IL|Elk-Grove-Village,-IL|Highland-Park,-IL|Buffalo-Grove,-IL|Highwood,-IL|Great-Lakes,-IL|Winnetka,-IL|Lincolnshire,-IL|Schaumburg,-IL|Waukegan,-IL|Wauconda,-IL|Round-Lake,-IL|Rolling-Meadows,-IL|Lake-Bluff,-IL|Draper,-UT|Mount-Prospect,-IL|Des-Plaines,-IL|Island-Lake,-IL|Arlington-Heights,-IL|Prospect-Heights,-IL|Glenview,-IL|Glencoe,-IL|Libertyville,-IL|Deerfield,-IL|Hoffman-Estates,-IL|Gurnee,-IL|Fox-River-Grove,-IL|Northbrook,-IL|Sandy,-UT|Ingleside,-IL|North-Chicago,-IL|Mundelein,-IL|Vernon-Hills,-IL|Wheeling,-IL|Palatine,-IL|" -a database="EricLandoll126" -a industrylist1="Appliance-Repair-Service|Architectural-Designer|Cabinets|Carpenter|Carpet-Cleaner|Chimney-Sweeper|Roofing|Cleaning-Service|Concrete-Contractor|Construction-Company|Contractor|Countertops|Damage-Restoration-Service|Deck-&-Patio-Builder|Demolition-&-Excavation-Company|Doors|Electrician|Elevator-Service|Fence-&-Gate-Contractor|Fireplaces|Flooring|Furniture|Garage-Door-Service|Gardener|Roofing-Contractor|Gutter-Cleaning-Service|Handyman|Heating-Ventilating-&-Air-Conditioning-Service|Home-Audio-Visual|Home-Remodeling|Home-Security-Company|House-Painting|Interior-Design-Studio|Janitorial-Service|Landscaping|Lighting|Lumber-Yard|Masonry-Contractor|Moving-Service|Painters|Paving-&-Asphalt-Service|Pest-Control-Service|Roofing|Plumbing-Service|Portable-Building-Service|Portable-Toilet-Rentals|Poultry-Farm|Powder-Coating-Service|Refrigeration-Service|Roofing-Service|Sandblasting-Service|Septic-Tank-Service|Sewer-Service|Solar-Energy-Service|Swimming-Pool-&-Hot-Tub-Service|Tiling-Service|Tree-Cutting-Service|Vinyl-Siding-Company|Water-Treatment-Service|Well-Water-Drilling-Service|Window-Services" -a industrylist1_admin="Appliance-Repair-Service|Appliance-Sales|Appliance-Installation|Appliance-Repair|Cooktop,-Range-&-Stove-Installation|Oven-Installation|Range-Hood-Installation|Appliance-Removal|Oven-Repair|Cooktop,-Range-&-Stove-Repair|Dishwasher-Installation|Architectural-Designer|Cabinets|Custom-Kitchen-Cabinets|Custom-Cabinets|Custom-Bathroom-Vanities|Custom-Cabinet-Doors|Custom-Built-ins|Cabinet-Installation|Cabinet-Sales|Custom-Entertainment-Centers|Custom-Bookcases|Custom-Pantries|Carpenter|Handyman|Carpentry|Custom-Built-ins|Custom-Shelving|Custom-Bookcases|Custom-Cabinets|Finish-Carpentry|Custom-Furniture|Custom-Entertainment-Centers|Custom-Pantries|Custom-Fireplace-Mantels|Carpet-Cleaner|Chimney-Sweeper|Cleaning-Service|Commercial-Cleaning|House-Cleaning|Concrete-Contractor|Concrete-Sales|Patio-Construction|Hardscaping|Stone-Masonry|Retaining-Wall-Construction|Paver-Installation|Masonry|Concrete-Construction|Stone-Installation|Concrete-Driveway-Installation|Driveway-Sealing|Concrete-Driveway-Installation|Concrete-Construction|Hardscaping|Driveway-Repair|Driveway-Resurfacing|Asphalt-Paving|Land-Leveling-&-Grading|Paver-Installation|Masonry|Construction-Company|Contractor|General-Contracting|Home-Remodeling|Kitchen-Remodeling|Bathroom-Remodeling|Home-Additions|Home-Extensions|Custom-Homes|New-Home-Construction|Basement-Remodeling|Deck-Building|Kitchen-Design|Bathroom-Design|Custom-Cabinets|Custom-Kitchen-Cabinets|Custom-Bathroom-Vanities|Custom-Countertops|3D-Rendering|Custom-Pantries|Home-Additions|Custom-Walk-in-Closets|Countertops|Custom-Countertops|Tile-Sales|Countertop-Sales|Countertop-Installation|Backsplash-Installation|Tile-Installation|Natural-Stone-Countertops|Quartz-Countertops|Granite-Countertops|Marble-Countertops|Damage-Restoration-Service|Deck-&-Patio-Builder|Pergola-Construction|Deck-Building|Patio-Construction|Porch-Design-&-Construction|Gazebo-Design-&-Construction|Sunroom-Design-&-Construction|Deck-Design|Trellis-Construction|Patio-Design|Pool-Deck-Design-&-Construction|Demolition-&-Excavation-Company|Doors|Door-Dealer|Custom-Exterior-Doors|Door-Sales|Exterior-Door-Installation|Custom-Interior-Doors|Custom-Folding-Doors|Interior-Door-Installation|Sliding-Door-Installation|Bifold-Doors|Custom-Retractable-Screens|Door-Repair|Electrician|Electricians|Electrical-Installation|Electrical-Repair|Electrical-Inspection|Circuit-Breaker-Installation-&-Repair|Lighting-Design|Electrical-Outlet-&-Light-Switch-Installation|Exhaust-Fan-Installation|House-Wiring|Deck-Lighting-Installation|Home-Energy-Audit|Elevator-Service|Fence-&-Gate-Contractor|Fence-Contractors|Driveway-Gate-Installation|Fence-Installation|Gate-Installation|Fence-Repair|Chain-Link-Fence-Installation|Gate-Repair|Fence-Sales|Wrought-Iron-Fence-Installation|Aluminum-Fence-Installation|Wood-Fence-Installation|Fireplaces|Fireplace-Installation|Fireplace-Sales|Custom-Fireplaces|Gas-Fireplace-Installation|Custom-Fireplace-Mantels|Custom-Fire-Pits|Wood-Stove-Installation|Electric-Fireplace-Installation|Outdoor-Fireplace-Construction|Fireplace-Repair|Flooring|Carpet-Installation|Carpet-Sales|Custom-Rugs|Custom-Flooring|Carpet-Repair|Carpet-Stretching|Rug-Cleaning|Carpet-Cleaning|Flooring-Installation|Laminate-Flooring-Installation|Custom-Flooring|Wood-Floor-Installation|Vinyl-Flooring-Installation|Wood-Flooring-Sales|Flooring-Sales|Tile-Installation|Laminate-Flooring-Sales|Vinyl-Flooring-Sales|Stair-Installation|Railing-Installation|Baluster-Installation|Staircase-Design|Railing-Repair|Stair-Repair|Glass-Railings|Furniture|Antique-Restoration|Furniture-Refinishing|Upholstery-Repair|Custom-Upholstery|Custom-Furniture|Furniture-Repair|Wall-Upholstery|Custom-Drapery|Leather-Repair|Upholstery-Cleaning|Furniture-Repair-&-Upholstery-Service|Custom-Furniture|Pool-Table-Repair|Furniture-Repair|Furniture-Refinishing|Upholstery-Repair|Antique-Restoration|Custom-Tables|Sandblasting|Furniture-Sales|Custom-Furniture|Outdoor-Furniture-Sales|Furniture-Delivery|Custom-Rugs|Custom-Tables|Lighting-Sales|Custom-Pool-Tables|Antique-Furniture-Sales|Custom-Framing|Garage-Door-Service|Garage-Door-Installation|Garage-Door-Repair|Garage-Door-Installation|Garage-Door-Repair|Garage-Door-Sales|Custom-Garage-Doors|Gardener|Glass-Service|Shower-Door-Installation|Shower-Door-Sales|Mirror-Installation|Glass-Installation|Shower-Door-Repair|Stained-Glass-Repair-&-Design|Window-Installation|Glass-Cutting|Glass-Repair|Window-Repair|Gutter-Cleaning-Service|Handyman|Closet-Design|Custom-Walk-in-Closets|Closet-Organization|Space-Planning|Custom-Cabinets|Professional-Organizing|Garage-Storage|Decluttering|Custom-Storage|Sports-Equipment-Storage|Kitchen-Design|Bathroom-Design|Custom-Cabinets|Custom-Kitchen-Cabinets|Custom-Bathroom-Vanities|Custom-Countertops|3D-Rendering|Custom-Pantries|Home-Additions|Custom-Walk-in-Closets|Heating-Ventilating-&-Air-Conditioning-Service|Air-Conditioning-&-Heating|Heating-&-Cooling-Sales-&-Repair|HVAC|Air-Conditioning-Installation|Heat-Pump-Installation|HVAC-Installation|Air-Conditioning-Repair|Furnace-Installation|Oil-to-Gas-Conversion|HVAC-Inspection|Heating-System-Installation|Ventilation-Installation-&-Repair|Thermostat-Repair|Home-Audio-Visual|Home-Automation|Home-Theater-Installation|Outdoor-Audio-Installation|Surround-Sound-Installation|Home-Theater-Design|Security-Camera-Installation|TV-Installation|Smart-Homes|Home-Security-Companies-&-Installation|Home-Audio-Systems|Home-Remodeling|Kitchen-&-Bath-Contractor|Custom-Homes|Home-Remodeling|New-Home-Construction|Home-Additions|Kitchen-Remodeling|Home-Extensions|Bathroom-Remodeling|Architectural-Design|Kitchen-Design|Bathroom-Design|Kitchen-Remodeling|Bathroom-Remodeling|Home-Remodeling|Home-Additions|Cabinet-Installation|Custom-Cabinets|Custom-Kitchen-Cabinets|Home-Extensions|Custom-Bathroom-Vanities|Custom-Countertops|Home-Improvement|Home-Security-Company|House-Painting|Custom-Artwork|Texture-Painting|Decorative-Painting|Mural-Painting|Wall-Stenciling|Faux-Painting|Stained-Glass-Repair-&-Design|Custom-Framing|Art-Installation|Custom-Furniture|Interior-Design-Studio|Home-Staging|Furniture-Selection|Space-Planning|Color-Consulting|Decluttering|Downsizing|Art-Selection|Furniture-Rental|Holiday-Decorating|Feng-Shui-Design|Interior-Design|Kitchen-Design|Bathroom-Design|Bedroom-Design|Living-Room-Design|Space-Planning|Color-Consulting|Furniture-Selection|Kids-Bedroom-Design|Dining-Room-Design|Janitorial-Service|Landscaping|Landscape-Company|Landscape-Architects-&-Landscape-Designers|Landscape-Contractors|Gardeners-&-Lawn-Care|Landscape-Construction|Hardscaping|Landscape-Maintenance|Garden-Design|Patio-Construction|Custom-Fire-Pits|Custom-Water-Features|Paver-Installation|Outdoor-Fireplace-Construction|Pool-Landscaping|Planting|Lawn-Care|Irrigation-System-Installation|Weed-Control|Tree-Pruning|Brush-Clearing|Drought-Tolerant-Landscaping|Lawn-Aeration|Yard-Waste-Removal|Drip-Irrigation-Installation|Lighting|Lighting-Sales|Lighting-Design|Outdoor-Lighting-Design|Lighting-Installation|Outdoor-Lighting-Installation|Landscape-Lighting-Installation|Deck-Lighting-Installation|Recessed-Lighting-Installation|Ceiling-Fan-Installation|Pool-Lighting-Installation|Outdoor-Lighting-Installation|Landscape-Lighting-Installation|Lighting-Installation|Deck-Lighting-Installation|Outdoor-Lighting-Design|Lighting-Design|Lighting-Sales|Home-Automation|Pool-Lighting-Installation|Outdoor-Audio-Installation|Lumber-Yard|Masonry-Contractor|Moving-Service|Piano-Moving|Local-Moving|Long-Distance-Moving|Painters|Painting|Door-Painting|Drywall-Repair|Interior-Painting|Drywall-Texturing|Baseboard-Installation|Interior-Door-Installation|Door-Repair|Ceiling-Painting|Paint-Removal|Backsplash-Installation|Paint-Sales|Wallcovering-Sales|Paving-&-Asphalt-Service|Pest-Control-Service|Plumbing-Service|Plumbers|Plumber|Faucet-Installation|Emergency-Plumbing|Faucet-Repair|Water-Heater-Repair|Plumbing-Repair|Drain-Cleaning|Garbage-Disposal-Repair|Garbage-Disposal-Installation|Water-Heater-Installation|Tankless-Water-Heater-Installation|Water-Heater-Installation-&-Repair-Service|Portable-Building-Service|Portable-Toilet-Rentals|Poultry-Farm|Powder-Coating-Service|Refrigeration-Service|Roofing-Service|Roof-Replacement|Gutter-Installation|Roof-Installation|Asphalt-Shingle-Roofing|Roof-Repair|Metal-Roofing|Roof-Inspection|Composition-Roofing|Gutter-Repair|Soffit-Installation|Sandblasting-Service|Septic-Tank-Service|Sewer-Service|Solar-Energy-Service|Solar-Energy-Systems|Solar-Panel-Installation|Home-Energy-Audit|Solar-Panel-Repair|Solar-Panel-Cleaning|Passive-Solar-Heating-&-Cooling|Solar-Pool-Heating|Solar-Water-Heating|Solar-Tube-Installation|Skylight-Installation|Skylight-Repair|Swimming-Pool-&-Hot-Tub-Service|Swimming-Pool-Cleaner|Hot-Tub-Installation|Hot-Tub-Sales|Custom-Hot-Tubs|Sauna-Installation|Sauna-Sales|Sauna-Repair|Pool-Liner-Replacement|Pool-and-Spa-Repair|Pool-Cleaning-&-Maintenance|Sauna-Repair|Solar-Pool-Heating|Aboveground-Pools|Aboveground-Pool-Liner-Replacement|Pool-Covers|Natural-Swimming-Pools|Swimming-Pool-Design|Swimming-Pool-Construction|Pool-Deck-Design-&-Construction|Pool-Lighting-Installation|Pool-Remodeling|Custom-Hot-Tubs|Natural-Swimming-Pools|Hot-Tub-Installation|Pond-Construction|Sauna-Installation|Tiling-Service|Tree-Cutting-Service|Tree-Pruning|Tree-Removal|Stump-Removal|Tree-Planting|Wood-Chipping|Stump-Grinding|Hedge-Trimming|Mulching|Land-Clearing|Vinyl-Siding-Company|Water-Treatment-Service|Mold-Removal-&-Remediation|Water-Removal|Historic-Building-Conservation|Water-Testing|Indoor-Air-Quality-Testing|Basement-Waterproofing|Attic-Restoration|Fire-Damage-Restoration|Land-Surveying|Popcorn-Ceiling-Removal|Well-Water-Drilling-Service|Window-Services|Window-Replacement|Window-Installation|Custom-Windows|Window-Sales|Window-Repair|Egress-Windows|Bifold-Windows|Trim-Work|Skylight-Installation|Window-Screen-Installation|Window-Installation-Service|Home-Window-Service|Custom-Blinds-&-Shades|Motorized-Blinds|Blinds-&-Shades-Sales|Custom-Drapery|Blind-Installation|Plantation-Shutters|Interior-Shutters|Custom-Retractable-Screens|Exterior-Shades|Exterior-Shutters" -a klentyCadence="Cadence1" -a klentyapikey="60AD20DF50832D00294CD58D" -a klentymail="eric.landoll@n2pub.com" -a stateslist1="None" -a user_id="126" -a vmdapi="3528899"

from ..items import FbaboutItem2

listcount = []
class Fbbookinbound22(scrapy.Spider):
    name = 'FBBOOK'
    # start_urls = ['https://scrapethissite.com/pages/simple/']
    # start_urls = ["https://www.google.com/search?q=(385)%2331-8208",
    #               "https://www.google.com/search?q=(541)%2442-0708",
    #               "https://www.google.com/search?q=(903)%2543-0277",
    #               "https://www.google.com/search?q=(878)%2888-7314",
    #               "https://www.google.com/search?q=(659)%2928-9885",
    #               "https://www.google.com/search?q=(727)%2699-6030",
    #               "https://www.google.com/search?q=(904)%2688-1843",
    #               "https://www.google.com/search?q=(313)%2641-6502",
    #               "https://www.google.com/search?q=(415)%2404-4351",
    #               "https://www.google.com/search?q=(385)%2331-8857",
    #               "https://www.google.com/search?q=(251)%2686-7815",
    #               "https://www.google.com/search?q=(703)%2989-6303",
    #               "https://www.google.com/search?q=(603)%2692-4237",
    #               "https://www.google.com/search?q=(689)%2787-4519",
    #               "https://www.google.com/search?q=(714)%2326-3835",
    #               "https://www.google.com/search?q=(385)%2231-2657",
    #               "https://www.google.com/search?q=(256)%2675-6692",
    #               "https://www.google.com/search?q=(541)%2653-8171",
    #               "https://www.google.com/search?q=(267)%2487-7368",
    #               "https://www.google.com/search?q=(906)%2465-4040",
    #               "https://www.google.com/search?q=(660)%2710-3370",
    #               "https://www.google.com/search?q=(330)%2597-9678",
    #               "https://www.google.com/search?q=(801)%2567-1234",
    #               "https://www.google.com/search?q=(316)%2308-2057",
    #               "https://www.google.com/search?q=(385)%2529-1032",
    #               "https://www.google.com/search?q=(518)%2711-1774",
    #               "https://www.google.com/search?q=(801)%2810-4937",
    #               "https://www.google.com/search?q=(385)%2228-5680",
    #               "https://www.google.com/search?q=(801)%2792-9969",
    #               "https://www.google.com/search?q=(833)%2724-2756",
    #               ]
    custom_settings = {
        'ITEM_PIPELINES': {
            # 'deploytoscloud.pipelines.GRAVVISOFT_LEADSDB_Pipeline': 100,
            # 'deploytoscloud.pipelines.PhonyDuplicatesPipeline': 200,
            # 'deploytoscloud.pipelines.BRIANSCHULLERCityFilterPipeline': 300,

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
        "RETRY_TIMES": 58,
        "RETRY_HTTP_CODES": [500, 502, 503, 504, 400, 401, 403, 404, 405, 406, 407, 408, 409, 410, 429],
        "DOWNLOAD_DELAY": 5,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 2,
        "CONCURRENT_REQUESTS": 2,
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


    def start_requests(self):


        # def parse(self, response, **kwargs):

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
        self.start_urls = []
        for ind in industry:
            for key in city:
                for n in range(0, 6):
                    link2 = f'https://www.google.com/search?q=Phone+number+"{key}"+{n}+{ind}+&start=0&num=100'
                    # yield scrapy.Request(url=link2, callback=self.parse2)
                    link3 = f'https://www.google.com/search?q=Phone+number+{key}+{ind}+{n}&start=0&num=100'
                    link4 = f'https://www.google.com/search?q=Phone+number+{ind}+{key}+{n}+&start=0&num=100'
                    link5 = f'https://www.google.com/search?q=Phone+number+{key}+{n}+{ind}+&start=0&num=100'
                    link6 = f'https://www.google.com/search?q=Phone+number+"{key}"+{ind}+{n}+&start=0&num=100'
                    link7 = f'https://www.google.com/search?q=Phone+number+{ind}+"{key}"+{n}+&start=0&num=100'

                    self.start_urls.append(link2)
                    self.start_urls.append(link3)
                    self.start_urls.append(link4)
                    self.start_urls.append(link5)
                    self.start_urls.append(link6)
                    self.start_urls.append(link7)

        for link in self.start_urls:
            yield scrapy.Request(url=link, callback=self.parse)


    def parse(self, response, **kwargs):

        getit = response.xpath('//body//div').extract()
        phone_number_list = []
        for d in getit:
            find_ph_num = re.findall(
                "(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})", d)
            # print(find_ph_num)
            for p in find_ph_num:
                for match in phonenumbers.PhoneNumberMatcher(p, "US"):
                    phoneage = phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.NATIONAL)
                    if not phoneage:
                        print(f'No phonage')
                    else:
                        phone_found = phoneage
                        # print(phoneage)
                        if phoneage not in phone_number_list:
                            phone_number_list.append(phoneage)
                            # yield scrapy.Request(url=f'https://www.google.com/search?q={phoneage}',
                            #                      callback=self.googlecheck)
                        else:
                            pass
        for phyo in phone_number_list:
            yield scrapy.Request(url=f'https://www.google.com/search?q={phyo}',
                                 callback=self.googlecheck)

    def googlecheck(self, response):
        global city_found1, titleyo, category3, industry_found1, final_city, found_industry
        item = FbaboutItem2()

        findh2 = response.xpath("//h2")
        print(findh2)

        cityitup = response.xpath('//a//h3/text()').extract()
        print(cityitup)
        cityjoin = " ".join(cityitup)
        # for u in url:
        #     print(u)

        for i in findh2:
            titleyo = i.xpath("//h2/span/text()").extract()
            print(titleyo)
        if titleyo:
            print(titleyo[0])
            item["company"] = titleyo[0]

            # followingdiv = response.xpath("//h2/following-sibling::div/*//span").extract()
            # print(followingdiv)
            website = response.xpath("//h2/following-sibling::div/*//div[text()='Website']/ancestor-or-self::a/@href").extract()
            if website:
                item['url'] = website[0]
            else:
                item['url'] = ""




            # print(website[0])

            # with eventlet.Timeout(10):
            #     em = ExtractEmails(url=website[0], depth=1)
            #     emails = em.emails
            #     print(emails)
            # for e in emails:
            #     item['email'] = e
            # for ays in urlgdiv:
            #     print(ays)

            def FindIndustry(string):
                iindustrylist = []
                industrylist1 = getattr(self, "industrylist1", "")
                industrylist1_admin = getattr(self, "industrylist1_admin", "")
                industrylistwhatwhat = f'{industrylist1}{industrylist1_admin}'
                ind = industrylistwhatwhat.split("|")
                for i in ind:
                    if "" != i:
                        iindustrylist.append(i)

                indjoin = "|".join(iindustrylist)
                injoin = indjoin.replace("-", " ")
                # print(citjoin)

                indies3 = injoin.replace("|", r"\b|\b")

                regexind = fr'\b{indies3}\b'
                industryyoo = re.findall(regexind, string)
                return [x for x in industryyoo]

            findh = response.xpath(
                "//h2[contains(text(),'Complementary Results')]/following-sibling::div/div/div//*/span/text()").extract()
            print(findh)
            # indi_list = []
            for f in findh:
                if " in " in f:
                    print(f.title())
                    # indi_list.append(f.title())
            # print(f'IND LISSSSSSST: {indi_list}')
            #         if indi_list:
                    found_industry1 = FindIndustry(f.title())
                    if found_industry1:
                        found_industry = found_industry1[0]
                        item['industry'] = found_industry
                        print(found_industry)
                        print(f'Categorie: {FindIndustry(found_industry)}')

                        phone_list = []
                        followingdiv = response.xpath("//h2/following-sibling::div/*//text()").extract()
                        for d in followingdiv:
                        #     if " | " in d:
                        #         category = d.split("|")
                        #         category2 = category[-1]
                        #         category3 = category2.strip()
                        #         found_industry3 = FindIndustry(category3 + cityjoin)
                        #         found_industry = found_industry3[0]
                        #         item['industry'] = found_industry
                        #         print(f'Categorie: {FindIndustry(category3 + cityjoin)}')

                                # print(d)
                            # print(d)
                            # print(d)
                            find_ph_num = re.findall(
                                "(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})", d)
                            # print(find_ph_num)
                            for p in find_ph_num:
                                for match in phonenumbers.PhoneNumberMatcher(p, "US"):
                                    phoneage = phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.NATIONAL)
                                    if not phoneage:
                                        print(f'No phonage')
                                    else:
                                        phone_found = phoneage
                                        if phone_found not in phone_list:
                                            phone_list.append(phone_found)
                                        print(phoneage)

                        print(f'PHONE FOUND: {phone_list[0]}')
                        item['phone'] = phone_list[0]

                        addressdiv = response.xpath(
                            "//h2/following-sibling::div/*//a[text()='Address']/following::span[1]/text()").extract()

                        print(addressdiv)


                        def FindCity(string):
                            citylist = []
                            stateies = getattr(self, "stateslist1", "")
                            cityies = getattr(self, "citylist1", "")

                            if stateies:
                                cityies = f"{cityies}{stateies}"

                            cit = cityies.split("|")
                            for c in cit:
                                if "" != c:
                                    citylist.append(c)

                            citjoin = "|".join(citylist)
                            cijoin = citjoin.replace("-", " ")
                            # print(citjoin)

                            cityies3 = cijoin.replace("|", r"\b|\b")

                            regex_city = fr'\b{cityies3}\b'
                            ciityyoo = re.findall(regex_city, string)
                            return [x for x in ciityyoo]

                        if addressdiv:
                            city_found1 = FindCity(addressdiv[0])
                            print(f'CITYFOUND: {city_found1}')
                        else:
                            pass
                            # city_found1 = FindCity(cityjoin)
                            # print(f'CITYFOUND: {city_found1}')
                        if city_found1:
                            final_city = city_found1[0]
                            item['city'] = final_city
                            print(f'Final City: {final_city}')

                        if found_industry and final_city:
                            print(f'FOUND BOTH THE INDUSTRY AND CITY: {found_industry} {final_city}')
                            urlccciittyy = 'https://www.gravvisoft.com/api/lead/'
                            itemcity = {
                                "user_id": getattr(self, 'user_id', ''),
                                "date": str(datetime.date.today()),
                                'city': final_city,
                                'company': item["company"],
                                'industry': found_industry,
                                'phone': item['phone'],
                                'url': item['url'],
                                "calls_actual": "0",

                            }
                            print(itemcity)
                            x = requests.post(urlccciittyy, data=itemcity)
                            # print(x.content)
                            data = x.json()
                            # print(data., x.content, x.text)
                            # datayo = json.loads(x)
                            print(data)
                            if data:
                                data_id = data['id']
                                print(data_id)
                                yield scrapy.Request(url=website[0], callback=self.getemail, meta={'city': item['city'],
                                                                                                   'company': item["company"],
                                                                                                   'industry': found_industry,
                                                                                                   'phone': item['phone'],                                                               "data_id": data_id})
                                yield item

    def getemail(self, response):
        global datadebounce
        item = FbaboutItem2()

        city = response.meta['city']
        industry = response.meta['industry']
        phone = response.meta['phone']
        company = response.meta['company']
        data_id = response.meta['data_id']
        print(f'THIS IS THE META DATA: {data_id}')
        bodytext = response.xpath('//body//text()').extract()
        bodyjoin = " ".join(bodytext)
        # print(bodyjoin)
        emailfind = re.findall(
            "[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?",
            bodyjoin)
        # print(emailfind)
        if emailfind:

            item['email'] = emailfind[0]

            ademail = getattr(self, 'klentymail', '')
            adklentyapikey = getattr(self, 'klentyapikey', '')
            adcadenceName = getattr(self, 'klentyCadence', '')
            ### EMAIL API
            try:
                addprospect = requests.post(
                    f"https://api.debounce.io/v1/?api=5f43170b7690e&email={item['email']}")
                datadebounce = json.loads(addprospect.content)
            except JSONDecodeError:
                pass
            if not datadebounce:
                item['free_email'] = None
                item['valid_email'] = None
                item['email_drop'] = None

            if datadebounce:
                print(datadebounce['debounce']['send_transactional'])
                processemail = datadebounce['debounce']['send_transactional']

                item['free_email'] = datadebounce['debounce']['send_transactional']
                item['valid_email'] = datadebounce['debounce']['reason']

                if processemail != "1":
                    item['email_drop'] = None

                elif processemail == "1":
                    item["email_drop"] = "Valid"

                    addprospect = requests.post(
                        f'https://app.klenty.com/apis/v1/user/{ademail}/prospects',
                        json={"Email": f"{item['email']}",
                              "Company": f"{company}",
                              "City": f"{city}",
                              "Department": f"{industry}",
                              "Phone": f"{phone}",
                              },
                        headers={'x-api-key': adklentyapikey})
                    try:
                        data = json.loads(addprospect.content)
                        print(data)
                    except JSONDecodeError:
                        pass
                    addtocadence = requests.post(
                        f'https://app.klenty.com/apis/v1/user/{ademail}/startcadence',
                        json={"Email": f"{item['email']}",
                              "cadenceName": adcadenceName},
                        headers={'x-api-key': adklentyapikey})
                    try:
                        data2 = json.loads(addtocadence.content)
                        print(data2)
                    except JSONDecodeError:
                        pass


            emailccciittyy = f'https://www.gravvisoft.com/api/lead/update/{data_id}/'
            itemcity2 = {
                'email': item['email'],
                'phone': phone,
                'valid_email': item['valid_email'],
                "free_email": item['free_email'] ,
                "email_drop": item["email_drop"],
            }
            print(itemcity2)
            x2 = requests.put(emailccciittyy, data=itemcity2)
            if x2.status_code == 200:
                print(f'EMAIL ADDED SUCCESSFULLY')
            # print(x2.content)

