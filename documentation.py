import justpy as jp
from webapp import layout
from webapp import page


class About(page.Page):
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        lay = layout.DefaultLayout(a=wp, view="hHh lpR fFf")
        container = jp.QPageContainer(a=lay)
        div = jp.Div(a=container, classes="bg-yellow-200 h-screen")
        jp.Div(a=div, text="About page")
        jp.Div(a=div, text="""D:\PYTHON\App\APP_Instant_Dictionary_Web_App_&_API_Planning Phase
            \vert\Scripts\python.exe" "D:\PYTHON\App\APP_Instant_Dictionary_Web_App_&_API_Planning Phase\main.py" 
            D:/PYTHON/App/APP_Instant_Dictionary_Web_App_&_API_Planning Phase/vert/lib/site-packages/justpy
            Module directory: D:\PYTHON\App\APP_Instant_Dictionary_Web_App_&_API_Planning Phase
            \vert\lib\site-packages\justpy, Application directory: D:\PYTHON\App\APP_Instant_Dictionary_Web_App_&_API_Planning
             Phase""")
        return wp