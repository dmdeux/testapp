import streamlit as st
#emoticonos en https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Testing", page_icon=":saluting_face:", layout="wide")
with st.container():
   st.subheader("¡Hi, my name is Darío Martínez Martínez!")
   st.title("Student at CFIS-UPC")
   st.write("This is a test, meanwhile, here you have a [nice song](https://youtu.be/wM4XDbkFvhk?si=9oZM3q9hj5ynefmd)")

  with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
      st.header("What I do")
      st.write("##")
      st.write(
          """
          To be honest, I still do not have any project, for the moment, making this web app is the first one. I mean, I am fine with my degree, and I do not usually have much spare time to spend in side projects. I am currently in the third year (out of five) of a double degree in Mathematics and Engineering Physics, I benefit from a scholarship from the CFIS programme at Universitat Politècnica de Catalunya.
          I would define myself as a curious guy, who enjoys science and maths.
          """
      )
