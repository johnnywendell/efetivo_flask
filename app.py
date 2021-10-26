from flask import Flask, render_template, make_response, request, redirect, url_for
from flask_restful import Api, Resource
from models import Pacotes

app = Flask(__name__, static_url_path='/static')
api = Api(app)

# DEF *****************************

# VIEWS ***************************
class Pacote(Resource):
    def get(self):
        pacote = Pacotes.query.all()
        pacotes = [{'id':i.id, 'nome':i.nome} for i in pacote]
        return make_response(render_template('main.html', pacotes=pacotes))

class Con_pacote(Resource):
    def get(self, pacote_id):
        pacote = Pacotes.query.filter_by(id=pacote_id).first()
        return make_response(render_template('efetivo.html', pacote=pacote))
class Create_pacote(Resource):
    def post(self):
        nome = request.form['nome']
        pacote = Pacotes(nome=nome)
        pacote.save()
    def get(self):
        return make_response(render_template('create.html'))
class Edit_pacote(Resource):
    def post(self, pacote_id):
        pacote = Pacotes.query.filter_by(id=pacote_id).first()
        pacote.nome = request.form['title']
        pacote.save()
        return redirect(url_for('pacote'))
    def get(self, pacote_id):
        pacote = Pacotes.query.filter_by(id=pacote_id).first()
        return make_response(render_template('edit.html', pacote=pacote))
class Delete_pacote(Resource):
    def post(self, pacote_id):
        pacote = Pacotes.query.filter_by(id=pacote_id).first()
        pacote.delete()
        return redirect(url_for('pacote'))

# URL PATTERNS *********************

api.add_resource(Pacote, '/pacote/')
api.add_resource(Con_pacote, '/<int:pacote_id>')
api.add_resource(Create_pacote, '/create_pacote')
api.add_resource(Edit_pacote, '/<int:pacote_id>/edit')
api.add_resource(Delete_pacote, '/<int:pacote_id>/delete')

if __name__ == '__main__':
    app.run(debug=True)