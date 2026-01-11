from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

notes = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', note=notes)
    elif request.method == 'POST':
        if request.form.get('_method') == 'DELETE':
            notes.clear()
            return render_template('index.html', note=notes)
        else:
            notes.append(request.form.get('noteadd'))
            return render_template('index.html', note=notes)
    else:
        return 'failiure'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)