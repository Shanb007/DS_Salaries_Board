# DS_Salaries_Board
* Created a tool that estimates data science salaries.
* Scraped over 1000 job descriptions from glassdoor using python and selenium.
* Did some feature enginnering by extracting skills given in JD, and how influenced the salaries are from them and similarly from the job title as well.
* Performed Linear, Lasso, Ridge and Random Forest Regressors and then hypertuned using GridsearchCV to get the best model.
* Built a client facing API using flask.

# Code and Resources considered:

**Python Version:** 3.8        
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle, requests            
**For Flask Requirements:**  ```pip install -r requirements.txt```

**Scraper:**  https://towardsdatascience.com/web-scraping-using-selenium-python-8a60f4cf40ab                          
**Flask Productionization:** https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2                 
**Flask Productionization with VS code:** https://code.visualstudio.com/docs/python/tutorial-flask


# Web Scraping

Refrring to the above article, tried to scrape some necessary feature for a making a Salary Estimate of Data Driven jobs in India:

* Company Name
* Job title
* Salary Estimate
* Job Description
* Rating
* Size
* Location
* Founded
* Type of Ownership
* Industry
* Sector
* Revenue

# Data Pre-Processing and Feature Engineering
After Scraping, Data was kind of in some unstructered form, It needed some cleaning.

* Fixed features like 'Salary_estimate', 'Company_Name', 'Founded', 'Type of Ownership', 'Industry', 'Sector', 'Revenue'
* Engineered features on top skills/tools, req. to be a Data Scientist as stated by the internet, like Python, Sql, Tensoflow, cloud, excel.
* Simplified Job Job titles between Junior, Senior.
* created other feature like total employess and description length too.

# Model Building
Created four regression models: Linear, Lasso, Rigid and Random forest.
Random Forest performed the best out of all of them, then further applied GridSearchCV on randomForest ie. tuned our model to improve the solution further.
Hence we achieved the best model with GridSearchCV.
* Used MAE as evaluation metrics to compare the models.

# Flask Production
In this step, I built a flask API endpoint that was hosted on a local webserver by following along with the TDS tutorial in the reference section above. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary.

# Deployement on Heroku
soon. :)
