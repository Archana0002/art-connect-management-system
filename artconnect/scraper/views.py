import json
import os
from django.shortcuts import render
from django.http import JsonResponse
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scraper.scraper.spiders.event_scrapper import EventScraper

def scrape_events(request):
    city = request.GET.get("city", "goa")
    formatted_city = city.lower().replace(" ", "-")

    # Define the URL dynamically
    start_url = f"https://insider.in/all-events-in-{formatted_city}/art-%26-craft"

    # Run the Scrapy spider dynamically
    process = CrawlerProcess(get_project_settings())
    process.crawl(EventScraper, start_urls=[start_url])
    process.start()

    # Load the scraped data
    try:
        with open("scraper/scraped_data.json", "r", encoding="utf-8") as f:
            events = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        events = []

    # ✅ Render the events in an HTML page instead of returning JSON
    return render(request, "scraper.html", {"events": events})
