from django.shortcuts import render
from django.views.generic.base import View
from .models import Movie

# КОНЕЦ 7 УРОКА ЬУЫИЗ ВЬЮ ЛИСТ ВЬЮ
# 8 урок 6я минута перенести стиль
#
#
#
class MoviesView(View):
    """Список фильмов"""
    def get(self, request):
        """
        Метод принимает get-запросы http, принимает request - вся информация,
        присланная от клиента(браузера)
        """
        movies = Movie.objects.all()
        return render(
            request, 'movies/movie_list.html', {'movie_list': movies}
        )


class MovieDetailView(View):
    """Полное описание фильма"""
    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(
            request, 'movies/movie_detail.html', {'movie': movie}
        )


