import os
import multiprocessing

bind = '127.0.0.1:8000'
backlog = 2048
timeout = 30
worker_class = 'gevent'

workers = multiprocessing.cpu_count() * 2 + 1
threads = 4
daemon = True