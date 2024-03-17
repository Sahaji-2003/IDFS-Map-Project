import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox as tmsg
class GUI:
    line_id = 0

    def __init__(self, root):
        self.distance = 0
        self.source_var = tk.StringVar()
        self.destination_var = tk.StringVar()
        self.source_var1 = tk.StringVar()
        self.destination_var1 = tk.StringVar()
        self.start_node=tk.StringVar()
        self.goal_node=tk.StringVar()
        self.count = 0
        
        
        self.path = []
        self.path_label = None


       
        self.root = root
        self.root.title("Romania Map")
        self.canvas_width = 1550
        self.canvas_height = 790

        self.view = tk.StringVar()
        self.view.set("#090231")  
        self.vehicle = tk.StringVar()
        self.vehicle.set("Plane") 

        def yourfunc(option):
            a=tmsg.askquestion(f'"Are you sure",viewing as{option}')
            if option == "Light":
                option = "grey"
            elif option== "Medium":
                option = "#090231"
            else :
                option = "black"
            self.view.set(option)
            print(self.view.get())
            self.update_canvas_color() 

        def myfunc(option1):
            a=tmsg.showinfo(f'"You will be travelling with{option1}')
            if option1 == "Airplane":
                option1 = "Plane"
            elif option1 == "Train":
                option1 = "Train"
            else :
                option1 = "Car"
            self.vehicle.set(option1)
            print(self.vehicle.get())
            self.plane_image = tk.PhotoImage(file=f"{self.vehicle.get()}.png")
   
        

        def mysource(option3):
            self.source_var=option3
            

        def mydestination(option4):
            print("submitted")
            self.destination_var=option4
            

        def onsubmit(option5):
            print("on clicked")
            if option5== "Yes":
                self.submit_button_clicked()
            else:
                print("Not submitted")

        def onreset(option6):
            print("on reset")
            if option6 == "Yes":
                self.reset()
            else:
                print("Not reseted")


        
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg=self.view.get())
        self.canvas.pack()

        self.background_image = Image.open("Map.png")
        self.background_image = self.background_image.resize((1150, 670))
        self.background_image = ImageTk.PhotoImage(self.background_image)
        self.background_label = self.canvas.create_image(65, 55, anchor="nw", image=self.background_image)
        Yourmenubar=tk.Menu(root)

        m1=tk.Menu(Yourmenubar,tearoff=0)
        m1.add_command(label="Light", command=lambda: yourfunc("Light"))
        m1.add_separator()
        m1.add_command(label="Medium",command=lambda: yourfunc("Medium"))
        m1.add_separator()
        m1.add_command(label="Dark",command=lambda: yourfunc("Dark"))
        m1.add_separator()
        root.config(menu=Yourmenubar)

        Yourmenubar.add_cascade(label="View", menu=m1)

        m2=tk.Menu(Yourmenubar, tearoff=0)
        m2.add_command(label="Airplane", command=lambda: myfunc("Airplane"))
        m2.add_separator()
        m2.add_command(label="Tain", command=lambda: myfunc("Train"))
        m2.add_separator()
        m2.add_command(label="Car", command=lambda: myfunc("Car"))
        m2.add_separator()
        root.config(menu=Yourmenubar)

        Yourmenubar.add_cascade(label="Go with", menu=m2)


        m3=tk.Menu(Yourmenubar, tearoff=0)
        m3.add_command(label="Arad", command=lambda: mysource("Arad"))
        m3.add_separator()
        m3.add_command(label="Zerind", command=lambda: mysource("Zerind"))
        m3.add_separator()
        m3.add_command(label="Oradea", command=lambda: mysource("Oradea"))
        m3.add_separator()
        m3.add_command(label="Sibiu", command=lambda: mysource("Sibiu"))
        m3.add_separator()
        m3.add_command(label="Timisoara ", command=lambda: mysource("Timisoara"))
        m3.add_separator()
        m3.add_command(label="Lugoj", command=lambda: mysource("Lugoj"))
        m3.add_separator()
        m3.add_command(label="Mehadia", command=lambda: mysource("Mehadia"))
        m3.add_separator()
        m3.add_command(label="Drobeta", command=lambda: mysource("Drobeta"))
        m3.add_separator()
        m3.add_command(label="Craiova", command=lambda: mysource("Craiova"))
        m3.add_separator()
        m3.add_command(label="Rimnicu Vilcea", command=lambda: mysource("Rimnicu Vilcea"))
        m3.add_separator()
        m3.add_command(label="Fagaras", command=lambda: mysource("Fagaras"))
        m3.add_separator()
        m3.add_command(label="Pitesti", command=lambda: mysource("Pitesti"))
        m3.add_separator()
        m3.add_command(label="Bucharest", command=lambda: mysource("Bucharest"))
        m3.add_separator()
        m3.add_command(label="Giurgiu", command=lambda: mysource("Giurgiu"))
        m3.add_separator()
        m3.add_command(label="Urziceni", command=lambda: mysource("Urziceni"))
        m3.add_separator()
        m3.add_command(label="Hirsova", command=lambda: mysource("Hirsova"))
        m3.add_separator()
        m3.add_command(label="Eforie", command=lambda: mysource("Eforie"))
        m3.add_separator()
        m3.add_command(label="Vaslui", command=lambda: mysource("Vaslui"))
        m3.add_separator()
        m3.add_command(label="Iasi", command=lambda: mysource("Iasi"))
        m3.add_separator()
        m3.add_command(label="Neamt", command=lambda: mysource("Neamt"))
        m3.add_separator()
        root.config(menu=Yourmenubar)
        Yourmenubar.add_cascade(label="Source", menu=m3)

        m4=tk.Menu(Yourmenubar, tearoff=0)
        m4.add_command(label="Arad", command=lambda: mydestination("Arad"))
        m4.add_separator()
        m4.add_command(label="Zerind", command=lambda: mydestination("Zerind"))
        m4.add_separator()
        m4.add_command(label="Oradea", command=lambda: mydestination("Oradea"))
        m4.add_separator()
        m4.add_command(label="Sibiu", command=lambda: mydestination("Sibiu"))
        m4.add_separator()
        m4.add_command(label="Timisoara ", command=lambda: mydestination("Timisoara"))
        m4.add_separator()
        m4.add_command(label="Lugoj", command=lambda: mydestination("Lugoj"))
        m4.add_separator()
        m4.add_command(label="Mehadia", command=lambda: mydestination("Mehadia"))
        m4.add_separator()
        m4.add_command(label="Drobeta", command=lambda: mydestination("Drobeta"))
        m4.add_separator()
        m4.add_command(label="Craiova", command=lambda: mydestination("Craiova"))
        m4.add_separator()
        m4.add_command(label="Rimnicu Vilcea", command=lambda: mydestination("Rimnicu Vilcea"))
        m4.add_separator()
        m4.add_command(label="Fagaras", command=lambda: mydestination("Fagaras"))
        m4.add_separator()
        m4.add_command(label="Pitesti", command=lambda: mydestination("Pitesti"))
        m4.add_separator()
        m4.add_command(label="Bucharest", command=lambda: mydestination("Bucharest"))
        m4.add_separator()
        m4.add_command(label="Giurgiu", command=lambda: mydestination("Giurgiu"))
        m4.add_separator()
        m4.add_command(label="Urziceni", command=lambda: mydestination("Urziceni"))
        m4.add_separator()
        m4.add_command(label="Hirsova", command=lambda: mydestination("Hirsova"))
        m4.add_separator()
        m4.add_command(label="Eforie", command=lambda: mydestination("Eforie"))
        m4.add_separator()
        m4.add_command(label="Vaslui", command=lambda: mydestination("Vaslui"))
        m4.add_separator()
        m4.add_command(label="Iasi", command=lambda: mydestination("Iasi"))
        m4.add_separator()
        m4.add_command(label="Neamt", command=lambda: mydestination("Neamt"))
        m4.add_separator()
        root.config(menu=Yourmenubar)
        Yourmenubar.add_cascade(label="Destination", menu=m4)

        m5=tk.Menu(Yourmenubar, tearoff=0)
        m5.add_command(label="Yes", command=lambda: onsubmit("Yes"))
        m5.add_command(label="No", command=lambda: onsubmit("No"))
        Yourmenubar.add_cascade(label="Submit", menu=m5)


        m6=tk.Menu(Yourmenubar, tearoff=0)
        m6.add_command(label="Yes", command=lambda: onreset("Yes"))
        m6.add_command(label="No", command=lambda: onreset("No"))
        Yourmenubar.add_cascade(label="Reset", menu=m6)

        
        


        self.create_map()
        self.Display_name()
        self.create_input_fields()
        self.create_submit_button()
        self.create_reset_button()

        self.graph = Graph()
        self.path = []
        self.path_index = 0
        plane = "Plane"
        self.plane_image = tk.PhotoImage(file=f"{plane}.png")
        self.plane_image = self.plane_image.subsample(3, 3)
        self.plane_id = None
        self.total_distance = 0

    def update_canvas_color(self):  
      self.canvas.config(bg=self.view.get()) 


    def create_map(self):
        city_coordinates = {
            'Arad': (270, 320),
            'Zerind': (350, 220),
            'Oradea': (430, 160),
            'Sibiu': (400, 320),
            'Timisoara': (220, 420),
            'Lugoj': (320, 490),
            'Mehadia': (440, 510),
            'Drobeta': (470, 610),
            'Craiova': (600, 590),
            'Rimnicu Vilcea': (500, 370),
            'Fagaras': (550, 250),
            'Pitesti': (600, 450),
            'Bucharest': (750, 420),
            'Giurgiu': (730, 530),
            'Urziceni': (860, 370),
            'Hirsova': (1000, 450),
            'Eforie': (1120, 510),
            'Vaslui': (920, 280),
            'Iasi': (880, 190),
            'Neamt': (750, 110),
        }

        for city, coordinates in city_coordinates.items():
            oval_color = 'white' 
            if city == self.source_var:
                oval_color = 'green' 
            elif city == self.destination_var:
                oval_color = 'green'
            elif city == self.start_node:
                oval_color='green'
            elif city == self.goal_node:
                oval_color='green'
            self.canvas.create_oval(coordinates[0] - 10, coordinates[1] - 10, coordinates[0] + 10, coordinates[1] + 10,
                                fill=oval_color, outline='black')
            self.canvas.create_text(coordinates[0], coordinates[1] + 19, text=city, font=("Arial", 10, "bold"))

        connections = [('Arad', 'Zerind'), ('Arad', 'Sibiu'), ('Arad', 'Timisoara'), ('Zerind', 'Oradea'),('Oradea', 'Sibiu'),
                    ('Fagaras', 'Bucharest'), ('Craiova', 'Pitesti'), ('Sibiu', 'Fagaras'),
                   ('Sibiu', 'Rimnicu Vilcea'),('Timisoara', 'Lugoj'), ('Rimnicu Vilcea', 'Pitesti'), ('Rimnicu Vilcea', 'Craiova'),
                   ('Pitesti', 'Bucharest'), ('Craiova', 'Drobeta'), ('Drobeta', 'Mehadia'), ('Mehadia', 'Lugoj'),
                   ('Lugoj', 'Timisoara'), ('Bucharest', 'Giurgiu'), ('Bucharest', 'Urziceni'), ('Urziceni', 'Vaslui'),
                   ('Urziceni', 'Hirsova'), ('Vaslui', 'Iasi'), ('Iasi', 'Neamt'), ('Hirsova', 'Eforie')]

        for connection in connections:
            start_city, end_city = connection
            start_x, start_y = city_coordinates[start_city]
            end_x, end_y = city_coordinates[end_city]
            self.canvas.create_line(start_x, start_y, end_x, end_y, fill='#9a981a',width=2)
    
    def Display_name(self):
        Romania_map_label = tk.Label(self.root, text="Romania Map",background="#090231",fg="yellow", font=("Times", 35, "bold"))
        Romania_map_label.place(x=1145, y=50)
        idfs_label = tk.Label(self.root, text="Iterative Deepening DFS",background="#090231",fg="white", font=("Times", 17, "bold"))
        idfs_label.place(x=1220, y=110)
       # Romania_map_label.pack()

    def create_submit_button(self):
        submit_button = tk.Button(self.root, text="Submit",bg="green",fg="white", font=("Arial", 13, "bold"), command=self.submit_button_clicked1)
        submit_button.place(x=1320, y=700)

    def create_reset_button(self):
        reset_button = tk.Button(self.root, text="Reset", bg="blue",fg="white",font=("Arial", 13, "bold"), command=self.reset)
        reset_button.place(x=1246, y=700)

    def create_input_fields(self):
        source_label = tk.Label(self.root, text="Source City:",background="#090231",fg="white" ,font=("Arial", 14, "bold"))
        source_label.place(x=1130, y=625)
        self.source_var1 = tk.StringVar()
        source_entry = tk.Entry(self.root, textvariable=self.source_var1,font=("Arial", 13, "bold"))
        source_entry.place(x=1300, y=625)

        destination_label = tk.Label(self.root, text="Destination City:",background="#090231",fg="white", font=("Arial", 14, "bold"))
        destination_label.place(x=1130, y=660)
        self.destination_var1 = tk.StringVar()
        destination_entry = tk.Entry(self.root, textvariable=self.destination_var1,font=("Arial", 13, "bold"))
        destination_entry.place(x=1300, y=660)

    def submit_button_clicked(self):
        self.create_map()
        start_node = self.source_var
        goal_node = self.destination_var
        max_search_depth = 10
        self.path = self.graph.iddfs(start_node, goal_node, max_search_depth)
        
        if self.path is None:
            print("Path not found!")
        else:
            self.path.reverse()
            self.path_index = 0
            self.total_distance = 0
            self.animate_airplane()


    def submit_button_clicked1(self):
        self.start_node = self.source_var1.get()
        self.goal_node = self.destination_var1.get()
        self.create_map()
        max_search_depth = 10
        self.path = self.graph.iddfs(self.start_node, self.goal_node, max_search_depth)
        #self.visit = self.graph.visited

        if self.path is None:
            print("Path not found!")
        else:
            self.path.reverse()
            self.path_index = 0
            self.total_distance = 0
            self.animate_airplane()
    
    def reset(self):
        self.canvas.delete("path")  
        self.canvas.delete(self.plane_id)  
        self.source_var=""  
        self.destination_var=""  
        self.source_var1.set("")  
        self.destination_var1.set("")
        self.start_node=""
        self.goal_node=""
        self.create_map()
        self.total_distance = 0
        self.update_distance_label()
       
        if self.path_label is not None:
            self.path_label.destroy()
            self.path_label = None
        self.path = []
        


    def animate_airplane(self):
       if self.path_index < len(self.path) - 1:
          current_city = self.path[self.path_index]
          next_city = self.path[self.path_index + 1]
  
          start_x, start_y = self.get_city_coordinates(current_city)
          end_x, end_y = self.get_city_coordinates(next_city)

          self.canvas.delete(self.plane_id)  #Remove the previous plane image
          self.line_id = self.canvas.create_line(start_x, start_y, end_x, end_y, fill='blue', width=4, tag="path")
          self.plane_id = self.canvas.create_image(start_x, start_y, image=self.plane_image)
          
          #Yaha se plane move hoga

          dx = end_x - start_x
          dy = end_y - start_y
          distance = max(abs(dx), abs(dy))
        
          if distance > 0:
            speed = 5
            steps = distance // speed
            dx = dx / steps
            dy = dy / steps

            self.total_distance += distance
            self.update_distance_label()
            self.path_show()

            self.move_plane(start_x, start_y, end_x, end_y, dx, dy, steps)

    def move_plane(self, start_x, start_y, end_x, end_y, dx, dy, steps):
       if steps > 0:
          self.canvas.move(self.plane_id, dx, dy)
          self.root.after(50, lambda: self.move_plane(start_x + dx, start_y + dy, end_x, end_y, dx, dy, steps - 1))
       else:
          self.path_index += 1
          self.animate_airplane()





    def get_city_coordinates(self, city):
        city_coordinates = {
            'Arad': (270, 320),
            'Zerind': (350, 220),
            'Oradea': (430, 160),
            'Sibiu': (400, 320),
            'Timisoara': (220, 420),
            'Lugoj': (320, 490),
            'Mehadia': (440, 510),
            'Drobeta': (470, 610),
            'Craiova': (600, 590),
            'Rimnicu Vilcea': (500, 370),
            'Fagaras': (550, 250),
            'Pitesti': (600, 450),
            'Bucharest': (750, 420),
            'Giurgiu': (730, 530),
            'Urziceni': (860, 370),
            'Hirsova': (1000, 450),
            'Eforie': (1120, 510),
            'Vaslui': (920, 280),
            'Iasi': (880, 190),
            'Neamt': (750, 110),
        }

        return city_coordinates[city]

    def update_distance_label(self):
        distance_label = tk.Label(self.root, text=f"Total Distance: {self.total_distance} km",fg="white",bg="#090231", font=("Arial", 13, "bold"))
        distance_label.place(x=1220, y=570)
    
    def path_show(self):
        if self.path_label is not None:
            self.path_label.destroy()
        self.path_label = tk.Label(self.root,text=f"Path : {self.path}",font="Arial 13 bold",fg="white",bg="#090231")
        self.path_label.place(x=50, y=720)
   
    def visit_show(self,visit,count):
         self.count=count
         #self.count += 1
         self.visit = visit
         #self.count = self.count + 1
         print(self.count)
         self.visit_label = tk.Label(text=f"Visit : {self.visit}",font="Arial 13 bold",fg="white",bg="#090231")
         self.visit_label.place(x=50, y=(520+self.count*30))

class Graph(GUI):
    
    def __init__(self):
        self.adjacency_list = {
            'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
            'Zerind': ['Arad', 'Oradea'],
            'Oradea': ['Zerind', 'Sibiu'],
            'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
            'Timisoara': ['Arad', 'Lugoj'],
            'Lugoj': ['Timisoara', 'Mehadia'],
            'Mehadia': ['Lugoj', 'Drobeta'],
            'Drobeta': ['Mehadia', 'Craiova'],
            'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
            'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
            'Fagaras': ['Sibiu', 'Bucharest'],
            'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
            'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
            'Giurgiu': ['Bucharest'],
            'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
            'Hirsova': ['Urziceni', 'Eforie'],
            'Eforie': ['Hirsova'],
            'Vaslui': ['Urziceni', 'Iasi'],
            'Iasi': ['Vaslui', 'Neamt'],
            'Neamt': ['Iasi']
        }
        


        
    

    def iddfs(self, start, goal, max_depth):
        self.count=0
        for depth in range(max_depth + 1):
            
            visited = []
            path = []
            if self.dfs(start, goal, depth, visited, path,self.count):
                return path
            self.count +=1
        return None

    def dfs(self, node, goal, depth, visited, path,count):
        self.count = count
        if node == goal:
            path.append(node)
            return True
        if depth <= 0:
            return False
        
        visited.append(node)
        super().visit_show(visited,self.count)
        
        for neighbor in self.adjacency_list[node]:
            if neighbor not in visited:
                if self.dfs(neighbor, goal, depth - 1, visited, path,count):
                    self.count +=1
                    path.append(node)
                    return True

        return False


if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()
