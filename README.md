# Scraping Data from Worldometer using Scrapy

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Project Setup](#project-setup)
- [Creating a Spider](#creating-a-spider)
- [Running the Spider](#running-the-spider)
- [Storing the Scraped Data](#storing-the-scraped-data)
- [Conclusion](#conclusion)

## Introduction
Scrapy is a powerful web scraping framework in Python used to extract data from websites. This guide will walk you through scraping data from Worldometer, a popular statistics website, using Scrapy.

## Installation
First, ensure you have Python installed. Then, install Scrapy using pip:

```sh
pip install scrapy
```

## Project Setup
Create a new Scrapy project:

```sh
scrapy startproject worldometer
cd worldometer
```

This will create a new directory named `worldometer` with the following structure:

```
worldometer/
    scrapy.cfg
    worldometer/
        __init__.py
        items.py
        middlewares.py
        pipelines.py
        settings.py
        spiders/
            __init__.py
```

## Creating a Spider
Create a new spider in the `spiders` directory. For example, `worldometer_spider.py`:

```python
# worldometer/spiders/worldometer_spider.py

import scrapy

class WorldometerSpider(scrapy.Spider):
    name = "worldometer"
    start_urls = [
        'https://www.worldometers.info/coronavirus/'
    ]

    def parse(self, response):
        rows = response.xpath('//table[@id="main_table_countries_today"]/tbody[1]/tr')
        
        for row in rows:
            yield {
                'country': row.xpath('td[2]/text()').get(),
                'total_cases': row.xpath('td[3]/text()').get(),
                'new_cases': row.xpath('td[4]/text()').get(),
                'total_deaths': row.xpath('td[5]/text()').get(),
                'new_deaths': row.xpath('td[6]/text()').get(),
                'total_recovered': row.xpath('td[7]/text()').get(),
                'active_cases': row.xpath('td[8]/text()').get(),
                'serious_critical': row.xpath('td[9]/text()').get(),
                'total_cases_per_million': row.xpath('td[10]/text()').get(),
                'deaths_per_million': row.xpath('td[11]/text()').get(),
                'total_tests': row.xpath('td[12]/text()').get(),
                'tests_per_million': row.xpath('td[13]/text()').get(),
            }
```

## Running the Spider
Navigate to the project root directory and run the spider:

```sh
scrapy crawl worldometer -o worldometer_data.json
```

This command will run the spider and output the scraped data into a file named `worldometer_data.json`.

## Storing the Scraped Data
Scrapy supports various data formats for storing scraped data, such as JSON, CSV, and XML. To store data in CSV format, use the following command:

```sh
scrapy crawl worldometer -o worldometer_data.csv
```

To store data in XML format, use:

```sh
scrapy crawl worldometer -o worldometer_data.xml
```

## Conclusion
You have now successfully scraped data from Worldometer using Scrapy. This guide covered setting up a Scrapy project, creating a spider, running the spider, and storing the scraped data. Scrapy is a versatile tool for web scraping and can be used for a variety of web scraping tasks.

For more advanced usage and customization, refer to the [official Scrapy documentation](https://docs.scrapy.org/en/latest/).
