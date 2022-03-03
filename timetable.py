import random
from database import *
def timetable(subjects,hours,noofweaks,breaks,cid):
	with open("static/timetable/course"+cid+".txt", "a+") as file_object:
		file_object.seek(0)
		# # If file is not empty then append '\n'
		
		file_object.write("")

	file = open("static/timetable/course"+cid+".txt","r+")
	file.truncate(0)
	file.close()
	# subjects=("a","b","c","d")
	subject = tuple(subjects)
	print(subjects)
	# hours=['h1','h2','h3','h4','h5','h6']

	weeks=['monday','Tuesday','Wenesday','Thursday','Friday','Saturday']
	hoursss=str(hours)
	hoursss=hoursss.replace("[","")
	hoursss=hoursss.replace("]","")



	with open("static/timetable/course"+cid+".txt", "a+") as file_object:
		file_object.seek(0)
		# # If file is not empty then append '\n'
		# data = file_object.read(100)
		# if len(data) > 0 :
		# file_object.write("\n")
		# Append text at the end of file
		file_object.write("         "+str(hoursss))
	print(len(hours))
	# breaks=['h3','h5']
	print(len(breaks))
	th=len(hours)-len(breaks)
	print(th)

	# noofweaks=5
	# print(weeks[:str(noofweaks)])
	noc=noofweaks*th
	print(noc)
	# //////////////////////////
	# for element in breaks:
	# 	if element in hours:
	# 		hours.remove(element)
	# 		for elements in weeks:
	# 			q="insert into ttable values(null,'%s','%s','%s')" %(element,'break',elements)
	# 			insert(q)

	 # /////////////////////////////////////
	for i in range(1,int(noofweaks)+1):
		ss=[]
		random_num=""
		# print(subject)
		subjects=[]
		subjects=list(subject)
		if len(subject)<int(noc):
			# print("hhh")
			random.shuffle(subjects)


			# subject = subject[:-1]
			# print(subjects)
			# valout=subject

			# for row in subjects:
			# 	print(row)
			subjectss=str(subjects)
			subjectss=subjectss.replace("[","")
			subjectss=subjectss.replace("]","")
			print(subjectss)

			# valll=subjects.remove("'")
			with open("static/timetable/course"+cid+".txt", "a+") as file_object:
			    # Move read cursor to the start of file.
			    file_object.seek(0)
			    # If file is not empty then append '\n'
			    data = file_object.read(100)
			    if len(data) > 0 :
			        file_object.write("\n")
			    # Append text at the end of file


			    file_object.write(weeks[i-1]+"      "+str(subjectss))
		else:
			random_num = random.choice(subjects)
			# print(random_num)
			ss=subjects
			ss.append(random_num)
			# print(ss)
			random.shuffle(ss)
			# subject = subject[:-1]
			# for row in th:
			# 	print(row)


			valss=ss
			with open("static/timetable/course"+cid+".txt", "a+") as file_object:
			    # Move read cursor to the start of file.
			    file_object.seek(0)
			    # If file is not empty then append '\n'
			    data = file_object.read(100)
			    if len(data) > 0 :
			        file_object.write("\n")
			    # Append text at the end of file
			    file_object.write(str(vals))


		# return valss
	breaksss=str(breaks)
	breaksss=breaksss.replace("[","")
	breaksss=breaksss.replace("]","")
	with open("static/timetable/course"+cid+".txt", "a+") as file_object:
		file_object.seek(0)
		# # If file is not empty then append '\n'
		data = file_object.read(100)
		if len(data) > 0 :
			file_object.write("\n")
			file_object.write("\n")
		# Append text at the end of file
		file_object.write(" Break Time is         "+str(breaksss))

	q="update course set path='static/timetable/course"+cid+".txt' where course_id='%s'"%(cid)
	update(q)