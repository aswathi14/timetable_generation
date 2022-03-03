from flask import *
from database import *

student=Blueprint('student',__name__)

@student.route('studenthome')
def studenthome():
	return render_template('studenthome.html')

@student.route('studentviewprofile')
def studentviewprofile():
	data={}
	uid=session['studentid']
	q="select * from student where student_id='%s'"%(uid)
	r=select(q)
	data['stu']=r
	return render_template('studentviewprofile.html',data=data)

@student.route('studentviewtimetable')
def studentviewtimetable():
	data={}
	q="select * from course "
	r=select(q)
	data['timetable']=r
	return render_template('studentviewtimetable.html',data=data)