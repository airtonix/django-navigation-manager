from django.template import Context, loader
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse

NAVIGATIONBARS = {}

class NavigationManager:

	def __init__(self):
		pass

	def add_bar(self, name, data=None):
		if not name in NAVIGATIONBARS.keys() :
			bar = NavigationList(self, name)
			NAVIGATIONBARS[name] = bar
		else :
			bar = NAVIGATIONBARS[name]

		if data :
			bar.add( data )
		return bar

	def bars(self):
			return NAVIGATIONBARS.items()

	def get_bar(self,name=None):
		if name in NAVIGATIONBARS.keys() :
			return NAVIGATIONBARS[name]
		else :
			return None

	def add_to_bar(self, name, items):
		bar = self.get_bar(name)
		if not bar :
			bar = self.add_bar(name, [])
		bar.add(items)

class NavigationList :
	items = []

	def __init__(self, parent, name, items=None):
		self.name = name
		if items :
			self.add(items)

	def add(self, items):
		for item in items :
			self._add(item)

	def _add(self, item):
		if isinstance(item,dict):
			data = {
				"label" : item['label'],
				"url" : reverse(item['viewname'], urlconf=item['urlconf'], args=item['args'])
			}

		self.items.append(data)

	def render(self,template_path = "navigation_bar.html"):
		return render_to_string(template_path,{
			"Bar"	: self.items,
			"Name" : self.name
		})

	def __str__(self):
		return self.render()

