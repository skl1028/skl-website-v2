from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'New York',
    'salary': '$120,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Los Angeles',
    'salary': '$110,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Boston',
    'salary': '$110,000'
  }
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name='SKL')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  