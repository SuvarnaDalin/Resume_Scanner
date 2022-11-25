# -*- coding: utf-8 -*-
"""
Created on Thurs Jul 29 17:00:05 2022

@author: suvarna
# -*- coding: utf-8 -*-
"""
import warnings
warnings.filterwarnings('ignore')

from resume_parser import resumeparse
import os
import sys


res_DIR = 'D:/WORK/2022/8_Sept2022/Resume_Scanner_Py/Resumes'
res_LIST = os.listdir(res_DIR)
res_responses = []
for res in range(0, len(res_LIST)):
    data = resumeparse.read_file(os.path.join(res_DIR, res_LIST[res]))
    #'Python' and 'Flask' in 
    for sk in range(0, len(data['skills'])):
        data['skills'][sk] = data['skills'][sk].replace(' ','')
        data['skills'][sk] = data['skills'][sk].lower()
    res_responses.append(data)
search_string = ['python', 'flask', 'javascript', 'html', 'django', 'dataanalytic', 'c++', 'c#', 'datascience' ]
for res in range(0, len(res_LIST)):
    matches = []
    for orgstr in range(0, len(res_responses[res]['skills'])):
        for substr in range(0, len(search_string)):
            try:
                res_responses[res]['skills'][orgstr].index(search_string[substr])
                if(search_string[substr] not in matches):
                    matches.append(search_string[substr])
            except:
                continue
    if(len(matches) >=4):
        print(res_LIST[res], matches, file=sys.stdout)
        #sys.stdout.write(res_LIST[res], matches)