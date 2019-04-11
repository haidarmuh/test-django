#mesti ditambahin
from django.shortcuts import render

#mesti ditambahin untuk index
def index(request):
	context = {
	'title':'Kelas Ganteng',
	'heading' : 'Welcome',
	'subheading' : 'haidar'

	}
	return render(request, 'index.html', context)