from funix.views.problem import ProblemView, ProblemListBeta,ProblemComments
from funix.views.submission import abort_submission
from django.urls import path, include
from judge.views.widgets import rejudge_submission


urlpatterns = [
    path('/problems', ProblemListBeta.as_view(), name='beta_problem_list'),
    path('/problem/<str:problem>', include([
        path('', ProblemView.as_view(), name='beta_problem'), 
        path('/comments', ProblemComments.as_view(), name='beta_problem_comments'), 
        path('/submission/<int:submission>', ProblemView.as_view(), name='beta_problem'), 
    ])),
    path('submission/<int:submission>', include([
        path('/abort', abort_submission, name='beta_submission_abort'), 
    ])),
    path('widgets/', include([
        path('rejudge', rejudge_submission, name='beta_submission_rejudge'),
        ])
    )
]