from flask import Flask,render_template,request 
import joblib

###Loading model and cv
model = joblib.load('language_identification.sav')

app = Flask(__name__) ## defining flask name

@app.route('/') ## home route
def home():
    return "hello good morning stupid people" #render_template('index.html') ##at home route returning index.html to show

@app.route('/')#('/predict',methods=['POST']) ## on post request /predict 
def test_model(test_sentence):
    languages = {
    'Arabic' : 0,
    'Danish' : 1,
    'Dutch' : 2,
    'English' : 3,
    'French' : 4,
    'German' : 5,
    'Greek' : 6,
    'Hindi' : 7, 
    'Italian' : 8, 
    'Kannada' : 9, 
    'Malayalam' : 10,
    'Portugese' : 11,
    'Russian' : 12,
    'Spanish' : 13,
    'Swedish' : 14,
    'Tamil' : 15,
    'Turkish' : 16
    }
    
    
    
    rev = re.sub('^[a-zA-Z]',' ',test_sentence)
    rev = rev.lower()
    rev = rev.split()
    rev = [ps.stem(word) for word in rev if word not in set(stopwords.words())]
    rev = ' '.join(rev)
    
    rev = cv.transform([rev]).toarray()
    
    output = model.predict(rev)[0]
    
    keys = list(languages)
    values = list(languages.values())
    position = values.index(output)
    
    output = keys[position]
    
    print(output)
if __name__ == "__main__":
    app.run(debug=True)     ## running the flask app as debug==True
