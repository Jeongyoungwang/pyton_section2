#urlopen
import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')#아톰에서 한글 출력 할려면 필수 코드

imgUrl ="http://www.yonhapnewstv.co.kr/contents/mpic/YH/2017/12/07/MYH20171207015500038.jpg"
htmlURL ="http://google.com"

savePath1 ="c:/test2.jpg"
savePath2 ="c:/index2.html"

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlURL).read()

saveFile1 = open(savePath1, 'wb')
saveFile1.write(f)
saveFile1.close()

with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)

print("다운로드 완료!")
