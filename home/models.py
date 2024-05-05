from django.db import models
import uuid
import random
# Create your models here.
class BaseModel(models.Model): 
    uid = models.UUIDField(primary_key = True, default=uuid.uuid4, editable = False)
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    category_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.category_name
    
class Question(BaseModel):
    category = models.ForeignKey(Category, related_name = 'Category', on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    marks = models.IntegerField(default=5)

    def __str__(self) -> str:
        return self.question

    def get_answer(self):
    # Access all related Ans objects through the custom related name
        Ans_objs = Ans.objects.filter(question=self)

        data = []

        for Ans_obj in Ans_objs:
            data.append({
                'ans': Ans_obj.ans,
                'isCorrect': Ans_obj.isCorrect
            })
        return data


    

class Ans(BaseModel):
    question = models.ForeignKey(Question, related_name = 'Question', on_delete=models.CASCADE)
    ans = models.CharField(max_length=100)
    isCorrect = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.ans