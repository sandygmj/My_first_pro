import requests

def detect_face(image_url,api_key="B2ngMpctNs9KD4Z9AGemrocN_5SRa",api_secret="SXAMkNk7xa4BNe7BJz8SG0hqfD-nisSG",image_url,return_landmark=1,return_attributes=1):
	url = "https://api-cn.faceplusplus.com/facepp/v3/detect"
	params = {
	"api_key":api_key,
	"api_secret":api_secret,
	"image_url":image_url,
	"return_landmark":return_landmark,
	"return_attributes":return_attributes
	}
	r = requests.post(url=url,params=params)
	return r