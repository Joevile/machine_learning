import os
import re
import csv


def search_file():
	for root,dirs,files in os.walk(r'C:\Users\caoyangang\Desktop\dang'):  #遍历路径
		for file in files:
			fileobj = re.match(r'Result',file,re.I)  # 匹配不论大小写的result
			if fileobj:
				yield os.path.join(root,file)  # 建立生成器对象
				
				
def merge_file():	
	lis = []  
	for path in search_file():
		with open(path,'r') as rf:
			reader = csv.reader(rf)						
			lis.append([row[5] for row in reader])  # 将某列元素写入列表
	lis=zip(*lis)  # 将列表转置，不转置的话列会变成行，lis是生成器
	wf = open('all.csv', 'w',newline='')
	writer = csv.writer(wf)
	for row in lis:
		writer.writerow(row)  # 将转置后的列表写入新的csv文件	
	wf.close

			
if __name__ == '__main__':
	merge_file()
	
    