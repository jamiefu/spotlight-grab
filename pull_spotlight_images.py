import os
import shutil

#general spotlight path:
#"%LocalAppData%\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"
#copy-paste into File Explorer to obtain actual Spotlight path
spotlight_path = "C:/Users/Jamie/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets"
#destination location
folder = 'C:/Users/Jamie/Pictures/Windows Spotlight/'

for root, dirs, filenames in os.walk(spotlight_path):
    for filename in filenames:
        filename = os.path.join(root, filename)
        stats = os.stat(filename)
        if stats.st_size > 100000:
            shutil.copy2(filename, folder)

for root, dirs, filenames in os.walk(folder):
    for filename in filenames:           
        filename = os.path.join(root, filename)
        if os.path.exists(filename + '.jpg'):
            os.remove(filename)
        elif not filename.endswith('.jpg'):
            os.rename(filename, filename + '.jpg')
        # consider using PIL Image to check jpg dimensions and delete accordingly
        
