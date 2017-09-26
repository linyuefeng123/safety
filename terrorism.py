import Youtuyun

def image_terrorism(image_path, data_type = 0):
	appid = '10093167'
	secret_id = 'AKIDxnSxMaYT7Zs1xhBMUQDoCON990f5NwjL'
	secret_key = 'azzqVy5JyXvLp5DUg1hEduywmQxzxvmp'
	userid = 'liang.zixuan'
	end_point = Youtuyun.conf.API_YOUTU_END_POINT
	youtu = Youtuyun.YouTu(appid, secret_id, secret_key, userid, end_point)

	result = youtu.imageterrorism(image_path, data_type = data_type)

	# RETURN RESULT EXAMPLE
	# {
	#  u'errorcode': 0, 
	#  u'errormsg': u'OK', 
	#  u'faces': [], 
	#  u'feas': {u'name': u'global_pool', u'feature': u''}, 
	#  u'tags': 
	#  	[{u'tag_name': u'terrorists', u'tag_confidence_f': 1.563651153446699e-06, u'tag_confidence': 0}, 
	#  	 {u'tag_name': u'knife', u'tag_confidence_f': 0.016784466803073883, u'tag_confidence': 1}, 
	#  	 {u'tag_name': u'guns', u'tag_confidence_f': 1.0, u'tag_confidence': 100}, 
	#  	 {u'tag_name': u'blood', u'tag_confidence_f': 2.1156195373350783e-07, u'tag_confidence': 0}, 
	#  	 {u'tag_name': u'fire', u'tag_confidence_f': 6.669731374131516e-05, u'tag_confidence': 0}, 
	#  	 {u'tag_name': u'flag', u'tag_confidence_f': 2.741180082921346e-07, u'tag_confidence': 0}, 
	#  	 {u'tag_name': u'crowd', u'tag_confidence_f': 0.1500011831521988, u'tag_confidence': 15}, 
	#  	 {u'tag_name': u'other', u'tag_confidence_f': 0.027535710483789444, u'tag_confidence': 2}]
	#  }

	if result['errormsg'] == 'OK':
		tags = result['tags']
		tag = max(tags, key = lambda x : x['tag_confidence'])
		return(tag['tag_name'], tag['tag_confidence'])
	else:
		return 'error', 'error'

if __name__ == "__main__":
	url = 'https://gss0.bdstatic.com/-4o3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268%3Bg%3D0/sign=c8f8b21fd588d43ff0a996f44525b526/359b033b5bb5c9ea21351689d639b6003bf3b391.jpg'
	print(image_terrorism(url, data_type = 1)[0])
	url = 'https://gss2.bdstatic.com/9fo3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268%3Bg%3D0/sign=b3bc759f293fb80e0cd166d10eea4813/b8014a90f603738d1b22758cbb1bb051f819ec30.jpg'
	print(image_terrorism(url, data_type = 1)[0])
	url = 'https://gss3.bdstatic.com/7Po3dSag_xI4khGkpoWK1HF6hhy/baike/s%3D220/sign=3e927d96befd5266a32b3b169b199799/3812b31bb051f81939417237d2b44aed2e73e763.jpg'
	print(image_terrorism(url, data_type = 1)[0])
