import subprocess

cmd = 'python 1_PptxToPdf.py'
p = subprocess.Popen(cmd,shell=True)
out, err = p.communicate()
print(err)
print(out)

cmd = 'python 2_PdfToImages.py'
p = subprocess.Popen(cmd,shell=True)
out, err = p.communicate()
print(err)
print(out)

cmd = 'python 3_ImagesToVideo.py'
p = subprocess.Popen(cmd,shell=True)
out, err = p.communicate()
print(err)
print(out)

cmd = 'python 4_TextToMp3(IBM).py'
p = subprocess.Popen(cmd,shell=True)
out, err = p.communicate()
print(err)
print(out)

cmd = 'python 5_MergeVideoAndMp3.py'
p = subprocess.Popen(cmd,shell=True)
out, err = p.communicate()
print(err)
print(out)

cmd = 'python 6_ConvertMp3ToSrt.py'
p = subprocess.Popen(cmd,shell=True)
out, err = p.communicate()
print(err)
print(out)


print("\n--->All python files are executed succesfully<---\n")