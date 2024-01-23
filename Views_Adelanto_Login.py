from django.contrib.auth import login, logout, authenticate

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

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
