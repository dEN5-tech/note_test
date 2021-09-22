from kivy.uix.scrollview import ScrollView


class EndEventScroll(ScrollView):
    def __init__(self, **kwargs):
        super(EndEventScroll, self).__init__(**kwargs)
        self.do_scroll_x = False
        self.do_scroll_y = True

    def on_scroll_stop(self, *args, **kwargs):
        result = super(EndEventScroll, self).on_scroll_stop(*args, **kwargs)

        if self.scroll_y < 0 and hasattr(self, 'on_end_event'):
            self.on_end_event()
        return result


if __name__ == '__main__':
    from kivymd.app import MDApp
    from yandex_parser import get_req_img_whith_yandex as YandImg
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.gridlayout import GridLayout
    from kivy.uix.button import Button
    from kivy.properties import ObjectProperty,NumericProperty,StringProperty
    from kivy.uix.image import AsyncImage
    from kivymd.uix.gridlayout import MDGridLayout
    from kivy.clock import Clock
    import asynckivy as ak
    from kivymd.uix.label import MDLabel as Label
    from kivy.graphics import *
    from kivymd.uix.textfield import MDTextFieldRect

    def add_img(i):
        btn = AsyncImage(source=f"{i}", size_hint=(None, None),
                             size=(250, 250))
        return btn


    def _del(all):
        for i in all.children:
            all.remove_widget(i)



    class CustomScrollView(EndEventScroll):

        layout1 = ObjectProperty(None)
        base_add = NumericProperty(0)
        search_string = StringProperty("")

        def __init__(self, **kwargs):
            super(CustomScrollView, self).__init__(**kwargs)
            self.start = 3
          

        def on_end_event(self):
            height = 0.0
            print(f"   start search start:{self.start}#stop:{self.start + 1}")
            async def add_async(height,i):
                    btn = await ak.run_in_thread(lambda: add_img(i=i))
                    self.layout1.add_widget(btn)
                    height += btn.height
            for i in YandImg(self.search_string,start_=self.start,limit= self.start + 1,type_="all",add_page = True):
                ak.start(add_async(height,i))
            height = float(height / self.layout1.cols)
            procent = (100.0 * height)/float(self.layout1.height)
            self.scroll_y += procent/100.0
            self.start+=1


    class ScrollViewApp(MDApp):
        def __init__(self, **kwargs):
            super(ScrollViewApp, self).__init__(**kwargs)
            self.number = 0
            self.base_add = 30

        async def add_async(self,layout1,i):
            try:
                btn = await ak.run_in_thread(lambda: add_img(i=i))
                layout1.add_widget(btn)
            except:
                return False
        def start_yand_img(self):
            for i in YandImg(self.scrollview1.search_string,start_=0,limit=2,type_="all",add_page = True):
                ak.start(self.add_async(self.layout1,i))
        def build(self):
            self.layout1 = MDGridLayout(cols=1, spacing=2, size_hint=(None, None), row_force_default=False, row_default_height=50)
            self.layout1.bind(minimum_height=self.layout1.setter('height'),
                         minimum_width=self.layout1.setter('width'))
            self.scrollview1 = CustomScrollView(bar_width='2dp', layout1=self.layout1,base_add=self.base_add,search_string='site:"safebooru.org" "smile"')
            self.out_search = self.scrollview1.search_string
            self.start_yand_img()
            self.scrollview1.add_widget(self.layout1)
            root = BoxLayout(orientation="vertical")
            self.text = MDTextFieldRect(text=f"{self.scrollview1.search_string}",size_hint=(0.65, 0.04))
            root.add_widget(self.text)

            root.add_widget(self.scrollview1)
            Clock.schedule_interval(self.update, 0.1)
            return root

        def update(self, *args):
            _del(self.layout1)
            self.scrollview1.search_string = self.text.text
            self.scrollview1.start = 3
            self.start_yand_img()
            self.out_search = self.text.text


            

    ScrollViewApp().run()