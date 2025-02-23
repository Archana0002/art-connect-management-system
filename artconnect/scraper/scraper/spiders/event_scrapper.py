import scrapy
import json
from ..items import ScraperItem

class EventScraper(scrapy.Spider):
    name = "event"

    def __init__(self, start_urls=None, *args, **kwargs):
        super(EventScraper, self).__init__(*args, **kwargs)
        self.start_urls = start_urls or []

    def parse(self, response):
        items = []
        all_div_items = response.css('li.card-list-item')

        for e_items in all_div_items:
            item = ScraperItem()
            item['head'] = e_items.css('.css-17ztqjg::text').get()
            item['image_url'] = e_items.css('#event_image img::attr(src)').get()
            items.append(dict(item))

        # Save data to JSON
        with open("scraper/scraped_data.json", "w", encoding="utf-8") as f:
            json.dump(items, f, ensure_ascii=False, indent=4)

        self.log(f"Scraped {len(items)} items")
