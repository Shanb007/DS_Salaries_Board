#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 13:57:07 2021

@author: shanb007
"""

from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException
from selenium import webdriver
import time
import pandas as pd

def scrape_jobs(keyword, num_jobs, verbose, path):
    
    i=1 #initial entry
    #Initializing the webdriver
    options = webdriver.ChromeOptions()
    #remeber to set the path to your own folder, tho here i passed it as an arguement, check scraper_cmd.py
    driver = webdriver.Chrome(executable_path=path, options=options)
    driver.set_window_size(1120, 1000)

    url = "https://www.glassdoor.co.in/Job/india-"+keyword+"-jobs-SRCH_IL.0,5_IN115_KO6,20.htm"
    #print(url)
    driver.get(url)
    jobs = []

    while len(jobs) < num_jobs:  #If true, should be still looking for new jobs.

        #Let the page load.
        time.sleep(10)
        #Sign-up prompt appears after the second click, get rid of it by below try
        try:
            driver.find_element_by_class_name("react-job").click()
            #print("selected vala worked")
        except NoSuchElementException:
            #print("no ele vala try kre")
            pass
        except ElementClickInterceptedException:
            #print("selected vala didn't work")
            pass

        time.sleep(3)

        try:
            driver.find_element_by_css_selector('[alt="Close"]').click() #clicking to the X.
            #print("it clicked X")
        except NoSuchElementException:
            #print("it didn't clicked X")
            pass
        
        #Going through each job in this page
        job_buttons = driver.find_elements_by_class_name("react-job-listing") #jl for Job Listing. These are the buttons we're going to click.
        #print(job_buttons)
        for job_button in job_buttons: 
            
            time.sleep(1)
            try:
                driver.find_element_by_css_selector('[alt="Close"]').click() #clicking to the X.
                #print("it clicked X")
            except NoSuchElementException:
                #print("it didn't clicked X")
                pass

            if len(jobs) >= num_jobs:
                break
            #print("job button start")
            try:
                job_button.click()  #we browse through jobs with clicks
            except StaleElementReferenceException:
                continue
            #print("job button clicked")
            time.sleep(4)
            collected_successfully = False
            
            while not collected_successfully:
                try:
                    company_name = driver.find_element_by_xpath(".//div[@class='css-87uc0g e1tk4kwz1']").text
                    #print("done with comp")
                    location = driver.find_element_by_xpath(".//div[@class='css-56kyx5 e1tk4kwz5']").text
                    #print("done with loc")
                    job_title = driver.find_element_by_xpath('.//div[@class="css-1vg6q84 e1tk4kwz4"]').text
                    #print("done with tit")
                    job_description = driver.find_element_by_xpath('.//div[@class="jobDescriptionContent desc"]').text
                    #print("done with desc")
                    collected_successfully = True
                except:
                    #print("kyA mai yaha aa rha hu")
                    time.sleep(5)
           
            #if feature not found set it's value to -1
            #at times you might catch StaleElement exception, just add it in the block it occurs at.
            time.sleep(3)
            try:
                salary_estimate = driver.find_element_by_xpath(".//div[@class='css-nq3w9f pr-xxsm']/span[@class='css-56kyx5 css-16kxj2j e1wijj242']").text
            except NoSuchElementException:
                salary_estimate = -1
            except StaleElementReferenceException:
                salary_estimate = -1
            
            try:
                rating = driver.find_element_by_xpath(".//div[@class='mr-sm css-ey2fjr e1pr2f4f2']").text
            except NoSuchElementException:
                rating = -1
            except StaleElementReferenceException:
                rating = -1

            try:
                size = driver.find_element_by_xpath(".//div[@class='d-flex justify-content-start css-rmzuhb e1pvx6aw0'][1]").text
            except NoSuchElementException:
                size = -1
            except StaleElementReferenceException:
                size = -1    
            try:
                founded = driver.find_element_by_xpath(".//div[@class='d-flex justify-content-start css-rmzuhb e1pvx6aw0'][2]").text
            except NoSuchElementException:
                founded = -1
            except StaleElementReferenceException:
                founded = -1
            try:
                type_of_ownership = driver.find_element_by_xpath(".//div[@class='d-flex justify-content-start css-rmzuhb e1pvx6aw0'][3]").text
            except NoSuchElementException:
                type_of_ownership = -1
            except StaleElementReferenceException:
                type_of_ownership = -1
            try:
                industry = driver.find_element_by_xpath(".//div[@class='d-flex justify-content-start css-rmzuhb e1pvx6aw0'][4]").text
            except NoSuchElementException:
                industry = -1
            except StaleElementReferenceException:
                industry = -1
            try:
                sector = driver.find_element_by_xpath(".//div[@class='d-flex justify-content-start css-rmzuhb e1pvx6aw0'][5]").text
            except NoSuchElementException:
                sector = -1
            except StaleElementReferenceException:
                sector = -1
            try:
                revenue = driver.find_element_by_xpath(".//div[@class='d-flex justify-content-start css-rmzuhb e1pvx6aw0'][6]").text
            except NoSuchElementException:
                revenue = -1
            except StaleElementReferenceException:
                revenue = -1
            #Printing for checking.
            if verbose:
                print("Job Title: {}".format(job_title))
                print("Salary Estimate: {}".format(salary_estimate))
                print("Job Description: {}".format(job_description[:500]))
                print("Rating: {}".format(rating))
                print("Company Name: {}".format(company_name))
                print("Location: {}".format(location))
                print("Size: {}".format(size))
                print("Founded: {}".format(founded))
                print("Type of Ownership: {}".format(type_of_ownership))
                print("Industry: {}".format(industry))
                print("Sector: {}".format(sector))
                print("Revenue: {}".format(revenue))
            
            #print("did it start?")
            #add job to jobs
            jobs.append({"Job Title" : job_title,
            "Salary Estimate" : salary_estimate,
            "Job Description" : job_description,
            "Rating" : rating,
            "Company Name" : company_name,
            "Location" : location,
            "Size" : size,
            "Founded" : founded,
            "Type of ownership" : type_of_ownership,
            "Industry" : industry,
            "Sector" : sector,
            "Revenue" : revenue})
            
            #print("yes it did mf")
            print("Entry No. {}/{} is Done.".format(i,num_jobs))
            i = i +1

        #Clicking on the "next page" button
        try:
            driver.find_element_by_xpath(".//div[@class='middle']/ul/li[@class='css-114lpwu e1gri00l4']/a/span[@class='SVGInline']").click()
        except NoSuchElementException:
            print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
            break
    
    return pd.DataFrame(jobs)  #Dic to DF.