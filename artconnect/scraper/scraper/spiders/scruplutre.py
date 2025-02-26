import scrapy
import json
from ..items import ScraperItem

class sclupture_scraper(scrapy.Spider):
    name = "sclupture"

    def __init__(self, start_urls=None, *args, **kwargs):
        super(sclupture_scraper, self).__init__(*args, **kwargs)
        self.start_urls = start_urls or [
            "https://www.metmuseum.org/art/collection/search?showOnly=withImage&department=3"
        ]

    def parse(self, response):
        items = []
        all_div_items = response.css('figure.collection-object_collectionObject__SuPct')

        for e_items in all_div_items:
            item = ScraperItem()
            item['head'] = e_items.css('.collection-object_link__qM3YR::text').get()
            item['image_url'] = e_items.css('.collection-object_image__XVQPm.collection-object_gridView__8kZLF::attr(src)').get()
            items.append(dict(item))

        # Save data to JSON
        with open("scraper/scraped_data_scluptrue.json", "w", encoding="utf-8") as f:
            json.dump(items, f, ensure_ascii=False, indent=4)

        self.log(f"Scraped {len(items)} items")
