# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('final_deployment.pkl', 'rb'))


# creating a function for Prediction

def Fraud_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The case is Fraud'
    else:
      return 'The case is genuine'
  
    
  
def main():
    
    
    # giving a title
    st.title('Insurance Fraud Analysis')
    
    # getting the input data from the user
    
    
    Age = st.text_input('Age of the person-  0 to 17: 1 , 18 to 29: 2 , 30 to 49: 3 , 50 to 69: 4 , 70 or Older: 5')
    Gender = st.text_input('Gender-  Female :0,  Male : 1')
    Days_spend_hsptl = st.text_input('Number of Days spent in Hospital')
    ccs_diagnosis_code = st.text_input('Enter Diagnosis Code')
    ccs_procedure_code = st.text_input('Enter Procedure Code')
    apr_drg_description = st.text_input('Enter Drug Description')
    Code_illness = st.text_input('Enter Illness Code')
    Mortality_risk = st.text_input('Enter Risk of Mortality')
    Weight_baby = st.text_input('Enter the Weight of Baby')
    Emergency = st.text_input('Emergency- Yes: 1, No: 0')
    Tot_charg = st.text_input('Amount of Total Charge')
    Tot_cost = st.text_input('Amount of Total Cost')
    ratio_of_total_costs_to_total_charges = st.text_input('Ratio of Total cost/Total charge')
    Payment_Typology = st.text_input('Payment Method-  Medicare: 1,  Medicaid: 2,  Other Governments: 3')
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Predict'):
        diagnosis = Fraud_prediction([Age, Gender,Days_spend_hsptl,
                                      ccs_diagnosis_code, ccs_procedure_code,apr_drg_description,
                                      Code_illness, Mortality_risk,Weight_baby, Emergency,
                                      Tot_charg,Tot_cost, ratio_of_total_costs_to_total_charges,
                                      Payment_Typology])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()