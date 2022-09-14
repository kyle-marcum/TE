import os
import time

import redis
from dotenv import load_dotenv


load_dotenv()

# initialize connection
username = os.getenv('CLUSTER_1_USER')
password = os.getenv('CLUSTER_1_PASS')

r1 = redis.Redis(
    host=os.getenv('CLUSTER_1_HOST'),
    port=os.getenv('CLUSTER_1_PORT'),
    username=None if not username else username,
    password=None if not password else password,
    db=0
)

# test connectivity
try:
  r1.ping()
except:
  print('unable to connect to cluster 1')
  exit()

print('connected successfully to cluster 1')

# increment counter on cluster 1
r1.set('test', 0)

count = 0
while count < 120:
  r1.incrby('test', 2)
  count += 1
  time.sleep(1)
