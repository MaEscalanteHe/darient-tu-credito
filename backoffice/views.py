from django.shortcuts import render, redirect
from .models import Bank, Credit, Client
from .forms import BankForm, ClientForm, CreditForm

""" Landing Page. """
def home(request):
    return render(request, 'home.html')

###################################################################################################
# Bank module. 
###################################################################################################

""" Main bank page. """
def bank(request):
    banks = Bank.objects.all()
    return render(request, 'banks.html', {'banks': banks})

""" Form to add new bank. """
def addBank(request):
    if request.method == 'POST':
        form = BankForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('banks')
    else:
        form = BankForm()
    return render(request, 'addBank.html', {'form': form})

###################################################################################################
# Client module. 
###################################################################################################

""" Main client page. """
def client(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients' : clients})

""" Get client description by id. """
def viewClient(request, client_id):
    client = Client.objects.get(id=client_id)
    return render(request, 'viewClient.html', {'client': client})

""" Form to add new client. """
def addClient(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients')
    else:
        form = ClientForm()
    return render(request, 'addClient.html', {'form': form})

""" Form to update client data. """
def updateClient(request, client_id):
    client = Client.objects.get(id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('clients')
    else:
        form = ClientForm(instance=client)
    return render(request, 'updateClient.html', {'form': form})

""" Method to remove a client. """
def removeClient(request, client_id):
    client = Client.objects.get(id=client_id)
    client.delete()
    return redirect('clients')

###################################################################################################
# Credit module. 
###################################################################################################

""" Main credit page. """
def credit(request):
    credits = Credit.objects.all()
    return render(request, 'credits.html', {'credits': credits})

""" Form to add new credit information. """
def addCredit(request):
    if request.method == 'POST':
        form = CreditForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('credits')
    else:
        form = CreditForm()
    return render(request, 'addCredit.html', {'form': form})