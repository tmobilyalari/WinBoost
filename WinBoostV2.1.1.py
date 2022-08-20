import os
import shutil

print('WinBoost V2.1.1 by OfluTEAM')
input('İşlemi başlatmak için <Enter> tuşuna basın ve işlemin bitmesini bekleyin.')
    
klasor = 'C:/Users/'+os.getlogin()+'/AppData/Local/Temp'
klasor2 = 'C:/Windows/Temp'

sayacdosya = 0
sayacklasor = 0
sayacdosya2 = 0
sayacklasor2 = 0

for the_file in os.listdir(klasor):
    dosyayolu = os.path.join(klasor, the_file)
    indexNo = dosyayolu.find('\\')
    itemName = dosyayolu[indexNo+1:]
    try:
        if os.path.isfile(dosyayolu):
            os.unlink(dosyayolu)
            print( '%s dosyası silindi.' % itemName )
            sayacdosya = sayacdosya + 1

        elif os.path.isdir(dosyayolu):
            if dosyayolu.__contains__('chocolatey'):  continue
            shutil.rmtree(dosyayolu)
            print( '%s klasörü silindi.' % itemName )
            sayacklasor = sayacklasor + 1

    except Exception as e:
        print('Hata Erişim Engelli veya Bozuk Dosya/Klasör: %s' % itemName )

for the_file2 in os.listdir(klasor2):
    dosyayolu2 = os.path.join(klasor2, the_file2)
    indexNo2 = dosyayolu2.find('\\')
    itemName2 = dosyayolu2[indexNo2+1:]
    try:
        if os.path.isfile(dosyayolu2):
            os.unlink(dosyayolu2)
            print( '%s dosyası silindi.' % itemName2 )
            sayacdosya2 = sayacdosya2 + 1

        elif os.path.isdir(dosyayolu2):
            if dosyayolu2.__contains__('chocolatey'):  continue
            shutil.rmtree(dosyayolu2)
            print( '%s klasörü silindi.' % itemName2 )
            sayacklasor2 = sayacklasor2 + 1

    except Exception as e:
        print('Hata Erişim Engelli veya Bozuk Dosya/Klasör: %s' % itemName2 )

sayacklasor3 = sayacklasor2 + sayacklasor
sayacdosya3 = sayacdosya2 + sayacdosya

print('Toplam '+str(sayacdosya3)+' adet dosya ve '+ str(sayacklasor3)+' adet klasör bulundu ve silindi.')
input('Çıkmak için <Enter> tuşuna basın.')
