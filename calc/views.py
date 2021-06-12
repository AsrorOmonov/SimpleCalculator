from django.shortcuts import render


# Create your views here.

def index(request):
    number1 = int(request.POST.get('num1', 0))
    number2 = int(request.POST.get('num2', 0))
    op = request.POST.get('op')

    result = 0

    if op == '+':
        result = number1 + number2
    elif op == '-':
        result = number1 - number2
    elif op == '*':
        result = number1 * number2
    elif op == '/':
        result = number1 / number2
    else:
        print('Invalid operator !')

    context = {

        'result': result
    }

    return render(request, 'index.html', context)
