import customtkinter  as ctk
from bson import ObjectId

from components.template_frame import TemplateFrame
from components.grid_frame import GridFrame

class CreateFrame(ctk.CTkFrame, TemplateFrame):
    def __init__(self, master, name=str(ObjectId()), grid_frame=GridFrame(dim=(1,1), arr=None), **kwargs):
        ctk.CTkFrame.__init__(self, master=master, **kwargs)
        TemplateFrame.__init__(self, father=master, name=name, grid_frame=grid_frame, grid_information=self.grid_info())
        
        self.create_specific_grid_frame(grid_frame=grid_frame)

    def destroy(self):
        ctk.CTkFrame.destroy(self)

    def create_specific_grid_frame(self, grid_frame: GridFrame):
        self.grid_frame=grid_frame
        self.destroy_all()
        self.elements={}
        
        h,w=self.grid_frame.dim
        for i in range(h):
            self.grid_rowconfigure(i, weight=1) 
            for j in range(w): 
                self.grid_columnconfigure(j, weight=1)

    def hide_frame(self):
        if self.is_visible:
            self.is_visible=False
            self.grid_information=self.grid_info()
            self.grid_forget()

    def show_frame(self):
        if not self.is_visible:
            self.is_visible=True
            self.grid(**self.grid_information)
    
    def enable_fixed_size(self):
        self.grid_propagate(False)

    def desable_fixed_size(self):
        self.grid_propagate(True)

   