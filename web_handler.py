import flask
import sqlite3

app = flask.Flask(__name__)
app.debug = False

@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/filter', methods=['POST'])
def filter():
    db = sqlite3.connect('bakery.db')
    source = flask.request.form['source']
    results = db.execute("SELECT BakeryItem.ItemNumber, BakeryItem.Name, BakeryItem.Source FROM BakeryItem WHERE BakeryItem.Source = ?", (source,)).fetchall()
    html = flask.render_template('filter.html', results = results)
    db.close()
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
