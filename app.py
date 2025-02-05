import streamlit as st
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv('diabetes.csv')

df.columns = df.columns.str.lower()

x = df.drop(['outcome'], axis=1)
y = df['outcome']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

rf = RandomForestClassifier()
rf.fit(x_train, y_train)

st.title('Ashwin DENTAL CLINIC: Diabetes Checkup')

st.subheader('Training Data Stats')
st.write(df.describe())

st.subheader('Visualization')
st.bar_chart(df)

def user_report():
    pregnancies = st.sidebar.slider('Pregnancies', 0, 17, 3)
   

    glucose = st.sidebar.slider('Glucose', 0, 200, 120)
    bp = st.sidebar.slider('Blood Pressure', 60, 122, 70)
    skinthickness = st.sidebar.slider('Skin Thickness', 10, 100, 20)
    insulin = st.sidebar.slider('Insulin', 0, 846, 79)
    bmi = st.sidebar.slider('BMI', 0, 67, 20)
    dpf = st.sidebar.slider('Diabetes Pedigree Function', 0.0, 2.4, 0.47)
    age = st.sidebar.slider('Age', 21, 88, 33)

    user_report_data = {
        'pregnancies': pregnancies,
        'glucose': glucose,
        'bloodpressure': bp,
        'skinthickness': skinthickness,
        'insulin': insulin,
        'bmi': bmi,
        'diabetespedigreefunction': dpf,
        'age': age
    }
    report_data = pd.DataFrame(user_report_data, index=[0])
    return report_data

user_data = user_report()

st.subheader('Accuracy:')
st.write(str(accuracy_score(y_test, rf.predict(x_test)) * 100) + '%')

user_result = rf.predict(user_data)

st.subheader('Report:')
output = ''
if user_result[0] == 0:
    output = 'You are healthy'
else:
    output = 'You have Diabetes'

st.write(output)
