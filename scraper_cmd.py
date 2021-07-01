#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 14:25:07 2021

@author: shanb007
"""

import gd_scrapper as gds
import pandas as pd

path = "/home/shanb007/Desktop/Data Science/Project DS Salaries/chromedriver"
#while giving the keyword i.e. job searching for put '-' in between.
df = gds.scrape_jobs('data-scientist', 1000, False, path)

df.to_csv('glassdoor_jobs.csv', index = False)


