import pickle

# load saved model
model = pickle.load(open("spam_model.pkl", "rb"))

# load vectorizer
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# take user input
msg = input("Enter SMS message: ")

# convert message to vector
msg_vector = vectorizer.transform([msg])

# predict
prediction = model.predict(msg_vector)

# show result
if prediction[0] == 1:
    print("This message is SPAM")
else:
    print("This message is HAM (Normal Message)")