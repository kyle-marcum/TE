import os
import time

import redis
from dotenv import load_dotenv


load_dotenv()

# initialize connection
username = os.getenv('CLUSTER_2_USER')
password = os.getenv('CLUSTER_2_PASS')

r2 = redis.Redis(
    host=os.getenv('CLUSTER_2_HOST'),
    port=os.getenv('CLUSTER_2_PORT'),
    username=None if not username else username,
    password=None if not password else password,
    db=0
)

# test connectivity
try:
  r2.ping()
except:
  print('unable to connect to cluster 2')
  exit()

print('connected successfully to cluster 2')

# increment counter on cluster 1
count = 0
while count < 120:
  r2.decr('test')
  count += 1
  time.sleep(1)
