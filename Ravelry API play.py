# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 17:48:01 2021

@author: catal
"""
import pdb
import requests
from requests.adapters import HTTPAdapter
import sqlite3 as s

connection = s.connect("ravelry_play_db.db")
c = connection.cursor()

# create mini yarn table
# c.execute("""CREATE TABLE ravelry_yarns(
#   [id] INTEGER PRIMARY KEY
# , [is_discontinued] TEXT
# , [gauge_divisor] INTEGER
# , [grams] INTEGER
# , [machine_washable] TEXT
# )""")

# c.execute("""CREATE TABLE ravelry_yarns(
# [id] INTEGER PRIMARY KEY
# , [discontinued] TEXT
# , [gauge_divisor] INTEGER
# , [grams] INTEGER
# , [machine_washable] TEXT
# , [max_gauge] REAL
# , [min_gauge] REAL
# , [name] TEXT
# , [permalink] TEXT
# , [texture] TEXT
# , [thread_size] INTEGER
# , [wpi] INTEGER
# , [yardage] INTEGER
# , [notes_html] TEXT
# , [min_needle_size_id] INTEGER
# , [min_needle_size_us] REAL
# , [min_needle_size_metric] REAL
# , [min_needle_size_us_steel] TEXT
# , [min_needle_size_crochet] TEXT
# , [min_needle_size_knitting] TEXT
# , [min_needle_size_hook] TEXT
# , [min_needle_size_name] TEXT
# , [max_needle_size_id] INTEGER
# , [max_needle_size_us] REAL
# , [max_needle_size_metric] REAL
# , [max_needle_size_us_steel] TEXT
# , [max_needle_size_crochet] TEXT
# , [max_needle_size_knitting] TEXT
# , [max_needle_size_hook] TEXT
# , [max_needle_size_name] TEXT
# , [min_hook_size] TEXT
# , [max_hook_size] TEXT
# , [personal_attributes] TEXT
# , [yarn_weight_crochet_gauge] INTEGER
# , [yarn_weight_id] INTEGER
# , [yarn_weight_knit_gauge] INTEGER
# , [yarn_weight_min_gauge] INTEGER
# , [yarn_weight_name] TEXT
# , [yarn_weight_ply] INTEGER
# , [yarn_company_id] INTEGER
# , [yarn_company_name] TEXT
# , [yarn_company_permalink] TEXT
# , [yarn_fibers0_id] INTEGER
# , [yarn_fibers0_percentage] INTEGER
# , [yarn_fibers0_fiber_type_animal_fiber] INTEGER
# , [yarn_fibers0_fiber_type_id] INTEGER
# , [yarn_fibers0_fiber_type_name] TEXT
# , [yarn_fibers0_fiber_type_synthetic] TEXT
# , [yarn_fibers0_fiber_type_vegetable_fiber] TEXT
# , [yarn_fibers0_fiber_category_id] INTEGER
# , [yarn_fibers0_fiber_category_name] TEXT
# , [yarn_fibers0_fiber_category_permalink] TEXT
# , [yarn_fibers01id] INTEGER
# , [yarn_fibers1_percentage] INTEGER
# , [yarn_fibers1_fiber_type_animal_fiber] TEXT
# , [yarn_fibers1_fiber_type_id] INTEGER
# , [yarn_fibers1_fiber_type_name] TEXT
# , [yarn_fibers1_fiber_type_synthetic] TEXT
# , [yarn_fibers1_fiber_type_vegetable_fiber] TEXT
# , [yarn_fibers1_fiber_category_id] INTEGER
# , [yarn_fibers1_fiber_category_name] TEXT
# , [yarn_fibers1_fiber_category_permalink] TEXT
# , [yarn_fibers2_id] INTEGER
# , [yarn_fibers2_percentage] INTEGER
# , [yarn_fibers2_fiber_type_animal_fiber] TEXT
# , [yarn_fibers2_fiber_type_id] INTEGER
# , [yarn_fibers2_fiber_type_name] TEXT
# ,[yarn_fibers2_fiber_type_synthetic] TEXT
# , [yarn_fibers2_fiber_type_vegetable_fiber] TEXT
# , [yarn_fibers2_fiber_category_id] INTEGER
# , [yarn_fibers2_fiber_category_name] TEXT
# , [yarn_fibers2_fiber_category_permalink] TEXT
# )""")

with requests.Session() as a_session:
    auth_name = "read-046277a3027f680ebe3fa030e755eb34"
    auth_pass = "O+mL0KzfjgQ1eLA7K8FO9s28QPvr6QuiL+pOvFHZ"
    a_session.auth = (auth_name, auth_pass)

    ravelry_adapter = HTTPAdapter(max_retries=3)
    a_session.mount('https://ravelry.com', ravelry_adapter)
    response_2 = a_session.get('https://api.ravelry.com/patterns/search.json?query=velvet-cache-cou')
    print(response_2.json())

#     # get() yarns
#     for num in range(10060, 10066):  # TODO change range as needed
#         yarn_id = str(num)
#         url_base = 'https://api.ravelry.com/'
#         endpoint_patterns = 'patterns.json?ids='
#         endpoint_yarns1 = 'yarns.json?ids='
#         response1 = a_session.get(url_base + endpoint_yarns1 + yarn_id)
#         if response1.status_code == 200:
#             # TODO get all categories
#             response_1_id = response1.json()['yarns'][yarn_id]['id']
#             response_1_discontinued = response1.json()['yarns'][yarn_id]['discontinued']
#             response_1_gauge_divisor = response1.json()['yarns'][yarn_id]['gauge_divisor']
#             response_1_grams = response1.json()['yarns'][yarn_id]['grams']
#             response_1_machine_washable = response1.json()['yarns'][yarn_id]['machine_washable']
#             response_1_max_gauge = response1.json()['yarns'][yarn_id]['max_gauge']
#             response_1_min_gauge = response1.json()['yarns'][yarn_id]['min_gauge']
#             response_1_name = response1.json()['yarns'][yarn_id]['name']
#             response_1_permalink = response1.json()['yarns'][yarn_id]['permalink']
#             response_1_texture = response1.json()['yarns'][yarn_id]['texture']
#             response_1_thread_size = response1.json()['yarns'][yarn_id]['thread_size']
#             response_1_wpi = response1.json()['yarns'][yarn_id]['wpi']
#             response_1_yardage = response1.json()['yarns'][yarn_id]['yardage']
#             response_1_notes_html = response1.json()['yarns'][yarn_id]['notes_html'].replace("\"", "\'")
#             if response1.json()['yarns'][yarn_id]['min_needle_size'] != None:
#                 response_1_min_needle_size_id = response1.json()['yarns'][yarn_id]['min_needle_size']['id']
#                 response_1_min_needle_size_us = response1.json()['yarns'][yarn_id]['min_needle_size']['us']
#                 response_1_min_needle_size_metric = response1.json()['yarns'][yarn_id]['min_needle_size']['metric']
#                 response_1_min_needle_size_us_steel = response1.json()['yarns'][yarn_id]['min_needle_size']['us_steel']
#                 response_1_min_needle_size_crochet = response1.json()['yarns'][yarn_id]['min_needle_size']['crochet']
#                 response_1_min_needle_size_knitting = response1.json()['yarns'][yarn_id]['min_needle_size']['knitting']
#                 response_1_min_needle_size_hook = response1.json()['yarns'][yarn_id]['min_needle_size']['hook']
#                 response_1_min_needle_size_name = response1.json()['yarns'][yarn_id]['min_needle_size']['name']
#             else:
#                 response_1_min_needle_size_id = None
#                 response_1_min_needle_size_us = None
#                 response_1_min_needle_size_metric = None
#                 response_1_min_needle_size_us_steel = None
#                 response_1_min_needle_size_crochet = None
#                 response_1_min_needle_size_knitting = None
#                 response_1_min_needle_size_hook = None
#                 response_1_min_needle_size_name = None
#             if response1.json()['yarns'][yarn_id]['max_needle_size'] != None:
#                 response_1_max_needle_size_id = response1.json()['yarns'][yarn_id]['max_needle_size']['id']
#                 response_1_max_needle_size_us = response1.json()['yarns'][yarn_id]['max_needle_size']['us']
#                 response_1_max_needle_size_metric = response1.json()['yarns'][yarn_id]['max_needle_size']['metric']
#                 response_1_max_needle_size_us_steel = response1.json()['yarns'][yarn_id]['max_needle_size']['us_steel']
#                 response_1_max_needle_size_crochet = response1.json()['yarns'][yarn_id]['max_needle_size']['crochet']
#                 response_1_max_needle_size_knitting = response1.json()['yarns'][yarn_id]['max_needle_size']['knitting']
#                 response_1_max_needle_size_hook = response1.json()['yarns'][yarn_id]['max_needle_size']['hook']
#                 response_1_max_needle_size_name = response1.json()['yarns'][yarn_id]['max_needle_size']['name']
#             else:
#                 response_1_max_needle_size_id = None
#                 response_1_max_needle_size_us = None
#                 response_1_max_needle_size_metric = None
#                 response_1_max_needle_size_us_steel = None
#                 response_1_max_needle_size_crochet = None
#                 response_1_max_needle_size_knitting = None
#                 response_1_max_needle_size_hook = None
#                 response_1_max_needle_size_name = None
#             response_1_min_hook_size = response1.json()['yarns'][yarn_id]['min_hook_size']
#             response_1_max_hook_size = response1.json()['yarns'][yarn_id]['max_hook_size']
#             response_1_personal_attributes = response1.json()['yarns'][yarn_id]['personal_attributes']
#             response_1_yarn_weight_crochet_gauge = response1.json()['yarns'][yarn_id]['yarn_weight']['crochet_gauge']
#             response_1_yarn_weight_id = response1.json()['yarns'][yarn_id]['yarn_weight']['id']
#             response_1_yarn_weight_knit_gauge = response1.json()['yarns'][yarn_id]['yarn_weight']['knit_gauge']
#             response_1_yarn_weight_min_gauge = response1.json()['yarns'][yarn_id]['yarn_weight']['min_gauge']
#             response_1_yarn_weight_name = response1.json()['yarns'][yarn_id]['yarn_weight']['name']
#             response_1_yarn_weight_ply = response1.json()['yarns'][yarn_id]['yarn_weight']['ply']
#             response_1_yarn_company_id = response1.json()['yarns'][yarn_id]['yarn_company']['id']
#             response_1_yarn_company_name = response1.json()['yarns'][yarn_id]['yarn_company']['name']
#             response_1_yarn_company_permalink = response1.json()['yarns'][yarn_id]['yarn_company']['permalink']
#             response_1_yarn_fibers0_id = response1.json()['yarns'][yarn_id]['yarn_fibers'][0]['id']
#             response_1_yarn_fibers0_percentage = response1.json()['yarns'][yarn_id]['yarn_fibers'][0]['percentage']
#             response_1_yarn_fibers0_fiber_type_animal_fiber = response1.json()['yarns'][yarn_id]['yarn_fibers'][0]['fiber_type']['animal_fiber']
#             response_1_yarn_fibers0_fiber_type_id = response1.json()['yarns'][yarn_id]['yarn_fibers'][0]['fiber_type']['id']
#             response_1_yarn_fibers0_fiber_type_name = response1.json()['yarns'][yarn_id]['yarn_fibers'][0]['fiber_type']['name']
#             response_1_yarn_fibers0_fiber_type_synthetic = response1.json()['yarns'][yarn_id]['yarn_fibers'][0]['fiber_type']['synthetic']
#             response_1_yarn_fibers0_fiber_type_vegetable_fiber = response1.json()['yarns'][yarn_id]['yarn_fibers'][0]['fiber_type']['vegetable_fiber']
#             response_1_yarn_fibers0_fiber_category_id = response1.json()['yarns'][yarn_id]['yarn_fibers'][0]['fiber_category']['id']
#             response_1_yarn_fibers0_fiber_category_name = response1.json()['yarns'][yarn_id]['yarn_fibers'][0]['fiber_category']['name']
#             response_1_yarn_fibers0_fiber_category_permalink = response1.json()['yarns'][yarn_id]['yarn_fibers'][0]['fiber_category']['permalink']
#             try:
#                 response_1_yarn_fibers01id = response1.json()['yarns'][yarn_id]['yarn_fibers'][1]['id']
#                 response_1_yarn_fibers1_percentage = response1.json()['yarns'][yarn_id]['yarn_fibers'][1]['percentage']
#                 response_1_yarn_fibers1_fiber_type_animal_fiber = response1.json()['yarns'][yarn_id]['yarn_fibers'][1]['fiber_type']['animal_fiber']
#                 response_1_yarn_fibers1_fiber_type_id = response1.json()['yarns'][yarn_id]['yarn_fibers'][1]['fiber_type']['id']
#                 response_1_yarn_fibers1_fiber_type_name = response1.json()['yarns'][yarn_id]['yarn_fibers'][1]['fiber_type']['name']
#                 response_1_yarn_fibers1_fiber_type_synthetic = response1.json()['yarns'][yarn_id]['yarn_fibers'][1]['fiber_type']['synthetic']
#                 response_1_yarn_fibers1_fiber_type_vegetable_fiber = response1.json()['yarns'][yarn_id]['yarn_fibers'][1]['fiber_type']['vegetable_fiber']
#                 response_1_yarn_fibers1_fiber_category_id = response1.json()['yarns'][yarn_id]['yarn_fibers'][1]['fiber_category']['id']
#                 response_1_yarn_fibers1_fiber_category_name = response1.json()['yarns'][yarn_id]['yarn_fibers'][1]['fiber_category']['name']
#                 response_1_yarn_fibers1_fiber_category_permalink = response1.json()['yarns'][yarn_id]['yarn_fibers'][1]['fiber_category']['permalink']
#             except:
#                 response_1_yarn_fibers01id = None
#                 response_1_yarn_fibers1_percentage = None
#                 response_1_yarn_fibers1_fiber_type_animal_fiber = None
#                 response_1_yarn_fibers1_fiber_type_id = None
#                 response_1_yarn_fibers1_fiber_type_name = None
#                 response_1_yarn_fibers1_fiber_type_synthetic = None
#                 response_1_yarn_fibers1_fiber_type_vegetable_fiber = None
#                 response_1_yarn_fibers1_fiber_category_id = None
#                 response_1_yarn_fibers1_fiber_category_name = None
#                 response_1_yarn_fibers1_fiber_category_permalink = None
#             try:
#                 response_1_yarn_fibers2_id = response1.json()['yarns'][yarn_id]['yarn_fibers'][2]['id']
#                 response_1_yarn_fibers2_percentage = response1.json()['yarns'][yarn_id]['yarn_fibers'][2]['percentage']
#                 response_1_yarn_fibers2_fiber_type_animal_fiber = response1.json()['yarns'][yarn_id]['yarn_fibers'][2]['fiber_type']['animal_fiber']
#                 response_1_yarn_fibers2_fiber_type_id = response1.json()['yarns'][yarn_id]['yarn_fibers'][2]['fiber_type']['id']
#                 response_1_yarn_fibers2_fiber_type_name = response1.json()['yarns'][yarn_id]['yarn_fibers'][2]['fiber_type']['name']
#                 response_1_yarn_fibers2_fiber_type_synthetic = response1.json()['yarns'][yarn_id]['yarn_fibers'][2]['fiber_type']['synthetic']
#                 response_1_yarn_fibers2_fiber_type_vegetable_fiber = response1.json()['yarns'][yarn_id]['yarn_fibers'][2]['fiber_type']['vegetable_fiber']
#                 response_1_yarn_fibers2_fiber_category_id = response1.json()['yarns'][yarn_id]['yarn_fibers'][2]['fiber_category']['id']
#                 response_1_yarn_fibers2_fiber_category_name = response1.json()['yarns'][yarn_id]['yarn_fibers'][2]['fiber_category']['name']
#                 response_1_yarn_fibers2_fiber_category_permalink = response1.json()['yarns'][yarn_id]['yarn_fibers'][2]['fiber_category']['permalink']
#             except:
#                 response_1_yarn_fibers2_id = None
#                 response_1_yarn_fibers2_percentage = None
#                 response_1_yarn_fibers2_fiber_type_animal_fiber = None
#                 response_1_yarn_fibers2_fiber_type_id = None
#                 response_1_yarn_fibers2_fiber_type_name = None
#                 response_1_yarn_fibers2_fiber_type_synthetic = None
#                 response_1_yarn_fibers2_fiber_type_vegetable_fiber = None
#                 response_1_yarn_fibers2_fiber_category_id = None
#                 response_1_yarn_fibers2_fiber_category_name = None
#                 response_1_yarn_fibers2_fiber_category_permalink = None

#             # insert pattern
#             # c.execute(f"""INSERT INTO ravelry_yarns
#             #           (id, is_discontinued, gauge_divisor, grams, machine_washable)
#             #           VALUES ({response_1_id}, "{response_1_discontinued}", "{response_1_gauge_divisor}", "{response_1_grams}","{response_1_machine_washable}")""")
#             c.execute(f"""INSERT INTO ravelry_yarns
#                       (id, discontinued, gauge_divisor, grams, machine_washable, max_gauge, min_gauge, name, permalink, texture, thread_size, wpi, yardage, notes_html, min_needle_size_id, min_needle_size_us, min_needle_size_metric, min_needle_size_us_steel, min_needle_size_crochet, min_needle_size_knitting, min_needle_size_hook, min_needle_size_name, max_needle_size_id, max_needle_size_us, max_needle_size_metric, max_needle_size_us_steel, max_needle_size_crochet, max_needle_size_knitting, max_needle_size_hook, max_needle_size_name, min_hook_size, max_hook_size, personal_attributes, yarn_weight_crochet_gauge, yarn_weight_id, yarn_weight_knit_gauge, yarn_weight_min_gauge, yarn_weight_name, yarn_weight_ply, yarn_company_id, yarn_company_name, yarn_company_permalink, yarn_fibers0_id, yarn_fibers0_percentage, yarn_fibers0_fiber_type_animal_fiber, yarn_fibers0_fiber_type_id, yarn_fibers0_fiber_type_name, yarn_fibers0_fiber_type_synthetic, yarn_fibers0_fiber_type_vegetable_fiber, yarn_fibers0_fiber_category_id, yarn_fibers0_fiber_category_name, yarn_fibers0_fiber_category_permalink, yarn_fibers01id, yarn_fibers1_percentage, yarn_fibers1_fiber_type_animal_fiber, yarn_fibers1_fiber_type_id, yarn_fibers1_fiber_type_name, yarn_fibers1_fiber_type_synthetic, yarn_fibers1_fiber_type_vegetable_fiber, yarn_fibers1_fiber_category_id, yarn_fibers1_fiber_category_name, yarn_fibers1_fiber_category_permalink, yarn_fibers2_id, yarn_fibers2_percentage, yarn_fibers2_fiber_type_animal_fiber, yarn_fibers2_fiber_type_id, yarn_fibers2_fiber_type_name,yarn_fibers2_fiber_type_synthetic, yarn_fibers2_fiber_type_vegetable_fiber, yarn_fibers2_fiber_category_id, yarn_fibers2_fiber_category_name, yarn_fibers2_fiber_category_permalink)
#                       VALUES ( "{response_1_id}" , "{response_1_discontinued}" , "{response_1_gauge_divisor}" , "{response_1_grams}" , "{response_1_machine_washable}" , "{response_1_max_gauge}" , "{response_1_min_gauge}" , "{response_1_name}" , "{response_1_permalink}" , "{response_1_texture}" , "{response_1_thread_size}" , "{response_1_wpi}" , "{response_1_yardage}" , "{response_1_notes_html}" , "{response_1_min_needle_size_id}" , "{response_1_min_needle_size_us}" , "{response_1_min_needle_size_metric}" , "{response_1_min_needle_size_us_steel}" , "{response_1_min_needle_size_crochet}" , "{response_1_min_needle_size_knitting}" , "{response_1_min_needle_size_hook}" , "{response_1_min_needle_size_name}" , "{response_1_max_needle_size_id}" , "{response_1_max_needle_size_us}" , "{response_1_max_needle_size_metric}" , "{response_1_max_needle_size_us_steel}" , "{response_1_max_needle_size_crochet}" , "{response_1_max_needle_size_knitting}" , "{response_1_max_needle_size_hook}" , "{response_1_max_needle_size_name}" , "{response_1_min_hook_size}" , "{response_1_max_hook_size}" , "{response_1_personal_attributes}" , "{response_1_yarn_weight_crochet_gauge}" , "{response_1_yarn_weight_id}" , "{response_1_yarn_weight_knit_gauge}" , "{response_1_yarn_weight_min_gauge}" , "{response_1_yarn_weight_name}" , "{response_1_yarn_weight_ply}" , "{response_1_yarn_company_id}" , "{response_1_yarn_company_name}" , "{response_1_yarn_company_permalink}" , "{response_1_yarn_fibers0_id}" , "{response_1_yarn_fibers0_percentage}" , "{response_1_yarn_fibers0_fiber_type_animal_fiber}" , "{response_1_yarn_fibers0_fiber_type_id}" , "{response_1_yarn_fibers0_fiber_type_name}" , "{response_1_yarn_fibers0_fiber_type_synthetic}" , "{response_1_yarn_fibers0_fiber_type_vegetable_fiber}" , "{response_1_yarn_fibers0_fiber_category_id}" , "{response_1_yarn_fibers0_fiber_category_name}" , "{response_1_yarn_fibers0_fiber_category_permalink}" , "{response_1_yarn_fibers01id}" , "{response_1_yarn_fibers1_percentage}" , "{response_1_yarn_fibers1_fiber_type_animal_fiber}" , "{response_1_yarn_fibers1_fiber_type_id}" , "{response_1_yarn_fibers1_fiber_type_name}" , "{response_1_yarn_fibers1_fiber_type_synthetic}" , "{response_1_yarn_fibers1_fiber_type_vegetable_fiber}" , "{response_1_yarn_fibers1_fiber_category_id}" , "{response_1_yarn_fibers1_fiber_category_name}" , "{response_1_yarn_fibers1_fiber_category_permalink}" , "{response_1_yarn_fibers2_id}" , "{response_1_yarn_fibers2_percentage}" , "{response_1_yarn_fibers2_fiber_type_animal_fiber}" , "{response_1_yarn_fibers2_fiber_type_id}" , "{response_1_yarn_fibers2_fiber_type_name}" ,"{response_1_yarn_fibers2_fiber_type_synthetic}" , "{response_1_yarn_fibers2_fiber_type_vegetable_fiber}" , "{response_1_yarn_fibers2_fiber_category_id}" , "{response_1_yarn_fibers2_fiber_category_name}" , "{response_1_yarn_fibers2_fiber_category_permalink}" )""")
#         connection.commit()

# connection.row_factory = s.Row
# # print all rows
# rows = c.execute('SELECT personal_attributes FROM ravelry_yarns')
# for row in rows:
#     print(row)

c.close()
connection.close()

