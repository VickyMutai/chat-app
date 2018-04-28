from uuid import uuid4
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
def deserialize_user(user):
    """Deserialize user instance to JSON."""
    return {
        'id': user.id, 'username': user.username, 'email': user.email,
    }

class TrackDate(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

def _generate_unique_uri():
    """Generates a unique uri for the chat session."""
    return str(uuid4()).replace('-', '')[:15]

class Chat(TrackDate):
    admin = models.ForeignKey(User, on_delete=models.PROTECT)
    uri = models.URLField(default=_generate_unique_uri)

class ChatMessage(TrackDate):
    """Store messages for a session."""
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.PROTECT)
    message = models.TextField(max_length=2000)

    def convert(self):
        return{'user':deserialize_user(self.user),
                'message':self.message}

class ChatMember(TrackDate):
    chat = models.ForeignKey(Chat, related_name='members', on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

