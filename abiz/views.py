from abiz.models import Article

from django.views import generic


class ArticleListView(generic.ListView):
    model = Article
    context_object_name = 'articles'
    paginate_by = 6


class ArticleDetailView(generic.DetailView):
    model = Article
    context_object_name = 'article'


# Create your views here.
