import streamlit as st
import requests
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(layout='wide')

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

lottie_coder=load_lottieurl('https://assets4.lottiefiles.com/packages/lf20_7VEmrT02fx.json')
hello = load_lottieurl('https://assets9.lottiefiles.com/private_files/lf30_jyxnt8gq.json')
eda = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_aKYYCrPjTp.json")
sql = load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_w11f2rwn.json")
info=load_lottieurl('https://assets2.lottiefiles.com/packages/lf20_dhcsd5b5.json')
image=Image.open('my.jpg')

co1, co2 = st.columns((1,2))
with co1:
    st.title("Welcome to my Portfolio") 
    st.image(image, width = 300)
with co2:
    st_lottie(hello, height=400)
st.divider()



with st.container():
    selected=option_menu(
        menu_title=None,
        options=['About','Projects','Contact'],
        icons=['person','projector','phone'],
        orientation='horizontal'
    )

if selected =='About':
    with st.container():
        col1, col2=st.columns(2)
        with col1:
            st.write("##")
            st.subheader('Hey Guys :wave:')
            st.subheader('My protfolio Website')
            st.title("I am Mitrabhanu Panda")
            st.subheader("SOME INFORMATIONS ABOUT ME IS IN BELOW")
            
        with col2:
            st_lottie(lottie_coder)

    st.divider()

    with st.container():
        col3, col4=st.columns(2)
        with col3:
            st.subheader("""
            :book: **:green[EDUCATION]**
                 """)
            st.write("""
            - **:blue[PARALA MAHARAJA ENGINEERING COLLEGE (2018 - 2022)]**
                 - Bachelor of Technology : ELECTRICAL ENGINEERING
                 - Percentage : 78%
            - **:blue[NAVAJYOTI JUNIOR SCIENCE COLLEGE (2016 - 2018)]**
                 - Intermediate : SCIENCE
                 - Precentage : 70%
            - **:blue[BALARAMDEV BIDYAPITHA         (2004 - 2016)]**
                 - 10th
                 - Percentage : 82%
                 """)

        with col4:
            st.subheader("""
            :computer: **:green[SKILLS]**
            - Python
            - SQL
            - Data Analysis
            - Data Visuilization
            - Tableau
            - MS Excel
            - Web Scraping
            """)

        st.divider()

    with st.container():
        col5, col6 = st.columns(2)

        with col5:
            st.subheader("""
            :male-student: **:green[PERSONAL COMPETENCIES]**
            - Communication Skills
            - Work Ethic
            - Quick Learner 
            - Problem Solving
            - Teamwork Skills
            - Positive Attitude
            - Self Confidence
            """)

        with col6:
            st.subheader("""
            :man-bouncing-ball: **:green[HOBBIES/INTERESTS]**
            - Playing Cricket
            - Travelling
            - Learning New Technologies
            - Learning new things
            """)

        st.divider()

    with st.container():

        c, l = st.columns(2)
        with c:
            st.subheader("""
            :microphone: **:green[LANGUAGES]**
            - English
            - Odia
            - Hindi
            """)

if selected == "Projects":
    with st.container():
        st.header("**:red[My Projects]**")
        st.write("##")
        col9, col10 = st.columns((1,2))
        with col9:
            st.subheader("**:blue[1)]**")
            st_lottie(eda)
        with col10:
            st.subheader("**:blue[CITY-WISE EXPLORATORY DATA ANALYSIS ON APARTMENTS]**")
            st.subheader("""
            **:green[Problem Statement:-]**
             1. In which city we can buy an apartment in average price.
             2. Which owner have more apartments in every cities.
             3. Which Construction Status is More in every cities.
             4. Which type of Bhk is more in every cities
             5. Which type of Bhk are more price on every cities.

            """)
            st.subheader("""
            **:green[Objective of the Project:-]**
            - Finding a average price apartments.
            - To visualize the data using various visualization techniques
            """)
            st.subheader("""
            **:green[Summary:-]**
            - I have selected  Makaan.com website for our web scraping project
            - Request to the website
            - Import Beautiful Soup and all the necessary libraries for scraping data
            - Check length’s of all columns  and create the DataFrame 
            - Export into .csv format and read csv file  and  clean the Data
            - Analysis of Univariate, Bivariate and Multivariate
            """)
            st.markdown("[Visit Github Repo](https://github.com/MitrabhanuPanda/Python/blob/e1f96da087093c19cdeb818b82ef9a69a2c797b5/City-wise%20Apartment's%20Data%20Analysis.ipynb)")
    
    st.divider()

    with st.container():
        col11, col12 = st.columns((1,2))
        with col11:
            st.subheader("**:blue[2)]**")
            st_lottie(sql)
        with col12:
            st.subheader("**:blue[SQL PROJECT:-  E-Commerce DATA ANALYSIS]**")
            st.subheader(""" 
            **:green[Description:-]**
            - I have created all the required tables with the required constraints and created a relation between tables then using Primary Key and Foreign Key, then insert data into this tables. 
            """)
            st.subheader("""
            **:green[Objective of the Project:-]**
            - Finding and Analyzing the E-Commerce  Data using SQL Querries.
            """)
            st.markdown("[Visit Githuib Repo](https://github.com/MitrabhanuPanda/SQL/blob/ce978d97caf797a3266f2bc5505813626771cfaf/PROJECT/E-COMMERCE%20PROJECT.sql)")


if selected == "Contact":
    with st.container():
        col11, col12 = st.columns((1,2))
        with col11:
            st_lottie(info)
        with col12:
            st.header("**:red[My Info:]**")
            st.write('**Name: Mitrabhanu Panda**')
            st.write('**Contact Number: 7437049800**')
            st.write('**email: mitrabhanupanda22@gmail.com**')
            st.write('**linkdin:[Mitrabhanu Panda](https://www.linkedin.com/public-profile/settings?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_self_edit_contact-info%3BaYgx4T2SRhCDGkiJJVK6fw%3D%3D)**')
            st.write('**github:[MitrabhanuPanda](https://github.com/MitrabhanuPanda)**')
   

