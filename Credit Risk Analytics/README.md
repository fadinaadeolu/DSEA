# CREDIT RISK ANALYTICS (todo)

Book [http://www.creditriskanalytics.net/table-of-content.html]
Data description [http://www.creditriskanalytics.net/datasets-private2.html]

**Data Set HMEQ**
The data set HMEQ reports characteristics and delinquency information for 5,960 home equity loans. A home equity loan is a loan where the obligor uses the equity of his or her home as the underlying collateral. The data set has the following characteristics:
- BAD: 1 = applicant defaulted on loan or seriously delinquent; 0 = applicant paid loan
- LOAN: Amount of the loan request
- MORTDUE: Amount due on existing mortgage
- VALUE: Value of current property
- REASON: DebtCon = debt consolidation; HomeImp = home improvement
- JOB: Occupational categories
- YOJ: Years at present job
- DEROG: Number of major derogatory reports
- DELINQ: Number of delinquent credit lines
- CLAGE: Age of oldest credit line in months
- NINQ: Number of recent credit inquiries
- CLNO: Number of credit lines
- DEBTINC: Debt-to-income ratio

**Data Set Mortgage** 
The data set mortgage is in panel form and reports origination and performance observations for 50,000 residential U.S. mortgage borrowers over 60 periods. The periods have been deidentified. As in the real world, loans may originate before the start of the observation period (this is an issue where loans are transferred between banks and investors as in securitization). The loan observations may thus be censored as the loans mature or borrowers refinance. The data set is a randomized selection of mortgage-loan-level data collected from the portfolios underlying U.S. residential mortgage-backed securities (RMBS) securitization portfolios and provided by International Financial Research (www.internationalfinancialresearch.org). Go to www.win-rar.com if ﻿you require a program to decompress. Key variables include:

- id: Borrower ID
- time: Time stamp of observation
- orig_time: Time stamp for origination
- first_time: Time stamp for first observation
- mat_time: Time stamp for maturity
- balance_time: Outstanding balance at observation time
- LTV_time: Loan-to-value ratio at observation time, in %
- interest_rate_time: Interest rate at observation time, in %
- hpi_time: House price index at observation time, base year = 100
- gdp_time: Gross domestic product (GDP) growth at observation time, in %
- uer_time: Unemployment rate at observation time, in %
- REtype_CO_orig_time: Real estate type condominium = 1, otherwise = 0
- REtype_PU_orig_time: Real estate type planned urban development = 1, otherwise = 0
- REtype_SF_orig_time: Single-family home = 1, otherwise = 0
- investor_orig_time: Investor borrower = 1, otherwise = 0
- balance_orig_time: Outstanding balance at origination time
- FICO_orig_time: FICO score at origination time, in %
- LTV_orig_time: Loan-to-value ratio at origination time, in %
- Interest_Rate_orig_time: Interest rate at origination time, in %
- hpi_orig_time: House price index at origination time, base year = 100
- default_time: Default observation at observation time
- payoff_time: Payoff observation at observation time
- status_time: Default (1), payoff (2), and nondefault/nonpayoff (0) observation at observation time

**Data Set LGD**
The data set has been kindly provided by a European bank and has been slightly modified and anonymized. It includes 2,545 observations on loans and LGDs. Key variables are:

- LTV: Loan-to-value ratio, in %
- Recovery_rate: Recovery rate, in %
- lgd_time: Loss rate given default (LGD), in %
- y_logistic: Logistic transformation of the LGD
- lnrr: Natural logarithm of the recovery rate
- Y_probit: Probit transformation of the LGD
- purpose1: Indicator variable for the purpose of the loan; 1 = renting purpose, 0 = other- 
- event: Indicator variable for a default or cure event; 1 = event, 0 = no event
 
**Data Set Ratings**
The ratings data set is an anonymized data set with corporate ratings where the ratings have been numerically encoded (1 = AAA, etc.). It has the following variables:

- COMMEQTA: Common equity to total assets
- LLPLOANS: Loan loss provision to total loans
- COSTTOINCOME: Operating costs to operating income
- ROE: Return on equity
- LIQASSTA: Liquid assets to total assets
- SIZE: Natural logarithm of total assets