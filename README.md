# The Effect Tenure and Dependability Have on Churn

## 1) Question about the data
* What factors are customers willing to scrifice more money for while not being at risk of churning? In additoin, can those factors (features) be proven through data manipulation and analysis

## Project Goal
* Discover factors within the telco.dataset that support the theory that factors related to comfort, such as tenure and tech security/backup will deter churn
* Use features produce a machine learning model which classify assists in prediction of if a customer will churn based on feature significance.
* A "Churn" customer means he/she fails to do future business witht he company
* This information could be used to identify and anticipate churnable consumers as soon as possible. This will help us to rectify the issues of the customer beforehand, thus avoiding loss of business and profit.

## Hypothesis & Questions 
* Is there is a relationship between tenure and customer churn.More specifically, if a customer has been with a company and feels they're reliable, are they less willing to churn despite better offers from outside vendors.
* Is there is a relationship between security options the customer might have access to and churn
* There is a relationship between backup assurance and if a customer is more likely to churn
* Is there is a relationship between tech support and if a customer is more likely to churn
* I feel in today's interoperability atmospherics that there is more and more of a demand for reliable security offerings: through data exploratin and model building I will look to show an importance, for the customer, of ensuring minimal data loss or corruption, the ability to report to customer service/tech support any trouble shooting needs, and knowing that there is an way to mitigate damage for discovered cyberthreats and malware.


## The Plan
* Acquire data from sql.database with the use of .py model (acquire)
* Prepare data
    - string formatting on the telco 'total_charge' column
    - replace method used to transfer 'yes' and 'no' to 0,1 for 'churn'
    - functions that range in test size, which split the data for preparation of modeling
* Conduct EDA (Exploratory Data Analysis) to spot patterns, correlations, relationships, and evidence connecting the hypothesis and questions being examined.
* Develop a Model to predict if a customer would churn (Dependent variable) based on features (Indeoendent variables)

  ## Data Dictionary
  
  























