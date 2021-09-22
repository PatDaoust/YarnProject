# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 18:34:41 2021

@author: catal
"""

import requests
from requests.adapters import HTTPAdapter
import sqlite3 as s
import pdb


def get_and_store_pattern(num):
    """assumes num is an int, representing the pattern ID of the desired yarn
    stores the yarn data to the database
    returns None
    """
    pattern_id = str(num)
    url_base = 'https://api.ravelry.com/'
    endpoint_patterns = 'patterns.json?ids='
    response1 = a_session.get(url_base + endpoint_patterns + pattern_id)
    if response1.status_code == 200:
        response_1_name = response1.json()['patterns'][pattern_id]["name"].replace("\"", "")
        response1_yarn_weight_description = response1.json()['patterns'][pattern_id]["yarn_weight_description"]
        response1_craft_type = response1.json()['patterns'][pattern_id]["craft"]["name"]
        response1_notes = response1.json()['patterns'][pattern_id]["notes"]
        if response1_notes:
            response1_notes = response1.json()['patterns'][pattern_id]["notes"].replace("\"", "\'")
        response1_is_free = str(response1.json()['patterns'][pattern_id]["free"])
        response1_created_at = response1.json()['patterns'][pattern_id]['created_at']
        response1_gauge = response1.json()['patterns'][pattern_id]['gauge']
        response1_gauge_divisor = response1.json()['patterns'][pattern_id]['gauge_divisor']
        response1_permalink = response1.json()['patterns'][pattern_id]['permalink']
        response1_updated_at = response1.json()['patterns'][pattern_id]['updated_at']
        response1_yardage = response1.json()['patterns'][pattern_id]['yardage']
        response1_yardage_max = response1.json()['patterns'][pattern_id]['yardage_max']
        response1_personal_attributes = response1.json()['patterns'][pattern_id]['personal_attributes']
        response1_gauge_description = response1.json()['patterns'][pattern_id]['gauge_description']
        if response1_gauge_description:
            response1_gauge_description = response1.json()['patterns'][pattern_id]['gauge_description'].replace("\"", "inch")
        if response1.json()['patterns'][pattern_id]['pattern_needle_sizes']:
            response1_pattern_needle_sizes_us = response1.json()['patterns'][pattern_id]['pattern_needle_sizes'][0]['us']
            response1_pattern_needle_sizes_metric = response1.json()['patterns'][pattern_id]['pattern_needle_sizes'][0]['metric']
            response1_pattern_needle_sizes_us_steel = response1.json()['patterns'][pattern_id]['pattern_needle_sizes'][0]['us_steel']
            response1_pattern_needle_sizes_crochet = response1.json()['patterns'][pattern_id]['pattern_needle_sizes'][0]['crochet']
            response1_pattern_needle_sizes_knitting = response1.json()['patterns'][pattern_id]['pattern_needle_sizes'][0]['knitting']
            response1_pattern_needle_sizes_hook = response1.json()['patterns'][pattern_id]['pattern_needle_sizes'][0]['hook']
            response1_pattern_needle_sizes_name = response1.json()['patterns'][pattern_id]['pattern_needle_sizes'][0]['name']
        else:
            response1_pattern_needle_sizes_us = None
            response1_pattern_needle_sizes_metric = None
            response1_pattern_needle_sizes_us_steel = None
            response1_pattern_needle_sizes_crochet = None
            response1_pattern_needle_sizes_knitting = None
            response1_pattern_needle_sizes_hook = None
            response1_pattern_needle_sizes_name = None
        try:
            response1_yarn_weight_crochet_gauge = response1.json()['patterns'][pattern_id]['yarn_weight']['crochet_gauge']
            response1_yarn_weight_knit_gauge = response1.json()['patterns'][pattern_id]['yarn_weight']['knit_gauge']
            response1_yarn_weight_knit_gauge = response1.json()['patterns'][pattern_id]['yarn_weight']['knit_gauge']
            response1_yarn_weight_min_gauge = response1.json()['patterns'][pattern_id]['yarn_weight']['min_gauge']
            response1_yarn_weight_name = response1.json()['patterns'][pattern_id]['yarn_weight']['name']
            response1_yarn_weight_ply = response1.json()['patterns'][pattern_id]['yarn_weight']['ply']
            response1_yarn_weight_wpi = response1.json()['patterns'][pattern_id]['yarn_weight']['wpi']
        except KeyError:
            response1_yarn_weight_crochet_gauge = None
            response1_yarn_weight_knit_gauge = None
            response1_yarn_weight_knit_gauge = None
            response1_yarn_weight_min_gauge = None
            response1_yarn_weight_name = None
            response1_yarn_weight_ply = None
            response1_yarn_weight_wpi = None
        response1_pattern_categories_id = response1.json()['patterns'][pattern_id]['pattern_categories'][0]['id']
        response1_pattern_categories_name = response1.json()['patterns'][pattern_id]['pattern_categories'][0]['name']
        try:
            response1_categories_parent_name = response1.json()['patterns'][pattern_id]['pattern_categories'][0]['parent']['name']
            try:
                response1_categories_parent_parent_name = response1.json()['patterns'][pattern_id]['pattern_categories'][0]['parent']['parent']['name']
                try:
                    response1_categories_parent_parent_parent_name = response1.json()['patterns'][pattern_id]['pattern_categories'][0]['parent']['parent']['parent']['name']
                except KeyError:
                    response1_categories_parent_parent_parent_name = None
            except KeyError:
                response1_categories_parent_parent_name = None
                response1_categories_parent_parent_parent_name = None
        except KeyError:
            response1_categories_parent_name = None
            response1_categories_parent_parent_name = None
            response1_categories_parent_parent_parent_name = None
        response1_pattern_attributes = str(response1.json()['patterns'][pattern_id]['pattern_attributes'])
        response1_pattern_author_id = response1.json()['patterns'][pattern_id]['pattern_author']['id']
        response1_pattern_author_name = response1.json()['patterns'][pattern_id]['pattern_author']['name']
        if response1_pattern_author_name:
            response1_pattern_author_name = response1.json()['patterns'][pattern_id]['pattern_author']['name'].replace("\"","")
        response1_pattern_author_notes = response1.json()['patterns'][pattern_id]['pattern_author']['notes']
        if response1_pattern_author_notes:
            response1_pattern_author_notes = response1.json()['patterns'][pattern_id]['pattern_author']['notes'].replace("\"", "\'")
        response1_pattern_author_permalink = response1.json()['patterns'][pattern_id]['pattern_author']['permalink']
        response1_pattern_type_is_clothing = response1.json()['patterns'][pattern_id]['pattern_type']['clothing']
        response1_pattern_type_id = response1.json()['patterns'][pattern_id]['pattern_type']['id']
        response1_pattern_type_name = response1.json()['patterns'][pattern_id]['pattern_type']['name']
        # insert patterns
        c.execute(f"""INSERT INTO ravelry_patterns
                  (id, name, yarn_weight_description, craft_type,notes, is_free, created_at, gauge, gauge_divisor, permalink, updated_at, yardage, yardage_max, personal_attributes, personal_attributes, gauge_description, pattern_needle_sizes_us, pattern_needle_sizes_metric, pattern_needle_sizes_us_steel, pattern_needle_sizes_crochet, pattern_needle_sizes_knitting, pattern_needle_sizes_hook, pattern_needle_sizes_name, yarn_weight_crochet_gauge, yarn_weight_knit_gauge, yarn_weight_min_gauge, yarn_weight_name, yarn_weight_ply, yarn_weight_wpi, pattern_categories_id, pattern_categories_name, categories_parent_name, categories_parent_parent_name, categories_parent_parent_parent_name, pattern_attributes, pattern_author_id, pattern_author_name, pattern_author_notes, pattern_author_permalink, pattern_type_is_clothing, pattern_type_id, pattern_type_name)
                  VALUES ("{num}", "{response_1_name}", "{response1_yarn_weight_description}", "{response1_craft_type}","{response1_notes}", "{response1_is_free}", "{response1_created_at}", "{response1_gauge}", "{response1_gauge_divisor}", "{response1_permalink}", "{response1_updated_at}", "{response1_yardage}", "{response1_yardage_max}", "{response1_personal_attributes}", "{response1_personal_attributes}", "{response1_gauge_description}", "{response1_pattern_needle_sizes_us}", "{response1_pattern_needle_sizes_metric}", "{response1_pattern_needle_sizes_us_steel}", "{response1_pattern_needle_sizes_crochet}", "{response1_pattern_needle_sizes_knitting}", "{response1_pattern_needle_sizes_hook}", "{response1_pattern_needle_sizes_name}", "{response1_yarn_weight_crochet_gauge}", "{response1_yarn_weight_knit_gauge}", "{response1_yarn_weight_min_gauge}", "{response1_yarn_weight_name}", "{response1_yarn_weight_ply}", "{response1_yarn_weight_wpi}", "{response1_pattern_categories_id}", "{response1_pattern_categories_name}", "{response1_categories_parent_name}", "{response1_categories_parent_parent_name}", "{response1_categories_parent_parent_parent_name}", "{response1_pattern_attributes}", "{response1_pattern_author_id}", "{response1_pattern_author_name}", "{response1_pattern_author_notes}", "{response1_pattern_author_permalink}", "{response1_pattern_type_is_clothing}", "{response1_pattern_type_id}", "{response1_pattern_type_name}")
                  """)
    connection.commit()


def get_and_store_yarn(num):
    """assumes num is an int, representing the pattern ID of the desired yarn
    stores the yarn data to the database
    returns none
    """
    yarn_id = str(num)
    url_base = 'https://api.ravelry.com/'
    endpoint_patterns = 'patterns.json?ids='
    endpoint_yarns1 = 'yarns.json?ids='
    response1 = a_session.get(url_base + endpoint_yarns1 + yarn_id)
    if response1.status_code == 200:
        response_1_id = response1.json()['yarns'][yarn_id]['id']
        response_1_discontinued = response1.json()['yarns'][yarn_id]['discontinued']
        response_1_gauge_divisor = response1.json()['yarns'][yarn_id]['gauge_divisor']
        response_1_grams = response1.json()['yarns'][yarn_id]['grams']
        response_1_machine_washable = response1.json()['yarns'][yarn_id]['machine_washable']
        response_1_max_gauge = response1.json()['yarns'][yarn_id]['max_gauge']
        response_1_min_gauge = response1.json()['yarns'][yarn_id]['min_gauge']
        response_1_name = response1.json()['yarns'][yarn_id]['name'].replace("\"","")
        response_1_permalink = response1.json()['yarns'][yarn_id]['permalink']
        response_1_texture = response1.json()['yarns'][yarn_id]['texture']
        if response_1_texture:
            response_1_texture = response1.json()['yarns'][yarn_id]['texture'].replace("\"", "")
        response_1_thread_size = response1.json()['yarns'][yarn_id]['thread_size']
        response_1_wpi = response1.json()['yarns'][yarn_id]['wpi']
        response_1_yardage = response1.json()['yarns'][yarn_id]['yardage']
        response_1_notes_html = response1.json()['yarns'][yarn_id]['notes_html']
        if response_1_notes_html:
            response_1_notes_html = response1.json()['yarns'][yarn_id]['notes_html'].replace("\"", "\'")
        if response1.json()['yarns'][yarn_id]['min_needle_size']:
            response_1_min_needle_size_id = response1.json()['yarns'][yarn_id]['min_needle_size']['id']
            response_1_min_needle_size_us = response1.json()['yarns'][yarn_id]['min_needle_size']['us']
            response_1_min_needle_size_metric = response1.json()['yarns'][yarn_id]['min_needle_size']['metric']
            response_1_min_needle_size_us_steel = response1.json()['yarns'][yarn_id]['min_needle_size']['us_steel']
            response_1_min_needle_size_crochet = response1.json()['yarns'][yarn_id]['min_needle_size']['crochet']
            response_1_min_needle_size_knitting = response1.json()['yarns'][yarn_id]['min_needle_size']['knitting']
            response_1_min_needle_size_hook = response1.json()['yarns'][yarn_id]['min_needle_size']['hook']
            response_1_min_needle_size_name = response1.json()['yarns'][yarn_id]['min_needle_size']['name']
        else:
            response_1_min_needle_size_id = None
            response_1_min_needle_size_us = None
            response_1_min_needle_size_metric = None
            response_1_min_needle_size_us_steel = None
            response_1_min_needle_size_crochet = None
            response_1_min_needle_size_knitting = None
            response_1_min_needle_size_hook = None
            response_1_min_needle_size_name = None
        if response1.json()['yarns'][yarn_id]['max_needle_size'] != None:
            response_1_max_needle_size_id = response1.json()['yarns'][yarn_id]['max_needle_size']['id']
            response_1_max_needle_size_us = response1.json()['yarns'][yarn_id]['max_needle_size']['us']
            response_1_max_needle_size_metric = response1.json()['yarns'][yarn_id]['max_needle_size']['metric']
            response_1_max_needle_size_us_steel = response1.json()['yarns'][yarn_id]['max_needle_size']['us_steel']
            response_1_max_needle_size_crochet = response1.json()['yarns'][yarn_id]['max_needle_size']['crochet']
            response_1_max_needle_size_knitting = response1.json()['yarns'][yarn_id]['max_needle_size']['knitting']
            response_1_max_needle_size_hook = response1.json()['yarns'][yarn_id]['max_needle_size']['hook']
            response_1_max_needle_size_name = response1.json()['yarns'][yarn_id]['max_needle_size']['name']
        else:
            response_1_max_needle_size_id = None
            response_1_max_needle_size_us = None
            response_1_max_needle_size_metric = None
            response_1_max_needle_size_us_steel = None
            response_1_max_needle_size_crochet = None
            response_1_max_needle_size_knitting = None
            response_1_max_needle_size_hook = None
            response_1_max_needle_size_name = None
        response_1_min_hook_size = response1.json()['yarns'][yarn_id]['min_hook_size']
        response_1_max_hook_size = response1.json()['yarns'][yarn_id]['max_hook_size']
        response_1_personal_attributes = response1.json()['yarns'][yarn_id]['personal_attributes']
        try:
            response_1_yarn_weight_crochet_gauge = response1.json()['yarns'][yarn_id]['yarn_weight']['crochet_gauge']
            response_1_yarn_weight_id = response1.json()['yarns'][yarn_id]['yarn_weight']['id']
            response_1_yarn_weight_knit_gauge = response1.json()['yarns'][yarn_id]['yarn_weight']['knit_gauge']
            response_1_yarn_weight_min_gauge = response1.json()['yarns'][yarn_id]['yarn_weight']['min_gauge']
            response_1_yarn_weight_name = response1.json()['yarns'][yarn_id]['yarn_weight']['name']
            response_1_yarn_weight_ply = response1.json()['yarns'][yarn_id]['yarn_weight']['ply']
        except KeyError:
            response_1_yarn_weight_crochet_gauge = None
            response_1_yarn_weight_id = None
            response_1_yarn_weight_knit_gauge = None
            response_1_yarn_weight_min_gauge = None
            response_1_yarn_weight_name = None
            response_1_yarn_weight_ply = None
        response_1_yarn_company_id = response1.json()['yarns'][yarn_id]['yarn_company']['id']
        response_1_yarn_company_name = response1.json()['yarns'][yarn_id]['yarn_company']['name']
        response_1_yarn_company_permalink = response1.json()['yarns'][yarn_id]['yarn_company']['permalink']
        try:
            response_1_yarn_fibers0_id = response1.json()['yarns'][yarn_id]['yarn_fibers'][0]['id']
            response_1_yarn_fibers0_percentage = response1.json()['yarns'][yarn_id]['yarn_fibers'][0]['percentage']
            response_1_yarn_fibers0_fiber_type_animal_fiber = response1.json()['yarns'][yarn_id]['yarn_fibers'][0]['fiber_type']['animal_fiber']
            response_1_yarn_fibers0_fiber_type_id = response1.json()['yarns'][yarn_id]['yarn_fibers'][0]['fiber_type']['id']
            response_1_yarn_fibers0_fiber_type_name = response1.json()['yarns'][yarn_id]['yarn_fibers'][0]['fiber_type']['name']
            response_1_yarn_fibers0_fiber_type_synthetic = response1.json()['yarns'][yarn_id]['yarn_fibers'][0]['fiber_type']['synthetic']
            response_1_yarn_fibers0_fiber_type_vegetable_fiber = response1.json()['yarns'][yarn_id]['yarn_fibers'][0]['fiber_type']['vegetable_fiber']
            response_1_yarn_fibers0_fiber_category_id = response1.json()['yarns'][yarn_id]['yarn_fibers'][0]['fiber_category']['id']
            response_1_yarn_fibers0_fiber_category_name = response1.json()['yarns'][yarn_id]['yarn_fibers'][0]['fiber_category']['name']
            response_1_yarn_fibers0_fiber_category_permalink = response1.json()['yarns'][yarn_id]['yarn_fibers'][0]['fiber_category']['permalink']
        except:
            response_1_yarn_fibers0_id = None
            response_1_yarn_fibers0_percentage = None
            response_1_yarn_fibers0_fiber_type_animal_fiber = None
            response_1_yarn_fibers0_fiber_type_id = None
            response_1_yarn_fibers0_fiber_type_name = None
            response_1_yarn_fibers0_fiber_type_synthetic = None
            response_1_yarn_fibers0_fiber_type_vegetable_fiber = None
            response_1_yarn_fibers0_fiber_category_id = None
            response_1_yarn_fibers0_fiber_category_name = None
            response_1_yarn_fibers0_fiber_category_permalink = None
        try:
            response_1_yarn_fibers01id = response1.json()['yarns'][yarn_id]['yarn_fibers'][1]['id']
            response_1_yarn_fibers1_percentage = response1.json()['yarns'][yarn_id]['yarn_fibers'][1]['percentage']
            response_1_yarn_fibers1_fiber_type_animal_fiber = response1.json()['yarns'][yarn_id]['yarn_fibers'][1]['fiber_type']['animal_fiber']
            response_1_yarn_fibers1_fiber_type_id = response1.json()['yarns'][yarn_id]['yarn_fibers'][1]['fiber_type']['id']
            response_1_yarn_fibers1_fiber_type_name = response1.json()['yarns'][yarn_id]['yarn_fibers'][1]['fiber_type']['name']
            response_1_yarn_fibers1_fiber_type_synthetic = response1.json()['yarns'][yarn_id]['yarn_fibers'][1]['fiber_type']['synthetic']
            response_1_yarn_fibers1_fiber_type_vegetable_fiber = response1.json()['yarns'][yarn_id]['yarn_fibers'][1]['fiber_type']['vegetable_fiber']
            response_1_yarn_fibers1_fiber_category_id = response1.json()['yarns'][yarn_id]['yarn_fibers'][1]['fiber_category']['id']
            response_1_yarn_fibers1_fiber_category_name = response1.json()['yarns'][yarn_id]['yarn_fibers'][1]['fiber_category']['name']
            response_1_yarn_fibers1_fiber_category_permalink = response1.json()['yarns'][yarn_id]['yarn_fibers'][1]['fiber_category']['permalink']
        except:
            response_1_yarn_fibers01id = None
            response_1_yarn_fibers1_percentage = None
            response_1_yarn_fibers1_fiber_type_animal_fiber = None
            response_1_yarn_fibers1_fiber_type_id = None
            response_1_yarn_fibers1_fiber_type_name = None
            response_1_yarn_fibers1_fiber_type_synthetic = None
            response_1_yarn_fibers1_fiber_type_vegetable_fiber = None
            response_1_yarn_fibers1_fiber_category_id = None
            response_1_yarn_fibers1_fiber_category_name = None
            response_1_yarn_fibers1_fiber_category_permalink = None
        try:
            response_1_yarn_fibers2_id = response1.json()['yarns'][yarn_id]['yarn_fibers'][2]['id']
            response_1_yarn_fibers2_percentage = response1.json()['yarns'][yarn_id]['yarn_fibers'][2]['percentage']
            response_1_yarn_fibers2_fiber_type_animal_fiber = response1.json()['yarns'][yarn_id]['yarn_fibers'][2]['fiber_type']['animal_fiber']
            response_1_yarn_fibers2_fiber_type_id = response1.json()['yarns'][yarn_id]['yarn_fibers'][2]['fiber_type']['id']
            response_1_yarn_fibers2_fiber_type_name = response1.json()['yarns'][yarn_id]['yarn_fibers'][2]['fiber_type']['name']
            response_1_yarn_fibers2_fiber_type_synthetic = response1.json()['yarns'][yarn_id]['yarn_fibers'][2]['fiber_type']['synthetic']
            response_1_yarn_fibers2_fiber_type_vegetable_fiber = response1.json()['yarns'][yarn_id]['yarn_fibers'][2]['fiber_type']['vegetable_fiber']
            response_1_yarn_fibers2_fiber_category_id = response1.json()['yarns'][yarn_id]['yarn_fibers'][2]['fiber_category']['id']
            response_1_yarn_fibers2_fiber_category_name = response1.json()['yarns'][yarn_id]['yarn_fibers'][2]['fiber_category']['name']
            response_1_yarn_fibers2_fiber_category_permalink = response1.json()['yarns'][yarn_id]['yarn_fibers'][2]['fiber_category']['permalink']
        except:
            response_1_yarn_fibers2_id = None
            response_1_yarn_fibers2_percentage = None
            response_1_yarn_fibers2_fiber_type_animal_fiber = None
            response_1_yarn_fibers2_fiber_type_id = None
            response_1_yarn_fibers2_fiber_type_name = None
            response_1_yarn_fibers2_fiber_type_synthetic = None
            response_1_yarn_fibers2_fiber_type_vegetable_fiber = None
            response_1_yarn_fibers2_fiber_category_id = None
            response_1_yarn_fibers2_fiber_category_name = None
            response_1_yarn_fibers2_fiber_category_permalink = None
        # insert yarns into yarn table
        c.execute(f"""INSERT INTO ravelry_yarns
                  (id, discontinued, gauge_divisor, grams, machine_washable, max_gauge, min_gauge, name, permalink, texture, thread_size, wpi, yardage, notes_html, min_needle_size_id, min_needle_size_us, min_needle_size_metric, min_needle_size_us_steel, min_needle_size_crochet, min_needle_size_knitting, min_needle_size_hook, min_needle_size_name, max_needle_size_id, max_needle_size_us, max_needle_size_metric, max_needle_size_us_steel, max_needle_size_crochet, max_needle_size_knitting, max_needle_size_hook, max_needle_size_name, min_hook_size, max_hook_size, personal_attributes, yarn_weight_crochet_gauge, yarn_weight_id, yarn_weight_knit_gauge, yarn_weight_min_gauge, yarn_weight_name, yarn_weight_ply, yarn_company_id, yarn_company_name, yarn_company_permalink, yarn_fibers0_id, yarn_fibers0_percentage, yarn_fibers0_fiber_type_animal_fiber, yarn_fibers0_fiber_type_id, yarn_fibers0_fiber_type_name, yarn_fibers0_fiber_type_synthetic, yarn_fibers0_fiber_type_vegetable_fiber, yarn_fibers0_fiber_category_id, yarn_fibers0_fiber_category_name, yarn_fibers0_fiber_category_permalink, yarn_fibers01id, yarn_fibers1_percentage, yarn_fibers1_fiber_type_animal_fiber, yarn_fibers1_fiber_type_id, yarn_fibers1_fiber_type_name, yarn_fibers1_fiber_type_synthetic, yarn_fibers1_fiber_type_vegetable_fiber, yarn_fibers1_fiber_category_id, yarn_fibers1_fiber_category_name, yarn_fibers1_fiber_category_permalink, yarn_fibers2_id, yarn_fibers2_percentage, yarn_fibers2_fiber_type_animal_fiber, yarn_fibers2_fiber_type_id, yarn_fibers2_fiber_type_name,yarn_fibers2_fiber_type_synthetic, yarn_fibers2_fiber_type_vegetable_fiber, yarn_fibers2_fiber_category_id, yarn_fibers2_fiber_category_name, yarn_fibers2_fiber_category_permalink)
                  VALUES ( "{response_1_id}" , "{response_1_discontinued}" , "{response_1_gauge_divisor}" , "{response_1_grams}" , "{response_1_machine_washable}" , "{response_1_max_gauge}" , "{response_1_min_gauge}" , "{response_1_name}" , "{response_1_permalink}" , "{response_1_texture}" , "{response_1_thread_size}" , "{response_1_wpi}" , "{response_1_yardage}" , "{response_1_notes_html}" , "{response_1_min_needle_size_id}" , "{response_1_min_needle_size_us}" , "{response_1_min_needle_size_metric}" , "{response_1_min_needle_size_us_steel}" , "{response_1_min_needle_size_crochet}" , "{response_1_min_needle_size_knitting}" , "{response_1_min_needle_size_hook}" , "{response_1_min_needle_size_name}" , "{response_1_max_needle_size_id}" , "{response_1_max_needle_size_us}" , "{response_1_max_needle_size_metric}" , "{response_1_max_needle_size_us_steel}" , "{response_1_max_needle_size_crochet}" , "{response_1_max_needle_size_knitting}" , "{response_1_max_needle_size_hook}" , "{response_1_max_needle_size_name}" , "{response_1_min_hook_size}" , "{response_1_max_hook_size}" , "{response_1_personal_attributes}" , "{response_1_yarn_weight_crochet_gauge}" , "{response_1_yarn_weight_id}" , "{response_1_yarn_weight_knit_gauge}" , "{response_1_yarn_weight_min_gauge}" , "{response_1_yarn_weight_name}" , "{response_1_yarn_weight_ply}" , "{response_1_yarn_company_id}" , "{response_1_yarn_company_name}" , "{response_1_yarn_company_permalink}" , "{response_1_yarn_fibers0_id}" , "{response_1_yarn_fibers0_percentage}" , "{response_1_yarn_fibers0_fiber_type_animal_fiber}" , "{response_1_yarn_fibers0_fiber_type_id}" , "{response_1_yarn_fibers0_fiber_type_name}" , "{response_1_yarn_fibers0_fiber_type_synthetic}" , "{response_1_yarn_fibers0_fiber_type_vegetable_fiber}" , "{response_1_yarn_fibers0_fiber_category_id}" , "{response_1_yarn_fibers0_fiber_category_name}" , "{response_1_yarn_fibers0_fiber_category_permalink}" , "{response_1_yarn_fibers01id}" , "{response_1_yarn_fibers1_percentage}" , "{response_1_yarn_fibers1_fiber_type_animal_fiber}" , "{response_1_yarn_fibers1_fiber_type_id}" , "{response_1_yarn_fibers1_fiber_type_name}" , "{response_1_yarn_fibers1_fiber_type_synthetic}" , "{response_1_yarn_fibers1_fiber_type_vegetable_fiber}" , "{response_1_yarn_fibers1_fiber_category_id}" , "{response_1_yarn_fibers1_fiber_category_name}" , "{response_1_yarn_fibers1_fiber_category_permalink}" , "{response_1_yarn_fibers2_id}" , "{response_1_yarn_fibers2_percentage}" , "{response_1_yarn_fibers2_fiber_type_animal_fiber}" , "{response_1_yarn_fibers2_fiber_type_id}" , "{response_1_yarn_fibers2_fiber_type_name}" ,"{response_1_yarn_fibers2_fiber_type_synthetic}" , "{response_1_yarn_fibers2_fiber_type_vegetable_fiber}" , "{response_1_yarn_fibers2_fiber_category_id}" , "{response_1_yarn_fibers2_fiber_category_name}" , "{response_1_yarn_fibers2_fiber_category_permalink}" )""")
    connection.commit()


if __name__ == "__main__":
    connection = s.connect("ravelry_db.db")
    c = connection.cursor()

    with requests.Session() as a_session:
        auth_name = "read-046277a3027f680ebe3fa030e755eb34"
        auth_pass = "O+mL0KzfjgQ1eLA7K8FO9s28QPvr6QuiL+pOvFHZ"
        a_session.auth = (auth_name, auth_pass)
        ravelry_adapter = HTTPAdapter(max_retries=3)
        a_session.mount('https://ravelry.com', ravelry_adapter)

        for num in range(29000, 30000):
            print(num)
            get_and_store_pattern(num)
            get_and_store_yarn(num)
        print("insertions successful")

        print('kittens')
        # yarn_rows = c.execute('SELECT * FROM ravelry_yarns')
        # for row in yarn_rows:
        #     print(row)
        # pattern_rows = c.execute('SELECT * FROM ravelry_patterns')
        # for row in pattern_rows:
        #     print(row)

    c.close()
    connection.close()
