/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.4.14-MariaDB : Database - py_timetable_creation
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`py_timetable_creation` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `py_timetable_creation`;

/*Table structure for table `assign` */

DROP TABLE IF EXISTS `assign`;

CREATE TABLE `assign` (
  `assign_id` int(11) NOT NULL AUTO_INCREMENT,
  `teacher_id` int(11) DEFAULT NULL,
  `subject_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`assign_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `assign` */

insert  into `assign`(`assign_id`,`teacher_id`,`subject_id`) values (1,1,1);

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `complaint` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`staff_id`,`complaint`,`reply`,`date`) values (1,1,'bbbb','qhbhsjs','2022-01-19');

/*Table structure for table `course` */

DROP TABLE IF EXISTS `course`;

CREATE TABLE `course` (
  `course_id` int(11) NOT NULL AUTO_INCREMENT,
  `course` varchar(100) DEFAULT NULL,
  `coursedetail` varchar(100) DEFAULT NULL,
  `start_date` varchar(100) DEFAULT NULL,
  `end_date` varchar(100) DEFAULT NULL,
  `path` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

/*Data for the table `course` */

insert  into `course`(`course_id`,`course`,`coursedetail`,`start_date`,`end_date`,`path`) values (1,'mca','dudf','2022-02-01','2022-03-09','static/timetable/course1.txt'),(2,'bsc computer science','jfrjgjtgkb','2022-02-01','2022-03-12',NULL),(7,'bca','asert','2022-02-01','2022-03-12',NULL),(8,'irfkfr','mfvfdc','2022-02-21','2022-02-28',NULL);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(2,'s','s','student'),(5,'tt','tt','teacher'),(6,'ss','ss','student'),(7,'aa','aa','teacher'),(9,'abeel','abeel','student'),(14,'aswin','aswin','student'),(16,'Labore dolore et sae','Pa$$w0rd!','teacher'),(22,'as','as','pending'),(23,'ki','ki','pending');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `fromsubject_id` int(11) DEFAULT NULL,
  `tosubject_id` int(11) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

/*Data for the table `request` */

insert  into `request`(`request_id`,`fromsubject_id`,`tosubject_id`,`date`,`status`) values (1,8,9,'2022-01-20','changed'),(2,1,15,'2022-02-25','pending'),(3,1,15,'2022-02-25','pending'),(4,3,1,'2022-02-26','pending');

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `student_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  `firstname` varchar(100) DEFAULT NULL,
  `lastname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;

/*Data for the table `student` */

insert  into `student`(`student_id`,`login_id`,`course_id`,`firstname`,`lastname`,`place`,`phone`,`email`) values (4,9,2,'abeel','v','ekm','7896541233','abeel@gmail.com'),(5,14,2,'aswin','s','wynd','1234569874','aswin@gmail.com'),(10,23,2,'kichu','L','Kozhikode','9630011203','kichu@gmail.com');

/*Table structure for table `subject` */

DROP TABLE IF EXISTS `subject`;

CREATE TABLE `subject` (
  `subject_id` int(11) NOT NULL AUTO_INCREMENT,
  `course_id` int(11) DEFAULT NULL,
  `subject` varchar(100) DEFAULT NULL,
  `semester` varchar(100) DEFAULT NULL,
  `subject_hour` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`subject_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

/*Data for the table `subject` */

insert  into `subject`(`subject_id`,`course_id`,`subject`,`semester`,`subject_hour`) values (1,8,'ksgyusftr','s1','140'),(3,2,'jbjhjkkj','s3','200'),(5,7,'science','s1','120');

/*Table structure for table `teacher` */

DROP TABLE IF EXISTS `teacher`;

CREATE TABLE `teacher` (
  `teacher_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `firstname` varchar(100) DEFAULT NULL,
  `lastname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `designation` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`teacher_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;

/*Data for the table `teacher` */

insert  into `teacher`(`teacher_id`,`login_id`,`firstname`,`lastname`,`place`,`phone`,`email`,`designation`) values (1,5,'Athira','m','kochi','9977664433','a@gmail.com','professor'),(10,22,'aswani','K','kochi','9630011203','aswani@gmail.com','lecturer');

/*Table structure for table `timetable` */

DROP TABLE IF EXISTS `timetable`;

CREATE TABLE `timetable` (
  `timetable_id` int(11) NOT NULL AUTO_INCREMENT,
  `subject_id` int(11) DEFAULT NULL,
  `start_time` varchar(100) DEFAULT NULL,
  `end_time` varchar(100) DEFAULT NULL,
  `period` varchar(100) DEFAULT NULL,
  `week` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`timetable_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4;

/*Data for the table `timetable` */

insert  into `timetable`(`timetable_id`,`subject_id`,`start_time`,`end_time`,`period`,`week`,`status`) values (8,0,'2022-01-24','2022-02-16','select period','select week','added'),(9,4,'2022-01-24','2022-02-27','2','Monday','added'),(14,4,'2022-01-24','2022-02-28','3','Monday','added'),(15,1,'13:14','14:15','1','Monday','added'),(16,3,'15:15','16:15','3','Tuesday','added');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
