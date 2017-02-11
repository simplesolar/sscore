from django.shortcuts import render
from django.views.generic import View

class HomeView(View):
    """
    XXX
    """
    def get(self, request, *args, **kwargs):
        """
        handles get requests for the customer landing page.
        """
        context = {}
        return render(request, 'customer/home.html', context)


