import pandas as pd 
import os

def get_all_data():
    raw_data = pd.read_csv("./data/complaints.csv")
    return raw_data

def get_wells_fargo_data():
    raw_data = pd.read_csv("./data/complaints.csv")
    mask = raw_data['Company'].isin(["WELLS FARGO & COMPANY"])
    wells_fargo_data = raw_data[mask]
    return wells_fargo_data
