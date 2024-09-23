from django.contrib.auth.models import User
from django.db import models

class Tweet(models.Model):
    text = models.CharField(max_length=280)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Tweet by {self.author.username}: {self.text[:50]}..."


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'tweet')

    def __str__(self):
        return f"{self.user.username} liked {self.tweet.id}"


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following',)
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers',)
    created_at =  models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"

