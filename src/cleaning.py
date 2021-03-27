import pandas as pd 
import numpy as np 

def import_data():
    df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
    return df

def drop_cols(df):
    cols_to_drop = ['customerID', 'gender', 'SeniorCitizen', 'Partner', 'Dependents',
                    'PhoneService', 'MultipleLines', 'OnlineSecurity', 'OnlineBackup', 
                    'DeviceProtection','StreamingTV', 'StreamingMovies','PaperlessBilling',
                    'PaymentMethod', 'TotalCharges']
    df = df.drop(columns = cols_to_drop)
    return df

def make_dummy_cols(df):
    colums_to_dummy = ['InternetService', 'TechSupport', 'Contract']
    df = pd.get_dummies(df, columns=colums_to_dummy)
    return df

def clean_column_headers(df):
    #Duplicate 'no internet' columns
    new_df = df.drop(columns = "TechSupport_No internet service")
    new_df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})
    col_header_dict = {"tenure": "tenure", "MonthlyCharges": "monthly_charges", "Churn": "churn", "InternetService_DSL": "internet_dsl", "InternetService_Fiber optic": "internet_fiber", 
                        "InternetService_No": "internet_no", "TechSupport_No": "tech_support_no", "TechSupport_Yes": "tech_support_yes", "Contract_Month-to-month": "contract_monthly", 
                        "Contract_One year": "contract_1_year", "Contract_Two year": "contract_2_year"}
    new_df = new_df.rename(columns = col_header_dict)
    return new_df

def main():
    df = import_data()
    df = drop_cols(df)
    df = make_dummy_cols(df)
    df = clean_column_headers(df)
    df.to_csv("cleaned_data.csv")

if __name__ == "__main__":
    main()