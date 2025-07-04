from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Cloud Engineer',
        'location': 'Montreal, QC',
        'salary': '$98K'
    },
    {
        'id': 2,
        'title': 'Software Developer',
        'location': 'Toronto, ON',
        'salary': '$103K'
    },
    {
        'id': 3,
        'title': 'Data Scientist',
        'location': 'Toronto, ON',
        'salary': '$120K'
    },
    {
        'id': 4,
        'title': 'Frontend developer',
        'location': 'Brampton, ON',
        'salary': '$60K'
    },
    {
        'id': 5,
        'title': 'Backend Api Developer',
        'location': 'Toronto, ON',
        'salary': '$80K'
    }
]

company_name = "St Clair"

@app.route('/api/jobs')
def jobs():
    return jsonify(JOBS)
@app.route('/')
def hello_world():  # put application's code here
    return render_template('Home.html', jobs=JOBS, company_name=company_name)


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
