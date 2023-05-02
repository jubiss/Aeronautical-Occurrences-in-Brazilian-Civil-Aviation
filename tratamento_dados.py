import pandas as pd
import sklearn.impute as impute
import numpy as np
def treat_aeronave_data(df_aeronave):
    imp_cont = impute.SimpleImputer(strategy='constant', fill_value=1)
    imp_cont.fit(df_aeronave['quantidade_fatalidades'])
    df_aeronave['quantidade_fatalidades'] = imp_cont.transform(df_aeronave['quantidade_fatalidades'])
    #imp_knn = impute.KNNImputer()
    return df_aeronave