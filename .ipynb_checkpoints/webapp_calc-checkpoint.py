from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        expression = request.form['expression']
        try:
            result = str(eval(expression))
            return render_template('index.html', result=result, expression=expression)
        except:
            result = 'Error'
            return render_template('index.html', result=result, expression=expression)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
