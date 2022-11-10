import os
from dotenv import load_dotenv

from CouncilProcess import CouncilProcess
_ = load_dotenv()

urls = os.environ.get("URLS").split(',')

for url in urls:
    process = CouncilProcess(url)
    process.run()

