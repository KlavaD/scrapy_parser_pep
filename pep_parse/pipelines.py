import csv
import datetime as dt
from _csv import QUOTE_NONE
from collections import defaultdict

from pep_parse.settings import RESULT_DIR, DATETIME_FORMAT, BASE_DIR, OUTPUT_DIR

BASE_DIR = BASE_DIR


class PepParsePipeline:

    def open_spider(self, spider):
        self.count_status_peps = defaultdict(int)

    def process_item(self, item, spider):
        self.count_status_peps[item['status']] += 1
        return item

    def close_spider(self, spider):
        now_formatted = dt.datetime.now().strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        results_dir = BASE_DIR / OUTPUT_DIR
        file_path = results_dir / file_name
        with open(file_path, mode='w', encoding='utf-8') as f:
            csv.writer(
                f,
                dialect=csv.unix_dialect(),
                quoting=QUOTE_NONE
            ).writerows(
                (
                    ('Статус', 'Количество'),
                    *self.count_status_peps.items(),
                    ('Всего', sum(self.count_status_peps.values())),
                )
            )
