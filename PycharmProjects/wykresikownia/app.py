from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Dane do wykresu
    labels = ['Temperatura', 'Głośność', 'Wilgotność', 'Ciśnienie', 'PM2.5', 'PM10', 'PM1', 'Jakość powietrza']
    data = [9.4, 41.15, 75.5, 1013.8, 5, 5, 3, 65]

    return render_template('index.html', labels=labels, data=data)

if __name__ == '__main__':
    app.run(debug=True)
