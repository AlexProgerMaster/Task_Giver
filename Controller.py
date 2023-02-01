from tkinter import END

from Model import Model
from View import View
from random import shuffle


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self, self.model)

    def main(self):
        self.view.main()

    def click_btn_names(self):
        self.view.open_name_file()
        names = self.model.name_file.replace('/', '\\')
        print(names)
        if self.model.name_file != " ":
            with open(names, 'r', encoding='utf-8') as file:
                text = file.read()
            self.students_for_mix = text
            self.view.lbl_names.config(text=self.students_for_mix)

    def click_btn_tasks(self):
        self.view.open_task_file()
        tasks = self.model.task_file.replace('/', '\\')
        if self.model.task_file != " ":
            with open(tasks, 'r', encoding='utf-8') as file:
                text = file.read()
            self.tasks_for_mix = text
            self.view.lbl_tasks.config(text=self.tasks_for_mix)

    def click_btn_mix(self):
        if type(self.students_for_mix) == type(self.model.abc):
            self.students_for_mix = self.students_for_mix.split('\n')
            self.students_for_mix.remove('')
        if type(self.tasks_for_mix) == type(self.model.abc):
            self.tasks_for_mix = self.tasks_for_mix.split('\n')
            self.tasks_for_mix.remove('')
        if len(self.students_for_mix) > len(self.tasks_for_mix):
            self.view.list_warning()
        else:
            x = 0
            self.a = ''
            shuffle(self.tasks_for_mix)
            for i in self.students_for_mix:
                self.a = self.a + self.students_for_mix[x] + ' - ' + self.tasks_for_mix[x] + '\n'
                x = x+1
            self.view.lbl_result.config(text=self.a)

    def click_btn_save(self):
        if self.view.lbl_result.cget('text') == '':
            self.view.save_error()
        else:
            self.view.save_file()
            save = self.model.save_file.replace('/', '\\')
            if self.model.save_file != " ":
                with open(save, 'w', encoding='utf-8') as file:
                    file.write(self.view.lbl_result.cget('text'))
