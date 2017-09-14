# -*- coding: utf-8 -*-
import Youtuyun
from os import path
from jieba_call import cut_search
from jieba import load_userdict
import codecs
from dict import forbidden_list

def ocr_censor(image_path, data_type = 0):
    appid = '10093167'
    secret_id = 'AKIDxnSxMaYT7Zs1xhBMUQDoCON990f5NwjL'
    secret_key = 'azzqVy5JyXvLp5DUg1hEduywmQxzxvmp'
    userid = 'liang.zixuan'
    end_point = Youtuyun.conf.API_YOUTU_END_POINT
    youtu = Youtuyun.YouTu(appid, secret_id, secret_key, userid, end_point)
    result = youtu.generalocr(image_path, data_type = data_type)
    words = []
    #dict_dir = '/home/zixuan/word_censor/forbidden_list'
    #forbidden_list = codecs.open(dict_dir, 'r', 'utf-8').read().splitlines()
    #usr_dict='/home/zixuan/word_censor/dict.txt'
    #load_userdict(usr_dict)

    if result["errormsg"] == 'OK':

        for i in range(0, len(result['items'])):
            data=result['items'][i]['itemstring']
            data = data.encode('ISO-8859-1').decode('utf-8')
            words += ''.join(data)

        words = ''.join(words)
        words = cut_search(words)
        words = words.split('/')
        #print(words)

        if words==['']:
            return 'none'

        #dict_dir = '/home/zixuan/word_censor/forbidden_list'
        #forbidden_list = codecs.open(dict_dir, 'r', 'utf-8').read().splitlines()

        for word in words:
            if word in forbidden_list:
                #print(word)
                #print('contain forbidden word %s' % word)
                return 'vulgar'

    else:
        return 'error'


if __name__ == "__main__":
    image_path='/home/zixuan/image_censor/img_text/ocr1.jpeg'
    print(ocr_censor(image_path))
    image_path='/home/zixuan/image_censor/img_text/ocr2.jpeg'
    print(ocr_censor(image_path))
    image_path='/home/zixuan/image_censor/img_text/ocr3.jpeg'
    print(ocr_censor(image_path))
    image_path='/home/zixuan/image_censor/img_text/ocr4.jpg'
    print(ocr_censor(image_path))
