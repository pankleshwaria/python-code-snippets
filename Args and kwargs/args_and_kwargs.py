# With *args you can pass unlimited number of arguments to a function
# and it will be accepted as a list of arguments
# Basically *args = []

blog_1 = 'I am awesome'
blog_2 = 'Cars are cool'
blog_3 = 'Cats are cute'

site_title = 'My blogs'


def post_blog(*blogs):
    for blog in blogs:
        print(blog)


post_blog(blog_1, blog_2, blog_3)


# In this case the first argument will always be the title
def post_titled_blog(title, *blogs):
    print(title)
    for blog in blogs:
        print(blog)


post_titled_blog(site_title, blog_1, blog_2, blog_3)


# With **kwargs you can pass unlimited number of key value arguments to a function
# and it will be accepted as a dictionary (key/value) of arguments
# Basically **kwargs = {}
def post_author_blog(**blogs):
    for author, blog in blogs.items():
        print('{} posted {}'.format(author, blog))


post_author_blog(Percy=blog_1, Oliver=blog_3)

