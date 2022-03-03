from flask import *
from database import *

teacher=Blueprint('teacher',__name__)

@teacher.route('teacherhome')
def teacherhome():
	return render_template('teacherhome.html')

@teacher.route('/teacherviewtimetable')
def teacherviewtimetable():
	data={}
	q="select * from course "
	r=select(q)
	data['timetable']=r
	
	return render_template('teacherviewtimetable.html',data=data)


@teacher.route('/teacherviewsubjectassigned')
def teacherviewsubjectassigned():
	data={}
	uid=session['teacherid']
	q="SELECT * FROM `assign` INNER JOIN `subject` USING(subject_id) INNER JOIN `teacher` USING(teacher_id) where teacher_id='%s'"%(uid)
	r=select(q)
	data['assign_subject']=r
	return render_template('teacherviewsubjectassigned.html',data=data)

@teacher.route('/teachersendcomplaint',methods=['get','post'])
def teachersendcomplaint():
	data={}
	q="select * from complaint"
	r=select(q)
	data['comp']=r
	if "send" in request.form:
		complaint=request.form['com']
		sid=session['studentid']
		q="insert into complaint values(null,'%s','%s','reply-pending',curdate())"%(sid,complaint)
		insert(q)
		return redirect(url_for('teacher.teachersendcomplaint'))
	return render_template('teachersendcomplaint.html',data=data)

@teacher.route('/teacherchangetimetable',methods=['get','post'])
def teacherchangetimetable():
	data={}
	q="select * from timetable inner join subject using(subject_id)"
	res=select(q)
	data['timetable']=res

	tt_id=request.args['tt_id']

	if "change" in request.form:
		ctid=request.form['ctid']
		q="insert into request values(null,'%s','%s',curdate(),'pending')"%(ctid,tt_id)
		insert(q)
		flash("request send successfully")
		return redirect(url_for('teacher.teacherchangetimetable',tt_id=tt_id))

	return render_template('teacherchangetimetable.html',data=data)