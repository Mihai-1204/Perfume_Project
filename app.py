from flask import Flask, render_template, request, redirect, url_for
from perfume import Perfume
from operations.add_perfume import add_perfume
from operations.read_perfume import read_perfumes
from operations.update_perfume import update_perfume
from operations.delete_perfume import delete_perfume
from init_config import load_config


app = Flask(__name__)
config = load_config()



def parse_perfume_form(form):
    return {
        "name": form["name"],
        "brand": form["brand"],
        "price": float(form["price"]),
        "gender": form["gender"],
        "season": form.getlist("season[]"),
        "edt": "edt" in form,
        "edp": "edp" in form,
        "perfume": "perfume" in form,
        "type": form.getlist("type[]")
    }


@app.route('/')
def index():
    perfumes = read_perfumes("data/perfumes.json")
    return render_template('index.html', perfumes=perfumes)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = parse_perfume_form(request.form)
        new_perfume = Perfume(**data)
        add_perfume(new_perfume)
        return redirect(url_for('index'))
    return render_template('add_perfume.html', config=config)


@app.route('/update/<string:name>', methods=['GET', 'POST'])
def update(name):
    if request.method == 'POST':
        updated_info = parse_perfume_form(request.form)
        update_perfume(name, updated_info)
        return redirect(url_for('index'))
    return render_template('update_perfume.html', name=name, config=config)


@app.route('/delete/<string:name>')
def delete(name):
    delete_perfume(name)
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
