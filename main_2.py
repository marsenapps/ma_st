### https://www.youtube.com/watch?v=Ll-PBGeMZ6I&list=PLjyA8VTW-RcVI7deAqL0OXuIIptjMwlVL&index=2

import streamlit as st
import pandas as pd

import streamlit.components.v1 as components

components.html("<html><body><div style=\"background-color:tomato;padding:10px\"><h1 style=\"color:white;text-align:center;\"> Welcome to MSTECH</h1></div></body></html>")


html_temp="""
<div style="background-color:tomato; padding:10px">
<h2 style="color:white;text-align:center;">Very Excited to learn streamlit...</h2
<div>
"""
st.write("Forward step...")

## Part#2: Creating dataset and viz
df=pd.DataFrame({'First':['None',1,2,3,4,5],
	'Second':[6,7,8,9,10,11],
	'Third':[12,13,14,15,16,17]})
#>st.sidebar.write(df)
##or
#>df ## magic command
## Visualization###
#>st.line_chart(df)

### sidebar###
st.sidebar.write(df)
st.sidebar.line_chart(df)

### PART#1: Streamlit Tutorial For Beginners - #part1 Visualization, SideBar, CheckBox, SelectBox
#################################################################################################
if st.checkbox("Show the table..."):
	df

### SELECTBOX##
opt=st.selectbox("Which Num you want to select: ",df['First'])
if opt=='None':
	st.write("Nothing select.. Plz select a value: ",opt)
else:
	st.write("You just selected: ",opt)

### Streamlit Tutorial For beginners - #Part2 Slider, ProgressBar, Beta Columns, Beta Expander
##############################################################################################


	## 2. Progress Bar
	import time
	pro=st.progress(0)
	for i in range(50):
		pro.progress(i+1)
		time.sleep(0.1)

	## 4. Beta Expander
#expander=st.beta_expander("Hello")
expander=st.expander("Hello")
expander.write("How are you?")


### Streamlit Tutorial for Beginners - #part3 Spinner Widget, types of messages & Component widget
###################################################################################################

