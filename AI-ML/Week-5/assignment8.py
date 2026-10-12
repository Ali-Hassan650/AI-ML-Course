'''
Code for Spam Detection using Naive Bayes

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv('spam_detection_dataset.csv')

X = df.drop("spam", axis=1)
Y = df["spam"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size= 0.2, random_state= 42, stratify= Y
)   

model = GaussianNB()
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(Y_test, Y_pred))
print("Confusion Matrix:")
print(confusion_matrix(Y_test, Y_pred))


# ALl 4 Classifiers Head-to-Head

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

df = pd.read_csv('spam_detection_dataset.csv')

X = df.drop("spam", axis=1)
Y = df["spam"]
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size= 0.2, random_state= 42, stratify= Y
)

models = {'Logistic Regression': LogisticRegression(max_iter= 1000),
          'SVM (RBF)': SVC(), 'KNN (K=5)': KNeighborsClassifier(5),
          "Naive Bayes": GaussianNB()}
for name, m in models.items():
    pipe = make_pipeline(StandardScaler(), m).fit(X_train, Y_train)
    print(f'{name:20s} accuracy = {pipe.score(X_test, Y_test):.3f}')
'''

# Code for Spam Detection using Naive Bayes and Logistic Regression

import pandas as pd
import re

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


df = pd.read_csv("enron_spam_data.csv")

df = df[["Subject", "Message", "Spam/Ham"]]


df["Subject"] = df["Subject"].fillna("")
df["Message"] = df["Message"].fillna("")


df["text"] = df["Subject"] + " " + df["Message"]


def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"\S+@\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


df["text"] = df["text"].apply(clean_text)


df["spam"] = df["Spam/Ham"].map({
    "spam": 1,
    "ham": 0
})

df = df.dropna(subset=["spam"])


X = df["text"]
Y = df["spam"]


X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42,stratify=Y
)

vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=10000
)

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)


model = MultinomialNB()

model.fit(X_train, Y_train)


pred = model.predict(X_test)


print("Accuracy:", accuracy_score(Y_test, pred))

print("\nClassification Report:")
print(classification_report(Y_test, pred))

print("\nConfusion Matrix:")
print(confusion_matrix(Y_test, pred))


def predict_spam(message):

    message = clean_text(message)

    message = vectorizer.transform([message])

    prediction = model.predict(message)[0]

    if prediction == 1:
        return "Spam"
    else:
        return "Ham"


email = "Congratulations! You have won a free prize. Click here now!"

print("\nPrediction:", predict_spam(email))


# Logistic regression

# import pandas as pd
# import re

# from sklearn.model_selection import train_test_split
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.linear_model import LogisticRegression

# from sklearn.metrics import (
#     accuracy_score,
#     precision_score,
#     recall_score,
#     f1_score,
#     confusion_matrix
# )


# df = pd.read_csv("enron_spam_data.csv")

# # Select required columns
# df = df[["Subject", "Message", "Spam/Ham"]]

# df["Subject"] = df["Subject"].fillna("")
# df["Message"] = df["Message"].fillna("")

# # Combine Subject and Message
# df["text"] = df["Subject"] + " " + df["Message"]



# def clean_text(text):
#     text = text.lower()

#     text = re.sub(r"http\S+|www\S+", "", text)

#     text = re.sub(r"\S+@\S+", "", text)

#     text = re.sub(r"[^a-zA-Z\s]", " ", text)

#     text = re.sub(r"\s+", " ", text).strip()

#     return text


# df["text"] = df["text"].apply(clean_text)


# df["spam"] = df["Spam/Ham"].map({
#     "spam": 1,
#     "ham": 0
# })

# df = df.dropna(subset=["spam"])

# X = df["text"]
# Y = df["spam"]

# X_train, X_test, Y_train, Y_test = train_test_split(
#     X,
#     Y,
#     test_size=0.2,
#     random_state=42,
#     stratify=Y
# )

# vectorizer = TfidfVectorizer(
#     stop_words="english",
#     max_features=10000
# )

# X_train_tfidf = vectorizer.fit_transform(X_train)
# X_test_tfidf = vectorizer.transform(X_test)

# log_reg = LogisticRegression(max_iter=1000)

# log_reg.fit(X_train_tfidf, Y_train)

# Y_pred = log_reg.predict(X_test_tfidf)


# accuracy = accuracy_score(Y_test, Y_pred)
# precision = precision_score(Y_test, Y_pred)
# recall = recall_score(Y_test, Y_pred)
# f1 = f1_score(Y_test, Y_pred)

# cm = confusion_matrix(Y_test, Y_pred)

# print("=" * 50)
# print("Logistic Regression Results")
# print("=" * 50)

# print(f"Accuracy  : {accuracy:.3f}")
# print(f"Precision : {precision:.3f}")
# print(f"Recall    : {recall:.3f}")
# print(f"F1-Score  : {f1:.3f}")

# print("\nConfusion Matrix:")
# print(cm)

# print("\nConfusion Matrix Details:")
# print("TN =", cm[0][0])
# print("FP =", cm[0][1])
# print("FN =", cm[1][0])
# print("TP =", cm[1][1])
