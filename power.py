

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('C:/Users/HP/Music/power consumption/power.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('power consumption using machine learning',
                          
                          [ 'Home',
                            'power consumption using machine learning'
                           
                            ],
                          default_index=0)

# power consumption Prediction Page
if (selected == 'Home'):
    
    # page title
    st.title('power consumption using machine learning')

   
    st.image('5.jpg')

    

   
    
  
    
# power consumption Prediction Page
if (selected == 'power consumption using machine learning'):
    
    # page title
    st.title('power consumption using machine learning')

    
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    
    
        
    with col1:
        Globalreactivepower = st.text_input('Globalreactivepower')
    
    with col2:
        Voltage  = st.text_input('Voltage')
    
    with col3:
        Globalintensity	 = st.text_input('Globalintensity')

    with col1:
        Submetering1	 = st.text_input('Submetering1')

    with col2:
        Submetering2	 = st.text_input('Submetering2')

    with col3:
        Submetering3	 = st.text_input('Submetering3')
    
    
    
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('power Result'):
        diab_prediction = diabetes_model.predict([[Globalreactivepower, Voltage, Globalintensity,
        Submetering1, Submetering2, Submetering3]])

        st.success('The output is {}'.format(diab_prediction ))
        
        
        
    


    
    
    
   

if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")








