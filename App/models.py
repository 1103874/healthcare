from django.conf import settings
from django.db import models


class CheckVal(models.Model):

    checking = models.CharField(max_length=5)

    def __str__(self):
        return self.checking

    class Meta:
        verbose_name_plural = '체크값'


class DailyHealthCheck(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    check1 = models.ForeignKey(CheckVal, on_delete=models.CASCADE, related_name='check1',
                               verbose_name='1. 전일 과음 또는 음주 상태로 업무 수행이 어려운가요?')
    check2 = models.ForeignKey(CheckVal, on_delete=models.CASCADE, related_name='check2',
                               verbose_name='2. 맥박이 빠르고 조급함이 느껴지나요?')
    check3 = models.ForeignKey(CheckVal, on_delete=models.CASCADE, related_name='check3',
                               verbose_name='3. 머리가 무겁거나 어지러움이 있나요?')
    check4 = models.ForeignKey(CheckVal, on_delete=models.CASCADE, related_name='check4',
                               verbose_name='4. 충분한 수면을 하셨나요?(최소 5시간 이상)')
    check5 = models.ForeignKey(CheckVal, on_delete=models.CASCADE, related_name='check5',
                               verbose_name='5. 열이 있거나 질병이 있나요?')
    check6 = models.ForeignKey(CheckVal, on_delete=models.CASCADE, related_name='check6',
                               verbose_name='6. 오늘 업무수행에 문제가 없는 적절한 컨디션인가요?')

    class Meta:
        verbose_name_plural = '검진결과'