![galaxy](https://github.com/user-attachments/assets/264641a4-ff51-42f0-a10a-72cb6416d27c)
# Sloan Digital Sky Survey (SDSS) Project

## Table of contents
- [Project Introduction](#ProjectIntroduction)
- [Data Desecription](#DataDescription)
- [EDA](#Eda)
- [Model Buliding](#ModelBuliding)
- [Model Evalution](#ModelEvalution)
- [conclusion](#Conclusion)

### Project Introduction:
The Sloan Digital Sky Survey (SDSS) is one of the most ambitious and comprehensive astronomical surveys ever undertaken. 
It aims to map a significant portion of the night sky, cataloging celestial objects such as stars, galaxies, and quasars. 
The data gathered through this project provides essential insights into the large-scale structure of the universe and the evolution of galaxies.
This project focuses on the analysis and modeling of the SDSS dataset to extract meaningful astronomical insights and predictions.

### Dataset Description:

The dataset used in this project comes from the SDSS, containing information about millions of celestial objects. Each row in the dataset represents an object and includes various features such as:
RA (Right Ascension): The angular distance of an object from the Earth's equator.
DEC (Declination): The angular distance of an object north or south of the celestial equator.
u, g, r, i, z: Magnitudes of the object measured in different photometric bands.
Redshift: A measure of how much the wavelength of the light from the object has been stretched due to the expansion of the universe.
Object Type: Classification of the object (e.g., galaxy, star, quasar).
The dataset is large and complex, requiring significant preprocessing and exploratory data analysis to derive meaningful insights.

### Exploratory Data Analysis (EDA):
In this section, we conducted a thorough exploration of the SDSS dataset to uncover patterns and relationships between the features. Key steps included:
#### Distribution of Celestial Objects: 
Visualizing the distribution of different types of objects (e.g., galaxies, stars, quasars).
#### Outliers Detection: 
Identifying outliers that may represent either rare celestial phenomena or data issues.
### Insights gained from EDA helped guide the preprocessing and modeling steps.
#### Data Preprocessing:
Data preprocessing is essential to ensure the quality and usability of the dataset for modeling. Steps involved include:
#### Handling Missing Values:
Imputing or removing rows with missing or corrupt data.
#### Normalization: 
Scaling features such as magnitudes to ensure uniformity.
#### Feature Engineering:
Creating additional features, such as distance or galaxy type, that could improve model performance.

### Modeling Phase:
### The goal of the modeling phase was to classify celestial objects into categories such as stars, galaxies, and quasars based on their attributes. Various machine learning models were explored, including:
#### Logistic Regression:
A baseline model for classification tasks.
#### Random Forest:
A robust ensemble model that excels at handling large datasets with complex relationships.

### Evaluation Metric:
Model performance was evaluated using several metrics to ensure accuracy and generalizability:
#### Accuracy: 
The proportion of correct classifications out of total classifications.
#### Precision, Recall, F1-score: 
Used for assessing the performance of the models in handling imbalanced datasets.

### Conclusion:
This project aimed to explore, preprocess, and model the vast dataset from the Sloan Digital Sky Survey. Through extensive data exploration and the use of various machine learning models, we were able to classify celestial objects with high accuracy. The insights gained from this project contribute to a better understanding of the universe's structure and evolution.
