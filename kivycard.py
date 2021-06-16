from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
import kivy.properties as props
from kivy.utils import get_color_from_hex

Builder.load_string("""
#:import Window kivy.core.window.Window
#:import get_color_from_hex kivy.utils.get_color_from_hex
<MyBox>
	padding:15
	spacing:15
	cols:4 if Window.width >= 900  else 3 if Window.width >= 600 else 2
	canvas.before:
		Rectangle:
			size:self.size
			pos:self.pos

	Card:
		border_shadow_radius:10
		Label:
			canvas:
				Rectangle:
					source:"img3.jpg"
					size:self.size
					pos:self.pos
		Label:
			text:'Lorem Ipsuem'
			size_hint_y:.40
			color:get_color_from_hex("#0B0B0B")

		Button:
			text:'button'
			size_hint:.40,.20
			pos_hint:{"center_x":.5,"center_y":.5}
	Card:
		elevation:0.1
		border_shadow_radius:8
		Label:
			canvas:
				RoundedRectangle:
					source:"img2.jpg"
					size:self.size
					pos:self.pos

		Label:
			text:'Lorem Ipsuem'
			size_hint_y:.40
			color:get_color_from_hex("#0B0B0B")

		Button:
			text:'button'
			size_hint:.40,.20
			pos_hint:{"center_x":.5,"center_y":.5}
	Card:
		elevation:0.2
		joint:"round"
		Label:
			canvas:
				Ellipse:
					source:"img3.jpg"
					size:self.size
					pos:self.pos
		Label:
			text:'Lorem Ipsuem'
			size_hint_y:.40
			color:get_color_from_hex("#0B0B0B")

		Button:
			text:'button'
			size_hint:.40,.20
			pos_hint:{"center_x":.5,"center_y":.5}
	Card:
		elevation:0.3
		Label:
			text:str(self.parent.size)
	Card:
		border_shadow_radius:8
		elevation:0.055
		Label:
			text:str(self.parent.size)
	Card:
		elevation:0.080
		joint:"round"

		Label:
			text:str(self.parent.size)

<Card>
	orientation:'vertical'
	spacing:2
	padding:10
	canvas.before:
		Rectangle:
			size:self.size
			pos:self.pos
    	Color:
        	rgba: self.get_color(self.border_shadow_color, self.elevation,0)
    	Line:
    		rounded_rectangle:self.x, self.y, self.width, self.height ,self.border_shadow_radius
    		width:self.border_shadow_width + 3
    		joint: self.joint
            cap: self.cap
    	Color:
        	rgba: self.get_color(self.border_shadow_color, self.elevation,0.01)
    	Line:
    		rounded_rectangle:self.x, self.y, self.width, self.height ,self.border_shadow_radius
    		width:self.border_shadow_width + 1
    		joint: self.joint
            cap: self.cap
    	Color:
        	rgba: self.get_color(self.border_shadow_color, self.elevation,0.02)
    	Line:
    		rounded_rectangle:self.x, self.y, self.width, self.height ,self.border_shadow_radius
    		width:self.border_shadow_width + 0.5
    		joint: self.joint
            cap: self.cap
    	Color:
        	rgba: self.get_color(self.border_shadow_color,self.elevation, 0.03)
    	Line:
    		rounded_rectangle:self.x+4, self.y+4, self.width-8, self.height-8 ,self.border_shadow_radius
    		width:self.border_shadow_width
    		joint: self.joint
            cap: self.cap
    	
    	


	

			


""")

class Card(BoxLayout):
	border_shadow_color = props.StringProperty("#0B0B0B")
	elevation = props.BoundedNumericProperty(0, min=0, max=0.5)
	border_shadow_radius = props.NumericProperty(1)
	border_shadow_width = props.NumericProperty(1)
	joint = props.OptionProperty('none', options=('round', 'miter', 'bevel', 'none'))
	cap = props.OptionProperty('none', options=('round', 'square', 'none'))

	def get_color(self, color, elevation, additive):
		color = get_color_from_hex(color)
		color[3] = elevation + additive
		return color


class MyBox(GridLayout):
	pass
		


class SimpleApp(App):
	def build(self):
		return MyBox()



SimpleApp().run()