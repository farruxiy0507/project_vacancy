from django.db import models


# Vacancy

class Department(models.Model):
    department = models.CharField(max_length=150, verbose_name="departament, boshqarma yoki bo'lim nomi", blank=True, null=True)
    
    def __str__(self):
        return self.department

class Specialist(models.Model):
    specialist = models.CharField(max_length=150, verbose_name='mutaxassislik', blank=True, null=True)

    def __str__(self):
        return self.specialist

class Vacancy(models.Model):
    specialist = models.ForeignKey(Specialist, on_delete=models.SET_NULL, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    requirement = models.TextField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.specialist

#APPLICATION   

class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="first name", blank=True, null=True)
    last_name = models.CharField(max_length=50, verbose_name="last name", blank=True, null=True)
    fathers_name = models.CharField(max_length=50, verbose_name="fathers name", blank=True, null=True)
    birth_date = models.CharField(max_length=100, verbose_name="date of birth", blank=True, null=True)
    living_address = models.CharField(max_length=150, verbose_name="Living address", blank=True, null=True)
    phone_number = models.CharField(max_length=13, verbose_name="phone number", blank=True, null=True)
    speciality = models.ForeignKey(Vacancy, on_delete=models.SET_NULL, blank=True, null=True)
    email = models.EmailField(verbose_name="email", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    comment = models.TextField(max_length=255, blank=True, null=True)

class Education(models.Model):
    owner = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name="educations")
    name_of_education_institution = models.CharField(max_length=150, verbose_name="name of education institution",
                                                     blank=True, null=True)
    faculty_name = models.CharField(max_length=150, verbose_name="faculty name",
                                       blank=True, null=True)
    specialization = models.CharField(max_length=100, verbose_name="specialization",
                                       blank=True, null=True)
    completion_date = models.CharField(max_length=50, verbose_name="completion date",
                                       blank=True, null=True)    
                                       
class AdditionalEducation(models.Model):
    owner = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name="additional_educations")
    name_of_education_institution = models.CharField(max_length=150, verbose_name="name of education institution",
                                                     blank=True, null=True)
    specialization = models.CharField(max_length=100, verbose_name="specialization",
                                                     blank=True, null=True)
    completion_date = models.CharField(max_length=50, verbose_name="completion date",
                                                     blank=True, null=True)


class Languages(models.Model):
    owner = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name="language")
    language = models.CharField(max_length=20, verbose_name="language", blank=True, null=True)
    speaking = models.CharField(max_length=20, verbose_name="speach", blank=True, null=True)
    writing = models.CharField(max_length=20, verbose_name="writing", blank=True, null=True)
    reading = models.CharField(max_length=20, verbose_name="reading", blank=True, null=True)


class WorkPlaces(models.Model):
    owner = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name="work_place")
    start_date = models.CharField(max_length=20, verbose_name="start date")
    end_date = models.CharField(max_length=20, verbose_name="end date")
    organization_name = models.CharField(max_length=100, verbose_name="organization name")
    position = models.CharField(max_length=100, verbose_name="position")


class StartDateOfWork(models.Model):
    owner = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name="start_date_work")
    date = models.CharField(max_length=100, verbose_name="start date of work")
    salary = models.CharField(max_length=150, verbose_name="salary")
    information_source = models.CharField(max_length=50, verbose_name="information source")



class Help(models.Model):
    text = models.TextField()