from django.shortcuts import render

# Create your views here.
def template_view(request):
    name = 'gangothri'
    marks = "10"
    addr = "guntur"
    # to get all these details into html file, we create a dict
    
    my_dict = {'name': name, 'marks': marks, "addr": addr}
    
    return render(request, "student.html", my_dict)