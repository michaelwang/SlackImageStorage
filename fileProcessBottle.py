import os
from bottle import route,run,template,view,request

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!',name=name)

@route('/upload',method='GET')
def upload():
    return template('upload')
    
@route('/upload', method='POST')
def do_upload():
    category   = request.forms.get('category')
    upload     = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.txt','.png','.jpg','.jpeg'):
       return 'File extension not allowed.'
    save_path = get_save_path_for_category(category)
    upload.save(save_path) # appends upload.filename automatically
    return 'OK'

def get_save_path_for_category(category):
    UPLOAD_FOLDER = '/home/michael/workspace/projects/SlackImageStorage/uploads/'
    return UPLOAD_FOLDER

run(host='localhost',port=8080,debug=True,reloader=True)
