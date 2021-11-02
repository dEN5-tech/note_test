# -*- coding: utf8 -*-

from kivy.uix.button import Button
import asynckivy as ak
import asyncio
from kivy.uix.recycleview import RecycleView  as RV
from kivy.properties import BooleanProperty
from kivy.properties import ObjectProperty
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior as FB
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivymd.app import MDApp as App
from kivymd.uix.card import MDCard
import io
from kivy.uix.image import AsyncImage,Image
from kivy.core.image import Image as Img
from kivy.clock import Clock
import requests
from kivy.metrics import dp
from kivy.event import EventDispatcher as ED
from kivy.animation import Animation
from parseryn import get_req_img_whith_yandex as yand
def get_kivy_image_from_bytes(image_bytes, file_extension):
    # Return a Kivy image set from a bytes variable
    buf = io.BytesIO(image_bytes)
    cim = Img(buf, ext=file_extension)
    return Image(texture=cim.texture)

def urlTexture(url, obj):
#	bimage = requests.get(url).content
#	ext = "png"
#	image = get_kivy_image_from_bytes(bimage, ext)
	obj.source = url

from kivy.uix.scrollview import ScrollView


class EndEventScroll(ScrollView):

    def on_scroll_stop(self, *args, **kwargs):
        result = super(EndEventScroll, self).on_scroll_stop(*args, **kwargs)

        if self.scroll_y < 0 and hasattr(self, 'on_end_event'):
            self.on_end_event()
        return result
class Nimg(AsyncImage):
        	link = StringProperty(None)
        	def __init__(self, **kwargs):
        		super(Nimg, self).__init__(**kwargs)
        		#self.size = dp(0),dp(0)
        		#self.size_hint = 0.1,0.1
        		#Clock.schedule_once(self.onStart,0.01)
#        	def onStart(self,dt):
#        		while True:
#        			
#        			if self.link != None:
#        				print(self.link)
#        				async def urltexture():
#        					await ak.run_in_thread(lambda: urlTexture(self.link,self))
#        					ak.start(urltexture())
        		
#        	def update_(self,dt):
#        			while True:
#        				check = 0
#        				try:
#        					self.lstobj[0].texture
#        					check = 1
#        				except:
#        					check = 0
#        				if check:
#        					break
#        					print("set image")
#        					self.texture = self.lstobj[0].texture
        				
        			
        	

Builder.load_string('''
<RV>:
    RecycleBoxLayout:
        default_size: None, dp(160)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
''')

class RV(RecycleView,EndEventScroll):
        
        page = NumericProperty(0)
        def __init__(self, **kwargs):
        	super(RV, self).__init__(**kwargs)
        	self.viewclass= 'Nimg'
        	self.data = []
        	self.do_scroll_y = True
        	ak.start(self.someTask())
        def list_images(self,start,stop):
        	if self.page == 0:
        		stop+=1
        		self.page = 2
        	gemer = yand("lol",start_=start,limit=stop,type_="all",add_page = True)
        	print(type(gemer))
        	return gemer
        def scroll_to_index(self, index):
        	box = self.children[0]
        	pos_index = (box.default_size[1] + box.spacing) * index
        	scroll = self.convert_distance_to_scroll(
        	0, pos_index - (self.height * 0.5))[1]
        	if scroll > 1.0:
        		scroll = 1.0
        	elif scroll < 0.0:
        		scroll = 0.0
        	
        	self.scroll_y = 1.0 - scroll

        async def someTask(self):
        	self.do_scroll_y = False
        	async def yielder():
        				for i in self.list_images(self.page,self.page+1):
        					lnk = i
        					self.data.append({"source":f"{lnk}"})
        	await ak.run_in_thread(lambda:ak.start(yielder()))
        	self.do_scroll_y = True
        def on_end_event(self):
        	self.page+=1
        	main = len(self.children[0].children)-1
        	ak.start(self.someTask())
        	self.scroll_to_index(main)
        	
        	
        	
        #def on_scroll_move(self, *args, **kwargs):
        
#        	super(RV, self).on_scroll_move(*args, **kwargs)
#        
#        	if hasattr(self, 'on_end_event'):
#        		print("look")
        		
        		
     
        	
        


class TestApp(App):
    def build(self):
        return RV()

async def main():
	TestApp().run()

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())
