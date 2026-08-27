from django.shortcuts import render

def home(req):
  return render(req, 'core/home.html')

def menu(req):
  return render(req, 'core/menu.html')

def tracking(req):
  return render(req, 'core/tracking.html')

def reservation(req):
  return render(req, 'core/reservation.html')

def contacts(req):
  return render(req, 'core/contacts.html')
