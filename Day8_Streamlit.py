import streamlit as st
st.title('My first streamlit app')
st.header('Artificial Intelligence')
st.subheader('Deep Learning')

st.write('You can use Streamlit to create interactive web applications with python')

user_input=st.text_input('Enter your name:')
st.text(f'Hello ,{user_input}!')

#title
st.title('Streamlit Text Input Example')
#Single line text input
user_name=st.text_input('Enter your name')
st.write('Your name is:',user_name)
user_bio=st.text_area('Enter your biodata')
st.write('Your bio is:',user_bio)

#number input
user_age=st.number_input('Enter your age',min_value=18, max_value=100, value=25)
st.write('Your age is:',user_age)
appt_date=st.date_input('select appointment date')
st.write('appointment date:',appt_date)

 #time input
appt_time=st.time_input('select appointment time')
st.write('Appointment time:', appt_time)

#combining inputs
if st.button('Submit'):
    st.write('Name:',user_name)
    st.write('Bio',user_bio)
    st.write('Age:',user_age)
    st.write('Appointment Date:', appt_date)
    st.write('Appointment Time:', appt_time)