from django.db import models


class Quiz(models.Model):
    question = models.CharField( # 문제출력
        max_length=128
    )
    answer = models.CharField( # 정답입력
        max_length=128,
        blank=True,
        null=True
    )
    correct = models.BooleanField(
        default=False # False 오답, True 정답
    )

    def __str__(self):
        return '질문 : ' + self.question
