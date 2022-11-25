# -*- coding: utf-8 -*-
"""
Created on Thurs Jul 29 17:00:05 2022

@author: suvarna
# -*- coding: utf-8 -*-
"""

import streamlit as st
from resume_parser import resumeparse
import os
import sys
import pdfplumber

st.title('VISULON RESUME SCANNER APP')
st.sidebar.markdown("**Upload the Resumes**")
uploaded_files = st.sidebar.file_uploader("--------------------------------------------------------------------",
                                         type=["pdf","docx","txt"],
                                         accept_multiple_files = True)
if uploaded_files is not None:
    res_responses = []
    for res in range(0, len(uploaded_files)):
        #data = resumeparse.read_file(uploaded_files[res])
        #st.write(data)
        data = uploaded_files[res]
        st.write(data.type)

        if data.type == "application/pdf":
            with pdfplumber.open(data) as pdf:
                pages = pdf.pages[0]
                #st.write(pages.extract_text())
        import base64
        #with open(uploaded_files[res], "rb") as f:
        #base64_pdf = base64.b64encode(uploaded_files[res].read()).decode('utf-8')
        #st.write(uploaded_files[res].read())
        new_data = resumeparse.read_file(uploaded_files[res].read())
        # st.write(new_data)
    #     file_details = {"filename":data.name}
    #     st.write(file_details)
    #     for sk in range(0, len(data['skills'])):
    #         data['skills'][sk] = data['skills'][sk].replace(' ','')
    #         data['skills'][sk] = data['skills'][sk].lower()
    #     res_responses.append(data)
    # search_string = ['python', 'flask', 'javascript', 'html', 'django', 'dataanalytic', 'c++', 'c#', 'datascience' ]
    # for res in range(0, len(uploaded_files)):
    #     matches = []
    #     for orgstr in range(0, len(res_responses[res]['skills'])):
    #         for substr in range(0, len(search_string)):
    #             try:
    #                 res_responses[res]['skills'][orgstr].index(search_string[substr])
    #                 if(search_string[substr] not in matches):
    #                     matches.append(search_string[substr])
    #             except:
    #                 continue
    #     if(len(matches) >=4):
    #         st.write(uploaded_files[res], matches)