from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
class Company():

    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.rank = data['rank']
        self.location =data['location']
        self.marketCapitalization =data['marketCapitalization'] 
        self.news = data['news']
        self.create_at =data['create_at']
        self.update_at =data['update_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO companies (`rank`, marketCapitalization, `location`, news, `name`) VALUES ( %(server_rank)s,%(server_marketCapitalization)s,%(server_location)s,%(server_news)s, %(server_name)s);"
        result = connectToMySQL("company_schema").query_db(query,data)
        return result
        

    @classmethod
    def get_all_companies(cls):
        query = 'SELECT * FROM companies;'
        results = connectToMySQL('company_schema').query_db(query)
        companies = []
        for each_result in results:
            companies.append( Company(each_result) )
        return companies

    @classmethod
    def get_one_company(cls,data):
        query = 'SELECT * FROM companies WHERE id =%(server_id)s'
        results = connectToMySQL('company_schema').query_db(query, data)
        return Company(results[0])

    @classmethod
    def update_company(cls,data):
        query = 'UPDATE companies SET `name` = %(server_name)s, `rank` = %(server_rank)s, `location` = %(server_location)s, marketCapitalization = %(server_marketCapitalization)s,news = %(server_news)s WHERE id = %(server_id)s;'
        return connectToMySQL('company_schema').query_db( query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM companies WHERE id = %(server_id)s;'
        return connectToMySQL('company_schema').query_db( query, data)

    @staticmethod
    def validate_new_company(data):
        is_valid = True
        if data['template_name'] == "":
            is_valid = False
            flash("Name should be filled")
        if data['template_rank'] == "":
            is_valid = False
            flash("Rank should be filled")
        else:
            if int(data['template_rank'])<= 0:
                is_valid = False
                flash("Rank should be a number greater than 0")
        if data['template_location'] == "":
            is_valid = False
            flash("Location should be filled")
        if data['template_marketCapitalization'] == "":
            is_valid = False
            flash("Market Capitalization should be filled")
        else:
            if int(data['template_marketCapitalization'])<= 0:
                is_valid = False
                flash("Market Capitalization should be a number greater than 0")
        if data['template_news'] == "":
            is_valid = False
            flash("News should be filled")
        return is_valid


