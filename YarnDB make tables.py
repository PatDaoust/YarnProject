# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 18:32:48 2021

@author: catal
"""

import requests
from requests.adapters import HTTPAdapter
import sqlite3 as s

connection = s.connect("ravelry_db.db")
c = connection.cursor()

# create full sized pattern table
c.execute("""CREATE TABLE ravelry_patterns(
  [id] INTEGER PRIMARY KEY
, [name] TEXT
, [yarn_weight_description] TEXT
, [craft_type] TEXT
, [notes] TEXT
, [is_free] TEXT
, [created_at] TEXT
, [gauge] REAL
, [gauge_divisor] INTEGER
, [permalink] TEXT
, [updated_at] TEXT
, [yardage] INTEGER
, [yardage_max] INTEGER
, [personal_attributes]
, [gauge_description] TEXT
, [pattern_author_id] INTEGER
, [pattern_needle_sizes_us] INTEGER
, [pattern_needle_sizes_metric] INTEGER
, [pattern_needle_sizes_us_steel] TEXT
, [pattern_needle_sizes_crochet] TEXT
, [pattern_needle_sizes_knitting] TEXT
, [pattern_needle_sizes_hook] TEXT
, [pattern_needle_sizes_name] TEXT
, [yarn_weight_crochet_gauge] INTEGER
, [yarn_weight_knit_gauge] INTEGER
, [yarn_weight_min_gauge] INTEGER
, [yarn_weight_name] TEXT
, [yarn_weight_ply] INTEGER
, [yarn_weight_wpi] INTEGER
, [pattern_categories_id] INTEGER
, [pattern_categories_name] TEXT
, [categories_parent_name] TEXT
, [categories_parent_parent_name] TEXT
, [categories_parent_parent_parent_name] TEXT
, [pattern_attributes] TEXT
, [pattern_author_name] TEXT
, [pattern_author_notes] TEXT
, [pattern_author_permalink] TEXT
, [pattern_type_is_clothing] TEXT
, [pattern_type_id] INTEGER
, [pattern_type_name] TEXT
)""")

# create full sized yarn table
c.execute("""CREATE TABLE ravelry_yarns(
[id] INTEGER PRIMARY KEY
, [discontinued] TEXT
, [gauge_divisor] INTEGER
, [grams] INTEGER
, [machine_washable] TEXT
, [max_gauge] REAL
, [min_gauge] REAL
, [name] TEXT
, [permalink] TEXT
, [texture] TEXT
, [thread_size] INTEGER
, [wpi] INTEGER
, [yardage] INTEGER
, [notes_html] TEXT
, [min_needle_size_id] INTEGER
, [min_needle_size_us] REAL
, [min_needle_size_metric] REAL
, [min_needle_size_us_steel] TEXT
, [min_needle_size_crochet] TEXT
, [min_needle_size_knitting] TEXT
, [min_needle_size_hook] TEXT
, [min_needle_size_name] TEXT
, [max_needle_size_id] INTEGER
, [max_needle_size_us] REAL
, [max_needle_size_metric] REAL
, [max_needle_size_us_steel] TEXT
, [max_needle_size_crochet] TEXT
, [max_needle_size_knitting] TEXT
, [max_needle_size_hook] TEXT
, [max_needle_size_name] TEXT
, [min_hook_size] TEXT
, [max_hook_size] TEXT
, [personal_attributes] TEXT
, [yarn_weight_crochet_gauge] INTEGER
, [yarn_weight_id] INTEGER
, [yarn_weight_knit_gauge] INTEGER
, [yarn_weight_min_gauge] INTEGER
, [yarn_weight_name] TEXT
, [yarn_weight_ply] INTEGER
, [yarn_company_id] INTEGER
, [yarn_company_name] TEXT
, [yarn_company_permalink] TEXT
, [yarn_fibers0_id] INTEGER
, [yarn_fibers0_percentage] INTEGER
, [yarn_fibers0_fiber_type_animal_fiber] INTEGER
, [yarn_fibers0_fiber_type_id] INTEGER
, [yarn_fibers0_fiber_type_name] TEXT
, [yarn_fibers0_fiber_type_synthetic] TEXT
, [yarn_fibers0_fiber_type_vegetable_fiber] TEXT
, [yarn_fibers0_fiber_category_id] INTEGER
, [yarn_fibers0_fiber_category_name] TEXT
, [yarn_fibers0_fiber_category_permalink] TEXT
, [yarn_fibers01id] INTEGER
, [yarn_fibers1_percentage] INTEGER
, [yarn_fibers1_fiber_type_animal_fiber] TEXT
, [yarn_fibers1_fiber_type_id] INTEGER
, [yarn_fibers1_fiber_type_name] TEXT
, [yarn_fibers1_fiber_type_synthetic] TEXT
, [yarn_fibers1_fiber_type_vegetable_fiber] TEXT
, [yarn_fibers1_fiber_category_id] INTEGER
, [yarn_fibers1_fiber_category_name] TEXT
, [yarn_fibers1_fiber_category_permalink] TEXT
, [yarn_fibers2_id] INTEGER
, [yarn_fibers2_percentage] INTEGER
, [yarn_fibers2_fiber_type_animal_fiber] TEXT
, [yarn_fibers2_fiber_type_id] INTEGER
, [yarn_fibers2_fiber_type_name] TEXT
, [yarn_fibers2_fiber_type_synthetic] TEXT
, [yarn_fibers2_fiber_type_vegetable_fiber] TEXT
, [yarn_fibers2_fiber_category_id] INTEGER
, [yarn_fibers2_fiber_category_name] TEXT
, [yarn_fibers2_fiber_category_permalink] TEXT
)""")

connection.commit()
c.close()
connection.close()
