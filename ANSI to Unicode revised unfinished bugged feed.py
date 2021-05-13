import chardet, os, time
from chardet.universaldetector import UniversalDetector
UD = UniversalDetector()
last_time = time.time()
current_count = 0
feed_count = 20
current_directory = os.getcwd()
try:
	os.mkdir('converted-to-unicode')
except:
	pass

for each_file in os.listdir(current_directory):

	if '.srt' in each_file:
		raw_f = open(current_directory+'//'+each_file,'rb')
		bytestring_content = raw_f.read()
		# encoding_det = chardet.detect(bytestring_content)['encoding']
		while UD.done == False:
			UD.feed(bytestring_content[current_count:feed_count])
			
			current_count = feed_count
			feed_count = feed_count*2
		encoding_det = UD.result['encoding']
		print(encoding_det)
		raw_f.close()
		trans_f = open(current_directory+'//'+each_file, encoding = encoding_det)
		content_to_write = trans_f.read()
		trans_f.close()
		target_f = open(current_directory+'//converted-to-unicode//'+each_file,'w',encoding='utf-8')
		target_f.write(content_to_write)
		target_f.close()
print(time.time() - last_time)
