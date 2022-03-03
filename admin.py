from flask import *
from database import *
from timetable import *
admin=Blueprint('admin',__name__)

@admin.route('adminhome')
def adminhome():
	return render_template('adminhome.html')

@admin.route('adminmanagecourse',methods=['get','post'])
def adminmanagecourse():
	data={}
	q="select * from course"
	res=select(q)
	data['courses']=res
	if "register" in request.form:
		c=request.form['c']
		cd=request.form['cd']
		sd=request.form['sd']
		ed=request.form['ed']
		q="insert into course values(null,'%s','%s','%s','%s','')"%(c,cd,sd,ed)
		insert(q)
		return redirect(url_for('admin.adminmanagecourse'))


	if "action" in request.args:
		action=request.args['action']
		cid=request.args['cid']
		
	else:
		action=None

	if "update" in request.form:
		c=request.form['c']
		cd=request.form['cd']
		sd=request.form['sd']
		ed=request.form['ed']
		q="update  course set course='%s',coursedetail='%s',start_date='%s',end_date='%s' where course_id='%s'"%(c,cd,sd,ed,cid)
		print(q)
		update(q)
		flash("update successfully")

		return redirect(url_for('admin.adminmanagecourse'))
	if action=="update":
		q="select * from course where course_id='%s'"%(cid)
		res=select(q)
		data['updatecourse']=res
		
	if action=="delete":
		q="delete from course where course_id='%s'"%(cid)
		delete(q)
		flash("delete successfully")

		return redirect(url_for('admin.adminmanagecourse'))
	return render_template('adminmanagecourse.html',data=data)


@admin.route('/adminmanageteacher',methods=['get','post'])
def adminmanageteacher():
	data={}
	if "register" in request.form:
		fna=request.form['f']
		lna=request.form['l']
		pla=request.form['pl']
		pho=request.form['ph']
		em=request.form['e']
		de=request.form['desg']
		uname=request.form['u']
		pwd=request.form['p']
		ql="insert into login values(null,'%s','%s','teacher')"%(uname,pwd)
		rl=insert(ql)
		qs="insert into teacher values(null,'%s','%s','%s','%s','%s','%s','%s')"%(rl,fna,lna,pla,pho,em,de)
		insert(qs)
		print(qs)
		flash("added successfully")
		return redirect(url_for('admin.adminmanageteacher'))
	if "action" in request.args:
		action=request.args['action']
		mid=request.args['mid']
		lid=request.args['lid']
	else:
		action=None
	if "update" in request.form:
		fna=request.form['f']
		lna=request.form['l']
		pla=request.form['pl']
		pho=request.form['ph']
		em=request.form['e']
		de=request.form['desg']

		q="update teacher set  firstname='%s',lastname='%s',place='%s',phone='%s',email='%s',designation='%s' where teacher_id='%s'"%(fna,lna,pla,pho,em,de,mid)
		r=update(q)
		flash("update successfully")
		return redirect(url_for('admin.adminmanageteacher'))
	if action=="update":
		q="select * from  teacher where teacher_id='%s'"%(mid)
		r=select(q)
		data['updateteacher']=r
	if action=="delete":
		q="delete from teacher where login_id='%s'"%(lid)
		delete(q)
		q="delete from login where login_id='%s'"%(lid)
		delete(q)
		flash("delete successfully")
		return redirect(url_for('admin.adminmanageteacher'))
	q="select * from teacher "
	r=select(q)
	data['teachers']=r
	return render_template('adminmanageteacher.html',data=data)

@admin.route('/adminmanagestudent',methods=['get','post'])
def adminmanagestudent():
	data={}
	q="select * from course"
	r=select(q)
	data['courses']=r

	qq="SELECT * FROM student INNER JOIN course USING(course_id)"
	res=select(qq)
	data['student']=res
	
	if "register" in request.form:
		ccid=request.form['cc_id']
		fna=request.form['f']
		lna=request.form['l']
		pla=request.form['pl']
		pho=request.form['ph']
		em=request.form['e']
		uname=request.form['u']
		pwd=request.form['p']
		ql="insert into login values(null,'%s','%s','student')"%(uname,pwd)
		rl=insert(ql)
		qs="insert into student values(null,'%s','%s','%s','%s','%s','%s','%s')"%(rl,ccid,fna,lna,pla,pho,em)
		insert(qs)
		print(qs)
		flash("Added successfully")
		return redirect(url_for('admin.adminmanagestudent'))
	if "action" in request.args:
		action=request.args['action']
		mid=request.args['mid']
		lid=request.args['lid']
	else:
		action=None
	if "update" in request.form:
		ccid=request.form['cc_id']
		fna=request.form['f']
		lna=request.form['l']
		pla=request.form['pl']
		pho=request.form['ph']
		em=request.form['e']

		q="update student set course_id='%s', firstname='%s',lastname='%s',place='%s',phone='%s',email='%s' where student_id='%s'"%(ccid,fna,lna,pla,pho,em,mid)
		r=update(q)
		flash("update successfully")

		return redirect(url_for('admin.adminmanagestudent'))
	if action=="update":
		q1="select * from  student where student_id='%s'"%(mid)
		r1=select(q1)
		data['updatestudent']=r1
	if action=="delete":
		q="delete from login where login_id='%s'"%(lid)
		print(q)

		delete(q)
		q="delete from student where login_id='%s'"%(lid)
		delete(q)
		flash("delete successfully")
		return redirect(url_for('admin.adminmanagestudent'))
	return render_template('adminmanagestudent.html',data=data)


@admin.route('/adminmanagesubject',methods=['get','post'])
def adminmanagesubject():
	data={}
	q="select * from course"
	r=select(q)
	data['courses']=r

	qq="SELECT * FROM subject INNER JOIN course USING(course_id)"
	res=select(qq)
	data['subjects']=res
	
	if "register" in request.form:
		ccid=request.form['cc_id']
		s=request.form['s']
		se=request.form['se']
		sh=request.form['sh']
		qs="insert into subject values(null,'%s','%s','%s','%s')"%(ccid,s,se,sh)
		insert(qs)
		print(qs)
		flash("Added successfully")

		return redirect(url_for('admin.adminmanagesubject'))


	if "action" in request.args:
		action=request.args['action']
		sid=request.args['sid']
	else:
		action=None

	if "update" in request.form:
		ccid=request.form['cc_id']
		s=request.form['s']
		se=request.form['se']
		sh=request.form['sh']
		q="update subject set course_id='%s', subject='%s',semester='%s',subject_hour='%s' where subject_id='%s'"%(ccid,s,se,sh,sid)
		r=update(q)
		flash("update successfully")

		return redirect(url_for('admin.adminmanagesubject'))
	if action=="update":
		q1="select * from  subject where subject_id='%s'"%(sid)
		r1=select(q1)
		data['updatesubject']=r1
	if action=="delete":
		q="delete from subject where subject_id='%s'"%(sid)
		delete(q)
		flash("delete successfully")

		return redirect(url_for('admin.adminmanagesubject'))
	return render_template('adminmanagesubject.html',data=data)

@admin.route('/adminassignteacher',methods=['get','post'])
def adminassignteacher():
	data={}
	q="select * from teacher"
	r=select(q)
	data['teach']=r

	qq="SELECT * FROM assign INNER JOIN teacher USING(teacher_id) inner join subject USING(subject_id)"
	res=select(qq)
	data['ass']=res
	
	sid=request.args['sid']

	if "assign" in request.form:
		tid=request.form['t_id']
		q="insert into assign values(null,'%s','%s')"%(tid,sid)
		insert(q)
		flash("assigned successfully")
		return redirect(url_for('admin.adminassignteacher',sid=sid))
	return render_template('adminassignteacher.html',data=data)

@admin.route('/adminmanagetimetable',methods=['get','post'])
def adminmanagetimetable():
	data={}
	q="SELECT * FROM  subject INNER JOIN timetable using(subject_id)"
	r=select(q)
	data['ttable']=r

	qq="SELECT * FROM  subject"
	res=select(qq)
	data['sub']=res
	
	if "action" in request.args:
		action=request.args['action']
		ttid=request.args['ttid']
	else:
		action=None

	if "update" in request.form:
		sid=request.form['sid']
		sd=request.form['sd']
		ed=request.form['ed']
		p=request.form['p']
		w=request.form['w']
		q="update timetable set subject_id='%s',start_time='%s',end_time='%s',period='%s',week='%s' where timetable_id='%s'"%(sid,sd,ed,p,w,ttid)
		update(q)
		flash("update successfully")
		return redirect(url_for('admin.adminmanagetimetable'))
	

	if action=="update":
		s="select * from timetable where timetable_id='%s'"%(ttid)
		res=select(s)
		data['updatetimetable']=res

	if action=="delete":
		s="delete  from timetable where timetable_id='%s'"%(ttid)
		res=delete(s)
		flash("deleted successfully")
		return redirect(url_for('admin.adminmanagetimetable'))

	if "add" in request.form:
		sid=request.form['sid']
		sd=request.form['sd']
		ed=request.form['ed']
		p=request.form['p']
		w=request.form['w']
		q="select * from  timetable where period='%s' and week='%s' "%(p,w)
		res=select(q)
		if res:
			flash("entered only once")
		else:
			q="insert into timetable values(null,'%s','%s','%s','%s','%s','added')"%(sid,sd,ed,p,w)
			insert(q)
			flash("Added successfully")
			return redirect(url_for('admin.adminmanagetimetable'))
	return render_template('adminmanagetimetable.html',data=data)

@admin.route('/adminviewcomplaint',methods=['get','post'])
def adminviewcomplaint():
	data={}
	q="SELECT * FROM complaint INNER JOIN teacher ON complaint.`staff_id`=teacher.`teacher_id`"
	r=select(q)
	data['complaints']=r
	return render_template('adminviewcomplaint.html',data=data)

@admin.route('/adminsendreply',methods=['get','post'])
def adminsendreply():
	if "send" in request.form:
		r=request.form['r']
		cid=request.args['cid']
		q="update complaint set reply='%s' where complaint_id='%s'"%(r,cid)
		update(q)
		flash("send successfully")
		return redirect(url_for('admin.adminviewcomplaint'))

	return render_template('adminsendreply.html')


@admin.route('/adminviewrequest',methods=['get','post'])
def adminviewrequest():
	data={}
	q="select * from request INNER JOIN subject using(subject_id)"
	# q="SELECT r.`request_id`,r.date,r.status as rstatus,r.`totimetable_id`,r.fromtimetable_id,t1.period  AS tperiod,t2.period AS fperiod,t1.week AS tweek,t2.week AS fweek,t1.date AS tdate,t2.date AS fdate,s1.subject AS tsubject,s2.subject AS fsubject FROM request r,timetable t1,timetable t2,SUBJECT s1,SUBJECT s2  WHERE r.`totimetable_id`=t1.timetable_id AND r.fromtimetable_id=t2.timetable_id AND s1.subject_id=t1.subject_id AND s2.subject_id=t2.subject_id"
	res=select(q)
	data['tt']=res

	if "action" in request.args:
		action=request.args['action']
		rid=request.args['rid']
		fid=request.args['fid']
		tid=request.args['tid']
	else:
		action=None

	if action=="change":
		qf="select  subject_id from timetable where timetable_id='%s'"%(fid)
		res1=select(qf)
		qt="select  subject_id from timetable where timetable_id='%s'"%(tid)
		res2=select(qt)

		q="update timetable set subject_id='%s' where timetable_id='%s' " %(res1[0]['subject_id'],tid)
		print(q)
		update(q)
		q="update timetable set subject_id='%s' where timetable_id='%s' " %(res2[0]['subject_id'],fid)
		update(q)
		q="update request set status='changed' where request_id='%s'"%(rid)
		update(q)


	if action=="reject":
		q="delete from request where request_id='%s'"%(rid)
		delete(q)
		flash("deleted successfully")
		return redirect(url_for('admin.adminviewrequest'))
	return render_template('adminviewrequest.html',data=data)


@admin.route('/adminviewteacher',methods=['get','post'])
def adminviewteacher():
	data={}
	q="select * from teacher INNER join login using (login_id)"
	r=select(q)
	data['teachers']=r

	if "action" in request.args:
		action=request.args['action']
		lid=request.args['lid']
	else:
		action=None


	if action=="accept":
		q="update login set usertype='teacher' where login_id='%s'"%(lid)
		update(q)
		flash("accept successfully")
		return redirect(url_for('admin.adminviewteacher'))

	if action=="reject":
		q="update login set usertype='reject' where login_id='%s'"%(lid)
		update(q)
		flash("reject successfully")
	
		return redirect(url_for('admin.adminviewteacher'))
	return render_template('adminviewteacher.html',data=data)



@admin.route('/adminviewstudent',methods=['get','post'])
def adminviewstudent():
	data={}
	q="select * from student INNER join login using (login_id)INNER join course using (course_id)"
	r=select(q)
	data['view']=r

	if "action" in request.args:
		action=request.args['action']
		lid=request.args['lid']
	else:
		action=None


	if action=="accept":
		q="update login set usertype='student' where login_id='%s'"%(lid)
		update(q)
		flash("accept successfully")
		return redirect(url_for('admin.adminviewstudent'))
	if action=="reject":
		q="update login set usertype='reject' where login_id='%s'"%(lid)
		update(q)
		flash("reject successfully")
	
		return redirect(url_for('admin.adminviewstudent'))
	return render_template('adminviewstudent.html',data=data)

def Convert(string):
    li = list(string.split(","))
    return li
@admin.route('/check',methods=['get','post'])
def check():
	data={}
	course_id=request.args['course_id']
	if "submitss" in request.form:
		subject=str(request.form['subjectssd'])
		newsubject=Convert(subject)
		hour=request.form['hours']
		newhour=Convert(hour)
		breaks=request.form['breaks']
		newbreak=Convert(breaks)
		noofweak=request.form['noofweaks']
		# newnoofweak=Convert(noofweak)
		timetable(newsubject,newhour,noofweak,newbreak,course_id)
	
	return render_template('check.html',data=data)