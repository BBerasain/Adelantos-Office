from django.shortcuts import render

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contraseña)

            if user is not None:
                login(request, user)
                return render(request,"miapp/inicio.html", {"mensaje":f"Bienvenido {usuario}"} )
            
            else:
                return render(request,"miapp/inicio.html", {"mensaje":"Error, datos incorrectos"} )
        
        else:
            return render(request,"miapp/inicio.html", {"mensaje":"Error, formulario erroneo"} )
    
    form = AuthenticationForm()

    return render(request,"miapp/login.html", {"form":form} )

def register(request):

    if request.method == "POST":
        form =  UserCreationForm()
        if form.is_valid():
            username = form.cleaned_data("username")
            form.save()
            return render(request,"miapp/inicio.html" , {"mensaje":"Usuario Creado:)" })
        
    else:
        form = UserCreationForm()

    return render(request,"miapp/registro.html" , {"form":form})
