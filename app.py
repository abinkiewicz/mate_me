import streamlit as st
import pandas as pd  # type: ignore

DATA = 'welcome_survey_simple_v1.csv'

st.title(":wave: Mate Me")

@st.cache_data
def get_all_participants():
    all_df = pd.read_csv(DATA, sep=';')

    return all_df

with st.sidebar:
    st.header("Tell me something about you")
    st.markdown("I will help you find mates with matching interests")
    age = st.selectbox("Age", ['<18', '25-34', '45-54', '35-44', '18-24', '>=65', '55-64', 'Unknown'])
    edu_level = st.selectbox("Education", ['Primary', 'Secondary', 'Higher'])
    fav_animals = st.selectbox("Favourite animal", ['None', 'Dogs', 'Cats', 'Other', 'Dogs & cats'])
    fav_place = st.selectbox("Favourite place", ['By the wather', 'In the forest', 'In the mountains', 'Other'])
    gender = st.radio("Sex", ['Male', 'Female'])

    person_df = pd.DataFrame([
        {
            'age': age,
            'edu_level': edu_level,
            'fav_animals': fav_animals,
            'fav_place': fav_place,
            'gender': gender
        }
    ])


st.write("Your data:")
st.dataframe(person_df, hide_index=True)

all_df = get_all_participants()
st.write("Example of people from the base:")
st.dataframe(all_df.sample(10), hide_index=True)