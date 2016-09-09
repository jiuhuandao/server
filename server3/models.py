from utils import log
import json

def save(data,path):
    s = json.dumps(data,indent=2,ensure_ascii=False)
    with open(path,'w+',encoding='utf-8') as f:
        f.write(s)

def load(path):
    with open(path,'r',encoding='utf-8') as f:
        s = f.read()
        s = json.loads(s)
        log('load',s)
        return s


class User(object):
    def __init__(self,form):
        self.username = form.get('username','')
        self.password = form.get('password','')

    def save(self):
        log('save start...')
        l = load('User.txt')
        log('load',l)
        l = [User(i) for i in l]
        l.append(self)
        log(l)
        l = [i.__dict__ for i in l]
        log('debug save',l)
        save(l,'User.txt')

    def validate_login(self):
        if len(self.username) > 2 and len(self.password) > 2:
            return True
        else:
            return False

    def validate_register(self):
        if len(self.username) > 2 and len(self.password) > 2:
            return True
        else:
            return False

    def __repr__(self):
        classname = self.__class__.__name__
        properties = ['{}:{}'.format(k,v) for k,v in self.__dict__.items()]
        s = '\n'.join(properties)
        return '{}\n{}'.format(classname,s)


class Message(object):
    def __init__(self):
        self.message = ''
        self.author = ''

    def __repr__(self):
        return '{}: {}'.format(self.author, self.message)

