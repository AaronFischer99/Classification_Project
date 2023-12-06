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
  
**The data set includes information about:

CustomerID 	The unique ID of each customer

Gender 	The gender of a person

SeniorCitizen	Whether a customer can be classified as a senior citizen.

Partner 	If a customer is married/ in a live-in relationship.

Dependents	If a customer has dependents (children/ retired parents)

Tenure	The time for which a customer has been using the service.

PhoneService  	Whether a customer has a landline phone service along with the internet service.

MultipleLines	Whether a customer has multiple lines of internet connectivity.

InternetService 	The type of internet services chosen by the customer.

OnlineSecurity 	Specifies if a customer has online security.

OnlineBackup 	Specifies if a customer has online backup.

DeviceProtection 	Specifies if a customer has opted for device protection.

TechSupport 	Whether a customer has opted for tech support of not.

StreamingTV	Whether a customer has an option of TV streaming.

StreamingMovies 	Whether a customer has an option of Movie streaming.

Contract  	The type of contract a customer has chosen.

PaperlessBilling  	Whether a customer has opted for paperless billing.

PaymentMethod 	Specifies the method by which bills are paid.

MonthlyCharges 	Specifies the money paid by a customer each month.

TotalCharges 	The total money paid by the customer to the company.

Churn  	This is the target variable which specifies if a customer has churned or not.

## Steps to Reproduce
1. Clone this repo
2. Acquire data from Open-Source (websites include Kaggle, Github, etc)
3. Place file containing repo in folder of choice
4. Run notebook

## Takeaways and Conclusions
* Customers using online security and online backup services have relatively lower churn rates, indicating the value of these services.
  
* New customers are more prone to churn than long-term ones. Churn rates decrease as the tenure of customers increase.
  
* As businesses move more and more of their operations onto the cloud, cloud security has become an essential concern. Not only does cloud security help to protect data from external threats, but it also helps to reduce churn within businesses.

* Security backup practices lead to increased client satisfaction and loyalty. By providing reliable security services, a company can foster long-term relationships with their clients and reduce client churn.


* consumers inclined to stay longer with a company offering these services, but they are also willing to invest more for enhanced technical support and security – a prospect that not only boosts profitability but also acts as a powerful deterrent against churn


## Recommendations (Things that can be done toreduce the churn rate):
* Place emphasis on tailored retention strategies for younger customers, considering their unique preferences and needs.

* Develop targeted offers and services that address the needs of younger customers without partners or dependents, potentially through bundle packages or personalized plans.

* Offer incentives to encourage customers to commit to longer-term contracts, such as discounts or additional services.

* Highlight the benefits of online security and backup services to all customers to potentially reduce churn.


## Things to Consider Moving Forward
* Collect data regarding tower overage within different customer geolocational data.

* Collect data on the type of usage for the device (Business, Social Media, etc). This could give insight to the services that may prove more important to customers.

* Collect data on customer income based on zip code and possibly customer demographic. This information could better assist in identifying if monthly and total charges play a larger role in churn compared to the other features.

* Gather and bin churn based on a more specific age scale (I.e.: 21-30, 30-40,etc). By more tightly grouping the age range, it is posible to gain a better understanding of average time (tenure) continued iwth the company and age associated. Also, this could assist in correlating which security and backup services are most important to what specified age range.




























