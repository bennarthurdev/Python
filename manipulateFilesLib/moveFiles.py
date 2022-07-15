import os
def moveFiles(source , target , typeOfFile ):
    '''
    receives a string who contains the path of source folder

    receives a string who contains the folder will should receive files

    receive a type who should be 'photo', 'video' or 'documents'
    '''
    source_folder = r + source + '\\'
    target_folder = r + target + '\\'
    for path,dir,files in os.walk(source_folder):
        for fileName in files:
        # move fotos to specif folder
            if(typeOfFile == 'photo')
                if (fileName[-3:] == 'jpg' or fileName[-3:] == 'png'):                
                    os.rename(path + '\\' + fileName, target_folder + fileName)
            elif(typeOfFile == 'video'):
                if(fileName[-3:] == 'mov' or fileName[-3:] == 'mp4'or fileName[-3:] == 'm4p' or fileName[-3:] == 'm4v'):
                    os.rename(path + '\\' + fileName, target_folder + fileName)
            elif(typeOfFile == 'documents')
                 if(fileName[-4:] == 'docx' or fileName[-3:] == 'doc'):
                    os.rename(path + '\\' + fileName, target_folder + fileName)

