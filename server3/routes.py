# coding: utf-8

from utils import log
from models import Message,User



message_list = []

def route_register(request):
    header = 'HTTP/1.x 200 OK\r\nContent-Type: text/html\r\n'
    if request.method == 'POST':
        form = request.form()
        u = User(form)
        log(u)
        
        if u.validate_register():
            u.save()
            result = 'sucessful'
        else:
            result = 'username or password is wrong'
    else:
        result = ''
    body = template('register.html')
    body = body.replace('{{result}}',result)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')    


def route_login(request):
    header = 'HTTP/1.x 200 OK\r\nContent-Type: text/html\r\n'
    if request.method == 'POST':
        form = request.form()
        u = User(form)
        log(u)
        if u.validate_login():
            result = 'sucessful'
        else:
            result = 'username or password is wrong'
    else:
        result = ''
    body = template('login.html')
    body = body.replace('{{result}}',result)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')

def route_index(request):
    header = 'HTTP/1.x 210 VERY OK\r\nContent-Type: text/html\r\n'
    body = template('index.html')
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def route_message(request):
    log('method:', request.method)
    if request.method == 'POST':
        msg = Message()
        form = request.form()
        log('post', form)
        msg.author = form.get('author', '')
        msg.message = form.get('message', '')
        message_list.append(msg)
    header = 'HTTP/1.x 200 OK\r\nContent-Type: text/html\r\n'
    body = template('basic.html')
    msgs = '<br>'.join([str(m) for m in message_list])
    body = body.replace('{{messages}}', msgs)
    log(msgs)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


route_dict = {
        '/': route_index,
        '/login':route_login,
        '/register':route_register,
        '/messages': route_message,
        
    }    

def template(name):
    p = 'templates/' + name
    with open(p, 'r', encoding='utf-8') as f:
        return f.read()

    
