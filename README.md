![Screenshot 2024-09-18 231019](https://github.com/user-attachments/assets/e7fc14e4-4d6c-49d8-b3e1-e41557bc7059)

![Screenshot 2024-09-18 231058](https://github.com/user-attachments/assets/b8960c58-77e9-4548-926d-bfaa26c22680)
Diabetes Prediction Web App
----------------------------------------
This is a simple web application built with Streamlit that predicts whether a person has diabetes based on various health parameters. The prediction is done using a Random Forest Classifier trained on a dataset of medical records.

Features
---------------------------------------
1.Allows users to input their health parameters via sliders.

2.Predicts whether the user is likely to have diabetes or not based on the input data.

3.Displays the accuracy of the model on a test dataset.

4.Visualizes the dataset and provides basic statistics.

Dataset
--------------------------------------
The app uses the Pima Indians Diabetes Dataset, which consists of the following columns:

1.Pregnancies

2.Glucose

3.Blood Pressure

4.Skin Thickness

5.Insulin

6.BMI

7.Diabetes Pedigree Function

8.Age

9.Outcome (Target: 0 = Healthy, 1 = Diabetes)

How It Works
----------------------------------------
1.Data Input: The user provides their health data by adjusting sliders in the sidebar.

2.Model Training: A Random Forest Classifier is trained on the Pima Indians Diabetes dataset to predict the likelihood of diabetes.

3.Prediction: Based on the user input, the app predicts if the user is healthy or has diabetes and displays the result.

4.Accuracy: The app shows the accuracy of the trained model on test data.

Dependencies
----------------------------------------
1.Python 3.x

2.Streamlit

3.Pandas

4.Scikit-learn

You can install the necessary libraries using the following command:
-------------------------------------------

pip install streamlit pandas scikit-learn

How to Run
-----------------------------------
Clone the repository or download the source code.

Install the required dependencies.

Run the following command in your terminal:
-----------


streamlit run app.py


A new tab will open in your browser, where you can interact with the app.

How to Use the App
------------------------------
1.Adjust the health parameters on the sidebar using the sliders.

2.The app will show whether you are healthy or at risk of diabetes based on the input.

3.You can also see the accuracy of the model and basic statistics about the dataset.
