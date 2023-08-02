from pathlib import Path


BOT_NAME = 'pep_parse'

NEWSPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE, ]

ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

PEP_DOMAIN = 'peps.python.org'
PEP_DOC_URL = 'https://peps.python.org/'


BASE_DIR = Path(__file__).parent.parent
OUTPUT_DIR = 'results'
RESULT_DIR = BASE_DIR / OUTPUT_DIR
RESULT_DIR.mkdir(exist_ok=True)

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
FEEDS = {
    f'{OUTPUT_DIR}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}


DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
