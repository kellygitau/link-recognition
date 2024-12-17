from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.urls import reverse


def validate_links_in_text(text):
    """
    Validates that no URLs exist in the provided text.
    """
    url_validator = URLValidator()
    words = text.split()
    for word in words:
        try:
            url_validator(word)
        except ValidationError:
            pass  # Not a URL, ignore
        else:
            raise ValidationError(f"Text contains a URL: {word}")


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(validators=[validate_links_in_text])  # Moved validation here
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    class Meta:
        ordering = ['-date']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
