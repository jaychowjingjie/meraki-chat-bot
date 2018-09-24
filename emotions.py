import requests
# If you are using a Jupyter notebook, uncomment the following line.
#%matplotlib inline
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import patches
from io import BytesIO
import http.client, urllib.request, urllib.parse, urllib.error, base64

# Replace <Subscription Key> with your valid subscription key.
subscription_key = "96de259aff8947168a8cda4c74d75dc4"
#subscription_key = "fd0e389340064d0695478b520580b4fd"
assert subscription_key

w, no_of_people = 6, 10
Matrix = [[0 for x in range(w)] for y in range(no_of_people)]
counter=0
time=[915,933,1020,1045,1200,1234,1509,1601,1800,1928]

# You must use the same region in your REST call as you used to get your
# subscription keys. For example, if you got your subscription keys from
# westus, replace "westcentralus" in the URI below with "westus".
#
# Free trial subscription keys are generated in the westcentralus region.
# If you use a free trial subscription key, you shouldn't need to change
# this region.
face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'
headers = {'Ocp-Apim-Subscription-Key': subscription_key}

# Set image_url to the URL of an image that you want to analyze.
image_url_1 = 'https://media.gq.com/photos/56436afea3bd50211a99c42d/master/w_800/obama-gq-1215-05.jpg'

image_url_2 = 'https://media.gq.com/photos/56436afea3bd50211a99c42d/master/w_800/obama-gq-1215-05.jpg'

image_url_3 = 'http://www.familycounselling.com/wp-content/uploads/2015/05/Angry-man.jpg'

image_url_4 = 'http://www.pngall.com/wp-content/uploads/2016/04/Happy-Person-Free-Download-PNG.png'

image_url_5 = 'https://www.blogexpress.in/wp-content/uploads/2018/04/happy-person.jpg'

image_url_6 = 'http://menn.is/wp-content/uploads/2018/05/Man-surprised.jpg'

image_url_7 = 'https://s1.r29static.com//bin/entry/605/0,0,460,552/720x864,80/1368215/image.jpg'

image_url_8 = 'https://i.imgflip.com/bd4jb.jpg'

image_url_9 = 'https://thumbs.dreamstime.com/b/close-up-headshot-angry-face-man-straight-asian-light-beard-86586901.jpg'

image_url_10 = 'https://www.askideas.com/media/48/Angry-Face-Donald-Trump-Funny-Face-Picture.jpg'

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,' +
    'emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'
}

#get the first id
data = {'url': image_url_1}
response = requests.post(face_api_url, params=params, headers=headers, json=data)
faces = response.json()
image = Image.open(BytesIO(requests.get(image_url_1).content))
plt.figure(figsize=(8, 8))
ax = plt.imshow(image, alpha=0.6)
for face in faces:
    print("face is ", face)
    firstid = str(face["faceId"])
    fa = face["faceAttributes"]
    smile = fa["smile"]
    anger = fa["emotion"]["anger"]
    sadness = fa["emotion"]["sadness"]
    neutral = fa["emotion"]["neutral"]
    Matrix[counter][0]=counter+1
    Matrix[counter][1]=time[counter]
    Matrix[counter][2]=smile
    Matrix[counter][3]=anger
    Matrix[counter][4]=sadness
    Matrix[counter][5]=neutral
    counter=counter+1

data2 = {'url': image_url_2}
response = requests.post(face_api_url, params=params, headers=headers, json=data2)
print(response)
faces2 = response.json()
image = Image.open(BytesIO(requests.get(image_url_2).content))
plt.figure(figsize=(8, 8))
ax = plt.imshow(image, alpha=0.6)
for face in faces2:
    firstid = str(face["faceId"])
    fa = face["faceAttributes"]
    smile = fa["smile"]
    anger = fa["emotion"]["anger"]
    sadness = fa["emotion"]["sadness"]
    neutral = fa["emotion"]["neutral"]
    Matrix[counter][0]=counter+1
    Matrix[counter][1]=time[counter]
    Matrix[counter][2]=smile
    Matrix[counter][3]=anger
    Matrix[counter][4]=sadness
    Matrix[counter][5]=neutral
    counter=counter+1

data = {'url': image_url_3}
response = requests.post(face_api_url, params=params, headers=headers, json=data)
faces = response.json()
image = Image.open(BytesIO(requests.get(image_url_3).content))
plt.figure(figsize=(8, 8))
ax = plt.imshow(image, alpha=0.6)
for face in faces:
    firstid = str(face["faceId"])
    fa = face["faceAttributes"]
    smile = fa["smile"]
    anger = fa["emotion"]["anger"]
    sadness = fa["emotion"]["sadness"]
    neutral = fa["emotion"]["neutral"]
    Matrix[counter][0]=counter+1
    Matrix[counter][1]=time[counter]
    Matrix[counter][2]=smile
    Matrix[counter][3]=anger
    Matrix[counter][4]=sadness
    Matrix[counter][5]=neutral
    counter=counter+1

data = {'url': image_url_4}
response = requests.post(face_api_url, params=params, headers=headers, json=data)
faces = response.json()
image = Image.open(BytesIO(requests.get(image_url_4).content))
plt.figure(figsize=(8, 8))
ax = plt.imshow(image, alpha=0.6)
for face in faces:
    firstid = str(face["faceId"])
    fa = face["faceAttributes"]
    smile = fa["smile"]
    anger = fa["emotion"]["anger"]
    sadness = fa["emotion"]["sadness"]
    neutral = fa["emotion"]["neutral"]
    Matrix[counter][0]=counter+1
    Matrix[counter][1]=time[counter]
    Matrix[counter][2]=smile
    Matrix[counter][3]=anger
    Matrix[counter][4]=sadness
    Matrix[counter][5]=neutral
    counter=counter+1

data = {'url': image_url_5}
response = requests.post(face_api_url, params=params, headers=headers, json=data)
faces = response.json()
image = Image.open(BytesIO(requests.get(image_url_5).content))
plt.figure(figsize=(8, 8))
ax = plt.imshow(image, alpha=0.6)
for face in faces:
    firstid = str(face["faceId"])
    fa = face["faceAttributes"]
    smile = fa["smile"]
    anger = fa["emotion"]["anger"]
    sadness = fa["emotion"]["sadness"]
    neutral = fa["emotion"]["neutral"]
    Matrix[counter][0]=counter+1
    Matrix[counter][1]=time[counter]
    Matrix[counter][2]=smile
    Matrix[counter][3]=anger
    Matrix[counter][4]=sadness
    Matrix[counter][5]=neutral
    counter=counter+1

data = {'url': image_url_6}
response = requests.post(face_api_url, params=params, headers=headers, json=data)
faces = response.json()
image = Image.open(BytesIO(requests.get(image_url_6).content))
plt.figure(figsize=(8, 8))
ax = plt.imshow(image, alpha=0.6)
for face in faces:
    firstid = str(face["faceId"])
    fa = face["faceAttributes"]
    smile = fa["smile"]
    anger = fa["emotion"]["anger"]
    sadness = fa["emotion"]["sadness"]
    neutral = fa["emotion"]["neutral"]
    Matrix[counter][0]=counter+1
    Matrix[counter][1]=time[counter]
    Matrix[counter][2]=smile
    Matrix[counter][3]=anger
    Matrix[counter][4]=sadness
    Matrix[counter][5]=neutral
    counter=counter+1

data = {'url': image_url_7}
response = requests.post(face_api_url, params=params, headers=headers, json=data)
faces = response.json()
image = Image.open(BytesIO(requests.get(image_url_7).content))
plt.figure(figsize=(8, 8))
ax = plt.imshow(image, alpha=0.6)
for face in faces:
    firstid = str(face["faceId"])
    fa = face["faceAttributes"]
    smile = fa["smile"]
    anger = fa["emotion"]["anger"]
    sadness = fa["emotion"]["sadness"]
    neutral = fa["emotion"]["neutral"]
    Matrix[counter][0]=counter+1
    Matrix[counter][1]=time[counter]
    Matrix[counter][2]=smile
    Matrix[counter][3]=anger
    Matrix[counter][4]=sadness
    Matrix[counter][5]=neutral
    counter=counter+1

data = {'url': image_url_8}
response = requests.post(face_api_url, params=params, headers=headers, json=data)
faces = response.json()
image = Image.open(BytesIO(requests.get(image_url_8).content))
plt.figure(figsize=(8, 8))
ax = plt.imshow(image, alpha=0.6)
for face in faces:
    firstid = str(face["faceId"])
    fa = face["faceAttributes"]
    smile = fa["smile"]
    anger = fa["emotion"]["anger"]
    sadness = fa["emotion"]["sadness"]
    neutral = fa["emotion"]["neutral"]
    Matrix[counter][0]=counter+1
    Matrix[counter][1]=time[counter]
    Matrix[counter][2]=smile
    Matrix[counter][3]=anger
    Matrix[counter][4]=sadness
    Matrix[counter][5]=neutral
    counter=counter+1

data = {'url': image_url_9}
response = requests.post(face_api_url, params=params, headers=headers, json=data)
faces = response.json()
image = Image.open(BytesIO(requests.get(image_url_9).content))
plt.figure(figsize=(8, 8))
ax = plt.imshow(image, alpha=0.6)
for face in faces:
    firstid = str(face["faceId"])
    fa = face["faceAttributes"]
    smile = fa["smile"]
    anger = fa["emotion"]["anger"]
    sadness = fa["emotion"]["sadness"]
    neutral = fa["emotion"]["neutral"]
    Matrix[counter][0]=counter+1
    Matrix[counter][1]=time[counter]
    Matrix[counter][2]=smile
    Matrix[counter][3]=anger
    Matrix[counter][4]=sadness
    Matrix[counter][5]=neutral
    counter=counter+1

data = {'url': image_url_10}
response = requests.post(face_api_url, params=params, headers=headers, json=data)
faces = response.json()
image = Image.open(BytesIO(requests.get(image_url_10).content))
plt.figure(figsize=(8, 8))
ax = plt.imshow(image, alpha=0.6)
for face in faces:
    firstid = str(face["faceId"])
    fa = face["faceAttributes"]
    smile = fa["smile"]
    anger = fa["emotion"]["anger"]
    sadness = fa["emotion"]["sadness"]
    neutral = fa["emotion"]["neutral"]
    Matrix[counter][0]=counter+1
    Matrix[counter][1]=time[counter]
    Matrix[counter][2]=smile
    Matrix[counter][3]=anger
    Matrix[counter][4]=sadness
    Matrix[counter][5]=neutral
    counter=counter+1

#time in 24hour format
#emotion_index is in range of 0 to 1
def emotion_details(start_time,end_time,emotion,emotion_index):
    matched_people=0;
    if emotion=="happy":
        column_number=2
    if emotion=="angry":
        column_number=3
    if emotion=="sad":
        column_number=4
    if emotion=="neutral":
        column_number=5


    total_people_int_this_time_period=0
    for i in range(no_of_people):
        if (Matrix[i][1]>=start_time) and (Matrix[i][1]<=end_time):
            total_people_int_this_time_period=total_people_int_this_time_period+1
            if Matrix[i][column_number]>=emotion_index:
                matched_people = matched_people + 1

    return (matched_people,total_people_int_this_time_period)


