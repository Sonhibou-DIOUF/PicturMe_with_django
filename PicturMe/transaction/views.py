from django.shortcuts import render
from .forms import TransactionForm, TransactionModelForm
from .models import Transaction
# Create your views here.

def add_transaction(request):
    """
        Add a transaction
    """
    if request.method == 'POST':
        form = TransactionModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = TransactionModelForm()
    context = {'form': form}
    return render(request, 'transaction/addtransaction.html', context)

def one_transaction(request, id ):
    context = {}
    return render(request, 'transaction/onetransaction.html', context)



def all_transactions(request):
    context = {}
    return render(request, 'transaction/alltransactions.html', context)