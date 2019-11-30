from django.db import models


class Question(models.Model):
    question = models.CharField( # 문제출력
        max_length=128
    )
    answer = models.CharField( # 정답입력
        max_length=128,
    )
    input = models.CharField(
        max_length=128,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.question
