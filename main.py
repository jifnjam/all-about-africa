import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, Response, make_response
from PIL import Image

# for pythonanywhere
from pathlib import Path
THIS_FOLDER = Path(__file__).parent.resolve()
my_file_na = THIS_FOLDER / "/home/tobim/all-about-africa/northafrica.csv"
my_file_wa = THIS_FOLDER / "/home/tobim/all-about-africa/westafrica.csv"
my_file_sa = THIS_FOLDER / "/home/tobim/all-about-africa/southafrica.csv"
my_file_ca = THIS_FOLDER / "/home/tobim/all-about-africa/centralafrica.csv" 
my_file_ea = THIS_FOLDER / "/home/tobim/all-about-africa/eastafrica.csv"


# the code is too long. this results in internal sever errors after central africa

app = Flask(__name__)

def turn_to_text(choice): #for multi word country names
     choice = str(choice)
     choice = choice.replace("-", " ")
     choice = choice.title()

     if "Of" or "And" or "The" in choice:
          choice = choice.replace("Of", "of")
          choice = choice.replace("And", "and")
          choice = choice.replace("The", "the")     

     return choice

def turn_to_html(choice):
     choice = str(choice)
     spread = choice.lower()
     spread = spread.split()
     spread = "-".join(spread)
     return spread

def pic_finder(reg, country):
     if " " in country:
          country = country.replace(" ", "")
     
     my_pic = "static/" + "img/" + "Flag Pictures/" + reg + "/Flag_of_" + country + ".png"
     
     return my_pic

@app.route('/')
def home():
     return render_template('index.html')

@app.route('/<region>/')
def regions(region):

     na_df = pd.read_csv(my_file_na) # deployment
     na_ctrydf = na_df['Country'].str.lower()

     wa_df = pd.read_csv(my_file_wa) # deployment
     wa_ctrydf = wa_df['Country'].str.lower()

     sa_df = pd.read_csv(my_file_sa) # deployment
     sa_ctrydf = sa_df['Country'].str.lower()

     ca_df = pd.read_csv(my_file_ca) # deployment
     ca_ctrydf = ca_df['Country'].str.lower()

     ea_df = pd.read_csv(my_file_ea) # deployment
     ea_ctrydf = ea_df['Country'].str.lower()

     #change <country> into blank-blank-blank wording
     if region == 'northafrica':
          return render_template('regionpage.html', title="North Africa", title_lower=region, data=na_ctrydf) 
     elif region == 'eastafrica':
          return render_template('regionpage.html', title="East Africa", title_lower=region, data=ea_ctrydf)
     elif region == 'westafrica':
          return render_template('regionpage.html', title="West Africa", title_lower=region, data=wa_ctrydf)
     elif region == 'centralafrica':
          return render_template('regionpage.html', title="Central Africa", title_lower=region, data=ca_ctrydf)
     elif region == 'southafrica': 
          return render_template('regionpage.html', title="South Africa", title_lower=region, data=sa_ctrydf) 
     
#changed 1 2 3 4 5 6

@app.route('/<region>/<country>/')
def countries(region, country):

     region = str(region)
     country = str(country)


     if region == "northafrica":
          df = pd.read_csv(my_file_na)
          df = df.dropna(axis='columns')
          
          
     elif region == "westafrica":
          df = pd.read_csv(my_file_wa)
          df = df.dropna(axis='columns')

     
     elif region == "centralafrica":
          df = pd.read_csv(my_file_ca)
          df = df.dropna(axis='columns')

     
     elif region == "eastafrica":
          df = pd.read_csv(my_file_ea)
          df = df.dropna(axis='columns')

     
     elif region == "southafrica":
          df = pd.read_csv(my_file_sa)
          df = df.dropna(axis='columns')


     df = df.set_index('Country')
     df = df.astype('string')
     
     pic_ctry = country
     
     country = turn_to_text(country) 
     selection = df.loc[country]


     capital = selection['Capital']
     pres_leader = selection['President/Leader']
     language = selection['Language']
     tribes_ethn = selection['Tribes/Ethnic Groups']
     religion = selection['Religion']

     if "l" in region:
          region = region.replace("l", "l ")
          pic_path = pic_finder(region, pic_ctry)
     elif "t" in region:
          region = region.replace("t", "t ")
          pic_path = pic_finder(region, pic_ctry)
     elif "h" in region:
          region = region.replace("h", "h ")
          pic_path = pic_finder(region, pic_ctry)

     return render_template('countrypage.html', ctry=country, cap=capital,
                              pres=pres_leader, lang=language, tribes=tribes_ethn,
                              relg = religion, pic_name=pic_path)     
     
if __name__ == "__main__":
     app.run(debug=True) 