from django.shortcuts import render, redirect

def home(request):
    return render(request, 'catalog/home.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        print(f'Name: {name}\nMessage: {message}')  # Вывод данных в консоль
        return redirect('catalog:contact')  # Перенаправление после отправки формы
    return render(request, 'catalog/contact.html')
