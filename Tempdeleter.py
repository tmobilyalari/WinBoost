import os
import shutil

print('WinBoost by OfluTEAM')
input('İşlemi başlatmak için <Enter> tuşuna basın ve işlemin bitmesini bekleyin.')
    
folder = 'C:/Users/'+os.getlogin()+'/AppData/Local/Temp'

deleteFileCount = 0
deleteFolderCount = 0

for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    indexNo = file_path.find('\\')
    itemName = file_path[indexNo+1:]
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
            print( '%s Adet dosya silindi.' % itemName )
            deleteFileCount = deleteFileCount + 1

        elif os.path.isdir(file_path):
            if file_path.__contains__('chocolatey'):  continue
            shutil.rmtree(file_path)
            print( '%s Adet klasör silindi.' % itemName )
            deleteFolderCount = deleteFolderCount + 1

    except Exception as e:
        print('Hata Erişim Engelli Dosya: %s' % itemName )

print('Toplam '+str(deleteFileCount)+' adet dosya ve '+ str(deleteFolderCount)+' adet klasör bulundu ve silindi.')
input('Çıkmak için <Enter> tuşuna basın.')