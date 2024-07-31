import scrapy


class WorldometerSpider(scrapy.Spider):
    name = "worldometer"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country"]

    def parse(self, response):
        # title = response.xpath('//h1/text()').get()
        countries = response.xpath('//td/a')

        # country_name = response.xpath(".//td[2]/a/text()").getall()
        # link = response.xpath(".//td[2]/a/@href").getall()
        # population = response.xpath('//td[3][1]/text()').getall()
        # yearly_change = response.xpath('//td[4][1]/text()').getall()
        # net_change = response.xpath('//td[5][1]/text()').getall()
        # density = response.xpath('//td[6][1]/text()').getall()
        # land_area = response.xpath('//td[7][1]/text()').getall()
        # migrants = response.xpath('//td[8][1]/text()').getall()
        # fertility_rate = response.xpath('//td[9][1]/text()').getall()
        # median_age = response.xpath('//td[10][1]/text()').getall()
        # urban_pop = response.xpath('//td[11][1]/text()').getall()
        # world_share = response.xpath('//td[12][1]/text()').getall()
        #
        for country in countries:
            country_name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            # absolute_url
            #1st method
            # absolute_url = f"https://www.worldometers.info/{link}"
            # 2nd method
            # absolute_url = response.urljoin(link)
            # 3rd method
            # relative url
            yield response.follow(url=link,callback=self.parse_country) # call this parse_country and enters into the link

            # yield scrapy.Request(url=absolute_url)

            # yield {
            #     # 'titles': title,
            #     'country_name':country_name ,
            #     'link':link,
            # #     'population': population,
            # #     'yearly_change':yearly_change,
            # #     'net_change': net_change,
            # #     'density':density,
            # #     'land_area':land_area,
            # #     'migrants':migrants,
            # #     'fertility_rate':fertility_rate,
            # #     'median_age':median_age,
            # #     'urban_pop':urban_pop,
            # #     'world_share':world_share,
            # }
        # this function is to scrap information from the country link
    def parse_country(self,response):
        rows = response.xpath("//table[contains(@class,'table')]/tbody/tr")

        for row in rows:
            year = row.xpath('.//td[1]/text()').get()
            population = row.xpath('.//td[2]/text()').get()
            yearly_change_pct = row.xpath('.//td[3]/text()').get()
            yearly_change = row.xpath('.//td[4]/text()').get()
            migrants = row.xpath('.//td[5]/text()').get()
            median_age = row.xpath('.//td[6]/text()').get()
            fertility_rate = row.xpath('.//td[7]/text()').get()
            density_p_km2 = row.xpath('.//td[8]/text()').get()
            urban_pop_pct = row.xpath('.//td[9]/text()').get()
            urban_pop = row.xpath('.//td[10]/text()').get()
            share_of_world_pop_pct = row.xpath('.//td[11]/text()').get()
            world_pop = row.xpath('.//td[12]/text()').get()
            global_rank = row.xpath('.//td[13]/text()').get()


            yield {
        #     # 'titles': title,
        #     'country_name':country_name ,
        #     'link':link,
            'year':year,
            'population': population,
            'yearly_change_pct':yearly_change_pct,
            'yearly_change':yearly_change,
            'migrants': migrants,
            'median_age':median_age,
            'fertility_rate':fertility_rate,
            'density_p_km2':density_p_km2,
            'urban_pop_pct':urban_pop_pct,
            'urban_pop':urban_pop,
            'share_of_world_pop_pct':share_of_world_pop_pct,
            'world_pop':world_pop,
            'global_rank':global_rank,

        }


#%%
# (//div[@class='table-responsive'])[1]//td[3]) this one
# (//td[contains(text(),'2024')])[3]
# //body[1]/div[2]/div[3]/div[1]/div[1]/div[5]/table[1]/tbody[1]/tr[1]/td[1]
# //div[@class='row']//div[5]
# (//div[@class='table-responsive'])[1]//td[3]
# (//td[contains(text(),'2024')])[3]