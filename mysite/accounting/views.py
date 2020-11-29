from django.shortcuts import render

from django.http import HttpResponse

from .models import *

# Create your views here.

def member_list(request):
    context = {}

    print(request.user.user_type)

    members = []
    if request.user.is_authenticated and (request.user.user_type == 1):
        members = Member.objects.all()
        print(members)
    else:
        return HttpResponse('Need to be admin.')

    context['members'] = members

    print(context)

    return render(request, 'accounting/member_list.html', context=context)

def member_transactions(request, id):
    context = {}

    print(request.user)

    if request.user.is_authenticated and (request.user.user_type == 1):
        member = Member.objects.get(id=id)
        transactions = member.transaction_set.all()
        print(member)
        print(transactions)
    else:
        return HttpResponse('Need to be admin.')

    context['member'] = member
    context['transactions'] = transactions

    return render(request, 'accounting/member_transactions.html', context=context)