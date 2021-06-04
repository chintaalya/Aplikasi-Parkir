import wx
import wx.grid

class ImageGenerator(wx.grid.GridCellRenderer):
    def __init__(self,image):
        super().__init__()
        self.img = image
    
    def Draw(self, grid, attr, dc, rectangle, row, col, isSelected):
        image = wx.MemoryDC()
        image.SelectObject(self.img)
        dc.SetBackgroundMode(wx.SOLID)
        if isSelected:
            dc.SetBrush(wx.Brush(wx.BLUE, wx.SOLID))
            dc.SetPen(wx.Pen(wx.BLUE, 1, wx.SOLID))
        else:
            dc.SetBrush(wx.Brush(wx.WHITE, wx.SOLID))
            dc.SetPen(wx.Pen(wx.WHITE, 1, wx.SOLID))
        dc.DrawRectangle(rectangle)
        width, height = self.img.GetWidth(), self.img.GetHeight()
        if width > rectangle.width:
            width = rectangle.width
        if height > rectangle.height:
            height = rectangle.height
        dc.Blit(rectangle.x, rectangle.y, width, height, image, 0, 0, wx.COPY, True)
    
    def GetBestSize(self, grid, attr, dc, row, col):
        text = grid.GetCellValue(row,col)
        dc.SetFont(attr.GetFont())
        width, height = dc.GetTextExtent(text)
        return wx.Size(width,height)

    def __init__(self, image):
        wx.grid.GridCellRenderer.__init__(self)
        self.img = image

    # def Draw(self, grid, attr, dc, rectangle, row, col, isSelected):
    #     image = wx.MemoryDC()
    #     image.SelectObject(self.img)
    #     dc.SetBackgroundMode(wx.SOLID)
    #     if isSelected:
    #         dc.SetBrush(wx.Brush(wx.BLUE, wx.SOLID))
    #         dc.SetPen(wx.Pen(wx.BLUE, 1, wx.SOLID))
    #     else:
    #         dc.SetBrush(wx.Brush(wx.WHITE, wx.SOLID))
    #         dc.SetPen(wx.Pen(wx.WHITE, 1, wx.SOLID))
    #     dc.DrawRectangle(rect)
    #     width, height = self.img.GetWidth(), self.img.GetHeight()
    #     if width > rectangle.width - 2:
    #         width = rectangle.width - 2
    #     if height > rectangle.height - 2:
    #         height = rectangle.height - 2
    #     dc.Blit(rectangle.x + 1, rectangle.y + 1, width, height, image, 0, 0, wx.COPY, True)

    # def GetBestSize(self, grid, attr, dc, row, col):
    #     text = grid.GetCellValue(row, col)
    #     dc.SetFont(attr.GetFont())
    #     width, height = dc.GetTextExtent(text)
    #     return wx.Size(width, height)