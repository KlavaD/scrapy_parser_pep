from urllib.parse import urljoin

import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import PEP_DOMAIN, URL_HTTPS, RESULT_DIR


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [PEP_DOMAIN, ]
    start_urls = []
    for domain in allowed_domains:
        start_urls.append(URL_HTTPS + domain + '/')

    def parse(self, response):
        RESULT_DIR.mkdir(exist_ok=True)
        for pep_link in response.css('a.pep::attr(href)').getall():
            yield response.follow(
                urljoin(self.start_urls[0], pep_link),
                callback=self.parse_pep
            )

    def parse_pep(self, response):
        yield PepParseItem(
            number=response.css(
                '#pep-page-section ul li:nth-child(3)::text'
            ).get().replace('PEP ', '').strip(),
            name=response.css('.page-title::text').get(),
            status=response.css(
                'dt:contains("Status") + dd abbr::text'
            ).get()
        )
