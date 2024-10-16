import pandas as pd
from surprise import Dataset, Reader, SVD
import streamlit as st

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('ad_interactions.csv')

# Build the recommendation model
@st.cache_resource
def build_model(data):
    reader = Reader(rating_scale=(1, 5))  # Adjust scale according to your data
    surprise_data = Dataset.load_from_df(data[['user_id', 'ad_id', 'interaction']], reader)
    trainset = surprise_data.build_full_trainset()
    
    model = SVD()
    model.fit(trainset)
    
    return model

# Get recommendations
def get_recommendations(model, user_id, ad_ids, n_recommendations=5):
    user_ads = [(user_id, ad_id) for ad_id in ad_ids]
    predictions = model.predict(user_ads)
    recommended_ads = sorted(predictions, key=lambda x: x.est, reverse=True)
    return [(ad[1], ad.est) for ad in recommended_ads[:n_recommendations]]

# Streamlit app
st.title('Ad Recommendation System')

# Load the data
data = load_data()
ad_ids = data['ad_id'].unique()

# Select user ID
user_id = st.selectbox('Select User ID:', data['user_id'].unique())

# Build the model
model = build_model(data)

# Recommend ads
if st.button('Get Recommendations'):
    recommendations = get_recommendations(model, user_id, ad_ids)
    st.write(f"Recommended ads for User ID {user_id}:")
    for ad_id, score in recommendations:
        st.write(f"Ad ID: {ad_id}, Predicted Score: {score:.2f}")

# Run the app
if __name__ == '__main__':
    st.run()
