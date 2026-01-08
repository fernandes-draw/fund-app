from django.shortcuts import render
from django.views.generic import View
from projects.models import Project

# class DashboardView(View):

#     def get(self, request, *args, **kwargs):
#         return render(request, "accounts/dashboard.html")


class DashboardView(View):
    def get(self, request, *args, **kwargs):
        latest_projects = Project.objects.all()[:5]

        context = {}
        context["latest_projects"] = latest_projects
        return render(request, "accounts/dashboard.html", context)
