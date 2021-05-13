import chardet, os, time
last_time = time.time()
current_directory = os.getcwd()
if current_directory[len(current_directory)-1:] != "\\":
	current_directory += '//'
try:
	os.mkdir('converted-to-unicode')
except:
	pass

for each_file in os.listdir(current_directory):

	if '.srt' in each_file:
		f_ori = open(current_directory+'//'+each_file,'rb')
		bytestring_content = f_ori.read()
		f_ori.close()
		encoding_det = chardet.detect(bytestring_content[:len(bytestring_content)//2])['encoding']
		f = open(current_directory+'//'+each_file, encoding = encoding_det)
		content_to_write = f.read()
		f.close()
		target_f = open(current_directory+'converted-to-unicode//'+each_file,'w',encoding='utf-8')
		target_f.write(content_to_write)
		target_f.close()
finish_time = time.time()
while True:
	print(finish_time- last_time)
