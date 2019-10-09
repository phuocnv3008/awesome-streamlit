"""Page for viewing the awesome Streamlit vision"""
import pathlib

import streamlit as st


def write():
    """Method used to write the page in the app.py file"""
    url = pathlib.Path(__file__).parent.parent.parent / "AWESOME-STREAMLIT.md"
    with open(url, mode="r") as file:
        readme_md_contents = "".join(file.readlines())
    readme_md_contents = readme_md_contents.split("\n", 3)[-1]
    readme_md_contents = "# The Vision\n" + readme_md_contents
    st.markdown(readme_md_contents)
