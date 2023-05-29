from django import forms
from .models import Post, Image


class PostForm(forms.ModelForm):
    image = forms.ImageField(label='Image', required=False)

    class Meta:
        model = Post
        fields = '__all__'

    def save(self, commit=True, request=None):
        post = super(PostForm, self).save(commit=False)
        post.save()
        if request is not None:
            files = request.FILES.getlist('image')
            print(files)
            for f in files:
                image = Image(image=f, post=post)
                image.save()

        return post