from flask import Flask, render_template, request,url_for
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    id = request.form['id']
    password = request.form['password']
    return redirect(url_for('dashboard'))
  return render_template('login.html')

@app.route('/dashboard')
def dashboard():
  return render_template('dashboard.html')
if __name__ == '__main__':  
  app.run(debug=True)