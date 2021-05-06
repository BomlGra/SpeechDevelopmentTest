from zipfile import ZipFile
from io import BytesIO
from typing import List, Dict


class Compressor:
    def compress(self, files):
        pass
    

class ZipCompressor(Compressor):
    def compress(self, files: Dict[str, bytearray]) -> bytearray:
        in_memory = BytesIO()
        zf = ZipFile(in_memory, mode="w")
        
        #If you have data in text format that you want to save into the zip as a file
        for name, file in files.items():
            zf.writestr(name, file)
        
        #Close the zip file
        zf.close()

        #Go to beginning
        in_memory.seek(0)
        
        #read the data
        data = in_memory.read()
        
        return data
    
    
# f1 = open('/Users/alpha/Projects/Students/shumak/SpeechDevelopmentTest/storage/files/1/4a81fb4b-5c3d-4eb8-a9b2-b281f23c6cef.wav', 'rb')
# fst = f1.read()
# f1.close()

# f2 = open('/Users/alpha/Projects/Students/shumak/SpeechDevelopmentTest/storage/files/1/ef8888b2-1681-4915-a862-eb227ae21069.wav', 'rb')
# snd = f2.read()
# f2.close()

# compressor: Compressor = ZipCompressor()  
# archive = compressor.compress({
#     'a.wav': fst,
#     'b.wav': snd,
# })

# #You can save it to disk
# with open('audios.zip','wb') as out:
#     out.write(archive)