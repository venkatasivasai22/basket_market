import streamlit as st
import pandas as pd
import joblib

# Load association rules
Rules = joblib.load('association_rules.pkl')

def recommend_items(rules, input_items):
    recommended_items = set()
    
    for input_item in input_items:
        # Filter rules for the given input item in antecedents
        filtered_rules = rules[rules['antecedents'].apply(lambda x: input_item in x)]
        
        if not filtered_rules.empty:
            # Sort rules by lift, confidence, and support in descending order
            filtered_rules = filtered_rules.sort_values(by=['lift', 'confidence', 'support'], ascending=False)
            
            # Extract recommended items from consequents column
            recommended_items.update(filtered_rules['consequents'].iloc[0])
    
    return recommended_items

def load_association_rules():
    return Rules

# Load association rules
rules = load_association_rules()

# Streamlit app
st.title('Item Recommendation System')

# User input
user_input = st.text_input('Enter the items you are interested in (separated by commas):')

if st.button('Recommend') and user_input:
    input_items = [item.strip() for item in user_input.split(',')]
    
    # Get recommended items based on user input
    recommended_items = recommend_items(rules, input_items)
    
    st.write("Recommended items:", recommended_items)

