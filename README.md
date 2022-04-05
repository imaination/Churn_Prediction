# Churn_Prediction

Python = 3.9.5

Goal: Predict which of the customers will churn. 

Data: Customer information of a Belgian bank-insurer for retail customers above 18 years old.

File set up for this project:

code/ : contains all the code (.py, .ipynb) used in the project<br />
data/ : contains original data & transformed data<br />


code/ :

- load_data.py (reads and copies data provided the base path, returns a dictionary of dataframes)<br />
- Get_Base_Data_00.ipynb (merges training/test data)<br />
- Explore_Data_01.ipynb (exploratory data analysis)<br />
- Manual_Preprocess_02.ipynb (preprocess training/val/test data)<br />
- Model_Pipeline_03.ipynb (fits a model)<br />
- Prediction_04.ipynb (prediction on test data & outputs on specified format)<br />
  
-May still work on:<br />

        #preprocess data
            #dimension reduction (pca, automatic relavance determination, etc.)
            #add features (use automated methods?)-> extra_automated_feature_engineering.ipynb

        #model
            #try different models
            #tune hyper parameters -> 5_hypertuning.ipynb

        #model evaluation (identify important features, etc.)

- pipeline_simple_example.ipynb (a simple example of how to use a pipeline)

