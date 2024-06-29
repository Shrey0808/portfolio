from flask import Flask,render_template

app = Flask(__name__)
@app.route('/') # for home page
def home():
    return render_template('index.html') 

@app.route('/education') # for Education page
def education():
    return render_template('education.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')



if __name__ =='__main__':
    app.run(debug=True)