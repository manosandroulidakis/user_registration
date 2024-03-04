import os
from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
from werkzeug.exceptions import HTTPException

app = Flask(__name__, static_folder='static')

# Configure MySQL connection
app.config['MYSQL_HOST'] = os.environ["MYSQL_HOST"]
app.config['MYSQL_USER'] = os.environ["MYSQL_USER"]
app.config['MYSQL_PASSWORD'] = os.environ["MYSQL_PASSWORD"]
app.config['MYSQL_DB'] = os.environ["MYSQL_DB"]
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
@app.route('/index.html')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/user_list')
def user_list():
    try:
        cur = mysql.connection.cursor()
        sql = "SELECT * FROM users;"
        cur.execute(sql)
        users=cur.fetchall()
        cur.close()
    except Exception as e:
        print("Database selection error:", e)
        raise HTTPException(description="Internal Server Error", code=500) 
    return render_template('user_list.html', content=users)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/submit', methods=['POST'])
def register_user():
    try:
        data = request.form.to_dict()
        insert_user_data(data)
        return jsonify({"message": "Registration successful"})
    except HTTPException as e:
        return jsonify({"error": str(e)}), e.code

def insert_user_data(data):
    try:
        cur = mysql.connection.cursor()
        sql = "INSERT INTO users (first_name, last_name, age, gender, ethnicity) VALUES (%s, %s, %s, %s, %s)"
        cur.execute(sql, (data['first_name'], data['last_name'], data['age'], data['gender'], data['ethnicity']))
        mysql.connection.commit()
        cur.close()
    except Exception as e:
        print("Database insertion error:", e)
        raise HTTPException(description="Internal Server Error", code=500)

if __name__ == '__main__':
    app.run(debug=True)
