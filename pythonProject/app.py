from flask import Flask, render_template, url_for


app = Flask(__name__)


def __repr__(self):
    return '<Article %r>' % self.id


@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/create-article')
def create_article():
    return render_template("create-article.html")





if __name__ == "__main__":
    app.run(debug=True)
