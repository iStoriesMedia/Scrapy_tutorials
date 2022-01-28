import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class BookSpider(CrawlSpider):
  name = 'all_books'
  start_urls = ['https://book24.ru/']

  rules = (
      Rule(LinkExtractor(allow='catalog')),
      Rule(LinkExtractor(allow='product'), callback='parse_items')
  )
        
  def parse_items(self, response):
    yield {
          'first_type': response.css('a.breadcrumbs__link.smartLink span::text')[1].get().strip(),
          'second_type': response.css('a.breadcrumbs__link.smartLink span::text')[2].get().strip(),
          'third_type': response.css('a.breadcrumbs__link.smartLink span::text')[3].get().strip(),
          'name': response.css('h1.product-detail-page__title::text').get().strip(),
          'buy': response.css('p.product-detail-page__purchased-text::text').get().split()[1],                                                  
         }
  