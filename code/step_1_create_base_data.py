# Merge training data (month 1, month 2, month 3)

# Load Libraries
import step_0_load_data as load_data
import pandas as pd


# Set to display full dataframe
pd.set_option('display.max_rows', 999)
pd.set_option('display.max_columns', 999)

# Load Data
mypath = "../data/"
mydata = load_data.get_file_names(mypath)
data_files = load_data.load_copy_data(mydata, mypath)
# data = data_files['data_merged'].copy()

# Load Dataset
month_1 = data_files['train_month_1']
month_2 = data_files['train_month_2']
month_3 = data_files['train_month_3_with_target']

# df_1 = pd.DataFrame(month_1).copy()
# df_2 = pd.DataFrame(month_2).copy()
# df_3 = pd.DataFrame(month_3).copy()

#Check dimension of data
print(f"We have {month_1.shape[0]} rows and {month_1.shape[1]} columns in our month 1 training dataset.")
print(f"We have {month_2.shape[0]} rows and {month_2.shape[1]} columns in our month 2 training dataset.")
print(f"We have {month_3.shape[0]} rows and {month_3.shape[1]} columns in month 3 training dataset.")







# # Merge Dataframes
# df_1 =  df_1.drop(['customer_occupation_code', 'customer_education','customer_postal_code', 'customer_birth_date','customer_gender','customer_since_bank','customer_since_all'], axis=1)
# df_2 =  df_2.drop(['customer_occupation_code', 'customer_education','customer_postal_code', 'customer_birth_date','customer_gender','customer_since_bank','customer_since_all'], axis=1)
#
# df_1.columns=['client_id','homebanking_active_1', 'has_homebanking_1', 'has_insurance_21_1', 'has_insurance_23_1', 'has_life_insurance_fixed_cap_1', 'has_life_insurance_decreasing_cap_1', 'has_fire_car_other_insurance_1', 'has_personal_loan_1', 'has_mortgage_loan_1', 'has_current_account_1', 'has_pension_saving_1', 'has_savings_account_1', 'has_savings_account_starter_1', 'has_current_account_starter_1', 'bal_insurance_21_1', 'bal_insurance_23_1', 'cap_life_insurance_fixed_cap_1', 'cap_life_insurance_decreasing_cap_1', 'prem_fire_car_other_insurance_1', 'bal_personal_loan_1', 'bal_mortgage_loan_1', 'bal_current_account_1', 'bal_pension_saving_1', 'bal_savings_account_1', 'bal_savings_account_starter_1', 'bal_current_account_starter_1', 'visits_distinct_so_1', 'visits_distinct_so_areas_1', 'customer_self_employed_1', 'customer_children_1', 'customer_relationship_1']
# df_2.columns=['client_id','homebanking_active_2', 'has_homebanking_2', 'has_insurance_21_2', 'has_insurance_23_2', 'has_life_insurance_fixed_cap_2', 'has_life_insurance_decreasing_cap_2', 'has_fire_car_other_insurance_2', 'has_personal_loan_2', 'has_mortgage_loan_2', 'has_current_account_2', 'has_pension_saving_2', 'has_savings_account_2', 'has_savings_account_starter_2', 'has_current_account_starter_2', 'bal_insurance_21_2', 'bal_insurance_23_2', 'cap_life_insurance_fixed_cap_2', 'cap_life_insurance_decreasing_cap_2', 'prem_fire_car_other_insurance_2', 'bal_personal_loan_2', 'bal_mortgage_loan_2', 'bal_current_account_2', 'bal_pension_saving_2', 'bal_savings_account_2', 'bal_savings_account_starter_2', 'bal_current_account_starter_2', 'visits_distinct_so_2', 'visits_distinct_so_areas_2', 'customer_self_employed_2', 'customer_children_2', 'customer_relationship_2']
# data=[df,df_1, df_2]
#
# dataset = reduce(lambda left,right: pd.merge(left,right,on='client_id'), data)
#
# columns = dataset.columns.values.tolist()
# print(columns)
