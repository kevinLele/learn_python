# coding:utf-8

from mp3getter.utils.BaseUtils import log
import mp3getter.utils.DBUtils as DBUtils
import mp3getter.utils.WebUtils as WebUtils
import mp3getter.utils.FileUtils as FileUtils

log(u"开始下载。。。")
DBUtils.init_connection("audio.db")
cursor = DBUtils.search("select sn,id,name,extended,path from audio where is_download=0")
dir_path = "./download/"
FileUtils.create_dir(dir_path)

for row in cursor:
    sn = row[0]
    oid = row[1]
    name = row[2]
    extended = row[3]
    url = row[4]
    file_path = dir_path + name + extended

    try:
        WebUtils.download_file_form_url(url, file_path)

        DBUtils.execute_sql("update audio set is_download=1 where id=? ", (oid, ))
        print file_path + " is downloaded! url: " + url
    except Exception, msg:
        print msg


