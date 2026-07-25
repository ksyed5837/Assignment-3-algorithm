# MSCS 634 Project Deliverable 1

## Data Collection, Cleaning, and Exploration

### Group Members : 

Arun Gyawali

Kashif Ali Syed

Jiwon Jung

Hanuman Sai Chanukya Srinivas Chilamkuri

### Project Overview

This project uses the **Online Shoppers Purchasing Intention Dataset** to analyze customer browsing behavior and online purchasing outcomes. Each row represents one online shopping session.

The original dataset contains **12,330 records and 18 columns**, which exceeds the project requirement of at least 500 records and 8–10 attributes. The dataset includes page visits, page durations, bounce rates, exit rates, page values, visitor information, month, weekend status, traffic information, and the Revenue purchase outcome.

This same dataset will continue to be used in the remaining deliverables for regression, classification, clustering, and association rule mining.

## Dataset

**Dataset name:** Online Shoppers Purchasing Intention Dataset  
**Source:** UCI Machine Learning Repository  
**Original shape:** 12,330 rows and 18 columns  
**Cleaned shape:** 12,205 rows and 18 columns  
**Target variable:** Revenue

Revenue indicates whether an online shopping session resulted in a purchase.

## Main Data-Cleaning Steps

The following steps were completed:

1. Loaded and inspected the dataset using Pandas.
2. Reviewed column names, data types, descriptive statistics, and categorical values.
3. Checked every column for missing values.
4. Removed leading and trailing spaces from column names and text values.
5. Converted Month and VisitorType into categorical variables.
6. Validated the Weekend and Revenue Boolean columns.
7. Removed 125 exact duplicate records.
8. Checked numerical columns for negative and invalid values.
9. Examined possible outliers using the interquartile range method.
10. Excluded coded categorical variables such as Browser, Region, OperatingSystems, and TrafficType from numerical outlier and correlation analysis.
11. Capped extreme duration values above the 99th percentile instead of deleting complete sessions.
12. Saved the cleaned dataset as `online_shoppers_cleaned.csv`.

No missing values, negative numerical values, or invalid rate values were found.

## Outlier Treatment

The duration variables were strongly right-skewed and contained several unusually large observations. These values may represent genuine long sessions or inactive browser tabs.

Values above the 99th percentile were capped as follows:

| Feature | 99th Percentile Limit | Values Capped |
|---|---:|---:|
| Administrative_Duration | 838.70 | 123 |
| Informational_Duration | 722.38 | 123 |
| ProductRelated_Duration | 8,704.27 | 123 |

This approach reduced the influence of extreme values while preserving all unique customer sessions.

## Exploratory Data Analysis

The exploratory analysis included:

- Distribution of purchasing and non-purchasing sessions
- Histograms of important numerical features
- Log-transformed duration boxplots
- Correlation heatmap of behavioral features
- Conversion rates by visitor type
- Monthly conversion-rate analysis
- Weekday and weekend conversion comparison
- Engagement comparison by purchase outcome
- PageValues comparison by purchase outcome
- Product-related duration and PageValues scatterplot

## Key Findings

The cleaned dataset contains **10,297 non-purchasing sessions** and **1,908 purchasing sessions**.

| Purchase Outcome | Sessions | Percentage |
|---|---:|---:|
| No Purchase | 10,297 | 84.37% |
| Purchase | 1,908 | 15.63% |

The Revenue target is imbalanced because only 15.63% of sessions resulted in a purchase. Future classification models will therefore be evaluated using accuracy, F1 score, confusion matrices, and ROC curves rather than accuracy alone.

PageValues had the strongest positive correlation with Revenue at approximately **0.492**. ProductRelated_Duration and ProductRelated had positive correlations of approximately **0.175** and **0.156**.

ExitRates had a negative correlation of approximately **-0.20** with Revenue, while BounceRates had a correlation of approximately **-0.145**. This indicates that sessions with higher abandonment behavior were less likely to produce purchases.

ProductRelated and ProductRelated_Duration were strongly correlated at approximately **0.84**. BounceRates and ExitRates were also strongly correlated at approximately **0.90**, indicating possible multicollinearity.

Purchasing sessions showed greater engagement than non-purchasing sessions:

| Feature | No Purchase | Purchase |
|---|---:|---:|
| ProductRelated | 29.050 | 48.210 |
| ProductRelated_Duration | 1,047.250 | 1,797.836 |
| BounceRates | 0.023 | 0.005 |
| ExitRates | 0.046 | 0.020 |
| PageValues | 2.000 | 27.265 |

New visitors had the highest conversion rate at **24.93%**, while returning visitors had a conversion rate of **14.09%**. However, returning visitors generated most purchases because they represented most sessions.

November had the highest monthly conversion rate at **25.49%**, followed by October at **20.95%** and September at **19.20%**. February had the lowest conversion rate at **1.66%**.

Weekend sessions had a conversion rate of **17.45%**, compared with **15.08%** for weekday sessions. However, weekdays generated more total purchases because the dataset contained more weekday sessions.

## Challenges Encountered

One challenge was distinguishing statistical outliers from legitimate customer behavior. Several variables were strongly right-skewed and contained many zero values, so automatically removing every IQR outlier would have removed useful records. Only the most extreme duration values were capped.

Another challenge was that Browser, OperatingSystems, Region, and TrafficType were stored as numbers even though they represent categories. These variables were excluded from numerical outlier and Pearson correlation analysis.

The Revenue target was also highly imbalanced. The original distribution was preserved because it reflects actual customer behavior. This issue will be addressed during classification through stratified splitting and appropriate evaluation metrics.

## Repository Files

- `Project_Deliverable_1.ipynb` – Data cleaning, exploratory analysis, visualizations, and insights
- `online_shoppers_intention.csv` – Original dataset
- `online_shoppers_cleaned.csv` – Cleaned dataset used for future deliverables
- `README.md` – Project summary and findings

## How to Run

1. Place the notebook and original CSV file in the same folder.
2. Open `Project_Deliverable_1.ipynb` in Jupyter Notebook or Visual Studio Code.
3. Run the notebook cells from top to bottom.
4. Confirm that `online_shoppers_cleaned.csv` is created successfully.
5. Use the cleaned dataset for the remaining project deliverables.

## Required Libraries

```bash
pip install pandas numpy matplotlib seaborn