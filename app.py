from flask import Flask, render_template, request, redirect, url_for
from perfume import Perfume
from operations.add_perfume import add_perfume
from operations.read_perfume import read_perfumes
from operations.update_perfume import update_perfume
from operations.delete_perfume import delete_perfume

app = Flask(__name__)

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
        season = request.form['season']
        edt = 'edt' in request.form
        edp = 'edp' in request.form
        perfume = 'perfume' in request.form
        perfume_type = request.form['type']

        new_perfume = Perfume(name, brand, price, gender, season, edt, edp, perfume, perfume_type)
        add_perfume(new_perfume)
        return redirect(url_for('index'))

    return render_template('add_perfume.html')

@app.route('/update/<string:name>', methods=['GET', 'POST'])
def update(name):
    if request.method == 'POST':
        updated_info = {}

        updated_name = request.form.get('name')
        if updated_name:
            updated_info['name'] = updated_name

        updated_brand = request.form.get('brand')
        if updated_brand:
            updated_info['brand'] = updated_brand

        updated_price = request.form.get('price')
        if updated_price:
            updated_info['price'] = float(updated_price)

        updated_gender = request.form.get('gender')
        if updated_gender:
            updated_info['gender'] = updated_gender

        updated_season = request.form.get('season')
        if updated_season:
            updated_info['season'] = updated_season

        updated_edt = request.form.get('edt')
        if updated_edt:
            updated_info['edt'] = True

        updated_edp = request.form.get('edp')
        if updated_edp:
            updated_info['edp'] = True

        updated_perfume = request.form.get('perfume')
        if updated_perfume:
            updated_info['perfume'] = True

        updated_type = request.form.get('type')
        if updated_type:
            updated_info['type'] = updated_type

        update_perfume(name, updated_info)
        return redirect(url_for('index'))

    return render_template('update_perfume.html', name=name)

@app.route('/delete/<string:name>', methods=['GET', 'POST'])
def delete(name):
    delete_perfume(name)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
