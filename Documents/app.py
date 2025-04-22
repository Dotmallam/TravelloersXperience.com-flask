from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.to_dict()
    return render_template('thankyou.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)