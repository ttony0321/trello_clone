from django.db import models

# Create your models here.
class Fcuser(models.Model):
    user_name = models.CharField(max_length=70,
                                 verbose_name='사용자명')
    useremail = models.EmailField(max_length=120,
                                 verbose_name='이메일')
    password = models.CharField(max_length=70,
                                verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='등록시간')

    #user_name 으로 표시
    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 'fastcampus_fcuser'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'#복수형