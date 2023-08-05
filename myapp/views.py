from django.shortcuts import render

# data = hello()

# Create your views here.
# def index(request):
#     return render(request, 'index.html', {
#         'hello': hello()
#     })
# ***********************************************************************************

def mi_vista(request):
    if request.method == 'POST':
        switch1 = request.POST.get('switch1')
        switch2 = request.POST.get('switch2')  

        print(type(switch1))   
        print(switch2)

        if switch1 == 'True':
            def hello():
                return  print('Hello World')

        return render(request, 'resultado.html', {'switch1': switch1, 'switch2': switch2})

    return render(request, 'index2.html')