# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 20:01:32 2021

@author: NITRO 5 ACER
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 19:23:22 2021

@author: NITRO 5 ACER
"""

import queue
import threading
import random
import time

num_worker_threads = 1


def webservices():
    apiurl = 'https://pokeapi.co/api/v2/pokemon/pikachu'
    response = time.get(apiurl)
    html = response.json()
    print(html["weight"])
    


def run():
    webservices()

def do_work(item):
    print(item)

def source():
    return range(100)


def worker():
  #  return True
    while True:
        item = q.get()
        if item is None:
            break
        do_work(item)
        q.task_done()
    return True
   
    

q = queue.Queue()
threads = []

for i in range(num_worker_threads):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)
    

for item in source():
    q.put(item)

    q.join()

print('stop untuk perhitungan!')


for i in range(num_worker_threads):
    q.put(None)

for t in threads:
    t.join()

