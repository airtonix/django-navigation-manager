from django.template import Context, loader
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse

NAVIGATIONBARS = {}

class NavigationManager:
	_storage = {}

	def __init__(self, storage=None):
		if storage :
			self.storage = storage
		else :
			self.storage = NAVIGATIONBARS

	def get_storage(self):
		return self._storage
	def set_storage(self,value):
		self._storage = value
	storage = property(get_storage, set_storage)

	def add_bar(self, name, data=None):
		if not name in self.storage.keys() :
			bar = NavigationList(self, name)
			self.storage[name] = bar
		else :
			bar = self.storage[name]

		if data :
			bar.add_items( data )
		return bar

	def bars(self):
			return self.storage.items()

	def get_bar(self,name=None):
		if name in self.storage.keys() :
			return self.storage[name]
		else :
			return None

	def add_to_bar(self, name, items):
		bar = self.get_bar(name)
		if not bar :
			bar = self.add_bar(name, [])
		bar.add_items(items)

class NavigationList :
	_items = []

	def __init__(self, parent, name, items=None):
		self.name = name
		if items :
			self.add(items)

	def add_items(self, items):
		for item in items :
			self.add(item)

	def add(self, item):
		if isinstance(item,dict):
			item['url'] = reverse(
				item['viewname'],
				urlconf=item['urlconf'],
				args=item['args']
			)

		self._items.append(item)

	def get_items(self, context=None):
		user = context['request'].user

		if user :
			user_permissions = user.get_all_permissions()
		else:
			user_permissions = ()

		allowed_items = []
		for item in self._items :
			if "permissions" in item.keys() :
				try :
					if user and user.has_perms( item['permissions'] ) :
						allowed_items.append( item )
				except:
					pass
			else :
				allowed_items.append( item )

		return allowed_items

