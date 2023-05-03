





import pandas as pd
import numpy as np
import pickle 
import streamlit as st



model=pickle.load(open('pipe.pkl','rb'))
st.title('IRIS flower classification')


SepalLengthCm=st.number_input('sepel lenth in cm')
SepalWidthCm=st.number_input('sepel width in cm')
PetalLengthCm=st.number_input('petal lenth in cm')
PetalWidthCm=st.number_input('petal width in cm')



user_input=np.array([SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm])
user_input=user_input.reshape(1,4)


predict =st.button('predict')
prediction=model.predict(user_input)

if  predict:
    

    if prediction==0:
        st.header('setosa')
    elif prediction==1:
        st.header( 'versicolor')
    else:
        st.header('virginica')