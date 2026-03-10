import pickle
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
msg = input("Enter SMS message: ")
msg_vector = vectorizer.transform([msg])
prediction = model.predict(msg_vector)
if prediction[0] == 1:
    print("This message is SPAM")
else:
    print("This message is HAM (Normal Message)")
