This Scrapy project is the backend code for my B2B webscraping.  This particular script focuses on pulling data from google.   I use Zyte(formerly Crawlera) to handle proxy rotation.  I use shub and docker to package this script up and send it over to Zyte.  

My Django application uses the Zyte api to pass data back and forth.  The user is also able to select what industries they want to focus on, as well as location requirements.  Those arguments are sent to Zyte through a post request.
