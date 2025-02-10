from django.db import models
from django.utils import timezone

# Create your models here.
class UserInfo(models.Model):
    # user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    password_hash = models.CharField(max_length=255, null=True, blank=True)
    time_zone = models.CharField(max_length=50, null=True, blank=True)
    language = models.CharField(max_length=10, default='en')
    create_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'UserInfo'
    
    def __str__(self):
        return self.username

# class TimeBlock(models.Model):
#     LABLE_CHOISES = (
#         ('No Work', 'No Work'),
#         ('Deep Work', 'Deep Work'),
#     )

#     block_id = models.AutoField(primary_key=True)

#     user = models.ForeignKey(
#         UserInfo,
#         on_delete=models.CASCADE,
#         db_column='user_id'
#     )

#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()
#     label = models.CharField(
#         max_length=20,
#         choices=LABLE_CHOISES,
#         default='No Work'
#     )

#     is_completed = models.BooleanField(default=False)
#     create_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         db_table = 'time_blocks'
    
#     def __str__(self):
#         return f'{self.user.username} - {self.label}'
