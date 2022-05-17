import os

# Enable debugging for detailed logs
DEBUG = (os.getenv('DEBUG', 'False') == 'True')

# KAFKA Settings
KAFKA_SERVER = os.getenv('KAFKA_SERVER', 'localhost:9092')

# Scheduled Message Worker Settings
WORKER_STATUS_LIST = ['READY', 'WORKING', 'DONE', 'ERROR']
WORKER_READY_POLL_FREQ = 5
WORKER_WORKING_POLL_FREQ = 10

# Scheduled JOB Settings
JOB_STATUS_LIST = ['READY', 'WORKING', 'DONE', 'ERROR']
JOB_POLL_FREQ = 15
JOB_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

# Scheduled Messages Topic Settings
SM_TOPIC = 'SCHEDULED_MESSAGES'
SM_TOPIC_PARTITIONS = 50
SM_CONSUMER_GROUP_NAME = '__SM_GROUP'
SM_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

# Scheduled Message Bucketting Configuration
SM_MINIUMUM_DELAY = 5
SM_MAXIUMUM_DELAY = 80
SM_BUCKETS_MULTIPLICATION_RATIO = 2
SM_PARTITIONS_PER_BUCKET = 50
SM_BUCKET_TOPIC_FORMAT = '__SM_BUCKET_$start$_$end$'

# Configuration Server Settings
SERVER_HOST = os.getenv('SERVER_HOST', '0.0.0.0')
SERVER_PORT = os.getenv('SERVER_PORT', '8000')