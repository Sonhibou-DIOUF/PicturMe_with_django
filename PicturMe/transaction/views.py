from django.shortcuts import render

# Create your views here.

def add_transaction(request):
    context = {}
    return render(request, 'transaction/addtransaction.html', context)

def one_transaction(request, id ):
    context = {}
    return render(request, 'transaction/onetransaction.html', context)



def all_transactions(request):
    context = {}
    return render(request, 'transaction/alltransactions.html', context)