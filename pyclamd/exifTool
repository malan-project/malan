

import subprocess
input_file = "C:\\test\\test.png" #input 파일 경로


#exif 로 메타데이터를 추출하는 함수
def getExif(input_file):
    exe = "exiftool"
    output=[]
    process = subprocess.Popen([exe,input_file],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    
    for doutput in process.stdout:
        output.insert(1,doutput.decode('utf-8'))
    
    return output

#test print
out = getExif(input_file)
for i in out:
    print(i)







