from django.db import models

# Create your models here.

class Classe(models.Model) :
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=50)
    teacher = models.CharField(max_length=30)

    def __str__(self) :
        return (self.name)

class Assignment(models.Model) :
    class_name = models.ForeignKey(Classe, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    group_assignment = models.BooleanField(default=False)
    instructions = models.CharField(max_length=3000)
    link = models.URLField(max_length=200)
    due_date = models.DateField()

    def __str__(self) :
        return self.title

    def get_assignment(self) :
        self.assignment = {
            "class" : self.class_name,
            "assignment" : self.title,
            "description" : self.instructions,
            "link" : self.link,
            "due" : self.due_date
        }
        return self.assignment
        #return ('%s %s' % (self.title, ": ", self.link))