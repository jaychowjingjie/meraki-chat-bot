import re


index = 0
message['text'] = "happy sdfdsfewfwef 0.65 from 1700 to 2200"

re.search(".*(happy|sad|angry|neutral).*(0|1)\.(\d).* from (\d*) to (\d*)",message['text'])
index=float(re.group(1))+(0.1*float(re.group(2))
#print (index)
print(message['text'])