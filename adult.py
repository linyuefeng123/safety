import Youtuyun

def image_adult(image_path, data_type = 0):
	appid = '10093167'
	secret_id = 'AKIDxnSxMaYT7Zs1xhBMUQDoCON990f5NwjL'
	secret_key = 'azzqVy5JyXvLp5DUg1hEduywmQxzxvmp'
	userid = 'liang.zixuan'
	end_point = Youtuyun.conf.API_YOUTU_END_POINT
	youtu = Youtuyun.YouTu(appid, secret_id, secret_key, userid, end_point)

	result = youtu.imageporn(image_path, data_type = data_type)

	# RETURN RESULT EXAMPLE
	# {u'errorcode': 0, 
	# u'errormsg': u'OK', 
	# u'faces': [], 
	# u'tags': 
	# 	[{u'tag_name': u'hot', u'tag_confidence_f': 0.9977893829345703, u'tag_confidence': 99}, 
	# 	 {u'tag_name': u'normal', u'tag_confidence_f': 1.687981784925796e-05, u'tag_confidence': 0}, 
	# 	 {u'tag_name': u'porn', u'tag_confidence_f': 0.0021937687415629625, u'tag_confidence': 0}, 
	# 	 {u'tag_name': u'normal_hot_porn', u'tag_confidence_f': 0.26867473125457764, u'tag_confidence': 26}]
	# }


	if result['errormsg'] == 'OK':
		if result['tags'][2]['tag_confidence'] > 80:
			return 'porn', result['tags'][2]['tag_confidence']
		elif result['tags'][0]['tag_confidence'] > 80:
			return 'hot', result['tags'][0]['tag_confidence']
		elif result['tags'][1]['tag_confidence'] > 80:
			return 'normal', result['tags'][1]['tag_confidence']
		else:
			res = max(result['tags'], key = lambda x : x['tag_confidence'])
			return 'not sure but possibly ' + res['tag_name'], res['tag_confidence']
	else:
		return 'error', 'error'

if __name__ == "__main__":
	url = 'https://raw.githubusercontent.com/ZixuanLiang/resnet50_inappropriate_content_detect/master/test_images_adult/porn/original_10731801.jpg'
	print(image_adult(url, data_type = 1))
	url = 'https://raw.githubusercontent.com/ZixuanLiang/resnet50_inappropriate_content_detect/master/test_images_adult/porn/original_10731581.jpg'
	print(image_adult(url, data_type = 1))
	url = 'https://raw.githubusercontent.com/ZixuanLiang/resnet50_inappropriate_content_detect/master/test_images_adult/porn/original_1020831.jpg'
	print(image_adult(url, data_type = 1))
	url = 'https://raw.githubusercontent.com/ZixuanLiang/resnet50_inappropriate_content_detect/master/test_images_adult/porn/original_1020824.jpg'
	print(image_adult(url, data_type = 1))
