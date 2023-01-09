from django.shortcuts import render

# Create your views here.

posts_data = [
    {
        "slug":"nature-at-its-best",
        "title": "Nature at its best",
        "image": "some image",
        "description": "Some long text goes here, try loreol lumsum"
    },
    {
        "slug":"mountaing-hiking",
        "title": "Moutain hiking",
        "image": "some image 2",
        "description": "Some long text goes here for mountain hiking"
    },
    {
        "slug":"programming-is-great",
        "title": "Programming is great",
        "image": "some image 3",
        "description": "Some long text goes here for Programming is great"
    },
]


def index(request):
    return render(request, 'blog/index.html')


def posts(request):
    print(posts_data)
    return render(request, 'blog/posts.html',{"posts":posts_data})


def single_post(request, slug):
    single_post_data = next(post for post in posts_data if post['slug'] == slug)
    return render(request, 'blog/single_post.html',{"post":single_post_data})
