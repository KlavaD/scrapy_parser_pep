from urllib.parse import urljoin

import scrapy

from pep_parse.constants import PEP_DOC_URL
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [PEP_DOC_URL.replace('https://', '').strip('/')]
    start_urls = [PEP_DOC_URL, ]

    def parse(self, response):
        for pep_link in response.css('a.pep::attr(href)').getall():
            yield response.follow(
                urljoin(self.start_urls[0], pep_link),
                callback=self.parse_pep
            )

    def parse_pep(self, response):
        data = {
            'number': int(response.css(
                '#pep-page-section ul li:nth-child(3)::text'
            ).get().replace('PEP ', '').strip()),
            'name': response.css('.page-title::text').get(),
            'status': response.css(
                'dt:contains("Status") + dd abbr::text'
            ).get()
        }
        yield PepParseItem(data)
