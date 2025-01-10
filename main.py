from flask import Flask, render_template, request 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.abspath('db.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Klasse Message zur Speicherung von Nachrichten
class Message(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(200), nullable = True)
    content = db.Column(db.String(500), nullable = True)
    created_at = db.Column(db.DateTime, default = datetime.now)
    
@app.route('/<name>', methods=['GET', 'POST'])
def start_page(name):
    if request.method == 'POST': 
        new_message = Message(user = name, content = request.form['content'])
        db.session.add(new_message)
        db.session.commit()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)