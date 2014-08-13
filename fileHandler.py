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
        self.save_to_db(url,ext,fileName,diskName,nextIndex)
        return diskName
   

    def save_to_db(self,from_url,file_type,logical_name,physical_name,saved_position):
        conn = self.db.get_db_connection()    
        sql_insert ="""INSERT INTO files(logical_name,physical_name,file_type,from_url,saved_position) values('{logical_name}','{physical_name}','{file_type}','{from_url}','{saved_position}')""".format(
                          logical_name = logical_name,
                          physical_name = physical_name,
                          file_type = file_type,
                          from_url = from_url  ,
                          saved_position = saved_position
                        )
        self.db.excute(sql_insert)
        return 

