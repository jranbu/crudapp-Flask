from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
@app.route("/index")
def index():
    con = sql.connect("new_database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from studies")
    data = cur.fetchall()
    return render_template("index.html", datas=data)


@app.route("/add_study", methods=['POST', 'GET'])
def add_study():
    if request.method == 'POST':
        studyname = request.form['study name']
        sponsername = request.form['sponser name']
        studydescription = request.form['study description']
        con = sql.connect("new_database.db")
        cur = con.cursor()
        cur.execute("INSERT INTO studies (STUDYNAME, SPONSERNAME, STUDYDESCRIPTION) VALUES (?, ?, ?)",
                    (studyname, sponsername, studydescription))
        con.commit()
        flash('Study Added', 'success')
        return redirect(url_for("index"))
    return render_template("add_study.html")



@app.route("/edit_study/<string:uid>", methods=['POST', 'GET'])
def edit_user(uid):
    if request.method == 'POST':
        studyname = request.form['study name']
        sponsername = request.form['sponser name']
        studydescription = request.form['study description']
        con = sql.connect("new_database.db")
        cur = con.cursor()
        cur.execute("update studies set STUDYNAME=?,SPONSERNAME=?,STUDYDESCRIPTION=? where UID=?",
                    (studyname, sponsername, studydescription, uid))
        con.commit()
        flash('Study Updated', 'success')
        return redirect(url_for("index"))
    con = sql.connect("new_database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from studies where UID=?", (uid,))
    data = cur.fetchone()
    return render_template("edit_study.html", datas=data)


@app.route("/delete_study/<string:uid>", methods=['GET'])
def delete_study(uid):
    con = sql.connect("new_database.db")
    cur = con.cursor()
    cur.execute("delete from studies where UID=?", (uid,))
    con.commit()
    flash('study Deleted', 'warning')
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.secret_key = 'admin123'
    app.run(debug=True)
    