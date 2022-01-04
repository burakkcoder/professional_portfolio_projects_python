from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/portfolio-details-1')
def portfolio_details_1():
    return render_template("portfolio-details-1.html")

@app.route('/portfolio-details-2')
def portfolio_details_2():
    return render_template("portfolio-details-2.html")

@app.route('/portfolio-details-3')
def portfolio_details_3():
    return render_template("portfolio-details-3.html")

if __name__ == "__main__":
    app.run(debug=True)