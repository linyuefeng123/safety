import Youtuyun

def image_politician(image_path, data_type = 0):
	appid = '10093167'
	secret_id = 'AKIDxnSxMaYT7Zs1xhBMUQDoCON990f5NwjL'
	secret_key = 'azzqVy5JyXvLp5DUg1hEduywmQxzxvmp'
	userid = 'liang.zixuan'
	end_point = Youtuyun.conf.API_YOUTU_END_POINT
	youtu = Youtuyun.YouTu(appid, secret_id, secret_key, userid, end_point)

	result = youtu.FaceIdentify('politician', image_path, data_type = data_type)

	# RETURN RESULT EXAMPLE
	# {u'group_size': 101, 
	#  u'errormsg': u'OK', 
	#  u'session_id': u'', 
	#  u'errorcode': 0, 
	#  u'candidates': 
	#  	[{u'person_id': u'jiang_zemin', u'face_id': u'2168354003014947282', u'tag': u'', u'confidence': 98.0}, 
	#  	 {u'person_id': u'hua_jianmin', u'face_id': u'2168368314953267948', u'tag': u'', u'confidence': 89.0}, 
	#  	 {u'person_id': u'yan_junqi', u'face_id': u'2168312923867347596', u'tag': u'', u'confidence': 79.0}, 
	#  	 {u'person_id': u'li_ruihuan', u'face_id': u'2168387477346220589', u'tag': u'', u'confidence': 78.0}, 
	#  	 {u'person_id': u'qiao_shi', u'face_id': u'2168389744166211848', u'tag': u'', u'confidence': 78.0}], 
	#  u'time_ms': 135}


	if result['errormsg'] == 'OK':
		if result['candidates'][0]['confidence'] > 80:
			return result['candidates'][0]['person_id']
		else:
			return 'Not a Chinese Zhongnanhai Politician'
	else:
		return 'Error or There is no person face in image'

def add_politician(image_path, person_id, person_name, group_ids = ['politician'], data_type = 0):
	appid = '10093167'
	secret_id = 'AKIDxnSxMaYT7Zs1xhBMUQDoCON990f5NwjL'
	secret_key = 'azzqVy5JyXvLp5DUg1hEduywmQxzxvmp'
	userid = 'liang.zixuan'
	end_point = Youtuyun.conf.API_YOUTU_END_POINT
	youtu = Youtuyun.YouTu(appid, secret_id, secret_key, userid, end_point)

	youtu.NewPerson(person_id, image_path, group_ids, person_name, data_type = data_type)

if __name__ == "__main__":
	url = 'https://gss1.bdstatic.com/9vo3dSag_xI4khGkpoWK1HF6hhy/baike/s%3D220/sign=0bc608fdc895d143de76e32143f18296/9f2f070828381f30a0456957a9014c086f06f0f4.jpg'
	print(image_politician(url, data_type = 1))
	url = 'https://gss3.bdstatic.com/-Po3dSag_xI4khGkpoWK1HF6hhy/baike/s%3D220/sign=4e12161e9358d109c0e3aeb0e159ccd0/a5c27d1ed21b0ef48893ed3edcc451da81cb3e52.jpg'
	print(image_politician(url, data_type = 1))
	url = 'http://img1.cache.netease.com/catchpic/D/DA/DA13F74FF669F1B188BABFAABCC243FB.jpg'
	print(image_politician(url, data_type = 1))
