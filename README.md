# Churn_Prediction

Python = 3.9.5

Goal: Predict which of the customers will churn. 

Data: Customer information of a Belgian bank-insurer for retail customers above 18 years old.

File set up for this project:

code/ : contains all the code (.py, .ipynb) used in the project<br />
data/ : contains original data & transformed data<br />


code/ :

- load_data.py (reads and copies data provided the base path, returns a dictionary of dataframes)<br />
- get_base_data.ipynb (merges training data)<br />
- pipeline.ipynb (reads merged data, preprocesses data, and fits a model)<br />
  -did not tune any hyperparameters, just made a basic pipeline<br />
    
              -Things to work on:
              
                  #preprocess data
                      #dimension reduction (pca, automatic relavance determination, etc.)
                      #add features (use automated methods?)
                      #over sample/under sample to balance data?

                  #model
                      #try different models
                      #tune hyper parameters
                     
                  #model evaluation

- pipeline_simple_example.ipynb (a simple example of how to use a pipeline)

