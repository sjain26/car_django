import pytest
from django.contrib.auth.models import User 
from django.urls import reverse
from django.test import Client
from seller.views import *

client = Client
pytestmark = pytest.mark.django_db


def test_sign_up(client):
    assert User.objects.count() == 0
    url = 'signup'
    data = {
        "username": "username", "password": 12345, "email": "test@test.com", }
    response = client.post(reverse('signup'), data, format='json')
    assert response.status_code == 302
    assert User.objects.count() == 1
    
    
def test_log_in(client):
    test_user = User.objects.create_user(
        username='testuser',
        password='testpassword')
    client.login(username='testuser', password='testpassword')
    response = client.get(reverse('login'))
    assert response.status_code == 302
       
        
def test_home_page(client):
    client.login(username='testuser', password='testpassword')
    response = client.get(reverse('home'))
    assert response.status_code == 302

