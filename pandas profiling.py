#Exploratory Data Analysis with Pandas Profiling

#Installing Pandas Profiling
!pip install https://github.com/pandas-profiling/pandas-profiling/archive/master.zip

#Import function
from pandas_profiling import ProfileReport

#Create report and save it in html
profile = ProfileReport(df_members,title='report of members',html={'style':{'full_width':True}})

#Exporting Report

profile.to_notebook_iframe()
