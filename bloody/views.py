from django.core.checks import messages
from django.shortcuts import render, redirect, HttpResponse

from bloody.models import *


class BD:
    # def __init__(self):

        # if 'id' not in self.session:
        #     return render(self, 'signup.html')
        # else:
        #     return render(self, 'afterlogin.html')


    def index(self):
        return render(self, 'login.html')

    def sign(self):
        return render(self, 'signup.html')

    def register(self):
        name = self.POST.get("name")
        lame = self.POST.get("lname")
        mail = self.POST.get('mail')
        phone = self.POST.get('phone')
        password = self.POST.get('pass')
        blood = self.POST.get('bg')
        country = self.POST.get('cont')
        state = self.POST.get('state')
        city = self.POST.get('city')
        lati = self.POST.get('lat')
        long = self.POST.get('lng')
        student = Blood()
        # try:
        student.name = name
        student.lname = lame
        student.mail = mail
        student.phone = phone
        student.password = password
        student.bloodgrp = blood
        student.state = state
        student.city = city
        student.country = country
        student.lng = long
        student.lat = lati
        student.save()
        #
        # except Exception:
        #     pass
        return redirect('log')

    def login(self):
        email = self.POST.get("mail")
        passw = self.POST.get("password")
        try:
            profile = Blood.objects.get(mail=email, password=passw)
            self.session['id'] = profile.id
            self.session['name'] = profile.name
            self.session['lname'] = profile.lname
            self.session['phone'] = profile.phone
            self.session['email'] = profile.mail
            self.session['blud'] = profile.bloodgrp
            return render(self, 'afterlogin.html')
        except Exception:
            return redirect('log')

    def logout(request):
        del request.session['id']
        request.session.flush()
        request.session.set_expiry(0)

        return render(request, 'signup.html')

    def finddonor(self):
        state = self.POST.get("stateslist")
        blood = self.POST.get("bloodgroup")
        try:
            profile = Blood.objects.filter(state=state, bloodgrp=blood)
            data = {"obc": profile}
            return render(self, "afterlogin.html", data)
        except:
            pass
