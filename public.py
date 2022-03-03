from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/')
def home():
	return render_template('index.html')

@public.route('/login',methods=['get','post'])
def login():
	if "login" in request.form:
		uname=request.form['un']
		pwd=request.form['pa']
		q="select * from login where username='%s' and password='%s'"%(uname,pwd)
		res=select(q)
		if res:
			if res[0]['usertype']=="admin":
				return redirect(url_for('admin.adminhome'))
			elif res[0]['usertype']=="teacher":
				q="select * from teacher where login_id='%s'"%(res[0]['login_id'])
				r=select(q)
				session['teacherid']=r[0]['teacher_id']
				return redirect(url_for('teacher.teacherhome'))
			elif res[0]['usertype']=="student":
				q="select * from student where login_id='%s'"%(res[0]['login_id'])
				r=select(q)
				session['studentid']=r[0]['student_id']
				return redirect(url_for('student.studenthome'))


	return render_template('login.html')


@public.route('/a')
def a():
	return render_template('a.html')


@public.route('/teacherregister',methods=['get','post'])
def teacherregister():
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
		ql="insert into login values(null,'%s','%s','pending')"%(uname,pwd)
		rl=insert(ql)
		qs="insert into teacher values(null,'%s','%s','%s','%s','%s','%s','%s')"%(rl,fna,lna,pla,pho,em,de)
		insert(qs)
		print(qs)
		flash("register successfully")
		return redirect(url_for('public.teacherregister'))
	
	return render_template('teacherregister.html',data=data)

@public.route('/studentregister',methods=['get','post'])
def studentregister():
	data={}
	q="select * from course"
	r=select(q)
	data['courses']=r
	
	if "register" in request.form:
		ccid=request.form['cc_id']
		fna=request.form['f']
		lna=request.form['l']
		pla=request.form['pl']
		pho=request.form['ph']
		em=request.form['e']
		uname=request.form['u']
		pwd=request.form['p']
		ql="insert into login values(null,'%s','%s','pending')"%(uname,pwd)
		rl=insert(ql)
		qs="insert into student values(null,'%s','%s','%s','%s','%s','%s','%s')"%(rl,ccid,fna,lna,pla,pho,em)
		insert(qs)
		print(qs)
		flash("register successfully")
		return redirect(url_for('public.studentregister'))

	return render_template('studentregister.html',data=data)