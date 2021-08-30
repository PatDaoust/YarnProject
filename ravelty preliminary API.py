# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 11:41:46 2021

@author: catal
"""

import requests


class APIError(Exception):
    pass


resp = requests.get('https://www.ravelry.com/patterns/search#craft=crochet.json')
if resp.status_code != 200:
    # This means something went wrong.
    raise APIError('GET /tasks/ {}'.format(resp.status_code))
print(resp.text)


