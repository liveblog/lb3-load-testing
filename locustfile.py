from locust import HttpLocust, TaskSet, task
from locust import events
from locust.stats import global_stats
import csv
import os
import time

BLOG_ID = os.environ.get('BLOG_ID')


class UserBehavior(TaskSet):
    @task(1)
    def posts(self):
        url = '/api/client_blogs/{blog}/posts?max_results=20&page=1&source=%7B%22query%22:' + \
            '%7B%22filtered%22:%7B%22filter%22:%7B%22and%22:%5B%7B%22term%22:%7B%22post_stat' + \
            'us%22:%22open%22%7D%7D,%7B%22not%22:%7B%22term%22:%7B%22deleted%22:true%7D%7D%' + \
            '7D%5D%7D%7D%7D,%22sort%22:%5B%7B%22order%22:%7B%22order%22:%22desc%22,%22missi' + \
            'ng%22:%22_last%22,%22unmapped_type%22:%22long%22%7D%7D%5D%7D'
        self.client.get(url.format(blog=BLOG_ID))

    @task(1)
    def profile(self):
        url = '/api/client_blogs/{blog}/posts?page=1&source=%7B%22sort' + \
            '%22:%5B%7B%22_updated%22:%7B%22order%22:%22desc%22%7D%7D%5D,%22query%22:%7B%22filt' + \
            'ered%22:%7B%22filter%22:%7B%22and%22:%5B%7B%22range%22:%7B%22_updated%22:%7B%22gt%' + \
            '22:%222015-10-15T15:12:18%2B00:00%22%7D%7D%7D%5D%7D%7D%7D%7D'
        self.client.get(url.format(blog=BLOG_ID))


def on_quitting():
    requests_csv = global_stats.aggregated_stats()
    if not os.path.exists('results'):
        os.makedirs('results')
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    with open('results/%s.csv' % (timestamp), 'w') as csvfile:
        fieldnames = ['enpoint', 'median_response_time', 'num_requests']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for key, value in requests_csv.stats.entries.items():
            writer.writerow({
                'enpoint': ' '.join(key),
                'median_response_time': value.median_response_time,
                'num_requests': value.num_requests
            })

events.quitting += on_quitting

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 5000
