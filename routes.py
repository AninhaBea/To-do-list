from flask import Flask, render_template, request, redirect, session
from main import app
import json
import os

if os.path.exists('tarefas.json'):
    listatarefas = json.load(open('tarefas.json', 'r'))
else:
    listatarefas = []
    json.dump(listatarefas, open('tarefas.json', 'w'))

if os.path.exists('usuarios.json'):
    usuarios = json.load(open('usuarios.json', 'r'))
else:
    usuarios = [
    {'nome': 'admin', 'senha': 'admin', 'tipo': 'admin'},
    {'nome': 'aluno1', 'senha': '123', 'tipo': 'aluno'},
    ]
    json.dump(usuarios, open('usuarios.json', 'w'))

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        for usuario in usuarios:
            if usuario['nome'] == nome and usuario['senha'] == senha:
                user_type = usuario['tipo']
                if user_type == 'admin':
                    session['user_type'] = user_type
                    session['user_name'] = nome
                    return redirect('/admin')
                elif user_type == 'aluno':
                    session['user_type'] = user_type
                    session['user_name'] = nome
                    return redirect('/aluno')
            
        return '''Usuário ou senha incorretos. <button type="button" onclick="window.location.href='/'">Tente novamente</button>'''
    return render_template('login.html')


@app.route('/admin')
def admin():
    if session.get('user_type') != 'admin':
        return redirect('/')
    return render_template('admin.html', nome=session.get('user_name'))


@app.route('/usuarios', methods=['GET', 'POST'])
def gerenciar_usuarios():
    if session.get('user_type') != 'admin':
        return redirect('/')
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        tipo = request.form['tipo']
        usuarios.append({'nome': nome, 'senha': senha, 'tipo': tipo})
        json.dump(usuarios, open('usuarios.json', 'w'))
        return redirect('/usuarios')
    return render_template('usuarios.html', users=usuarios)


@app.route('/tarefas', methods=['GET', 'POST'])
def gerenciar_tarefas():
    if session.get('user_type') != 'admin':
        return redirect('/')
    if request.method == 'POST':
        tarefa = request.form['tarefa']
        responsavel = request.form['responsavel']
        listatarefas.append({'tarefa': tarefa, 'responsavel': responsavel, 'situacao': 'pendente'})
        json.dump(listatarefas, open('tarefas.json', 'w'))
        return redirect('/tarefas')
    return render_template('tarefas.html', tarefas=listatarefas, users=usuarios)


@app.route('/aluno', methods=['GET', 'POST'])
def aluno():
    if session.get('user_type') != 'aluno':
        return redirect('/')
    if request.method == 'POST':
        marcadas = request.form.getlist('tarefa')
        for tarefa in listatarefas:
            if tarefa['responsavel'] == session.get('user_name'):
                if tarefa['tarefa'] in marcadas:
                    tarefa['situacao'] = 'concluida'
                else:
                    tarefa['situacao'] = 'pendente'
        json.dump(listatarefas, open('tarefas.json', 'w'))

    return render_template('aluno.html', nome=session.get('user_name'), tarefas=listatarefas)