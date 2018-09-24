import cognitive_face as CF

def start_monitoring():
	# Replace <Subscription Key> with your valid subscription key.
	#subscription_key = "fd0e389340064d0695478b520580b4fd"
	subscription_key = "96de259aff8947168a8cda4c74d75dc4"
	assert subscription_key

	face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'
	headers = {'Ocp-Apim-Subscription-Key': subscription_key}

	# dad
	image_url_1 = 'https://ksassets.timeincuk.net/wp/uploads/sites/46/2017/07/most-beautiful-men-in-the-world.jpg'
	# mum
	image_url_2 = 'https://cdn-images-1.medium.com/max/1200/1*fx1XwPtWsy3uWAeGgcc0iA.jpeg'
	# kid
	image_url_3 = 'https://i.pinimg.com/736x/d8/3a/8e/d83a8e2fd6651055c4b656ae8b284342--american-girl-hairstyles-girls-braided-hairstyles.jpg'
	# robber
	image_url_4 = 'http://rmtracking.com/wp-content/uploads/2016/12/iStock_000014773673XSmall.jpg'

	# verify similarity index
	CF.Key.set(subscription_key)
	base_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
	CF.BaseUrl.set(base_url)
	img_urls = [image_url_1, image_url_2, image_url_3]  # create person group
	robber_url = [image_url_4]
	#3 family members faces
	faces = [CF.face.detect(img_url) for img_url in img_urls]
	#robber face
	face_robber = [CF.face.detect(img_url) for img_url in robber_url]

	similarity_with_dad = CF.face.verify(faces[0][0]['faceId'], face_robber[0][0]['faceId'])
	similarity_with_mum = CF.face.verify(faces[1][0]['faceId'], face_robber[0][0]['faceId'])
	similarity_with_kid = CF.face.verify(faces[2][0]['faceId'], face_robber[0][0]['faceId'])
	if (similarity_with_dad['isIdentical'] == False and similarity_with_mum['isIdentical'] == False and similarity_with_kid['isIdentical'] == False):
	    return ("ALERT ALERT, There is a potential intruder!", image_url_4)
	else:
		return ("Nothing to be worried about", "Have a good day ahead")
























































