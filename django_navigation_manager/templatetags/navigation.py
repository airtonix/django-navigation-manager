from django import template
from django.template import Context, loader
from django.template.loader import render_to_string
from ..lib.manager import NavigationManager

register = template.Library()

navigation_manager = NavigationManager()


@register.tag
def navigationbar ( parser, token ):
	try:
		tag_name, bar_name = token.split_contents()
	except ValueError:
		raise template.TemplateSyntaxError, "%r tag requires a single argument" % token.contents[0]
	return NavigationBarNode( bar_name )

class NavigationBarNode ( template.Node ):
	def __init__ ( self, bar_name ):
		self.bar_name = bar_name

	def render ( self, context ):

		try :
			bar = navigation_manager.get_bar( self.bar_name )
		except :
			bar = None
			error = """<!--Bar "%s" Not Found-->""" % self.bar_name

		if bar :
			return render_to_string("navigation_bar.html",{
				"Bar"	: bar.get_items(context),
				"Name" : bar.name
			})
		else :
			return error

