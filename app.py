import pandas as pd
import joblib
import streamlit as st

Rules = joblib.load('association_rules.pkl')

def recommend_items(rules, input_item):
    filtered_rules = rules[rules['antecedents'].apply(lambda x: input_item in x)]
    filtered_rules = filtered_rules.sort_values(by='support', ascending=False)
    recommended_items = filtered_rules['consequents'].tolist()
    return set(recommended_items[0]) if recommended_items else set()

def load_association_rules():
    return Rules

def main():
    rules = load_association_rules()

    st.title("Item Recommender")

    user_input = st.text_input("Enter an item:")

    if st.button("Recommend"):
        recommended_items = recommend_items(rules, user_input)
        st.write(f"Recommended items for {user_input}: {recommended_items}")

if __name__ == "__main__":
    main()