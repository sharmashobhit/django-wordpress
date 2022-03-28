# django-wordpress
Import your existing wordpress into Django without any hassle

If you have your blog on Wordpress.com(or your own wordpress hosting) then you can use this django application to get the data from the blog to your Django application in a jiffyq.

# Usage:11
INSTALLED_APPS = (
  ...
  'django_wordpress',
)

Add {% load fetch_from_wp %} to your template to import the templatetags.

The templatetags provide 3 options:a
* fetch_posts
* fetch_latest_post
* fetch_latest_comments
a
* fetch_posts
      {% fetch_posts url='yourwebsite.wordpress.com' as posts %}
      # You can also pass 'number' parameter to specify how many posts you want.
      Example:
      {% fetch_posts url='yourwebsite.wordpress.com' number=10 as posts%}
      #once you retrieve the posts, you can loop over the posts like:
      {% for post in posts %}
        {{post.title}}
      {% endfor %}
      
* fetch_latest_post
      {% fetch_posts url='yourwebsite.wordpress.com' as post %}
      #once you retrieve the post, you can see it as follows:
      {{post.title}}
      
* fetch_latest_comments
      {% fetch_latest_comments url='yourwebsite.wordpress.com' as comments %}
      # You can also pass 'number' parameter to specify how many comments you want.
      Example:
      {% fetch_posts url='yourwebsite.wordpress.com' number=10 as comments %}
      # once you retrieve the comments, you can loop over the comments like:
      {% for comment in comments %}
        {{comment.content}}
      {% endfor %}

For more info about the post and comment JSON, visit:
https://developer.wordpress.com/docs/api/1.1/get/sites/%24site/posts/
https://developer.wordpress.com/docs/api/1.1/get/sites/%24site/comments/
