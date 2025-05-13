from flask import Flask, render_template, request, redirect, url_for, flash
from perfume import Perfume
from operations.crud import add_perfume, get_all_perfumes, update_perfume, delete_perfume
import init_config
import os

app = Flask(__name__)
app.secret_key = os.environ.get('fragrance_app_key')

config = init_config.load_config()


@app.route('/')
def index():
    perfumes = get_all_perfumes()
    return render_template('index.html', perfumes=perfumes, config=config)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        try:
            concentration_value = request.form.get('concentration')
            concentration = [concentration_value] if concentration_value else []
            perfume = Perfume(
                name=request.form.get('name', '').strip(),
                brand=request.form.get('brand', '').strip(),
                price=float(request.form.get('price', 0)),
                currency=request.form.get('currency'),
                concentration=concentration,
                gender=request.form.get('gender'),
                season=request.form.getlist('season'),
                types=request.form.getlist('types')
            )
            perfume.validate()
            add_perfume(perfume)
            flash("Perfume added successfully!", "success")
            return redirect(url_for('index'))
        except Exception as e:
            flash(str(e), "danger")
            return redirect(url_for('add'))

    return render_template('add_perfume.html', config=config)


@app.route('/update/<name>/<concentration>', methods=['GET', 'POST'])
def update(name, concentration):
    perfume_data = None
    try:
        perfume_data = next(
            p for p in get_all_perfumes()
            if p['name'].lower() == name.lower() and concentration.lower() in [c.lower() for c in p['concentration']]
        )
    except StopIteration:
        flash("Perfume not found.", "danger")
        return redirect(url_for('index'))

    if request.method == 'POST':
        try:
            concentration_value = request.form.get('concentration')
            concentration_list = [concentration_value] if concentration_value else []
            updated_perfume = Perfume(
                name=request.form.get('name', '').strip(),
                brand=request.form.get('brand', '').strip(),
                price=float(request.form.get('price', 0)),
                currency=request.form.get('currency'),
                concentration=concentration_list,
                gender=request.form.get('gender'),
                season=request.form.getlist('season'),
                types=request.form.getlist('types')
            )
            updated_perfume.validate()
            update_perfume(name, concentration, updated_perfume)
            flash("Perfume updated successfully!", "success")
            return redirect(url_for('index'))
        except Exception as e:
            flash(str(e), "danger")
            return redirect(url_for('update', name=name, concentration=concentration))

    return render_template('update_perfume.html', perfume=perfume_data, config=config)


@app.route('/delete/<name>/<concentration>', methods=['POST'])
def delete(name, concentration):
    try:
        delete_perfume(name, concentration)
        flash("Perfume deleted successfully!", "success")
    except Exception as e:
        flash(str(e), "danger")
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
