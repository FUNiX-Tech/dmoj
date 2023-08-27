from django.db import models
from judge.models.problem_data import ProblemTestCase
from judge.models.problem import Problem
from zipfile import ZipFile
from judge.models.runtime import Language
from django.conf import settings


class ProblemTestCaseData(models.Model):
    problem_test_case = models.OneToOneField(ProblemTestCase, on_delete=models.CASCADE, related_name='data')
    input_data = models.TextField(verbose_name='input (criteria)', blank=True)
    output_data = models.TextField(verbose_name='expected output', blank=True)
    
    def __str__(self):
        input_data = self.input_data[0:20] + "..." if self.input_data else ""
        return f"{self.problem_test_case.dataset.code} - {self.problem_test_case.type}{self.problem_test_case.order} - {input_data}"

def save(self, *args, **kwargs):
    super(ProblemTestCase, self).save(*args, **kwargs)
    
    if (self.input_file != '' and self.input_file is not None) or (self.output_file != '' and self.output_file is not None):
        problem = Problem.objects.get(cases=self)
        archive = ZipFile(problem.data_files.zipfile.path, 'r')
        try:
            test_case_data = ProblemTestCaseData.objects.get(problem_test_case=self)
        except ProblemTestCaseData.DoesNotExist:
            test_case_data = ProblemTestCaseData.objects.create(problem_test_case=self)
    
        if self.input_file != '':
            test_case_data.input_data = archive.read(self.input_file).decode('utf-8')[0:200]
            
        if self.output_file != '':
            test_case_data.output_data = archive.read(self.output_file).decode('utf-8')[0:200]

        test_case_data.save()
        
def __str__(self):
    return self.type + " " + str(self.order)

ProblemTestCase.save = save
ProblemTestCase.__str__ = __str__
del save

class ProblemInitialSource(models.Model): 
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name="initial_codes")
    source = models.TextField(verbose_name="Problem Initial Source", max_length=65536, default="", blank=True)
    language = models.ForeignKey(Language, verbose_name="Initial Source Language", on_delete=models.CASCADE, related_name="initial_codes",  null=True)
    
    class Meta:
        unique_together = ('problem', 'language')
        
    def __str__(self): 
        return self.language.name


class ProblemTestCaseDataTranslation(models.Model):
    testcase = models.ForeignKey(ProblemTestCaseData, on_delete=models.CASCADE, related_name="translations")
    language = models.CharField(verbose_name='language', max_length=7, choices=settings.LANGUAGES)
    input_data = models.TextField(verbose_name='input', blank=True)
    output_data = models.TextField(verbose_name='expected output', blank=True)
    
    class Meta: 
        unique_together = ('testcase', 'language')
        verbose_name = 'testcase translation'
        verbose_name_plural = 'testcase translations'

