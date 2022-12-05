from threading import Timer
from CouncilProcess import CouncilProcess
import random
import os
from dotenv import load_dotenv

_ = load_dotenv()


def start_process(url2):
    process = CouncilProcess(url2)
    process.run()
    # set_timer(url2)


def set_timer(url1):
    if bool(int(os.environ.get("TEST_MODE"))):
        t = Timer(5, start_process, [url1])
    else:
        t = Timer(get_random_time(), start_process, [url1])
    t.start()


def get_random_time():
    return random.randint(600, 3600)


urls = os.environ.get("URLS").split(',')

for url in urls:
    set_timer(url)
