from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_world_view(request):
	s='''
	<html>
	   <body>
	       <h1>Hello this is the first line of response</h1>
	       <h1>Hello this is the second line of response</h1>
	       <h1>Hello this is the third line of response</h1>
	       <h1>Hello this is the fourth line of response</h1>
	</body>
	</html>'''
	 
	return HttpResponse(s)
