import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)


url = "https://raw.githubusercontent.com/prasertcbs/basic-dataset/master/Loan-Approval-Prediction.csv"

df = pd.read_csv(url)

print("Dataset loaded successfully!")

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())


print("\nDataset Information:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

df = df.drop("Loan_ID", axis=1)

categorical_columns = [
    "Gender",
    "Married",
    "Dependents",
    "Education",
    "Self_Employed",
    "Credit_History",
    "Loan_Amount_Term"
]

for column in categorical_columns:
    df[column] = df[column].fillna(df[column].mode()[0])


df["LoanAmount"] = df["LoanAmount"].fillna(
    df["LoanAmount"].median()
)


df["Dependents"] = df["Dependents"].replace(
    "3+",
    "3"
)

df["Gender"] = df["Gender"].map({

    "Male": 0,
    "Female": 1
})

df["Married"] = df["Married"].map({
    "No": 0,
    "Yes": 1
})

df["Education"] = df["Education"].map({
    "Not Graduate": 0,
    "Graduate": 1
})


df["Self_Employed"] = df["Self_Employed"].map({
    "No": 0,
    "Yes": 1
})


df["Dependents"] = df["Dependents"].astype(int)


df["Property_Area"] = df["Property_Area"].map({
    "Rural": 0,
    "Semiurban": 1,
    "Urban": 2
})


df["Loan_Status"] = df["Loan_Status"].map({
    "N": 0,
    "Y": 1
})


print("\nData after preprocessing:")
print(df.head())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values After Preprocessing:")
print(df.isnull().sum())


X = df.drop("Loan_Status", axis=1)

y = df["Loan_Status"]


print("\nFeatures:")
print(X.columns.tolist())

print("\nTarget:")
print("Loan_Status")


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


print("\nTraining Data Shape:")
print(X_train.shape)

print("\nTesting Data Shape:")
print(X_test.shape)


model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)


model.fit(X_train, y_train)

print("\nDecision Tree model trained successfully!")


y_pred = model.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)

print("MODEL ACCURACY")


print("Accuracy:", accuracy)
print("Accuracy (%):", accuracy * 100)



cm = confusion_matrix(y_test, y_pred)

print("CONFUSION MATRIX")

print(cm)


print("CLASSIFICATION REPORT")


print(
    classification_report(
        y_test,
        y_pred,
        target_names=[
            "Loan Rejected",
            "Loan Approved"
        ]
    )
)


print("LOAN APPROVAL PREDICTION")

print("\nEnter applicant information:")


gender = input("Gender (Male/Female): ")

married = input("Married (Yes/No): ")

dependents = input("Dependents (0/1/2/3): ")


education = input("Education (Graduate/Not Graduate): ")

self_employed = input("Self Employed (Yes/No): ")

applicant_income = float(
    input("Applicant Income: ")
)

coapplicant_income = float(
    input("Co-applicant Income: ")
)

loan_amount = float(
    input("Loan Amount: ")
)

loan_amount_term = float(
    input("Loan Amount Term: ")
)


credit_history = float(
    input("Credit History (1 = Good, 0 = Bad): ")
)

property_area = input(
    "Property Area (Rural/Semiurban/Urban): "
)



if gender == "Male":
    gender = 0
else:
    gender = 1


if married == "No":
    married = 0
else:
    married = 1


if education == "Not Graduate":
    education = 0
else:
    education = 1


if self_employed == "No":
    self_employed = 0
else:
    self_employed = 1


if property_area == "Rural":
    property_area = 0

elif property_area == "Semiurban":
    property_area = 1

else:
    property_area = 2


dependents = int(dependents)



user_data = pd.DataFrame({

    "Gender": [gender],

    "Married": [married],

    "Dependents": [dependents],

    "Education": [education],

    "Self_Employed": [self_employed],

    "ApplicantIncome": [applicant_income],

    "CoapplicantIncome": [coapplicant_income],

    "LoanAmount": [loan_amount],

    "Loan_Amount_Term": [loan_amount_term],

    "Credit_History": [credit_history],

    "Property_Area": [property_area]

})


prediction = model.predict(user_data)

print("\nDecision Path:")

node_indicator = model.decision_path(user_data)

leaf_id = model.apply(user_data)

feature = model.tree_.feature
threshold = model.tree_.threshold

node_index = node_indicator.indices[
    node_indicator.indptr[0]:
    node_indicator.indptr[1]
]

for node_id in node_index:

    if leaf_id[0] == node_id:
        continue

    feature_name = X.columns[feature[node_id]]

    print(
        f"{feature_name} <= {threshold[node_id]:.2f}"
    )

print("LOAN PREDICTION RESULT")



if prediction[0] == 1:

    print("LOAN APPROVED")

    print(
        "According to the Decision Tree model, "
        "the applicant is likely to get the loan."
    )

else:

    print("LOAN REJECTED")

    print(
        "According to the Decision Tree model, "
        "the applicant is unlikely to get the loan."
    )