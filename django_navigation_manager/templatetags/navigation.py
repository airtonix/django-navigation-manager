from django import template
register = template.Library()

from ..lib.manager import NavigationManager

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
			return bar
		except :
			return ""

@register.tag
def navigationbar_count ( parser, token = None):
	return NavigationBarCountNode( )

class NavigationBarCountNode ( template.Node ):
	def render ( self, context=None):
		try :
			return len(navigation_manager.bars())
		except :
			return ""

