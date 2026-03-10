import streamlit as st
import pickle
model = pickle.load(open("../models/spam_model.pkl", "rb"))
vectorizer = pickle.load(open("../models/vectorizer.pkl", "rb"))
st.title("📩 SMS Spam Detector")
st.write("Type a message and press Enter or click Check.")
with st.form("spam_form"):
    message = st.text_input("Enter SMS message")
    submit = st.form_submit_button("Check Message")
if submit and message:
    msg_vector = vectorizer.transform([message])
    prediction = model.predict(msg_vector)
    if prediction[0] == 1:
        st.error("🚫 This message is SPAM")
    else:
        st.success("✅ This message is NOT SPAM")
