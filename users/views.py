from django.http import HttpResponse
from django.template import loader
from .models import Users
import pandas as pd
# Create your views here.


def index(request):
    myusers = Users.objects.all().values()
    df = pd.DataFrame(myusers)
    template = loader.get_template("index.html")
    context = {
        "myusers": df.to_html()
    }
    print(df)
    return HttpResponse(template.render(context, request))
