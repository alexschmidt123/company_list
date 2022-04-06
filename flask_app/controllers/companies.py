from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.company import Company


@app.route('/')
def to_dashboard():
    return redirect ('/dashboard')

@app.route('/dashboard')
def companies_list():
    companies = Company.get_all_companies()
    return render_template('dashboard.html', companies = companies)

@app.route('/show/<int:company_id>')
def companys_company_id(company_id):
    data = {
        'server_id': company_id
    }
    company = Company.get_one_company(data)
    return render_template('view.html', company = company)


@app.route('/new')
def companys_new():
    return render_template ('new.html')


@app.route('/new/add', methods = ['POST'])
def companys_insert():
    if not Company.validate_new_company(request.form):
        return redirect('/new')
    else:
        data = {
            'server_rank': request.form['template_rank'],
            'server_location': request.form['template_location'],
            'server_news': request.form['template_news'],
            'server_name': request.form['template_name'],
            'server_marketCapitalization': request.form['template_marketCapitalization'],
        }
        print("-------------------------->")
        print(data)
        Company.save(data)  
        return redirect ('/dashboard')

@app.route('/edit/<int:company_id>')
def companys_company_id_edit(company_id):
    data = {
        'server_id': company_id
    }
    company = Company.get_one_company(data)
    return render_template('edit.html', company = company)

@app.route('/edit/update/<int:company_id>', methods = ['POST', 'GET'])
def companys_company_id_update(company_id):
    if not Company.validate_new_company(request.form):
        data = {
        'server_id': company_id
        }
        company = Company.get_one_company(data)
        return render_template('edit.html', company = company)
    else:
        data = {
            "server_id": company_id,
            'server_rank': request.form['template_rank'],
            'server_location': request.form['template_location'],
            'server_news': request.form['template_news'],
            'server_name': request.form['template_name'],
            'server_marketCapitalization': request.form['template_marketCapitalization'],
        }
        Company.update_company(data)
        return redirect ('/dashboard')

@app.route('/delete/<int:company_id>')
def companies_company_id_delete(company_id):
    data ={
        'server_id' : company_id
    }
    Company.delete(data)
    return redirect ('/dashboard')