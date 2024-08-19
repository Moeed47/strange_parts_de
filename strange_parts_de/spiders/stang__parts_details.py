import scrapy
import config


print (config.proxy_ip)
class StangPartsDetailsSpider(scrapy.Spider):
    name = "stang__parts_details"
    allowed_domains = ["stang-parts.de"]
    start_urls = ["https://stang-parts.de"]

    def parse(self, response):
        print (config.proxy_ip)
        a=response.css('div.block_content').css('a')
        link_list=[]
        for i in a:
            link_list.append(i.css('a').attrib['href'])
        filename = 'stang__parts_details_links.txt'
        with open(filename, 'w') as file:
            
            for i in range(len(link_list)):
                file.write(link_list[i]+ "\n")
        pass
