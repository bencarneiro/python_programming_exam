from flask import Flask, request, render_template, session, redirect, url_for
import pandas as pd
import requests

def number_resumes(job_tit, job_loc):
    wizehire_resume_data = pd.read_csv(r'Z:\wizehire\resume_count_dataset_small.csv',header=None)
    wizehire_resume_data = wizehire_resume_data.rename(columns={0: "Job Title", 1: "Job Location", 2: "Number of Resumes"})
    wizehire_resume_data = wizehire_resume_data[wizehire_resume_data['Job Title'] == job_tit]
    wizehire_resume_data = wizehire_resume_data[wizehire_resume_data['Job Location'] == job_loc]
    return sum(wizehire_resume_data['Number of Resumes'])
    
def number_jobs(job_tit, job_loc):
     dic = {"q":job_tit,"l":job_loc}
     indeed_response = requests.get("https://indeed.com/jobs", params=dic)   
     indeed_html = indeed_response.text
     indeed_html = indeed_html.split("Page 1 of ")[1]
     indeed_html = indeed_html.split()[0]
     return int(indeed_html.replace(",",""))
     
app = Flask(__name__)

@app.route('/', methods=("POST", "GET"))
def home():
    if request.method == "POST":
        job_tit = request.form['jobtitle']
        job_loc = request.form['joblocation']
        r = number_resumes(job_tit, job_loc)
        j = number_jobs(job_tit, job_loc)   
        difficulty = r/j
        
        return render_template('base.html', jt = job_tit, jl = job_loc, res = r, jobs = j, result = difficulty)
    else:
        return render_template('base.html')
        

if __name__=='__main__':
    app.run(debug=True)