import os
import datetime

def writeFile(path, file_name, data):
    if os.path.isdir(path) != True:
        os.makedirs(path)
    w = open(path + file_name,'a', encoding='utf-8')
    w.write(data+'\n')
    w.close()


def make_log(type, desc, detail=False):
    basePath = './log/'
    date = datetime.datetime.now().replace(microsecond=0)
    data = '[' + type + '] ' + str(date) + ' ' + desc
    strDate = str(date.year)+('0'+str(date.month))[-2:]+('0'+str(date.day))[-2:]

    if detail != True:
        path = basePath
        file_name = strDate +'.log'
        writeFile(path, file_name, data)

    path_detail = basePath + 'detail/'
    file_name_detail = strDate + '.log'
    writeFile(path_detail, file_name_detail, data)