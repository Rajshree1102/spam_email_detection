import streamlit as st
import joblib
import pandas as pd

model = joblib.load('Email_Classifier_model.pkl')

def predict_spam(text):
    prediction = model.predict([text])
    return prediction

def main():
    st.title('Email Spam Detection')
    st.write('Enter the email to check is it spam or not.')

    user_input = st.text_area('Enter text here:', '')

    if st.button('Detect'):
        prediction = predict_spam(user_input)
        if prediction == 'spam':
            st.error('SPAM Email.')
        else:
            st.success('Not Spam Email.')

if __name__ == '__main__':
    main()