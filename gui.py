# from tkinter import *
 
# from tkinter import Menu
 
# from tkinter import ttk

# window = Tk()
 
# window.title("Welcome to LikeGeeks app")

# tab_control = ttk.Notebook(window)

# menu = Menu(window)
 
# new_item = Menu(menu)
 
# new_item.add_command(label='New')
 
# new_item.add_separator()
 
# new_item.add_command(label='Edit')
 
# menu.add_cascade(label='File', menu=new_item)
 
# window.config(menu=menu)

# tab1 = ttk.Frame(tab_control)
 
# tab2 = ttk.Frame(tab_control)
 
# tab_control.add(tab1, text='First')
 
# tab_control.add(tab2, text='Second')
 
# lbl1 = Label(tab1, text= 'label1')
 
# lbl1.grid(column=0, row=0)
 
# lbl2 = Label(tab2, text= 'label2')
 
# lbl2.grid(column=0, row=0)
 
# tab_control.pack(expand=1, fill='both')
 
# window.mainloop()

# from tkinter import *
# window = Tk()
# window.title("Welcome to LikeGeeks app")
# window.geometry('350x200')
# lbl = Label(window, text="Hello")
# lbl.grid(column=0, row=0)
# txt = Entry(window,width=10)
# txt.grid(column=1, row=0)
# def clicked():
# 	res = "Welcome to " + txt.get()
# 	lbl.configure(text= res)
# 	btn = Button(window, text="Click Me", background="#c00", relief="flat", command=clicked)
# 	btn.grid(column=2, row=0)
# window.mainloop()

# First things, first. Import the wxPython package.
# import wx

# # Next, create an application object.
# app = wx.App()

# # Then a frame.
# frm = wx.Frame(None, title="Hello World")

# # Show it.
# frm.Show()

# # Start the event loop.
# app.MainLoop()


# import wxversion
# wxversion.select("2.8")
import wx, wx.html
import sys

aboutText = """<p>Sorry, there is no information about this program. It is
running on version %(wxpy)s of <b>wxPython</b> and %(python)s of <b>Python</b>.
See <a href="http://wiki.wxpython.org">wxPython Wiki</a></p>""" 

class HtmlWindow(wx.html.HtmlWindow):
    def __init__(self, parent, id, size=(600,400)):
        wx.html.HtmlWindow.__init__(self,parent, id, size=size)
        if "gtk2" in wx.PlatformInfo:
            self.SetStandardFonts()

    def OnLinkClicked(self, link):
        wx.LaunchDefaultBrowser(link.GetHref())
        
class AboutBox(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, "About <<project>>",
            style=wx.DEFAULT_DIALOG_STYLE|wx.THICK_FRAME|wx.RESIZE_BORDER|
                wx.TAB_TRAVERSAL)
        hwin = HtmlWindow(self, -1, size=(400,200))
        vers = {}
        vers["python"] = sys.version.split()[0]
        vers["wxpy"] = wx.VERSION_STRING
        hwin.SetPage(aboutText % vers)
        btn = hwin.FindWindowById(wx.ID_OK)
        irep = hwin.GetInternalRepresentation()
        hwin.SetSize((irep.GetWidth()+25, irep.GetHeight()+10))
        self.SetClientSize(hwin.GetSize())
        self.CentreOnParent(wx.BOTH)
        self.SetFocus()

class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, pos=(150,150), size=(350,200))
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        menuBar = wx.MenuBar()
        menu = wx.Menu()
        m_exit = menu.Append(wx.ID_EXIT, "E&xit\tAlt-X", "Close window and exit program.")
        self.Bind(wx.EVT_MENU, self.OnClose, m_exit)
        menuBar.Append(menu, "&File")
        menu = wx.Menu()
        m_about = menu.Append(wx.ID_ABOUT, "&About", "Information about this program")
        self.Bind(wx.EVT_MENU, self.OnAbout, m_about)
        menuBar.Append(menu, "&Help")
        self.SetMenuBar(menuBar)
        
        self.statusbar = self.CreateStatusBar()

        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)
        
        m_text = wx.StaticText(panel, -1, "Hello World!")
        m_text.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
        m_text.SetSize(m_text.GetBestSize())
        box.Add(m_text, 0, wx.ALL, 10)
        
        m_close = wx.Button(panel, wx.ID_CLOSE, "Close")
        m_close.Bind(wx.EVT_BUTTON, self.OnClose)
        box.Add(m_close, 0, wx.ALL, 10)
        
        panel.SetSizer(box)
        panel.Layout()

    def OnClose(self, event):
        dlg = wx.MessageDialog(self, 
            "Do you really want to close this application?",
            "Confirm Exit", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_OK:
            self.Destroy()

    def OnAbout(self, event):
        dlg = AboutBox()
        dlg.ShowModal()
        dlg.Destroy()  

app = wx.App(redirect=True)   # Error messages go to popup window
top = Frame("<<project>>")
top.Show()
app.MainLoop()