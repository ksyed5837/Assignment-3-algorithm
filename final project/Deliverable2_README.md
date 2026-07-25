# MSCS 634 Project Deliverable 2

## Regression Modeling and Performance Evaluation

### Group Members :

Arun Gyawali

Kashif Ali Syed

Jiwon Jung

Hanuman Sai Chanukya Srinivas Chilamkuri

### Project Overview

This deliverable builds on the cleaned **Online Shoppers Purchasing Intention Dataset** from Deliverable 1. New features were engineered from the existing behavioral columns, multiple regression models were trained to predict a continuous outcome, and their performance was evaluated and compared using R-squared, MSE, RMSE, and 5-fold cross-validation.

The cleaned dataset produced in Deliverable 1 (`online_shoppers_cleaned.csv`) was used directly as the input for this deliverable, so no additional cleaning was required.

## Dataset

**Dataset name:** Online Shoppers Purchasing Intention Dataset
**Source:** UCI Machine Learning Repository
**Input shape:** 12,205 rows and 18 columns (cleaned dataset from Deliverable 1)
**Regression target:** ProductRelated_Duration

## Selecting a Regression Target

`Revenue`, the dataset's primary target, is Boolean and is reserved for the classification task in Deliverable 3, so a continuous target was needed for this deliverable.

`PageValues` was the target originally proposed in the Deliverable 1 plan, but further inspection showed that it is **zero for about 77.6% of sessions**, making it too zero-inflated for standard regression models to fit well.

**ProductRelated_Duration** (total time spent on product-related pages in a session) was selected instead. Only about 5% of sessions have a value of zero, so it behaves as a genuine continuous variable, and it remains closely tied to customer engagement and purchasing intent — Deliverable 1 found this value was substantially higher for purchasing sessions (1,797.8s) than non-purchasing sessions (1,047.3s).

## Feature Engineering

Five new behavioral features were created without using the regression target:

| Engineered Feature | Description |
|---|---|
| Total_Pages | Total pages visited across Administrative, Informational, and ProductRelated categories |
| NonProduct_Duration | Total time spent on Administrative and Informational pages |
| Avg_NonProduct_Duration_Per_Page | Average time spent per non-product page |
| BounceExitRatio | Ratio of BounceRates to ExitRates |
| Engagement_Score | ProductRelated page count multiplied by PageValues |

`Month`, `VisitorType`, `OperatingSystems`, `Browser`, `Region`, and `TrafficType` were one-hot encoded. The coded numerical columns were treated as categories rather than continuous measurements.

`Weekend` and `Revenue` were converted to integers. Revenue was excluded from the regression predictors because it will be used as the classification target in Deliverable 3.

Redundant component variables were removed after creating `Total_Pages` and `NonProduct_Duration`. The final model used 68 predictor features.

## Modeling Approach

The data was split into an 80% training set and a 20% test set using a random state of 42. This produced 9,764 training records and 2,441 test records.

For held-out test evaluation, `StandardScaler` was fitted only on the training data. During five-fold cross-validation, scaling was performed inside model pipelines so that preprocessing was repeated independently within every fold.

Four regression models were compared:

1. **Linear Regression**
2. **Ridge Regression**
3. **Lasso Regression**
4. **Random Forest Regressor**

Each model was evaluated using R-squared, Mean Squared Error, Root Mean Squared Error, and five-fold cross-validation.

## Model Performance

### Test Set Results

| Model | R-squared | MSE | RMSE |
|---|---:|---:|---:|
| Linear Regression | 0.7188 | 692,990.14 | 832.46 |
| Ridge Regression | 0.7188 | 693,176.22 | 832.57 |
| Lasso Regression | 0.7190 | 692,592.87 | 832.22 |
| Random Forest | 0.7506 | 614,684.76 | 784.02 |

### Five-Fold Cross-Validation Results

| Model | CV R-squared Mean | CV RMSE Mean |
|---|---:|---:|
| Linear Regression | 0.7318 | 803.28 |
| Ridge Regression | 0.7318 | 803.28 |
| Lasso Regression | 0.7321 | 802.96 |
| Random Forest | 0.7702 | 742.97 |

Random Forest produced the highest R-squared and lowest RMSE on both the held-out test set and cross-validation. The cross-validation results were reasonably close to the test-set results, indicating that the models generalized consistently.

## Key Findings

- Random Forest was the best-performing model, with a test R-squared of **0.7506** and a cross-validated R-squared of **0.7702**.
- Random Forest reduced the test RMSE to **784.02 seconds**, compared with approximately **832 seconds** for the linear models.
- Linear Regression, Ridge Regression, and Lasso Regression performed similarly. The selected regularization settings did not provide a meaningful improvement over ordinary Linear Regression.
- `Total_Pages` was the most influential Random Forest feature, with an importance of approximately **0.564**.
- `ProductRelated` page count was the second-most influential feature, with an importance of approximately **0.315**.
- `ExitRates`, `Avg_NonProduct_Duration_Per_Page`, and `NonProduct_Duration` made smaller contributions.
- `BounceExitRatio` contributed a small amount, while `Engagement_Score` had limited individual importance in the final Random Forest model.
- The stronger performance of Random Forest indicates that the relationship between browsing behavior and product-related duration is partly non-linear.

## Challenges Encountered

One challenge was selecting an appropriate continuous regression target. `PageValues` was zero for approximately 77.6% of sessions, so `ProductRelated_Duration` was selected instead.

Another challenge was preventing target leakage. Revenue was excluded, and none of the engineered features directly used `ProductRelated_Duration`.

Several columns, including Browser, OperatingSystems, Region, and TrafficType, were stored as numbers even though they represented categories. These columns were converted and one-hot encoded.

Redundant component variables were removed after creating `Total_Pages` and `NonProduct_Duration` to reduce exact feature relationships.

Scaling was placed inside cross-validation pipelines so that preprocessing was fitted separately in every training fold.

Lasso Regression initially produced a convergence warning. Increasing `max_iter` to 10,000 resolved the issue.

## Repository Files

- `Deliverable_2.ipynb` – Feature engineering, regression modeling, evaluation, and comparison
- `online_shoppers_cleaned.csv` – Cleaned dataset from Deliverable 1, used as input for this notebook
- `Deliverable2_README.md` – Project summary and findings for this deliverable

## How to Run

1. Place the notebook and `online_shoppers_cleaned.csv` in the same folder.
2. Open `Deliverable_2.ipynb` in Jupyter Notebook or Visual Studio Code.
3. Ensure the notebook's kernel points to the Python environment where the required libraries are installed.
4. Run the notebook cells from top to bottom.
5. Review the printed metrics, comparison table, and plots for each model.

## Required Libraries

```bash
pip install pandas numpy matplotlib seaborn scikit-learn ipykernel
```
