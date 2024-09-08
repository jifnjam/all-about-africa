import pandas as pd
from flask import Flask, render_template, request, redirect, url_for
from fileinput import filename

# for pythonanywhere
from pathlib import Path
THIS_FOLDER = Path(__file__).parent.resolve()
my_file_na = THIS_FOLDER / "/home/tobim/all-about-africa/northafrica.csv"
my_file_wa = THIS_FOLDER / "/home/tobim/all-about-africa/westafrica.csv"
my_file_sa = THIS_FOLDER / "/home/tobim/all-about-africa/southafrica.csv"
my_file_ca = THIS_FOLDER / "/home/tobim/all-about-africa/centralafrica.csv"
my_file_ea = THIS_FOLDER / "/home/tobim/all-about-africa/eastafrica.csv"


app = Flask(__name__)

def turn_to_text(choice): #for multi word country names
     choice = str(choice)
     choice = choice.replace("-", " ")
     choice = choice.title()
     return choice

def turn_to_html(choice):
     choice = str(choice)
     spread = choice.lower()
     spread = spread.split()
     spread = "-".join(spread)
     return spread

def insert_pic(pic, reg):
     my_path = "/home/tobim/all-about-africa/Flag Pictures/" 
     my_path = my_path + reg + pic
     my_pic = THIS_FOLDER / my_path
     return my_pic

@app.route('/')
def home():
     return render_template('index.html')

@app.route('/<region>/')
def regions(region):
     #na_df = pd.read_csv("northafrica.csv") # production
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
     na_df = pd.read_csv(my_file_na)
     na_df = na_df.dropna(axis='columns')

     wa_df = pd.read_csv(my_file_wa)
     wa_df = wa_df.dropna(axis='columns')

     ea_df = pd.read_csv(my_file_ea)
     ea_df = ea_df.dropna(axis='columns')

     sa_df = pd.read_csv(my_file_sa)
     sa_df = sa_df.dropna(axis='columns')

     ca_df = pd.read_csv(my_file_ca)
     ca_df = ca_df.dropna(axis='columns')

     country = str(country)
     region = str(region)
     
     capital_col = 'Capital'
     lang_col = 'Language'
     pres_col = 'President/Leader' 
     tribes_col = 'Tribes/Ethnic Groups'
     relgion_col = 'Religion'

     if region == 'northafrica': 
          #for loop here
          if country == 'algeria': 
               na_df = na_df.loc[0]
               pics = insert_pic('North Africa', 'Flag_of_Algeria.svg.png')
               return render_template('countrypage.html', ctry=country.capitalize(), 
                                      cap=na_df[capital_col], pres=na_df[pres_col], 
                                      lang=na_df[lang_col], tribes=na_df[tribes_col], 
                                      relg = na_df[relgion_col], htpic = pics)
          elif country == 'egypt':
               na_df = na_df.loc[1]
               return render_template('countrypage.html', ctry=country.capitalize(), 
                                      cap=na_df[capital_col], pres=na_df[pres_col], 
                                      lang=na_df[lang_col], tribes=na_df[tribes_col], 
                                      relg = na_df[relgion_col], pre_file='North Africa',
                                      image_file='Flag_of_Egypt.png')
          elif country == 'libya':
               na_df = na_df.loc[2]
               return render_template('countrypage.html', ctry=country.capitalize(), 
                                      cap=na_df[capital_col], pres=na_df[pres_col], 
                                      lang=na_df[lang_col], tribes=na_df[tribes_col], 
                                      relg = na_df[relgion_col], pre_file='North Africa',
                                      image_file='Flag_of_Libya.png')
          elif country == 'morocco':
               na_df = na_df.loc[3]
               return render_template('countrypage.html', ctry=country.capitalize(), 
                                      cap=na_df[capital_col], pres=na_df[pres_col], 
                                      lang=na_df[lang_col], tribes=na_df[tribes_col], 
                                      relg = na_df[relgion_col],
                                      image_file='Flag_of_Morocco.png')
          elif country == 'sudan':
               na_df = na_df.loc[4]
               return render_template('countrypage.html', ctry=country.capitalize(), 
                                      cap=na_df[capital_col], pres=na_df[pres_col], 
                                      lang=na_df[lang_col], tribes=na_df[tribes_col], 
                                      relg = na_df[relgion_col],
                                      image_file='Flag_of_Sudan.png')
          elif country == 'tunisia':
               na_df = na_df.loc[5]
               return render_template('countrypage.html', ctry=country.capitalize(), 
                                      cap=na_df[capital_col], pres=na_df[pres_col], 
                                      lang=na_df[lang_col], tribes=na_df[tribes_col], 
                                      relg = na_df[relgion_col],
                                      image_file='Flag_of_Tunisia.png')
     elif region == 'centralafrica':
          if country == 'angola':
               ca_df = ca_df.loc[0]
               return render_template('countrypage.html', ctry=country.capitalize(), 
                                      cap=ca_df[capital_col], pres=ca_df[pres_col], 
                                      lang=ca_df[lang_col], tribes=ca_df[tribes_col], 
                                      relg = ca_df[relgion_col],
                                      image_file='Flag_of_Angola.png')
          elif country == 'cameroon':
               ca_df = ca_df.loc[1]
               return render_template('countrypage.html', ctry=country.capitalize(), 
                                      cap=ca_df[capital_col], pres=ca_df[pres_col], 
                                      lang=ca_df[lang_col], tribes=ca_df[tribes_col], 
                                      relg = ca_df[relgion_col],
                                      image_file='Flag_of_Cameroon.png')
          elif country == 'central-african-republic':
               ca_df = ca_df.loc[2]
               return render_template('countrypage.html', ctry=turn_to_text(country), 
                                      cap=ca_df[capital_col], pres=ca_df[pres_col], 
                                      lang=ca_df[lang_col], tribes=ca_df[tribes_col], 
                                      relg = ca_df[relgion_col],
                                      image_file='Flag_of_CentralAfricanRepublic.png') 
          elif country == 'chad':
               ca_df = ca_df.loc[3]
               return render_template('countrypage.html', ctry=country.capitalize(), 
                                      cap=ca_df[capital_col], pres=ca_df[pres_col], 
                                      lang=ca_df[lang_col], tribes=ca_df[tribes_col], 
                                      relg = ca_df[relgion_col],
                                      image_file='Flag_of_Tunisia.png')
          elif country == 'democratic-republic-of-the-congo':
               ca_df = ca_df.loc[4]
               return render_template('countrypage.html', ctry=turn_to_text(country), 
                                      cap=ca_df[capital_col], pres=ca_df[pres_col], 
                                      lang=ca_df[lang_col], tribes=ca_df[tribes_col], 
                                      relg = ca_df[relgion_col],
                                      image_file='Flag_of_DemocraticRepublicoftheCongo.png')
          elif country == 'equatorial-guinea':
               ca_df = ca_df.loc[5]
               return render_template('countrypage.html', ctry=turn_to_text(country), 
                                      cap=ca_df[capital_col], pres=ca_df[pres_col], 
                                      lang=ca_df[lang_col], tribes=ca_df[tribes_col], 
                                      relg = ca_df[relgion_col],
                                      image_file='Flag_of_EquatorialGuinea.png')
          elif country == 'gabon':
               ca_df = ca_df.loc[6]
               return render_template('countrypage.html', ctry=country.capitalize(), 
                                      cap=ca_df[capital_col], pres=ca_df[pres_col], 
                                      lang=ca_df[lang_col], tribes=ca_df[tribes_col], 
                                      relg = ca_df[relgion_col],
                                      image_file='Flag_of_Gabon.png')
          elif country == 'republic-of-the-congo':
               ca_df = ca_df.loc[7]
               return render_template('countrypage.html', ctry=turn_to_text(country), 
                                      cap=ca_df[capital_col], pres=ca_df[pres_col], 
                                      lang=ca_df[lang_col], tribes=ca_df[tribes_col], 
                                      relg = ca_df[relgion_col],
                                      image_file='Flag_of_RepublicoftheCongo.png')
          elif country == 'sao-tome-and-principe':
              ca_df = ca_df.loc[8]
              return render_template('countrypage.html', ctry=turn_to_text(country), 
                                      cap=ca_df[capital_col], pres=ca_df[pres_col], 
                                      lang=ca_df[lang_col], tribes=ca_df[tribes_col], 
                                      relg = ca_df[relgion_col],
                                      image_file='Flag_of_SaoTomeandPrincipe.png')
          elif region == 'westafrica':
               if country == 'benin':
                    wa_df = wa_df.loc[0]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=wa_df[capital_col], pres=wa_df[pres_col], 
                                        lang=wa_df[lang_col], tribes=wa_df[tribes_col], 
                                        relg = wa_df[relgion_col],
                                        image_file='Flag_of_Benin.png')
               elif country == 'burkina-faso':
                    wa_df = wa_df.loc[1]
                    return render_template('countrypage.html', ctry=turn_to_text(country), 
                                        cap=wa_df[capital_col], pres=wa_df[pres_col], 
                                        lang=wa_df[lang_col], tribes=wa_df[tribes_col], 
                                        relg = wa_df[relgion_col],
                                        image_file='Flag_of_BurkinaFaso.png')
               elif country == 'cape-verde':
                    wa_df = wa_df.loc[2]
                    return render_template('countrypage.html', ctry=turn_to_text(country), 
                                        cap=wa_df[capital_col], pres=wa_df[pres_col], 
                                        lang=wa_df[lang_col], tribes=wa_df[tribes_col], 
                                        relg = wa_df[relgion_col],
                                        image_file='Flag_of_CapeVerde.png') 
               elif country == 'gambia':
                    wa_df = wa_df.loc[3]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=wa_df[capital_col], pres=wa_df[pres_col], 
                                        lang=wa_df[lang_col], tribes=wa_df[tribes_col], 
                                        relg = wa_df[relgion_col],
                                        image_file='Flag_of_Gambia.png')
               elif country == 'ghana':
                    wa_df = wa_df.loc[4]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=wa_df[capital_col], pres=wa_df[pres_col], 
                                        lang=wa_df[lang_col], tribes=wa_df[tribes_col], 
                                        relg = wa_df[relgion_col],
                                        image_file='Flag_of_Ghana.png')
               elif country == 'guinea':
                    wa_df = wa_df.loc[5]
                    return render_template('countrypage.html', ctry=turn_to_text(country), 
                                        cap=wa_df[capital_col], pres=wa_df[pres_col], 
                                        lang=wa_df[lang_col], tribes=wa_df[tribes_col], 
                                        relg = wa_df[relgion_col],
                                        image_file='Flag_of_Guinea.png')
               elif country == 'guinea-bissau':
                    wa_df = wa_df.loc[6]
                    return render_template('countrypage.html', ctry=turn_to_text(country), 
                                        cap=wa_df[capital_col], pres=wa_df[pres_col], 
                                        lang=wa_df[lang_col], tribes=wa_df[tribes_col], 
                                        relg = wa_df[relgion_col],
                                        image_file='Flag_of_GuineaBissau.png')
               elif country == 'ivory-coast':
                    wa_df = wa_df.loc[7]
                    return render_template('countrypage.html', ctry=turn_to_text(country), 
                                        cap=wa_df[capital_col], pres=wa_df[pres_col], 
                                        lang=wa_df[lang_col], tribes=wa_df[tribes_col], 
                                        relg = wa_df[relgion_col],
                                        image_file='Flag_of_IvoryCoast.png')
               elif country == 'liberia':
                    wa_df = wa_df.loc[8]
                    return render_template('countrypage.html', ctry=turn_to_text(country), 
                                        cap=na_df[capital_col], pres=na_df[pres_col], 
                                        lang=na_df[lang_col], tribes=na_df[tribes_col], 
                                        relg = na_df[relgion_col],
                                        image_file='Flag_of_Liberia.png')
               elif country == 'mali':
                    wa_df = wa_df.loc[9]
                    return render_template('countrypage.html', ctry=turn_to_text(country), 
                                        cap=wa_df[capital_col], pres=wa_df[pres_col], 
                                        lang=wa_df[lang_col], tribes=wa_df[tribes_col], 
                                        relg = wa_df[relgion_col],
                                        image_file='Flag_of_Mali.png')
               elif country == 'mauritania':
                    wa_df = wa_df.loc[10]
                    return render_template('countrypage.html', ctry=turn_to_text(country), 
                                        cap=wa_df[capital_col], pres=wa_df[pres_col], 
                                        lang=wa_df[lang_col], tribes=wa_df[tribes_col], 
                                        relg = wa_df[relgion_col],
                                        image_file='Flag_of_Mauritania.png')
               elif country == 'niger':
                    wa_df = wa_df.loc[11]
                    return render_template('countrypage.html', ctry=turn_to_text(country), 
                                        cap=wa_df[capital_col], pres=wa_df[pres_col], 
                                        lang=wa_df[lang_col], tribes=wa_df[tribes_col], 
                                        relg = wa_df[relgion_col],
                                        image_file='Flag_of_Niger.png')
               elif country == 'nigeria':
                    wa_df = wa_df.loc[12]
                    return render_template('countrypage.html', ctry=turn_to_text(country), 
                                        cap=wa_df[capital_col], pres=wa_df[pres_col], 
                                        lang=wa_df[lang_col], tribes=wa_df[tribes_col], 
                                        relg = wa_df[relgion_col],
                                        image_file='Flag_of_Nigeria.png')
               elif country == 'senegal':
                    wa_df = wa_df.loc[13]
                    return render_template('countrypage.html', ctry=turn_to_text(country), 
                                        cap=wa_df[capital_col], pres=wa_df[pres_col], 
                                        lang=wa_df[lang_col], tribes=wa_df[tribes_col], 
                                        relg = wa_df[relgion_col],
                                        image_file='Flag_of_Senegal.png')
               elif country == 'sierra-leone':
                    wa_df = wa_df.loc[14]
                    return render_template('countrypage.html', ctry=turn_to_text(country), 
                                        cap=wa_df[capital_col], pres=wa_df[pres_col], 
                                        lang=wa_df[lang_col], tribes=wa_df[tribes_col], 
                                        relg = wa_df[relgion_col],
                                        image_file='Flag_of_SierraLeone.png')
               elif country == 'togo':
                    wa_df = wa_df.loc[15]
                    return render_template('countrypage.html', ctry=turn_to_text(country), 
                                        cap=wa_df[capital_col], pres=wa_df[pres_col], 
                                        lang=wa_df[lang_col], tribes=wa_df[tribes_col], 
                                        relg = wa_df[relgion_col],
                                        image_file='Flag_of_Togo.png')
          elif region == 'eastafrica':
               if country == 'burundi':
                    ea_df = ea_df.loc[0]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=ea_df[capital_col], pres=ea_df[pres_col], 
                                        lang=ea_df[lang_col], tribes=ea_df[tribes_col], 
                                        relg = ea_df[relgion_col],
                                        image_file='Flag_of_Benin.png')
               elif country == 'comoros':
                    ea_df = ea_df.loc[1]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=ea_df[capital_col], pres=ea_df[pres_col], 
                                        lang=ea_df[lang_col], tribes=ea_df[tribes_col], 
                                        relg = ea_df[relgion_col],
                                        image_file='Flag_of_Comoros.png')
               elif country == 'djibouti':
                    ea_df = ea_df.loc[2]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=ea_df[capital_col], pres=ea_df[pres_col], 
                                        lang=ea_df[lang_col], tribes=ea_df[tribes_col], 
                                        relg = ea_df[relgion_col],
                                        image_file='Flag_of_Djibouti.png')
               elif country == 'eritrea':
                    ea_df = ea_df.loc[3]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=ea_df[capital_col], pres=ea_df[pres_col], 
                                        lang=ea_df[lang_col], tribes=ea_df[tribes_col], 
                                        relg = ea_df[relgion_col],
                                        image_file='Flag_of_Eritrea.png')
               elif country == 'ethiopia':
                    ea_df = ea_df.loc[4]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=ea_df[capital_col], pres=ea_df[pres_col], 
                                        lang=ea_df[lang_col], tribes=ea_df[tribes_col], 
                                        relg = ea_df[relgion_col],
                                        image_file='Flag_of_Ethiopia.png')
               elif country == 'kenya':
                    ea_df = ea_df.loc[5]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=ea_df[capital_col], pres=ea_df[pres_col], 
                                        lang=ea_df[lang_col], tribes=ea_df[tribes_col], 
                                        relg = ea_df[relgion_col],
                                        image_file='Flag_of_Kenya.png')
               elif country == 'madagascar':
                    ea_df = ea_df.loc[6]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=ea_df[capital_col], pres=ea_df[pres_col], 
                                        lang=ea_df[lang_col], tribes=ea_df[tribes_col], 
                                        relg = ea_df[relgion_col],
                                        image_file='Flag_of_Madagascar.png')
               elif country == 'malawi':
                    ea_df = ea_df.loc[7]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=ea_df[capital_col], pres=ea_df[pres_col], 
                                        lang=ea_df[lang_col], tribes=ea_df[tribes_col], 
                                        relg = ea_df[relgion_col],
                                        image_file='Flag_of_Malawi.png')
               elif country == 'mauritius':
                    ea_df = ea_df.loc[8]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=ea_df[capital_col], pres=ea_df[pres_col], 
                                        lang=ea_df[lang_col], tribes=ea_df[tribes_col], 
                                        relg = ea_df[relgion_col],
                                        image_file='Flag_of_Mauritius.png')
               elif country == 'mozambique':
                    ea_df = ea_df.loc[9]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=ea_df[capital_col], pres=ea_df[pres_col], 
                                        lang=ea_df[lang_col], tribes=ea_df[tribes_col], 
                                        relg = ea_df[relgion_col],
                                        image_file='Flag_of_Mozambique.png')
               elif country == 'rwanda':
                    ea_df = ea_df.loc[10]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=ea_df[capital_col], pres=ea_df[pres_col], 
                                        lang=ea_df[lang_col], tribes=ea_df[tribes_col], 
                                        relg = ea_df[relgion_col],
                                        image_file='Flag_of_Rwanda.png')
               elif country == 'seychelles':
                    ea_df = ea_df.loc[11]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=ea_df[capital_col], pres=ea_df[pres_col], 
                                        lang=ea_df[lang_col], tribes=ea_df[tribes_col], 
                                        relg = ea_df[relgion_col],
                                        image_file='Flag_of_Seychelles.png')
               elif country == 'somalia':
                    ea_df = ea_df.loc[12]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=ea_df[capital_col], pres=ea_df[pres_col], 
                                        lang=ea_df[lang_col], tribes=ea_df[tribes_col], 
                                        relg = ea_df[relgion_col],
                                        image_file='Flag_of_Somalia.png')
               elif country == 'south-sudan':
                    ea_df = ea_df.loc[13]
                    return render_template('countrypage.html', ctry=turn_to_text(country), 
                                        cap=ea_df[capital_col], pres=ea_df[pres_col], 
                                        lang=ea_df[lang_col], tribes=ea_df[tribes_col], 
                                        relg = ea_df[relgion_col],
                                        image_file='Flag_of_SouthSudan.png')
               elif country == 'tanzania':
                    ea_df = ea_df.loc[14]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=ea_df[capital_col], pres=ea_df[pres_col], 
                                        lang=ea_df[lang_col], tribes=ea_df[tribes_col], 
                                        relg = ea_df[relgion_col],
                                        image_file='Flag_of_Tanzania.png')
               elif country == 'uganda':
                    ea_df = ea_df.loc[15]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=ea_df[capital_col], pres=ea_df[pres_col], 
                                        lang=ea_df[lang_col], tribes=ea_df[tribes_col], 
                                        relg = ea_df[relgion_col],
                                        image_file='Flag_of_Uganda.png')
               elif country == 'zambia':
                    ea_df = ea_df.loc[16]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=ea_df[capital_col], pres=ea_df[pres_col], 
                                        lang=ea_df[lang_col], tribes=ea_df[tribes_col], 
                                        relg = ea_df[relgion_col],
                                        image_file='Flag_of_Zambia.png')
               elif country == 'zimbabwe':
                    ea_df = ea_df.loc[17]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=ea_df[capital_col], pres=ea_df[pres_col], 
                                        lang=ea_df[lang_col], tribes=ea_df[tribes_col], 
                                        relg = ea_df[relgion_col],
                                        image_file='Flag_of_Zimbabwe.png')
          elif region == 'southafrica':
               if country == 'botswana':
                    sa_df = sa_df.loc[0]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=sa_df[capital_col], pres=sa_df[pres_col], 
                                        lang=sa_df[lang_col], tribes=sa_df[tribes_col], 
                                        relg = sa_df[relgion_col],
                                        image_file='Flag_of_Botswana.png')
               elif country == 'eswatini':
                    sa_df = sa_df.loc[1]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=sa_df[capital_col], pres=sa_df[pres_col], 
                                        lang=sa_df[lang_col], tribes=sa_df[tribes_col], 
                                        relg = sa_df[relgion_col],
                                        image_file='Flag_of_Eswatini.png')
               elif country == 'lesotho':
                    sa_df = sa_df.loc[2]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=sa_df[capital_col], pres=sa_df[pres_col], 
                                        lang=sa_df[lang_col], tribes=sa_df[tribes_col], 
                                        relg = sa_df[relgion_col],
                                        image_file='Flag_of_Lesotho.png')
               elif country == 'namibia':
                    sa_df = sa_df.loc[3]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=sa_df[capital_col], pres=sa_df[pres_col], 
                                        lang=sa_df[lang_col], tribes=sa_df[tribes_col], 
                                        relg = sa_df[relgion_col],
                                        image_file='Flag_of_Namibia.png')
               elif country == 'south-africa':
                    sa_df = sa_df.loc[4]
                    return render_template('countrypage.html', ctry=turn_to_text(country), 
                                        cap=sa_df[capital_col], pres=sa_df[pres_col], 
                                        lang=sa_df[lang_col], tribes=sa_df[tribes_col], 
                                        relg = sa_df[relgion_col],
                                        image_file='Flag_of_SouthAfrica.png')

if __name__ == "__main__":
     app.run(debug=True) 