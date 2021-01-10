from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    """Data entry model for a message that a user sends to another message"""
    content = models.CharField(max_length=255)
    from_user = models.ForeignKey(User, related_name="from_user", null=False, on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name="to_user", null=False, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


