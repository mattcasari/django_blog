from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post

class LatestEntriesFeed(Feed):
    title = "Blog Poss"
    link = "/sitenews/"
    description = "Updates on changes and additions to Blog posts."

    def items(self):
        published = Post.objects.exclude(published_date__exact=None)
        return published.order_by('-published_date')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text
    
    def item_link(self, item):
        return reverse('blog_detail', args=[item.pk])