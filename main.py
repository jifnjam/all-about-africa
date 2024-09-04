import pandas as pd
from flask import Flask, render_template, request, redirect, url_for
from fileinput import filename

app = Flask(__name__)

def turn_to_text(choice): #for multi word country names
     choice = choice.replace("-", " ")
     choice = choice.title()
     return choice

def turn_to_html(choice):
     spread = choice.lower()
     spread = spread.split()
     spread = "-".join(spread)
     return spread

@app.route('/')
def home():
     return render_template('index.html')

@app.route('/<region>/')
def regions(region):
     na_df = pd.read_csv('northafrica.csv')
     na_ctrydf = na_df['Country'].str.lower()

     #change <country> into blank-blank-blank wording
     if region == 'northafrica':
          return render_template('regionpage.html', title="North Africa", title_lower=region, data=na_ctrydf) 
     elif region == 'eastafrica':
          return render_template('regionpage.html', title="East Africa", title_lower=region, data=na_ctrydf)
     elif region == 'westafrica':
          return render_template('regionpage.html', title="West Africa", title_lower=region, data=na_ctrydf)
     elif region == 'centralafrica':
          return render_template('regionpage.html', title="Central Africa", title_lower=region, data=na_ctrydf)
     elif region == 'southafrica': 
          return render_template('regionpage.html', title="South Africa", title_lower=region, data=na_ctrydf) 
#changed 1 2 3 4 5 6

@app.route('/<region>/<country>/')
def countries(region, country):
     na_df = pd.read_csv('northafrica.csv')
     na_df = na_df.dropna(axis='columns')

     capital_col = 'Capital'
     lang_col = 'Language'
     pres_col = 'President/Leader' 
     tribes_col = 'Tribes/Ethnic Groups'
     relgion_col = 'Religion'

     if region == 'northafrica': 
          #for loop here
          if country == 'algeria': 
               na_df = na_df.loc[0]
               return render_template('countrypage.html', ctry=country.capitalize(), 
                                      cap=na_df[capital_col], pres=na_df[pres_col], 
                                      lang=na_df[lang_col], tribes=na_df[tribes_col], 
                                      relg = na_df[relgion_col], pre_file='North Africa',
                                      image_file='Flag_of_Algeria.svg.png')
          elif country == 'egypt':
               df = df.loc[1]
               return render_template('countrypage.html', ctry=country.capitalize(), 
                                      cap=df[capital_col], pres=df[pres_col], 
                                      lang=df[lang_col], tribes=df[tribes_col], 
                                      relg = df[relgion_col], pre_file='North Africa',
                                      image_file='Flag_of_Egypt.png')
          elif country == 'libya':
               df = df.loc[2]
               return render_template('countrypage.html', ctry=country.capitalize(), 
                                      cap=df[capital_col], pres=df[pres_col], 
                                      lang=df[lang_col], tribes=df[tribes_col], 
                                      relg = df[relgion_col], pre_file='North Africa',
                                      image_file='Flag_of_Libya.png')
          elif country == 'morocco':
               df = df.loc[3]
               return render_template('countrypage.html', ctry=country.capitalize(), 
                                      cap=df[capital_col], pres=df[pres_col], 
                                      lang=df[lang_col], tribes=df[tribes_col], 
                                      relg = df[relgion_col],
                                      image_file='Flag_of_Morocco.png')
          elif country == 'sudan':
               df = df.loc[4]
               return render_template('countrypage.html', ctry=country.capitalize(), 
                                      cap=df[capital_col], pres=df[pres_col], 
                                      lang=df[lang_col], tribes=df[tribes_col], 
                                      relg = df[relgion_col],
                                      image_file='Flag_of_Sudan.png')
          elif country == 'tunisia':
               df = df.loc[5]
               return render_template('countrypage.html', ctry=country.capitalize(), 
                                      cap=df[capital_col], pres=df[pres_col], 
                                      lang=df[lang_col], tribes=df[tribes_col], 
                                      relg = df[relgion_col],
                                      image_file='Flag_of_Tunisia.png')
     elif region == 'centralafrica':
          if country == 'angola':
               df = df.loc[0]
               return render_template('countrypage.html', ctry=country.capitalize(), 
                                      cap=df[capital_col], pres=df[pres_col], 
                                      lang=df[lang_col], tribes=df[tribes_col], 
                                      relg = df[relgion_col],
                                      image_file='Flag_of_Angola.png')
          elif country == 'cameroon':
               df = df.loc[1]
               return render_template('countrypage.html', ctry=country.capitalize(), 
                                      cap=df[capital_col], pres=df[pres_col], 
                                      lang=df[lang_col], tribes=df[tribes_col], 
                                      relg = df[relgion_col],
                                      image_file='Flag_of_Cameroon.png')
          elif country == 'central-african-republic':
               df = df.loc[2]
               return render_template('countrypage.html', ctry=turn_to_text(country), 
                                      cap=df[capital_col], pres=df[pres_col], 
                                      lang=df[lang_col], tribes=df[tribes_col], 
                                      relg = df[relgion_col],
                                      image_file='Flag_of_CentralAfricanRepublic.png') 
          elif country == 'chad':
               df = df.loc[3]
               return render_template('countrypage.html', ctry=country.capitalize(), 
                                      cap=df[capital_col], pres=df[pres_col], 
                                      lang=df[lang_col], tribes=df[tribes_col], 
                                      relg = df[relgion_col],
                                      image_file='Flag_of_Tunisia.png')
          elif country == 'democractic-republic-of-the-congo':
               df = df.loc[4]
               return render_template('countrypage.html', ctry=turn_to_text(country), 
                                      cap=df[capital_col], pres=df[pres_col], 
                                      lang=df[lang_col], tribes=df[tribes_col], 
                                      relg = df[relgion_col],
                                      image_file='Flag_of_DemocraticRepublicoftheCongo.png')
          elif country == 'equatorial-guinea':
               df = df.loc[5]
               return render_template('countrypage.html', ctry=turn_to_text(country), 
                                      cap=df[capital_col], pres=df[pres_col], 
                                      lang=df[lang_col], tribes=df[tribes_col], 
                                      relg = df[relgion_col],
                                      image_file='Flag_of_EquatorialGuinea.png')
          elif country == 'gabon':
               df = df.loc[6]
               return render_template('countrypage.html', ctry=country.capitalize(), 
                                      cap=df[capital_col], pres=df[pres_col], 
                                      lang=df[lang_col], tribes=df[tribes_col], 
                                      relg = df[relgion_col],
                                      image_file='Flag_of_Gabon.png')
          elif country == 'republic-of-the-congo':
               df = df.loc[7]
               return render_template('countrypage.html', ctry=turn_to_text(country), 
                                      cap=df[capital_col], pres=df[pres_col], 
                                      lang=df[lang_col], tribes=df[tribes_col], 
                                      relg = df[relgion_col],
                                      image_file='Flag_of_RepublicoftheCongo.png')
          elif country == 'sao-tome-and-principe':
               df = df.loc[8]
               return render_template('countrypage.html', ctry=turn_to_text(country), 
                                      cap=df[capital_col], pres=df[pres_col], 
                                      lang=df[lang_col], tribes=df[tribes_col], 
                                      relg = df[relgion_col],
                                      image_file='Flag_of_SaoTomeandPrincipe.png')
          elif region == 'westafrica':
               if country == 'benin':
                    df = df.loc[0]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_Benin.png')
               elif country == 'burkina-faso':
                    df = df.loc[1]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_BurkinaFaso.png')
               elif country == 'cape-verde':
                    df = df.loc[2]
                    return render_template('countrypage.html', ctry=turn_to_text(country), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_CapeVerde.png') 
               elif country == 'gambia':
                    df = df.loc[3]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_Gambia.png')
               elif country == 'ghana':
                    df = df.loc[4]
                    return render_template('countrypage.html', ctry=turn_to_text(country), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_Ghana.png')
               elif country == 'guinea':
                    df = df.loc[5]
                    return render_template('countrypage.html', ctry=turn_to_text(country), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_Guinea.png')
               elif country == 'guinea-bissau':
                    df = df.loc[6]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_GuineaBissau.png')
               elif country == 'ivory-coast':
                    df = df.loc[7]
                    return render_template('countrypage.html', ctry=turn_to_text(country), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_IvoryCoast.png')
               elif country == 'liberia':
                    df = df.loc[8]
                    return render_template('countrypage.html', ctry=turn_to_text(country), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_Liberia.png')
               elif country == 'mali':
                    df = df.loc[9]
                    return render_template('countrypage.html', ctry=turn_to_text(country), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_Mali.png')
               elif country == 'mauritania':
                    df = df.loc[10]
                    return render_template('countrypage.html', ctry=turn_to_text(country), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_Mauritania.png')
               elif country == 'niger':
                    df = df.loc[11]
                    return render_template('countrypage.html', ctry=turn_to_text(country), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_Niger.png')
               elif country == 'nigeria':
                    df = df.loc[12]
                    return render_template('countrypage.html', ctry=turn_to_text(country), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_Nigeria.png')
               elif country == 'senegal':
                    df = df.loc[13]
                    return render_template('countrypage.html', ctry=turn_to_text(country), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_Senegal.png')
               elif country == 'sierra-leone':
                    df = df.loc[14]
                    return render_template('countrypage.html', ctry=turn_to_text(country), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_SierraLeone.png')
               elif country == 'togo':
                    df = df.loc[15]
                    return render_template('countrypage.html', ctry=turn_to_text(country), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_Togo.png')
          elif region == 'eastafrica':
               if country == 'burundi':
                    df = df.loc[0]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_Benin.png')
               elif country == 'comoros':
                    df = df.loc[1]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_Comoros.png')
               elif country == 'djibouti':
                    df = df.loc[2]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_Djibouti.png')
               elif country == 'eritrea':
                    df = df.loc[3]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_Eritrea.png')
               elif country == 'ethiopia':
                    df = df.loc[4]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_Ethiopia.png')
               elif country == 'kenya':
                    df = df.loc[5]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_Kenya.png')
               elif country == 'madagascar':
                    df = df.loc[6]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_Madagascar.png')
               elif country == 'malawi':
                    df = df.loc[7]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_Malawi.png')
               elif country == 'mauritius':
                    df = df.loc[8]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_Mauritius.png')
               elif country == 'mozambique':
                    df = df.loc[9]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_Mozambique.png')
               elif country == 'rwanda':
                    df = df.loc[10]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_Rwanda.png')
               elif country == 'seychelles':
                    df = df.loc[11]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_Seychelles.png')
               elif country == 'somalia':
                    df = df.loc[12]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_Somalia.png')
               elif country == 'south-sudan':
                    df = df.loc[13]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_SouthSudan.png')
               elif country == 'tanzania':
                    df = df.loc[14]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_Tanzania.png')
               elif country == 'uganda':
                    df = df.loc[15]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_Uganda.png')
               elif country == 'zambia':
                    df = df.loc[16]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_Zambia.png')
               elif country == 'zimbabwe':
                    df = df.loc[17]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_Zimbabwe.png')
          elif region == 'southafrica':
               if country == 'botswana':
                    df = df.loc[0]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_Botswana.png')
               elif country == 'eswatini':
                    df = df.loc[1]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_Eswatini.png')
               elif country == 'lesotho':
                    df = df.loc[2]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_Lesotho.png')
               elif country == 'namibia':
                    df = df.loc[3]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_Namibia.png')
               elif country == 'south-africa':
                    df = df.loc[4]
                    return render_template('countrypage.html', ctry=country.capitalize(), 
                                        cap=df[capital_col], pres=df[pres_col], 
                                        lang=df[lang_col], tribes=df[tribes_col], 
                                        relg = df[relgion_col],
                                        image_file='Flag_of_SouthAfrica.png')

if __name__ == '__main__':
     app.run(debug=True)