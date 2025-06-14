def fibonacci(number):
    num1 = 1
    num2 = 1
    for i in range(number):
        print(f"{i+1}. iteration :{num1}")
        num1 , num2 = num2, num1 + num2
#fibonacci(15)


# f = open("Day_8\myfile.txt", "x") Create file

class Task:
    def __init__(self, description):
        self.description = description
        self.done = False

    def mark_as_done(self):
        self.done = True

    def __str__(self):
        return f"{self.description}, {self.done}"


class Todo:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        task = Task(task)
        self.tasks.append(task)
        with open("Day_8/myfile.txt", "a") as f:  
            f.write(str(task) + "\n")  

    def mark_task_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_done()
    
            with open("Day_8/myfile.txt", "w") as f:
                for task in self.tasks:
                    f.write(str(task) + "\n")

    def __str__(self):
        return '\n'.join(f"{i+1}. {task}" for i, task in enumerate(self.tasks))

task1 = Todo()
task1.add_task("learn programming")
task1.mark_task_done(0)
