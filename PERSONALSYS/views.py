from django.shortcuts import render, redirect
# from django.urls import reverse
# from django.views import View
from django.utils import timezone
# import json


def home_view(request):
	if request.user.is_authenticated:
		fecha_actual = timezone.now()
		return render(request, 'home.html', {'fecha': fecha_actual})
	else:
		return redirect('iniciar_sesion')


# class InicioView(View):
# 	def get(self, request, *args, **kwargs):
# 		fecha_actual = timezone.now()
# 		
# 		with open('data/menu_01.json', 'r', encoding='utf-8') as file:
# 			data = json.load(file)
# 		
# 		menu_items = data['menu_items']
# 		
# 		# Procesar URLs dinámicas
# 		def process_menu_urls(items):
# 			for item in items:
# 				if item['href'] and not item['href'].startswith("/"):
# 					# Usar reverse para obtener la URL real
# 					item['href'] = reverse(item['href'])
# 				if item.get('submenu'):
# 					process_menu_urls(item['submenu'])
# 		
# 		process_menu_urls(menu_items)
# 		
# 		return render(request, 'inicio.html', {'fecha': fecha_actual, 'menu_items': menu_items})
