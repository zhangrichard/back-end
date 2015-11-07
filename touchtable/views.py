from django.shortcuts import HttpResponse
from django.template import RequestContext, loader

# Create your views here.

from .models import TestModel
def index( request ):
    return HttpResponse( "Hello, World")

def test( request ):
    template = loader.get_template( 'data.json' )
    context  = RequestContext( request, { 'sometext': TestModel.objects.all()[ 0 ].name } )
    return HttpResponse( template.render( context ) )
