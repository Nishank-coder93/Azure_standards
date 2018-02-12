from flask import Flask, render_template
import pyodbc

app = Flask(__name__)
app.config.from_object('config')


server = ''
database = ''
username = ''
password = ''
driver= ''
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)


@app.route('/', methods=['GET'])
def home_page():
    cursor = cnxn.cursor()
    rows = cursor.execute("SELECT @@version").fetchall()

    strrows = ""

    for row in rows:
        strrows += "".join(row)

    info = "Not Connected to Database"
    if cnxn:
        info = "Connected to Database"

    return render_template("home_page.html", info=strrows)

if __name__ == '__main__':
  app.run()
