from flask import Flask, render_template, request, redirect, url_for
from perfume import Perfume
from operations.add_perfume import add_perfume
from operations.read_perfume import read_perfumes
from operations.update_perfume import update_perfume
from operations.delete_perfume import delete_perfume
from init_config import load_config

app = Flask(__name__)

config = load_config()

@app.route('/')
def index():
    perfumes = read_perfumes(file_path="data/perfumes.json")
    return render_template('index.html', perfumes=perfumes)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        brand = request.form['brand']
        price = float(request.form['price'])
        gender = request.form['gender']
        seasons = request.form.getlist('season')
        edt = 'edt' in request.form
        edp = 'edp' in request.form
        perfume = 'perfume' in request.form
        types = request.form.getlist('type')
        concentrations = request.form.getlist('concentration')  # Preluăm concentrațiile selectate

        new_perfume = Perfume(name, brand, price, gender, seasons, edt, edp, perfume, types, concentrations)
        add_perfume(new_perfume)
        return redirect(url_for('index'))

    return render_template('add_perfume.html', config=config)


@app.route('/update/<string:name>', methods=['GET', 'POST'])
def update(name):
    perfumes = read_perfumes("data/perfumes.json")
    perfume = next((p for p in perfumes if p['name'] == name), None)
    if not perfume:
        return "Perfume not found", 404

    if request.method == 'POST':
        updated_info = {
            'name': request.form['name'],
            'brand': request.form['brand'],
            'price': float(request.form['price']),
            'gender': request.form['gender'],
            'season': request.form.getlist('season'),
            'edt': 'edt' in request.form,
            'edp': 'edp' in request.form,
            'perfume': 'perfume' in request.form,
            'type': request.form.getlist('type')
        }
        update_perfume(name, updated_info)
        return redirect(url_for('index'))

    return render_template('update_perfume.html', perfume=perfume, config=config)


@app.route('/delete/<string:name>', methods=['GET', 'POST'])
def delete(name):
    delete_perfume(name)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)