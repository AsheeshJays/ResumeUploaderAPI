from django.shortcuts import render,redirect

from .models import Resume
from .forms import ResumeForm
from django.views import View

class HomeView(View):
    def get(self, request):
        form = ResumeForm()
        candidates = Resume.objects.all()
        return render(request, 'myfile.html',{'form':form,'candidates':candidates})
    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
            return render(request, 'myfile.html',{'form':form})

class CandidateView(View):
    def get(self, request, pk):
        candidate = Resume.objects.get(pk=pk)
        return render(request, 'candidate.html',{'candidate':candidate})
