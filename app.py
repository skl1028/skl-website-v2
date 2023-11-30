from flask import Flask, render_template, jsonify
from database import joblist_from_db, load_job_from_db

app = Flask(__name__)

@app.route("/")
def hello_skl():
  jobs = joblist_from_db()
  return render_template('home.html', 
                          jobs=jobs)
@app.route("/api/jobs")
def list_jobs():
  jobs = joblist_from_db()
  return jsonify(jobs)

@app.route("/about")
def about():
  return render_template('about.html')

@app.route("/job/<id>")
def job_info(id):
  job = load_job_from_db(id)
  if not job:
    return "Not Found", 404
  return render_template('jobpage.html', 
                          job=job)
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  