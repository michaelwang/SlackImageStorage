from dbHandler import DBHandler
import os
import time
import ConfigParser
import shutil
import uuid
class FileHandler(object):
    def __init__(self,num):
        self.db = DBHandler()
        self.machineNumbers = num
        self.count = 0
        self.config = ConfigParser.ConfigParser()
        self.config.read('config.properties')

    def nextMachine(self):
        self.count = self.getTotalFileCount()
        nextIndex = self.count % self.machineNumbers
        return nextIndex

    def parseFileMeta(self,filePath):
        basename = os.path.basename(filePath)
        name,ext = os.path.splitext(basename)
        nextIndex = self.nextMachine()
        currentTimestamp = int(time.time())
        savedPath = self.config.get('Section Folder','folder'+str(nextIndex))
#        savedPath = '/home/michael/1/'
#        mixedFileName = name + '|' + ext + '|' + str(currentTimestamp) + '|' + savedPath
        return name,ext,nextIndex,savedPath

    def getTotalFileCount(self):
        getAllFilesCount = ''' select count(*) from files  '''
        rows = self.db.excute(getAllFilesCount)
        return rows.getresult()[0][0]

    def save(self,path,url):
        fileName,ext,nextIndex,savedPath = self.parseFileMeta(path)
        diskName = str(uuid.uuid1()) + ext
        savedDiskName = savedPath + diskName 
        shutil.move(path,savedDiskName)
        return self.save_to_db(url,ext,fileName,diskName,nextIndex)

    def getTypeByUrl(self,url):
        sql = ''' select file_type from files where from_url = '{url}' '''.format   (
               url = url
             )
        rows = self.db.excute(sql)
        return rows.getresult()[0][0]

    def getTypeByID(self,fileId):
        sql = ''' select file_type from files where id = '{fileId}' '''.format        (
              fileId = fileId
        )
        rows = self.db.excute(sql)
        return rows.getresult()[0][0]

    def getFileByID(self,fileId):
        sql_get_file = """ select physical_name,saved_position from files where id = {fileId} """.format(
             fileId = fileId
        )
        rows = self.db.excute(sql_get_file)
        physical_name = rows.getresult()[0][0]
        saved_position = rows.getresult()[0][1]
        folder = self.config.get('Section Folder','folder' + str(saved_position))
        path = folder  + physical_name
        print 'file path is :' + path
        return open(path,'r')
        

    def save_to_db(self,from_url,file_type,logical_name,physical_name,saved_position):
        sql_insert ="""INSERT INTO files(logical_name,physical_name,file_type,from_url,saved_position) values('{logical_name}','{physical_name}','{file_type}','{from_url}','{saved_position}')""".format(
                          logical_name = logical_name,
                          physical_name = physical_name,
                          file_type = file_type,
                          from_url = from_url  ,
                          saved_position = saved_position
                        )
        self.db.excute(sql_insert)
        sql_id_selector = """ select id from files where from_url = '{from_url}' and logical_name = '{logical_name}' and physical_name = '{physical_name}' and saved_position = '{saved_position}' """.format(
                          logical_name = logical_name,
                          physical_name = physical_name,
                          file_type = file_type,
                          from_url = from_url  ,
                          saved_position = saved_position               
        )
        rows = self.db.excute(sql_id_selector)
        return rows.getresult()[0][0]

