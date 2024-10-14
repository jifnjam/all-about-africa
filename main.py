import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, Response, make_response
from PIL import Image

# for pythonanywhere
from pathlib import Path
THIS_FOLDER = Path(__file__).parent.resolve()
my_file_ma = THIS_FOLDER / "/home/tobim/all-about-africa/masterafrica.csv"
my_file_sa = THIS_FOLDER / "/home/tobim/all-about-africa/stereotypes.xlsx"


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

@app.route('/')
def home():
     return render_template('index.html')

@app.route('/<stereotype>/')
def stereotypes(stereo):

     stereo_df = pd.read_excel(my_file_sa)

     if stereo == 'economy':
          sterry = "Economy"
          stereo_df = stereo_df.loc[0]['Economy']
     elif stereo == 'landscape':
          sterry = "Landscape"
          stereo_df = stereo_df.loc[0]['Landscape']
     elif stereo == 'climate':
          sterry = "Climate"
          stereo_df = stereo_df.loc[0]['Climate']
     elif stereo == 'tecnology':
          sterry = "Technology"
          stereo_df = stereo_df.loc[0]['Technology']
     elif stereo == 'government': 
          sterry = "Government"
          stereo_df = stereo_df.loc[0]['Government']
     elif stereo == 'cult-lang': 
          sterry = "Culture and Language"
          stereo_df = stereo_df.loc[0]['Culture and Language']
     elif stereo == 'war': 
          sterry = "War"
          stereo_df = stereo_df.loc[0]['War']
     elif stereo == 'healthcare': 
          sterry = "Healthcare"
          stereo_df = stereo_df.loc[0]['Healthcare']
     elif stereo == 'infrastructure': 
          sterry = "Infrastructure" 
          stereo_df = stereo_df.loc[0]['Infrastructure']         
     elif stereo == 'education': 
          sterry = "Education"
          stereo_df = stereo_df.loc[0]['Education']

     if stereo == 'economy':
          return render_template('stereopage.html', title="Economy", data=stereo_df) 
     elif stereo == 'landscape':
          return render_template('stereopage.html', title="Landscape", data=stereo_df)
     elif stereo == 'climate':
          return render_template('stereopage.html', title="Climate", data=stereo_df)
     elif stereo == 'technology':
          return render_template('stereopage.html', title="Technology", data=stereo_df)
     elif stereo == 'government': 
          return render_template('stereopage.html', title="Government", data=stereo_df) 
     elif stereo == 'cult-lang':
          return render_template('stereopage.html', title="Culture and Language", data=stereo_df)
     elif stereo == 'war':
          return render_template('stereopage.html', title="War", data=stereo_df)
     elif stereo == 'healthcare':
          return render_template('stereopage.html', title="Healthcare", data=stereo_df)
     elif stereo == 'infrastructure': 
          return render_template('stereopage.html', title="Infrastructure", data=stereo_df) 
     elif stereo == 'education': 
          return render_template('stereopage.html', title="Education", data=stereo_df) 
     
if __name__ == "__main__":
     app.run(debug=True) 