import os
from bottle import route,run,template,view,request,static_file
import pg
from fileHandler import FileHandler

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!',name=name)

@route('/upload',method='GET')
def upload():
    return template('upload')
    
@route('/upload', method='POST')
def do_upload():
    upload     = request.files.get('upload')
    url = request.forms.get('url')
    content_type =  upload.content_type 
    name, ext = os.path.splitext(upload.filename)
    save_path = '/tmp'
    upload.filename = str(abs(hash(name)))+ ext
    upload.save(save_path,overwrite=True) # appends upload.filename automatically
    fileHandler = FileHandler(5)
    fileId,physicalName = fileHandler.save('/tmp/'+upload.filename ,url)
    return physicalName

@route('/getFileByName/<filename>',method='GET')
def getFileByName(filename):
    fileHandler = FileHandler(5)
    path = fileHandler.getFilePathByDiskName(filename)    
    return static_file(filename,root=path)

if __name__ == '__main__':
   run(host='localhost',port=8080,debug=True,reloader=True)
