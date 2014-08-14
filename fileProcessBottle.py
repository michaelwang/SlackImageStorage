import os
from bottle import route,run,template,view,request
import pg

fileHandler = FileHandler()

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!',name=name)

@route('/upload',method='GET')
def upload():
    return template('upload')
    
@route('/upload', method='POST')
def do_upload():
#    category   = request.forms.get('category')
    upload     = request.files.get('upload')
    url = request.forms.get('url')
    content_type =  upload.content_type
    name, ext = os.path.splitext(upload.filename)
#    if ext not in ('.txt','.png','.jpg','.jpeg'):
#       return 'File extension not allowed.'
    save_path = '/tmp'
    upload.filename = str(abs(hash(name)))+ ext
    upload.save(save_path,overwrite=True) # appends upload.filename automatically
    fileHandler.save('/tmp/'+upload.filename + ext,url)
    return upload.filename

def get_save_path_for_category(category):
    UPLOAD_FOLDER = '/home/michael/workspace/projects/SlackImageStorage/uploads/'
    return UPLOAD_FOLDER

def determineMachine(fileId):
    numberOfMachines = 5 ;
    position = fileId % numberOfMachines
    return position

def update_file_position(fileID,position):
    sql_update_position = "UPDATE files SET saved_position = '%s' WHERE id = %d"
    conn = get_db_connection()
    conn.query(sql_update_position % (position,fileID))

def get_db_connection():
    try:
         conn = pg.connect(dbname = 'filesCenter', host = 'localhost', user = 'postgres', passwd = '123123')
    except Exception, e:
         print e.args[0]
         return    
    return conn
    
def save_to_db(url,content_type,logical_name,physical_name):
    conn = get_db_connection()    
    sql_insert ="""INSERT INTO files(logical_name,physical_name,file_type,from_url) values('%s','%s','%s','%s')"""
    conn.query(sql_insert % (logical_name,physical_name,content_type,url))
    sql_id_select = """SELECT id FROM files WHERE logical_name = '%s' and physical_name = '%s' and file_type = '%s' and from_url = '%s' """
    rows = conn.query(sql_id_select % (logical_name,physical_name,content_type,url)).dictresult()
    return rows[0]['id']

@route('/getFileByName/<filename>')
def getFileByName():
    return filename
    

run(host='localhost',port=8080,debug=True,reloader=True)
