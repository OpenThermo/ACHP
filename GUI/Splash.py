# -*- coding: us-ascii -*-
# generated by wxGlade 0.6.3 on Fri Jun 18 13:00:26 2010

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode

# end wxGlade

class Splash(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Splash.__init__
        kwds["style"] = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.MAXIMIZE_BOX|wx.SYSTEM_MENU|wx.RESIZE_BORDER|wx.FRAME_NO_TASKBAR|wx.NO_BORDER|wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN
        wx.Frame.__init__(self, *args, **kwds)
        self.label_6 = wx.StaticText(self, -1, "ACHP", style=wx.ALIGN_CENTRE)
        self.label_7 = wx.StaticText(self, -1, "(c) 2010 Braun Consulting", style=wx.ALIGN_CENTRE)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Splash.__set_properties
        self.SetTitle("Splash")
        self.SetSize((366, 296))
        self.SetBackgroundColour(wx.Colour(255, 0, 0))
        self.label_6.SetFont(wx.Font(40, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Splash.__do_layout
        sizer_20 = wx.BoxSizer(wx.VERTICAL)
        sizer_20.Add(self.label_6, 0, 0, 0)
        sizer_20.Add(self.label_7, 0, 0, 0)
        self.SetSizer(sizer_20)
        sizer_20.SetSizeHints(self)
        self.Layout()
        self.Centre()
        # end wxGlade

    def closeSplash(self, event): # wxGlade: Splash.<event_handler>
        self.Close()
        event.Skip()

# end of class Splash


