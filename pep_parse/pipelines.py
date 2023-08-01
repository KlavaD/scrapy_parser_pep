import csv
from collections import defaultdict
import datetime as dt

from pep_parse.constants import OUTPUT_DIR, BASE_DIR

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'


class PepParsePipeline:
    count_status_peps = defaultdict(int)

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.count_status_peps[item['status']] += 1
        return item

    def close_spider(self, spider):
        now_formatted = dt.datetime.now().strftime(DATETIME_FORMAT)
        results_dir = BASE_DIR / OUTPUT_DIR
        results_dir.mkdir(exist_ok=True)
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = results_dir / file_name
        results = [
            ('Статус', 'Количество'),
            *self.count_status_peps.items(),
            ('Всего', sum(self.count_status_peps.values())),
        ]
        with open(file_path, mode='w', encoding='utf-8') as f:
            csv.writer(
                f,
                dialect=csv.unix_dialect()
            ).writerows(results)
