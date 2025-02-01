import streamlit as st

# --- PAGE SETUP ---
about_page = st.Page(
    "views/about_me.py",
    title="About Meisan",
    icon=":material/account_circle:",
    default=True,
)

project_2_page = st.Page(
    "views/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)


# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_2_page],
    }
)

st.set_page_config(page_title="YTU Chatbot", layout="centered")

with open( r"assets\\styles.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

# --- SHARED ON ALL PAGES ---
st.logo(r"assets\\Yangon_Technological_University.svg.png", size="large")
st.markdown("""<style>img[data-testid="stLogo"] {
            height: 5.5rem;
}</style>""", unsafe_allow_html=True)
# --- RUN NAVIGATION ---
pg.run()
