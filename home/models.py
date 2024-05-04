from django.db import models
import uuid
# Create your models here.
class BaseModel(models.Model): 
    uid = models.UUIDField(primary_key = True, default=uuid.uuid4, editable = False)
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    category_name = models.CharField(max_length=100)

class Question(BaseModel):
    category = models.ForeignKey(Category, related_name = 'Category', on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    marks = models.IntegerField(default=5)

class Ans(BaseModel):
    question = models.ForeignKey(Question, related_name = 'Question', on_delete=models.CASCADE)
    ans = models.CharField(max_length=100)
    isCorrect = models.BooleanField(default=False)