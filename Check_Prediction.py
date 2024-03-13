from tkinter import *
def Train():
    """GUI"""
from tkinter import *
from tkinter import ttk 
import tkinter as tk
import numpy as np
import pandas as pd

from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder

root = tk.Tk()

root.geometry("800x850+250+5")
root.title("Crop Yield Prediction")
root.configure(background="crimson")

State = tk.StringVar()
Year = tk.IntVar()
Season = tk.StringVar()
Crop = tk.StringVar()
Area = tk.IntVar()
Production = tk.IntVar()
Rainfall = tk.IntVar()
avg_temp = tk.IntVar()
PH_Value_of_Soil = tk.IntVar()
Type_of_soil= tk.StringVar()
#Suitable_Fertilizer = tk.IntVar()

    
    #===================================================================================================================
def Detect():
    e1=State.get()
    print(e1)
    if e1=="Andaman and Nicobar Islands":
        e1=0
    elif e1=="Arunachal Pradesh":
        e1=1
    else :
        e1=2
    e2=Year.get()
    print(e2)
   
    e3=Season.get()
    print(e3)
    if e3=="Autumn":
        e3=0
    elif e3=="Kharif":
        e3=1
    elif e3=="Rabi":
        e3=2
    elif e3=="Whole Year":
        e3=3
    else :
        e3=4
    
    e4=Crop.get()
    print(e4)
    if e4=="Banana":
       e4=0
    elif e4=="Cashewnut":
        e4=1
    elif e4=="Coconut":
        e4=2
    elif e4=="Coriander":
        e4=3
    elif e4=="Dry chillies":
        e4=4
    elif e4=="Dry ginger":
        e4=5
    elif e4=="Garlic":
        e4=6
    elif e4=="Onion":
        e4=7
    elif e4=="Potato":
        e4=8
    elif e4=="Rice":
        e4=9
    elif e4=="Sugarcane":
        e4=10
    elif e4=="Turmeric":
        e4=11
    else :
        e4=12
    e5=Area.get()
    print(e5)
    e6=Production.get()
    print(e6)
    e7=Rainfall.get()
    print(e7)
    e8=avg_temp.get()
    print(e8)
    e9=PH_Value_of_Soil.get()
    print(e9)
    e10=Type_of_soil.get()
    print(e10)
    if e10=="Clayey soil":
       e10=0
    elif e10=="Loamy soil":
        e10=1
    else :
        e10=2
    #e11= Suitable_Fertilizer.get()
    #print(e11)
    
     
        
        
#########################################################################################
    from joblib import dump , load
    a1=load('F:/Crop_Yield_Prediction/Crop_Yield_Prediction/CROP/crop_Model.joblib')
    v= a1.predict([[e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]])
    print(v)
    yes = tk.Label(root,text="Detect Crop Yeild:"  +'\n'+ str(v),background="blue",foreground="white",font=('times', 20, ' bold '),width=30)
    yes.place(x=800,y=650)
   
 # if v[0]==1:
 #     print("Yes")
 #     yes = tk.Label(root,text="Crop Yield Prediction \nReport is Generated",background="red",foreground="white",font=('times', 20, ' bold '),width=15)
 #     yes.place(x=300,y=100)
 #     file = open(r"D://100% project//21cg148-softwere defect//21cg148-softwere defect//Report.txt", 'w')
 #     file.write("-----Softwere Report-----\n As per input data and system model softwere defect prediction for Respective Paptien softwere."
 #                "\n***Kindly Follow info***"
             
 #             )
 #     file.close()
     
 # else:
 #     print("No")
 #     no = tk.Label(root, text="No softwere defect \nDetected", background="green", foreground="white",font=('times', 20, ' bold '),width=15)
 #     no.place(x=300, y=100)
 #     file = open(r"D://100% project//21cg148-softwere defect//21cg148-softwere defect//Report.txt", 'w')
 #     file.write("-----Softwere Report-----\n As per input data and system model No Softwere defect Detected for Respective softwere."
 #                "\n\n***Relax and Follow below mentioned softwere!!!***"
             
 #             )
 #     file.close()
 
def Detect1():
    e1=State.get()
    print(e1)
    if e1=="Andaman and Nicobar Islands":
        e1=0
    elif e1=="Arunachal Pradesh":
        e1=1
    else :
        e1=2
    e2=Year.get()
    print(e2)
   
    e3=Season.get()
    print(e3)
    if e3=="Autumn":
        e3=0
    elif e3=="Kharif":
        e3=1
    elif e3=="Rabi":
        e3=2
    elif e3=="Whole Year":
        e3=3
    else :
        e3=4
    
    e4=Crop.get()
    print(e4)
    if e4=="Banana":
       e4=0
    elif e4=="Cashewnut":
        e4=1
    elif e4=="Coconut":
        e4=2
    elif e4=="Coriander":
        e4=3
    elif e4=="Dry chillies":
        e4=4
    elif e4=="Dry ginger":
        e4=5
    elif e4=="Garlic":
        e4=6
    elif e4=="Onion":
        e4=7
    elif e4=="Potato":
        e4=8
    elif e4=="Rice":
        e4=9
    elif e4=="Sugarcane":
        e4=10
    elif e4=="Turmeric":
        e4=11
    else :
        e4=12
    e5=Area.get()
    print(e5)
    e6=Production.get()
    print(e6)
    e7=Rainfall.get()
    print(e7)
    e8=avg_temp.get()
    print(e8)
    e9=PH_Value_of_Soil.get()
    print(e9)
    e10=Type_of_soil.get()
    print(e10)
    if e10=="Clayey soil":
       e10=0
    elif e10=="Loamy soil":
        e10=1
    else :
        e10=2
    #e11= Suitable_Fertilizer.get()
    #print(e11)
    
     
        
        
#########################################################################################
    
    from joblib import dump , load
    a2=load('F:/Crop_Yield_Prediction/Crop_Yield_Prediction/CROP/crop_Model1.joblib')
    v1= a2.predict([[e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]])
    print(v1)
    yes = tk.Label(root,text=" Detect Suitable Fertilizer:"  +'\n'+ str(v1),background="blue",foreground="white",font=('times', 20, ' bold '),width=30)
    yes.place(x=800,y=650)
    
    import requests 
    api_address = "http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
    
    import json
    location_req_url='http://api.ipstack.com/103.51.95.183?access_key=4b0f43bbd8b7a123d8b9d6cde128e6ca'
    r = requests.get(location_req_url)
    location_obj = json.loads(r.text)
    
    lat = location_obj['latitude']
    lon = location_obj['longitude']
    latitude = lat
    longitude = lon
    
    
    location2 = "%s, %s" % (location_obj['city'], location_obj['region_code'])
    location2 = location2.replace(',','')
    print(location2.split()[0])
    city =location2.split()[0] 
    
    location_label = tk.Label(root,text="At location  "+str(location2),font=('Times New Roman',35,'italic'),bg="cyan3",fg="white")
    location_label.place(x=850,y=580)

              
def call_file():
            import location
            location.Train()
 
l1=tk.Label(root,text="State",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
l1.place(x=5,y=1)

monthchoosen = ttk.Combobox(root, width =15,font=20,textvariable =State)
    
    # Adding combobox drop down list
monthchoosen['values'] = ('Andaman and Nicobar Islands',
    					'Arunachal Pradesh',
    					'Bihar')
monthchoosen.place(x=500,y=1)
monthchoosen.current()


l2=tk.Label(root,text="Year",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
l2.place(x=5,y=50)
monthchoosen = ttk.Combobox(root, width =15,font=20,textvariable =Year)
    
    # Adding combobox drop down list
monthchoosen['values'] = ('2000',
    					'2001',
                        '2002',
                        '2003',
                        '2004',
                        '2005',
                        '2006',
                        '2007')
monthchoosen.place(x=500,y=50)
monthchoosen.current()

l3=tk.Label(root,text="Season",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
l3.place(x=5,y=100)
monthchoosen = ttk.Combobox(root, width =15,font=20,textvariable =Season)
    
    # Adding combobox drop down list
monthchoosen['values'] = ('Autumn',
    					'Kharif',
    					'Rabi',
                        'Whole Year',
                            'Winter')
monthchoosen.place(x=500,y=100)
monthchoosen.current()

l4=tk.Label(root,text="Crop",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
l4.place(x=5,y=150)
monthchoosen = ttk.Combobox(root, width =15,font=20,textvariable =Crop)
    
    # Adding combobox drop down list
monthchoosen['values'] = ('Banana',
    					'Cashewnut',
    					'Coconut',
                        'Coriander',
                        'Dry chillies',
                        'Dry ginger',
                        'Garlic',
                        'Onion'
                        'Potato',
                        'Rice',
                        'Sugarcane',
                        'Turmeric',
                        'Wheat')
monthchoosen.place(x=500,y=150)
monthchoosen.current()

l5=tk.Label(root,text="Area",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
l5.place(x=5,y=200)
Area=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Area)
Area.place(x=500,y=200)



l6=tk.Label(root,text="Production",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
l6.place(x=5,y=250)
Production=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Production)
Production.place(x=500,y=250)

l7=tk.Label(root,text="Rainfall",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
l7.place(x=5,y=300)
Rainfall=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Rainfall)
Rainfall.place(x=500,y=300)

l8=tk.Label(root,text="avg_temp",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
l8.place(x=5,y=350)
avg_temp=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=avg_temp)
avg_temp.place(x=500,y=350)

l9=tk.Label(root,text="PH_Value_of_Soil",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
l9.place(x=5,y=400)
PH_Value_of_Soil=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=PH_Value_of_Soil)
PH_Value_of_Soil.place(x=500,y=400)



 

l10=tk.Label(root,text="Type_of_soil",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
l10.place(x=5,y=450)
monthchoosen = ttk.Combobox(root, width =15,font=20,textvariable =Type_of_soil)
    
    # Adding combobox drop down list
monthchoosen['values'] = ('Clayey soil',
    						'Loamy soil',
    						'Sandy soil')
monthchoosen.place(x=500,y=450)
monthchoosen.current()

# l10=tk.Label(root,text="Suitable_Fertilizer",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
# l10.place(x=5,y=500)


button1 = tk.Button(root,text="Crop Yeild",command=Detect,font=('times', 20, ' bold '),width=10)
button1.place(x=300,y=600)

button1 = tk.Button(root,text="Suitable Fertilizer",command=Detect1,font=('times', 20, ' bold '),width=15)
button1.place(x=500,y=600)


root.mainloop()
            
Train()

        
       
          



    
    
    