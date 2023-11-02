# Churn Problem of Telecom Company
DESCRIPTION: This repository contains the solution of the churn problem of Telecom company. Predicting the curn customer means 
predicting the customer who will leave the company in the future. The solution is divided into two parts. 
 
## Problem 
The problem of churn is a problem when a number of individuals move out of a collective group. It is one of the main problems that determine the steady-state level of customers in any type of business. 
 
Recently a large number of customers has left Maastricht Telecom. To address this problem Maastricht Telecom provides customer data to solve two important tasks: 
1. Descriptive task: Characterize loyal and churn customers and propose a focused customer retention program. (This can be done through visualization, descriptive models etc. ) 
2. Predictive task: Find a model that identifies churn customers. Then: 
    * Select 300 customers using that model from a separate test set and report the number of true churn customers among them. 

    * Calculate the expected costs for Maastricht Telecom for one month when 
    using your model on the test set if: 
        * every customer predicted as churn will get a gift of 10 euro and 
        * every true churn customer predicted as loyal will cause a loss of 64 euros (an average month subscription).
 
## Data 
The data consists of two files: churn-train.csv and churn-test.csv. The first data churn-train.csv you can use to train and validate your classification models. Once you have selected the best model you can test it using the second data churn-test.csv. (Do not use in any way churn-test.csv for training your classification models). 
 
 
The data is represented by types of variables: 
 
### A. Demographic info about customers: 

 <!--table -->
| Variable |
| --- |
|gender|
|Senior Citizen (age range < 67)|
|Partner (yes, no)|
|Dependents (yes, no)|
 
### B. Customer account information: 
| Variable |
| --- |
|tenure (how long they've been a customer in months)|
|Contract (month, year, 2 years)|
|Paperless Billing (yes, no)|
|Payment Method (electronic check, mailed check, bank transfer, credit card)|
|Monthly Charges (in euros)|
|Total Charges (in euros)|
  
 
### C. Services that each customer has signed up for: 
| Variable |
| --- |
|Phone Service (yes, no)|
|Multiple Lines (no phone service, yes, no)|
|Internet Service (no, DSL, Fiber Optic)|
|Online Security (no Internet service, yes, no)|
|Online Backup (no Internet service, yes, no)|
|Device Protection (no Internet service, yes, no)|
|Tech Support (no Internet service, yes, no)|
|Streaming TV (no Internet service, yes, no)|
|Streaming Movies (no Internet service, yes, no)|
  
 
### D. Customers who left within the last month: 
| Variable |
| --- |
Churn (yes, no) 
  