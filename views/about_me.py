import streamlit as st
from streamlit_extras.switch_page_button import switch_page



# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/pngwing.com.png", width=250)
with col2:
    st.markdown("<h1 >Meet <span style='color: #FFC444;'>Meisan</span></h1>", unsafe_allow_html=True)

    st.write(
        "Hi, I’m Meisan, the chatbot for Yangon Technological University (YTU). I was developed by 5th-year EC students. Explore Yangon Technological University (YTU) like never before with me!"
    )

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n\n")

# Define custom card style
card_html = """
<div style="display: flex; gap: 2rem; flex-wrap: wrap; justify-content: center; align-item: center;">
<div style="
    width: 210px;
    background-color: #ffffff;  
    padding: 40px;
    border-radius: 10px;
    box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.2);
    text-align: center;
">
<?xml version="1.0" encoding="UTF-8"?>
<svg id="Layer_1" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" width="60" viewBox="0 0 19.91 19.9">
  <defs>
    <style>
      .cls-1 {
        fill: #343434;
      }
    </style>
  </defs>
  <path class="cls-1" d="M19.91,5.19v.97c-.16,1.54-.91,2.92-2.09,3.91v2.32c-.13.36-.43.38-.71.16-.22-.18-1.32-1.39-1.42-1.41-2.18.43-4.53.25-6.23-1.31-2.5-2.32-2.41-6.27.18-8.48C11.07.13,12.8-.08,14.62.03c2.74.16,5.08,2.42,5.3,5.16ZM17.04,11.32v-1.57c0-.12.51-.48.62-.59,3.05-3.07,1.07-8.13-3.24-8.36-1.56-.08-2.95.09-4.19,1.09-2.82,2.26-2.2,6.77,1.09,8.22,1.09.48,2.58.52,3.75.35.25-.04.63-.19.85-.14.31.07.82.82,1.11,1Z"/>
  <path class="cls-1" d="M6.84,19.9c-.64-.5-1.16-1.16-1.77-1.7-1.26-.11-2.71.29-3.81-.46-.69-.47-1.15-1.25-1.21-2.09-.13-2.07.11-4.28,0-6.37.12-1.33,1.2-2.42,2.54-2.5s2.84.05,4.21.02c.39.13.35.69-.06.76-1.32.08-2.77-.1-4.07,0-1,.08-1.76.85-1.84,1.84-.16,1.98.12,4.17,0,6.18.31,2.46,2.83,1.72,4.58,1.86l.15.08,1.01,1.03v-.83c0-.1.21-.29.33-.29,1.41-.1,2.99.13,4.38,0,2.4-.22,1.71-3.03,1.81-4.67.09-.46.72-.44.77.04-.13,1.71.5,3.61-1.03,4.83-.29.23-.99.58-1.36.58h-4.13v1.42c0,.1-.19.24-.27.29h-.23Z"/>
  <path class="cls-1" d="M2.44,12.07h8.3c.49.05.5.71,0,.77H2.51c-.46-.06-.5-.64-.07-.77Z"/>
  <path class="cls-1" d="M2.44,14.24l6.91.02c.3.17.3.55,0,.72l-6.84.03c-.46-.06-.5-.64-.07-.77Z"/>
  <path class="cls-1" d="M2.44,9.9h5.77c.49.05.5.71,0,.77H2.51c-.46-.06-.5-.64-.07-.77Z"/>
  <path class="cls-1" d="M10.63,14.24c.55-.11.64.71.14.77s-.6-.68-.14-.77Z"/>
  <path class="cls-1" d="M14.29,5.97s.03.85-.03,1.04c-.12.38-.68.33-.75-.02-.03-.19-.03-.96,0-1.16.09-.75,1.13-.45,1.24-1.32.13-1.02-1.34-1.36-1.67-.43-.07.2-.02.61-.3.67-.67.16-.57-.59-.41-.99.39-.98,1.59-1.31,2.45-.72,1.16.79.83,2.63-.54,2.93Z"/>
  <path class="cls-1" d="M13.6,8.15c.34-.35.92.14.59.53s-.94-.17-.59-.53Z"/>
</svg>
    <p style="margin: 20px 0 0; font-weight: 600; font-size: 16px; line-height: 1.25;"> 
        Frequently Asked Questions
    </p>
</div>

<div style="
    background-color: #ffffff;  
    width: 210px;
    padding: 40px;
    border-radius: 10px;
    box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.2);
    text-align: center;
">
   <?xml version="1.0" encoding="UTF-8"?>
<svg id="Layer_1" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" width="60" viewBox="0 0 359.56 356.58">
  <defs>
    <style>
      .cls-1 {
        fill: #343434;
      }
    </style>
  </defs>
  <path class="cls-1" d="M335.48,125.88h19.84c1.71,0,4.83,4.29,4.15,6.33l-.6,188.1-2.62,2.62-47.72.56c1.77,19.47-14.47,35.15-33.97,32.86-17.3-2.03-28.64-23.64-42.02-32.84l-227.49-.06c-3.19-.5-5.08-3.13-4.95-6.28V84.31c-.68-2.04,2.44-6.33,4.15-6.33h19.84v-31.81c0-.88,3.24-4.12,4.12-4.12h37.8V4.25c0-1.71,4.29-4.83,6.33-4.15l168.41.08c2.22.35,6.63,4.57,8.66,6.31,13.26,11.34,25.5,23.99,38.93,35.18,13.01,2.13,29.65-1.53,42.23.43,1.68.26,4.91,2.51,4.91,4.07v79.72ZM233.67,12.11H77.98v65.87h37.8c.75,0,2.68,1.95,3.26,2.73,2.42,3.26,10.68,23.6,12.57,24.14,5.77-1.09,11.96-2.58,17.82-2.95,39.28-2.42,81.02,1.89,120.56.01,8.78,1.02,5.51,11.99,1.48,11.99h-66.99l16.84,11.98h72.23v-59.88h-55.77c-.88,0-4.12-3.24-4.12-4.12V12.11ZM283.08,54.02l-37.43-33.68v33.68h37.43ZM66,54.02h-29.94v23.95h29.94v-23.95ZM323.5,54.02h-20.96c.34,1.1,2.99,3.21,2.99,4.12v67.74h17.96V54.02ZM220.95,311.52l-17.58-17.76c-49.89,26.78-113.09,6.48-138.4-43.71-27.44-54.4-1.91-119.08,53.87-141.37l-9.04-18.73H12.11v221.57h208.84ZM149.69,114.13c-69.62,4.81-107.38,84.16-67.08,141.49,37.79,53.75,119.93,49.24,151.66-8.25,34.36-62.24-13.88-138.13-84.59-133.24ZM347.45,137.86h-113.78c26.68,31.69,31.55,77,12.33,113.79,17.36,18.83,38.07,35.99,55.06,54.99,1.25,1.4,2.63,2.97,2.98,4.88h43.42v-173.66ZM239.29,262.13c-6.95,9.72-15.35,18.11-25.06,25.06l53.93,53.85c16.6,10.65,35.97-7.4,25.28-24.53l-54.14-54.38Z"/>
  <rect class="cls-1" x="149.84" y="77.98" width="125.75" height="11.98"/>
  <rect class="cls-1" x="131.87" y="54.02" width="77.85" height="11.98"/>
  <rect class="cls-1" x="143.85" y="30.07" width="65.87" height="11.98"/>
  <rect class="cls-1" x="95.94" y="30.07" width="29.94" height="11.98"/>
  <path class="cls-1" d="M148.19,126.11c66.44-5.92,109.82,68.01,71.12,122.77-29.63,41.93-91.93,43.9-124.1,3.86-38.68-48.15-8.38-121.16,52.98-126.63ZM151.18,138.08c-50.33,3.84-77.74,59.66-50.17,102.12,25.67,39.53,85.7,38.64,110.52-1.35,28.31-45.61-6.81-104.86-60.35-100.77Z"/>
</svg>
   <p style="margin: 20px 0 0; font-weight: 600; font-size: 16px; line-height: 1.25;"> 
        Student Affair Inquiries
    </p>
</div>

<div style="
    background-color: #ffffff;  
    width: 210px;
    padding: 40px;
    border-radius: 10px;
    box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.2);
    text-align: center;
">
   <?xml version="1.0" encoding="UTF-8"?>
<svg id="Layer_1" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" width="60" viewBox="0 0 368.62 371.74">
  <defs>
    <style>
      .cls-1 {
        fill: #343434;
      }
    </style>
  </defs>
  <path class="cls-1" d="M258.29,32.99h15.35c6.16,0,15.23,9.7,15.35,16.09l.1,158.59,1.12,1.12c7.29-.22,15.76-.53,18.41,7.79.66,2.05.33,5.9.67,6.44.24.38,7.47,3.15,8.32,3.36,3.26.8,3.31-2.09,6.02-3.42,3.47-1.7,7.3-1.51,10.78.02,3.67,1.61,18.6,16.64,20.06,20.36,2.59,6.6-.3,10.07-3.96,15.19l3.7,9.41c5.47-.74,12.43,2.57,13.8,8.28.82,3.41.83,24.46-.03,27.77-1.41,5.38-8.47,8.7-13.74,8.34l-3.77,8.66c-.34,2.34,2.73,3.47,3.8,5.65,1.79,3.65,1.58,8.26-.56,11.73-1.33,2.16-14.36,15.02-16.8,16.89-3.41,2.63-7.15,3.42-11.46,2.44-2.67-.6-5.26-4.53-7.45-4.23l-8.46,3.6c-.04,7.22-3.5,13.4-11.19,14.26-5.16.58-16.51.52-21.74.03-8.82-.83-10.86-6.93-12.31-14.64l-8.66-3.32c-13.08,11.58-19.68-.62-29.17-8.25H47.57c-6.55.04-16.84-9-16.84-15.36v-17.59h-15.35c-6.35,0-15.8-10.1-15.38-16.81V16.86C.57,9.03,6.34,2.81,13.66.56L240.73.02c7.28-.51,17.56,9.25,17.56,16.13v16.84ZM246.31,32.99v-14.6c0-2.01-2.94-5.71-5.22-6.01l-225.01.34-3.73,3.76v279.28c.44,1.68,3.77,4.45,5.28,4.45h13.1V48.33c0-5.65,9.69-15.35,15.35-15.35h200.23ZM205.89,302.83c-.71-4.25.52-10.14,0-14.6l-129.54-.34c-5.57-2.32-4.81-10.66,1.21-11.6h128.58c2.75-6.09,7.38-8.54,14.01-8.62l3.7-9.04-4.94-8.63-142.32-.52c-5.68-2.77-5.2-9.98.89-11.45h145.21c9.67-4.07,14.15-19.88,26.79-15.48,2.97,1.03,3.53,3.21,6.16,4.27l9.28-3.83c-.66-7.79,4.36-13.76,12.1-14.55l-1.21-160.45c-1.39-2.29-4.1-3.01-6.65-3.08l-220.67.21c-4.1.74-5.74,3.7-5.82,7.65l.38,275.14c1.01,3.2,3.4,4.84,6.74,5.24h169.57c-2.4-4.22,4.45-10.07,4.47-11.6.02-1.03-3.46-9-4.22-9.26-5.56.21-12.76-3.64-13.73-9.47ZM297.21,220.87h-20.21c-.23,4.55,1.49,10.28-3.73,12.36-11,1.53-18.76,13.75-27.43,1.17-1.39-.25-12.78,11.97-13.61,14.55,2.12,2.65,5.55,4.44,5.77,8.25-3.71,5.29-5.22,15.26-8.25,20.09-2.57,4.11-7.84,2.41-11.88,2.72v20.21c4.79.34,9.98-1.72,12.56,3.54-.12,5.24,7.65,15.37,7.57,19.31-.06,3.28-4.6,6.7-6.64,8.97l13.83,13.83c2.27-2.05,5.68-6.58,8.97-6.64,3.88-.08,14.68,7.61,19.79,7.84,4.74,2.77,2.67,7.67,3.05,12.29h20.21c.22-4.11-1.3-9.74,3.05-12.3,1.96-1.15,4.74-1.17,6.89-2.09,9.6-4.09,13.72-10.02,21.87.9l13.79-14.48c-12.46-8.54-.52-16.53,1.17-27.43l3.16-3.58,9.2-.16v-20.21c-4.55-.23-10.28,1.49-12.36-3.73-1.68-11.04-13.77-19.22-1.17-28.18l-13.15-13.69c-1.42-.25-4.63,4.62-6.45,5.37-5.17,2.13-10.16-2.28-14.8-4.28-8.92-3.85-12.6-1.22-11.21-14.61Z"/>
  <path class="cls-1" d="M88.21,81.1c12.35-1.56,41.03-1.35,53.67-.2,7.52.68,14,4.71,16.34,12.1-.7,20.49,2.69,45.22.52,65.36-.87,8.08-6.73,13.34-14.6,14.59-18.12-1.22-38.31,1.62-56.17.03-8.15-.73-14.1-6.64-15.32-14.62,1.65-19.87-2.24-43.37.09-62.8.97-8.1,7.66-13.48,15.47-14.47ZM87.39,93.76c-2.3,1.1-2.6,3.16-2.8,5.43-1.26,13.93-1.27,42.29,0,56.21.39,4.31,1.37,5.23,5.61,5.61,12.62,1.15,38.35,1.15,50.97,0,4.31-.39,5.23-1.37,5.61-5.61,1.67-18.32-1.35-39.12,0-57.71l-2.3-3.69-57.1-.25Z"/>
  <path class="cls-1" d="M74.39,200.9c1.2-1.1,3.69-1.76,5.34-1.78l172.62.37c6.07,2.55,5.89,10.85-1.15,11.66l-173.72.02c-4.7-.54-6.54-7.12-3.09-10.28Z"/>
  <path class="cls-1" d="M180.24,84.06l72.39-.13c8.73,3.23,7.17,11.73-2.21,12.67-21.45,2.15-46.29-1.58-68.11.01-8.06-.45-10.4-10.12-2.07-12.55Z"/>
  <path class="cls-1" d="M178.72,122.97l73.97-.17c8.14.95,6.92,11.11-.75,12.01-22.3-1.87-48.55,2.44-70.38-.02-7.39-.83-8.93-8-2.84-11.82Z"/>
  <path class="cls-1" d="M255.06,162.72c3.39,3.71,1.18,9.74-3.85,10.28-22.24-1.96-48.68,2.5-70.41-.02-7.72-.89-7.49-11.25,0-12.01,22.36,1.64,47.67-2.12,69.68-.03,1.63.15,3.42.51,4.58,1.78Z"/>
  <path class="cls-1" d="M281.31,254c54.32-6.87,61.85,73.92,10.2,79.06-52.41,5.21-59.46-72.84-10.2-79.06ZM283.56,265.98c-34.77,4.72-29.45,57.13,5.03,55.19,37.57-2.11,32.21-60.24-5.03-55.19Z"/>
</svg>
   <p style="margin: 20px 0 0; font-weight: 600; font-size: 16px; line-height: 1.25;"> 
        Commands & Instructions
    </p>
</div>

</div>
"""

st.markdown("<br />", unsafe_allow_html=True)
# Display the card using Markdown
st.markdown(card_html, unsafe_allow_html=True)


st.markdown("<br /> <br />", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col2:
    st.image("./assets/Artboard 35.png")
with col1:
  st.subheader("Frequently Asked Questions")
  st.write("""
  Curious about Yangon Technological University? Here are some common questions to ask.
  - What are the majors in YTU?
  - Tell me more about internship.
  - Who is the rector of YTU?
  """)
  # Inject custom CSS for hover effect
  st.markdown("""
  <style>
      .yellow1 {
          background-color: #FFC107; 
          padding: 10px 20px; 
          border-radius: 5px; 
          font-size: 16px; 
          font-weight: 600;
          display: inline-block;
          transition: background-color 0.3s ease;
          text-decoration: none !important; 
          color: white !important; 
      }
      .yellow1:hover {
      text-decoration: none; 
      color: white; 
          background-color: #FFA000;
      }
  </style>
  """, unsafe_allow_html=True)

  # Create the clickable button with the class "yellow1"
  st.markdown("""
    <a href="/chatbot" target="_self" class="yellow1">
        Chat now
    </a>
  """, unsafe_allow_html=True)


col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/Artboard 35.png")
with col2:
  st.subheader("Student Affair Inquiries")
  st.write("""
  Have questions about student life at YTU? Find answers to important topics like admission procedures, and campus accommodations.
  - How can I enroll?
  - How to apply for hostel?
  - How to suspend uni?
  """)
  st.markdown("""
    <a href="/chatbot" target="_self" class="yellow1">
        Chat now
    </a>
  """, unsafe_allow_html=True)


col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col2:
    st.image("./assets/Artboard 35.png")
with col1:
  st.subheader("Commands & Instructions")
  st.write("""
  Meisan is also trained to express emotions and follow movements. It can smile, show sadness, come closer, or spin around on command.
  - Come closer
  - Spin around
  - Make smiley face
  """)
  st.markdown("""
    <a href="/chatbot" target="_self" class="yellow1">
        Chat now
    </a>
  """, unsafe_allow_html=True)

  footer = """
<style>
.footer {
    width: 100%;
    background-color: #f8f9fa;
    color: #6c757d;
    text-align: center;
    padding: 40px;
    font-size: 14px;
    border-top: 1px solid #e9ecef;
}
</style>

<div class="footer">
    <p>Developed by 2024–2025 5th Year Electronics Students (Min Thant Kyaw, Hein Htet Zaw, Si Thu Lin Htet, Aung Kaung Set, Min Bala) as for our integrated design project.</p>
</div>
"""

st.markdown(footer, unsafe_allow_html=True)