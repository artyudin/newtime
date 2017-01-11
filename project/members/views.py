from django.shortcuts import render
from django.views.generic.list import ListView

from members.models import Member 


class MemberListView(ListView):

	model = Member

