install python

create `.env` file with the following rows:
```
CLUSTER_1_HOST=
CLUSTER_1_PORT=
CLUSTER_1_USER=
CLUSTER_1_PASS=

CLUSTER_2_HOST=
CLUSTER_2_PORT=
CLUSTER_2_USER=
CLUSTER_2_PASS=
```
**NOTE:**  leave the `user/pass` rows blank if not used

`pip install -r requirements.txt`

`chmod +x run.sh`

`./run.sh`
