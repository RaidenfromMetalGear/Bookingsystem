from flask import Flask, render_template, request, redirect, session
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'R0xq/EPm7dajWe9mmhB/XQSwd9QYV/gj'

# MONGODB
client = MongoClient('mongodb+srv://kvnvg2:Nesna=bra!@cluster1.1da3r.mongodb.net/test')
db = client['db_ak']
collection = db['Brukere']

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = collection.find_one({'brukernavn': username, 'passord': password})

        if user:
            session['brukernavn'] = username
            return redirect('/dashboard')
        else:
            error = 'Feil brukernavn eller passord, prøv på nytt'
            return render_template('login.html', error=error)

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'brukernavn' in session:
        username = session['brukernavn']
        return render_template('dashboard.html', username=username)
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.pop('brukernavn', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
