from django.db import models


from datetime import datetime
from accounts.models import Profile
from main.models import Post


class Register(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="registers")
    person = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="my_registers"
    )
    created_dt = models.DateTimeField(auto_now_add=True)

    time1 = models.DateTimeField(null=False, default=datetime.now)
    time2 = models.DateTimeField(null=True)
    time3 = models.DateTimeField(null=True)

    finalTime = models.DateTimeField(null=True)

    msg = models.TextField(null=True)

    class Meta:
        ordering = ('post', 'created_dt')

    def __str__(self):
        return f'{self.post}-{self.person} register'
