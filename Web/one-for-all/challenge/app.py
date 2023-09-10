from flask import Flask, request, make_response, render_template, jsonify
import sqlite3

__author__ = "sauman"

app = Flask(__name__, template_folder='templates')

def connection_create():
    con = None
    try:
        con = sqlite3.connect("test.db")
    except Error as e:
        print(e)

    return con

def insert(con):
    create = "create table if not exists accounts(id int NOT NULL PRIMARY KEY , email varchar(20) unique, username varchar(20), password varchar(200));"
    con.execute(create)

    test = ''' 
            insert or ignore into accounts values(112311, 'one@gmail.com', 'kiran', 'nothing here');
            insert or ignore into accounts values(112312, 'two@gmail.com', 'admin', 'something here');
            insert or ignore into accounts values(112313, 'three@gmail.com', 'flagishere90', 'and_Adm1t_');
            insert or ignore into accounts values(112314, 'four@gmail.com', 'complexname9191681', 'path:/secretsforyou');
        ''' 
    con.executescript(test)
    con.commit()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
            username = request.form['username']
            con = connection_create()
            insert(con)
            con.row_factory = sqlite3.Row
            try:
                 cur = con.execute(f'SELECT * from accounts where username = "{username}"')
                 res = cur.fetchone()
                 print(res)
                 try:
                    results = [str(row) for row in res]
                    return results
                 except:
                     results = "No such user exists"
                     return results
            except sqlite3.OperationalError as e:
                results = "No such user exists"
                return results
    resp = make_response(render_template('index.html'))
    resp.set_cookie('name', 'kiran')
    name = request.cookies.get('name')
    if name == "admin":
        return "PCTF{Hang_"
    return resp 

@app.route('/secretsforyou/', defaults={'path': ''})
@app.route('/secretsforyou/<path:path>')
def bypass(path):
    if path == '..;/':
        return "l00s3_"
    return render_template('403.html')

@app.route('/user', methods=["GET"])
def user():
    get_id = request.args.get('id', type=int)
    data=''
    if get_id == 0:
        data="ev3rYtH1nG}"
    else:
        data="This is a Short Description of the Client"
    return render_template('user.html', result=data)

if __name__ == '__main__':
    app.run(debug=False, 
            host='0.0.0.0', 
            port=9099)
