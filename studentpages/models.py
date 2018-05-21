from django.db import models

# Create your models here.
class Student(models.Model):

	english_name = models.CharField(max_length=200)
	khmer_name = models.CharField(max_length=200, blank=True, null=True)
	japanese_name = models.CharField(max_length=200, blank=True)
	nationality = models.CharField(max_length=50)
	place_of_birth = models.CharField(max_length=200)
	card_id = models.CharField(max_length=100, blank=True, null=True)
	khmer_salary = models.FloatField(max_length=10, default=150, blank=True, null=True)
	EDU = (
		('Primary School','Primary School'),
		('Secondary School','Secondary School'),
		('High School','High School'),
		('University','University'),
		('Vocation School', 'Vocation Shool'),
		('Traning School','Traning School'),
		)
	education = models.CharField(max_length=200, choices=EDU, null=True)
	date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
	age = models.PositiveIntegerField(default=0)
	GENDER = (
			('Male','Male'),
			('Female','Female'),
		)
	gender = models.CharField(max_length=200,choices=GENDER)
	state_of_healt = models.CharField(max_length=20, blank=True, null=True)
	blood_type = models.CharField(max_length=20, blank=True, null=True)
	vision = models.CharField(max_length=50, blank=True, null=True)
	interest = models.CharField(max_length=50, blank=True, null=True)
	year_of_experience = models.IntegerField(default=0, null=True)
	MARRIED = (
			('Yes','Yes'),
			('No','No'),
		)
	married = models.CharField(max_length=50, choices=MARRIED)
	position = models.CharField(max_length=50, blank=True, null=True)
	behavior = models.CharField(max_length=50, blank=True)
	went_to_japan = models.CharField(max_length=50, choices=MARRIED)
	japanese_conversation = models.CharField(max_length=50, choices=MARRIED)
	height = models.CharField(max_length=50, blank=True, null=True)
	weight = models.CharField(max_length=50, blank=True, null=True)
	current_address = models.CharField(max_length=200)

	REASON = (
		('Increase Revenue','Increase Revenue'),
		('Respect to parents','Respect to parents'),
		('Improve Living','Improve Living'),
		('Education','Education'),
		('Other Reason','Other Reason'),
		)
	reason = models.CharField(max_length=255, choices=REASON)
	arrang_money = models.TextField(max_length=255, blank=True, null=True)
	COMPANY=(
		('Company 168','Company 168'),
		('Phnom Penh Thmey','Phnom Penh Thmey'),
		('CL Supply Company','CL Supply COMPANY'),
		('Other Company','Other Company'),
		)
	sending_company = models.CharField(max_length=200, choices=COMPANY)
	LEVEL = (
		('level','level'),
		('N5','N5'),
		('N4','N4'),
		('N3','N3'),
		('N2','N2'),
		('N1','N1'),
	)
	japanese_level = models.CharField(max_length=50, choices=LEVEL)
	field_of_work = models.CharField(max_length=50, blank=True, null=True)
	date_go_japan = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
	prefecture = models.CharField(max_length=50, blank=True, null=True)
	zip_code = models.CharField(max_length=50, blank=True, null=True)
	address_in_japan = models.CharField(max_length=200, null=True)

	grammer_level = models.CharField(max_length=200, blank=True, null=True)
	idiom_level = models.CharField(max_length=200, blank=True, null=True)
	conversation_level = models.CharField(max_length=200, blank=True, null=True)
	life_attitude = models.CharField(max_length=200, blank=True, null=True)
	course_type = models.CharField(max_length=100, blank=True, null=True)
	last_peroid_of_study = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
	university_name = models.CharField(max_length=200, blank=True, null=True)
	subject_name = models.CharField(max_length=100, blank=True, null=True)
	teacher_name = models.CharField(max_length=50, blank=True, null=True)
	book_type = models.CharField(max_length=50, blank=True, null=True)
	start_date = models.DateField(blank=True, null=True)
	end_date = models.DateField(blank=True, null=True)
	status = models.CharField(max_length=50, blank=True, null=True)
	description = models.CharField(max_length=255, blank=True, null=True)

	admin_name = models.CharField(max_length=50, blank=True, null=True)
	email_address = models.EmailField(max_length=255, blank=True, null=True)
	phone_number = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return "Student Name : " + self.english_name

class Fujiyama(models.Model):

	student = models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True)
	entry_date = models.DateField(auto_now=False,auto_now_add=False, null=True)
	score = models.FloatField(default=0)
	player_learn_detail = models.CharField(max_length=200, null=True)
	correct_answer = models.IntegerField(default=0)
	duration = models.DurationField()
	email = models.EmailField(max_length=250, null=True)
	incorrect_answer = models.IntegerField(default=0)
	login_source = models.CharField(max_length=200)
	phone_number = models.CharField(max_length=20)
	status = models.CharField(max_length=200)

	def __str__(self):
		return "Registration type : " + self.login_source
