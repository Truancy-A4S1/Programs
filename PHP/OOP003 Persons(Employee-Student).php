<?php
class Person{ //PARENT CLASS NG INAMO
	protected $name;
	protected $age;

	public function __construct($name, $age){
		$this->name = $name;
		$this->age = $age;
	}
	public function do_walk(){
		echo "{$this->name} is walking...";
	}
	public function do_introduce(){
		echo "I'm {$this->name}<br>
		from 'Person' class: <br>
		I can <b>walk</b>";
	}
}

//Employee extends Person.. Employee will inherit all the methods from Person
class Employee extends Person{ //CHILD CLASS NG 'PERSON' NGINAMO
	protected $job;
	protected $company;

	public function __construct($name, $age, $job, $company){
		$this->name = $name;
		$this->age = $age;
		$this->job = $job;
		$this->company = $company;
	}
	//Overriding method ng inamo: may do_introduce() din sa Person class PERO di yun ang iru-run kasi na OVERRIDE/REPLACED na nitong do_introduce() sa Employee class: 
	public function do_introduce(){
		echo "I'm {$this->name} and I'm working as {$this->job} in {$this->company}<br>
		from 'Employee' class that inherits all the private and public properties and methods of my parent class named 'Person'<br>
		I can walk and <b>resign</b>";
	}
	public function do_resign(){
		echo "{$this->name} is resigning...";
	}
}
//ulul
class Student extends Person{ //CHILD CLASS DIN NG 'PERSON' NGINAMO
	protected $course;
	protected $year;

	public function __construct($name, $age, $course, $school){
		$this->name = $name;
		$this->age = $age;
		$this->course = $course;
		$this->school = $school;
	}
	public function do_introduce(){
		echo "I'm {$this->name} and I'm studying {$this->course} at {$this->school}<br>
		from 'Student' class that inherits all the private and public properties and methods of my parent class named 'Person'<br>
		I can walk and <b>study</b>";
	}
	public function do_study(){
		echo "{$this->name} is studying...";
	}
}

$per01 = new Person("Person Phoibe", 24);
$per02 = new Person("Person Tertia", 23);

$emp01 = new Employee("Employee Zahra", 24, "Nurse", "YMK Incs.");
$emp02 = new Employee("Employee Marta", 23, "Teacher", "ELS Pioneer Camp.");

$stu01 = new Student("Student Ninochka", 24, "BS in Computer Science", "YMK University");
$stu02 = new Student("Student Karyn", 23, "BA in English Literature", "ST GTS PMF");

echo "<br><hr> PERSONS <br>";
echo "{$per01->do_introduce()}<br><br>";
echo "{$per02->do_introduce()}<br><br>";

echo "<br><hr> EMPLOYEE <br>";
echo "{$emp01->do_introduce()}<br><br>";
echo "{$emp02->do_introduce()}<br><br>";

echo "<br><hr> STUDENT <br>";
echo "{$stu01->do_introduce()}<br><br>";
echo "{$stu02->do_introduce()}<br><br>";


?>