from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.views.generic import TemplateView
from oauth.models import OAuthUser
from oauth.models import OAuthClient

class AuthorizeView(TemplateView):
    template_name = "oauth/oauth.html"

    def get(self, request, *args, **kwargs):
        Gdata = request.GET
        context = self.get_context_data(**kwargs)
        try:
            context["response_type"] = Gdata["response_type"]
            context["client_id"] = Gdata["client_id"]
            context["redirect_uri"] = Gdata["redirect_uri"]
            context["state"] = Gdata.get("state")
        except:
            raise Http404()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        Pdata = request.POST
        try:
            OAuthUser.objects.get(name=Pdata["name"],passw = Pdata["pass"])
            OAuthClient.objects.get(client=Pdata["client_id"])
        except:
            return HttpResponse("Password Error or Unknown Error")
        from random import sample
        from time import time
        from oauth.models import OAuthCode

        code = ''.join(sample("1234567890qwertyuioADFGHJKLzxcNWEUalkdfj",10))
        CodeModel = OAuthCode()
        CodeModel.code = code
        CodeModel.url = Pdata["redirect_uri"]
        CodeModel.time = int(time())
        CodeModel.ClientId = Pdata["client_id"]
        CodeModel.save()
        return HttpResponseRedirect("%s?code=%s&state=%s"%(Pdata["redirect_uri"], code, Pdata["state"]))


