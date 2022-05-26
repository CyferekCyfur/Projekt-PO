from tkinter.filedialog import askopenfilename
class FileReadingPanel:
    def __init__(self, filename):
        self.filename = filename

    def file_reading(self):
        filename = askopenfilename()
        set_filename(filename)
    
    def get_filename(self):
        return self.filename
    
    def set_filename(self, fn):
        self.filename = fn
