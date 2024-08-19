import scrapy
import pandas as  pd
from bs4 import BeautifulSoup
from utils import *
import os
import time
from scrapy.selector import Selector


my_file = open("stang__parts_details_links.txt", "r") 
data = my_file.read() 
  
# replacing end splitting the text  
# when newline ('\n') is seen. 
data_into_list = data.split("\n")
s=['https://stang-parts.de/en/20-exhaust'] 

my_file.close() 
main_pd=pd.DataFrame(columns=['title','price','stock','image'])
#main_pd.loc[len(main_pd.index)]=['s','sdd','ass','asa']



class StangePartsLinkProductsSpider(scrapy.Spider):
    name = "stange__parts_link_products"
    allowed_domains = ["stang-parts.de"]
    start_urls = s
    def parse(self, response):
        #p= response.css('section#products div.thumbnail-container div.product-right .product-title').css('a::text')

        #product_block=response.css('section#products div.thumbnail-container')
        #product_image=a=response.css('section#products div.thumbnail-container img').attrib['src']
        #p= response.css('section#products div.thumbnail-container div.product-price-and-shipping').css('span.price::text')
        #response.css('section#products div.thumbnail-container div.availability span.pl-availability').get()
        #aa=response.css('section#products div.thumbnail-container div.availability span.pl-availability').getall()
        #print(type(aa))
        #print(Get_stock_text(aa))
        #product_title=response.css('section#products div.thumbnail-container img')
        #for i in product_title:
            #print(i.attrib['src'])
        #response.css('section#products div.thumbnail-container div.product-price-and-shipping span.price::text').getall()
        #a=response.css('section#products div.thumbnail-container div.product-right .product-title a::text').getall()
        product_block=response.css('section#products div.thumbnail-container')
        os.system('cls')
        product_title=response.css('section#products div.thumbnail-container div.product-right .product-title a::text').getall()
        product_price=response.css('section#products div.thumbnail-container div.product-price-and-shipping span.price::text').getall()
        product_img=response.css('section#products div.thumbnail-container img::attr(src)').getall()
        product_stock=response.css('section#products div.thumbnail-container div.availability span.pl-availability').getall()
        for i in range(len(product_block)):
            main_pd.loc[len(main_pd.index)]=[product_title[i],product_price[i],Get_stock_text(product_stock[i]),product_img[i]]
        print(main_pd)
        main_pd.to_csv('pandas.csv')
        '''
        print(len(product_img))
        for i in product_img:
            print(i.attrib['src'])
        print(main_pd)
        pass
        '''
