import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("vhi_dataset.csv")

st.set_page_config(layout="wide")
st.title("VHI Data Analysis")

def initialize_session_state():
    defaults = {
        'selected_index': 'VHI',
        'selected_region': df['Region_Name'].unique()[0],
        'week_range': (1, 52),
        'year_range': (df['Year'].min(), df['Year'].max()),
        'ascending_order': False
    }
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

initialize_session_state()
def reset_filters():
    st.session_state.selected_index = 'VHI'
    st.session_state.selected_region = df['Region_Name'].unique()[0]
    st.session_state.week_range = (1, 52)
    st.session_state.year_range = (df['Year'].min(), df['Year'].max())

col1, col2 = st.columns([1, 3])

with col1:
    index_options = ['VHI', 'VCI', 'TCI']
    selected_index = st.selectbox(
        "Select Index", 
        options=index_options, 
        index=index_options.index(st.session_state.get('selected_index', 'VHI')))
    st.session_state.selected_index = selected_index

    region_options = df['Region_Name'].unique()
    selected_region = st.selectbox(
        "Select Region", 
        options=region_options, 
        index=list(region_options).index(st.session_state.get('selected_region', region_options[0])))
    st.session_state.selected_region = selected_region

    week_range = st.slider(
        "Select Week Range", 
        1, 52, 
        st.session_state.get('week_range', (1, 52)))
    st.session_state.week_range = week_range

    year_range = st.slider(
        "Select Year Range", 
        int(df['Year'].min()), int(df['Year'].max()), 
        st.session_state.get('year_range',
        (df['Year'].min(), df['Year'].max())))
    st.session_state.year_range = year_range


    if st.button("Reset Filters"):
        reset_filters()

    ascending = st.checkbox("Ascending", key="ascending_checkbox")
    descending = st.checkbox("Descending", key="descending_checkbox")
    if ascending and descending:
        st.warning("Both sorting options selected. Defaulting to no sorting.")
        ascending, descending = False, False

with col2:
    filtered_df = df[(df['Region_Name'] == st.session_state.selected_region) & 
                     (df['Week'].between(st.session_state.week_range[0], st.session_state.week_range[1])) & 
                     (df['Year'].between(st.session_state.year_range[0], st.session_state.year_range[1]))]

    if ascending:
        filtered_df = filtered_df.sort_values(by=st.session_state.selected_index, ascending=True)
    elif descending:
        filtered_df = filtered_df.sort_values(by=st.session_state.selected_index, ascending=False)

    tab1, tab2, tab3 = st.tabs(["Table", "Time Series Plot", "Comparison Plot"])

    with tab1:
        st.dataframe(filtered_df)

    with tab2:
        fig1, ax1 = plt.subplots(figsize=(8, 4)) 
        filtered_df['pong'] = filtered_df[st.session_state.selected_index].rolling(window=5).mean()  
        
        sns.barplot(data=filtered_df, x='Year', y=f'{st.session_state.selected_index}', 
                    palette='Set2', ax=ax1, ci=None) 
        
        ax1.set_title(f"{st.session_state.selected_index} for {st.session_state.selected_region}", 
                    fontsize=16, fontweight='bold', pad=20)     

        plt.xticks(rotation=45, ha='right', fontsize=8)
        
        ax1.grid(True, linestyle='--', alpha=0.7, axis='y')
        st.pyplot(fig1)



    with tab3:
        comparison_df = df[(df['Week'].between(st.session_state.week_range[0], st.session_state.week_range[1])) & 
                           (df['Year'].between(st.session_state.year_range[0], st.session_state.year_range[1]))]
        comparison_data = comparison_df.groupby('Region_Name')[st.session_state.selected_index].mean().reset_index()

        fig2, ax2 = plt.subplots(figsize=(8, 4))
        sns.barplot(data=comparison_data, x='Region_Name', y=st.session_state.selected_index, ax=ax2)
        ax2.set_title(f"Average {st.session_state.selected_index} Comparison Across Regions")
        ax2.set_xlabel("Region")
        ax2.set_ylabel(f"Average {st.session_state.selected_index}")
        plt.xticks(rotation=45, ha='right', fontsize=8)

        selected_region_idx = comparison_data[comparison_data['Region_Name'] == st.session_state.selected_region].index[0]
        ax2.patches[selected_region_idx].set_facecolor('red')
        st.pyplot(fig2)
