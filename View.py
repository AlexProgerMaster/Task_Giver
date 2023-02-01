from tkinter import *
from tkinter import ttk, filedialog
import tkinter.font as tkfont
import tkinter.messagebox as ms


class View(Tk):
    def __init__(self, controller, model):
        super().__init__()
        self.controller = controller
        self.model = model
        self.userinput = StringVar()

        self.var = IntVar

        self.big_font_style = tkfont.Font(family='Courier', size=18, weight='bold')
        self.default_style_bold = tkfont.Font(family='Verdana', size=10, weight='bold')
        self.default_style = tkfont.Font(family='Verdana', size=10)

        # Window properties
        self.geometry('600x500')
        self.title('Random task giver')
        self.center(self)

        # Create two frames
        self.frame_top, self.frame_bottom = self.create_two_frames()

        self.btn_names, self.btn_tasks, self.btn_mix, self.btn_save = self.create_all_buttons()
        self.lbl_names, self.lbl_tasks, self.lbl_result = self.create_all_labels()

    def main(self):
        self.mainloop()

    @staticmethod
    def center(win):
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()

    def create_two_frames(self):
        frame_top = Frame(self, bg='#C3C3C3', height=50)  # blue
        frame_bottom = Frame(self, bg='#FFFFFF')  # yellow

        frame_top.pack(fill='both')
        frame_bottom.pack(expand=True, fill='both')

        return frame_top, frame_bottom

    def create_all_buttons(self):
        btn_names = Button(self.frame_top, text='Choose students', font=self.default_style,
                           command=self.controller.click_btn_names)
        btn_tasks = Button(self.frame_top, text='Choose Tasks', font=self.default_style,
                           command=self.controller.click_btn_tasks)
        btn_mix = Button(self.frame_top, text='Mix', font=self.default_style,
                         command=self.controller.click_btn_mix)
        btn_save = Button(self.frame_top, text='Save file', font=self.default_style,
                          command=self.controller.click_btn_save)
        btn_names.grid(row=0, column=0, padx=5, pady=2, sticky=EW)
        btn_tasks.grid(row=0, column=1, padx=5, pady=2, sticky=EW)
        btn_mix.grid(row=0, column=2, padx=5, pady=2, sticky=EW)
        btn_save.grid(row=0, column=3, padx=5, pady=2, sticky=EW)

        return btn_names, btn_tasks, btn_mix, btn_save

    def create_all_labels(self):
        lbl_names = Label(self.frame_bottom, anchor='w', font=self.default_style, justify=LEFT)
        lbl_tasks = Label(self.frame_bottom, anchor='center', font=self.default_style, justify=LEFT)
        lbl_result = Label(self.frame_bottom, anchor='e', font=self.default_style, justify=LEFT)

        lbl_names.grid(row=0, column=0, sticky=N, padx=5, pady=2)
        lbl_tasks.grid(row=0, column=1, sticky=N, padx=5, pady=2)
        lbl_result.grid(row=0, column=2, sticky=N, padx=5, pady=2)

        return lbl_names, lbl_tasks, lbl_result

    def open_name_file(self):
        self.model.name_file = filedialog.askopenfilename()

    def open_task_file(self):
        self.model.task_file = filedialog.askopenfilename()

    def save_file(self):
        self.model.save_file = filedialog.asksaveasfilename(filetypes=(('text file', '*.txt'), ('', '')))

    def list_warning(self):
        ms.showwarning('WARNING', 'Not enough tasks in tasks file')

    def save_error(self):
        ms.showerror('ERROR', 'Ypu can\'t save an empty file')
