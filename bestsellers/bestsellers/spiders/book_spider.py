import scrapy

class BookSpider(scrapy.Spider):
  name = 'book24'
  start_urls = ['https://book24.ru/knigi-bestsellery/']

  
  def parse(self, response):
    
      for link in response.css('div.product-card__image-holder a::attr(href)'):
        yield response.follow(link, callback=self.parse_book) 
      
      for i in range (1, 25):
        next_page = f'https://book24.ru/knigi-bestsellery/page-{i}/'
        yield response.follow(next_page, callback=self.parse)

        
  def parse_book(self, response):
    yield{
          'name': response.css('h1.product-detail-page__title::text').get().strip(),
          'buy': response.css('p.product-detail-page__purchased-text::text').get().split()[1],                                                  
          'type': response.css('div.product-characteristic__value a::attr(title)')[2].get()
            }
  