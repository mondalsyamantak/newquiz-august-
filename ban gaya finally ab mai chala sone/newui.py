import customtkinter as ctk
import tkinter.messagebox as tkmb
import tkinter as tk
from ttkbootstrap import Style
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
from PIL import Image, ImageTk
import threading
import random
import html
#https://github.com/RoyChng/customtkinter-examples
import pywinstyles as pw
from CTkMessagebox import CTkMessagebox
import sys

import mysql.connector as cord

user=None
name=None
exp=None
highscore=0
no_of_quiz=0
i=0
class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x600")
        self.root.title("Quizzipedia")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.resizable(0,0)
        

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.mydb=cord.connect(
        host="localhost",
        user="root",
        password="password",
        database="oracle"
        )
        
        print(self.mydb)
        self.tablemaker()
        
    def tablemaker(self):
        cursor = self.mydb.cursor()
        
        #geography QUESTIONS TABLE
        query = '''CREATE TABLE IF NOT EXISTS geography (
        id INT AUTO_INCREMENT PRIMARY KEY,
        question TEXT NOT NULL,
        option1 VARCHAR(255) NOT NULL,
        option2 VARCHAR(255) NOT NULL,
        option3 VARCHAR(255) NOT NULL,
        option4 VARCHAR(255) NOT NULL,
        correct_option TINYINT NOT NULL
        )'''
        cursor.execute(query)
        
        
        query = "SELECT question FROM geography WHERE id = 1"
        cursor.execute(query)
        result = cursor.fetchone()
        print (result)
        
        if result is None:
            query='''INSERT INTO geography (question, option1, option2, option3, option4, correct_option) VALUES
            ("Which is the largest state in India by area?", "Uttar Pradesh", "Maharashtra", "Rajasthan", "Madhya Pradesh", 3),
            ("Which river is known as the Ganges of the South?", "Godavari", "Krishna", "Cauvery", "Narmada", 3),
            ("Which Indian state has the longest coastline?", "Tamil Nadu", "Maharashtra", "Gujarat", "Andhra Pradesh", 3),
            ("Which is the smallest state in India by area?", "Goa", "Sikkim", "Tripura", "Meghalaya", 1),
            ("Which is the highest peak in India?", "Nanda Devi", "Kanchenjunga", "Mount Everest", "K2", 2),
            ("Which state is known as the 'Land of Five Rivers'?", "Uttar Pradesh", "Punjab", "Haryana", "Bihar", 2),
            ("Which plateau lies between the Aravalli and Vindhya ranges?", "Chota Nagpur Plateau", "Deccan Plateau", "Malwa Plateau", "Bastar Plateau", 3),
            ("Which river flows through the Thar Desert?", "Yamuna", "Sutlej", "Luni", "Mahanadi", 3),
            ("Which state is known as the 'Spice Garden of India'?", "Kerala", "Tamil Nadu", "Andhra Pradesh", "Karnataka", 1),
            ("Which Indian state shares its border with China, Bhutan, and Nepal?", "Arunachal Pradesh", "Sikkim", "West Bengal", "Assam", 2),
            ("Which lake is the largest freshwater lake in India?", "Chilka Lake", "Wular Lake", "Pulicat Lake", "Dal Lake", 2),
            ("Which state is known as the 'Tea Garden of India'?", "Assam", "West Bengal", "Kerala", "Tamil Nadu", 1),
            ("Which river is the lifeline of the state of Jammu and Kashmir?", "Ganga", "Yamuna", "Jhelum", "Indus", 3),
            ("Which state is known as the 'Land of Rising Sun' in India?", "Assam", "Sikkim", "Arunachal Pradesh", "Nagaland", 3),
            ("Which state in India is known for its backwaters?", "Goa", "Kerala", "Tamil Nadu", "Karnataka", 2),
            ("Which city is known as the 'Silicon Valley of India'?", "Hyderabad", "Chennai", "Pune", "Bangalore", 4),
            ("Which mountain range forms the eastern boundary of the Deccan Plateau?", "Western Ghats", "Eastern Ghats", "Aravalli Range", "Satpura Range", 2),
            ("Which river is known as the 'Sorrow of Bihar'?", "Ganga", "Kosi", "Gandak", "Bagmati", 2),
            ("Which is the largest delta in the world?", "Nile Delta", "Mississippi Delta", "Ganges-Brahmaputra Delta", "Amazon Delta", 3),
            ("Which city is known as the 'City of Lakes' in India?", "Udaipur", "Nainital", "Bhopal", "Srinagar", 1),
            ("Which desert is located in India?", "Sahara Desert", "Thar Desert", "Kalahari Desert", "Gobi Desert", 2);
            '''
                
            cursor.execute(query)
                
                
                
                
        #sports QUESTIONS TABLE
        query = '''CREATE TABLE IF NOT EXISTS sports (
        id INT AUTO_INCREMENT PRIMARY KEY,
        question TEXT NOT NULL,
        option1 VARCHAR(255) NOT NULL,
        option2 VARCHAR(255) NOT NULL,
        option3 VARCHAR(255) NOT NULL,
        option4 VARCHAR(255) NOT NULL,
        correct_option TINYINT NOT NULL
        )'''
        cursor.execute(query)
        
        
        query = "SELECT question FROM sports WHERE id = 1"
        cursor.execute(query)
        result = cursor.fetchone()
        print (result)
        
        if result is None:
                query='''INSERT INTO sports (question, option1, option2, option3, option4, correct_option) VALUES
                ("Which country won the FIFA World Cup in 2018?", "Brazil", "Germany", "France", "Argentina", 3),
                ("In which sport is the term 'love' used?", "Basketball", "Tennis", "Football", "Cricket", 2),
                ("Who holds the record for the most home runs in a single MLB season?", "Barry Bonds", "Babe Ruth", "Hank Aaron", "Alex Rodriguez", 1),
                ("How many players are there in a rugby team?", "11", "13", "15", "17", 3),
                ("Which country hosts the Australian Open tennis tournament?", "USA", "UK", "France", "Australia", 4),
                ("In what year did the Boston Red Sox break the 'Curse of the Bambino'?", "2000", "2004", "2007", "2013", 2),
                ("Who is known as 'The King of Football'?", "Cristiano Ronaldo", "Lionel Messi", "Pele", "Diego Maradona", 3),
                ("Which team won the first Super Bowl?", "Dallas Cowboys", "Green Bay Packers", "New England Patriots", "Pittsburgh Steelers", 2),
                ("In which sport would you perform a slam dunk?", "Basketball", "Volleyball", "Soccer", "Tennis", 1),
                ("How many Grand Slam titles has Roger Federer won?", "18", "19", "20", "21", 3),
                ("Which country won the most medals in the 2016 Summer Olympics?", "China", "Great Britain", "Russia", "USA", 4),
                ("Who was the first athlete to run a mile in under 4 minutes?", "Roger Bannister", "Jesse Owens", "Usain Bolt", "Carl Lewis", 1),
                ("In which city were the 2012 Summer Olympics held?", "Beijing", "London", "Rio de Janeiro", "Tokyo", 2),
                ("Which NBA player is known as 'The Black Mamba'?", "Michael Jordan", "LeBron James", "Kobe Bryant", "Shaquille O'Neal", 3),
                ("Which country has won the most Cricket World Cups?", "India", "Australia", "West Indies", "England", 2),
                ("In which sport is the Stanley Cup awarded?", "Baseball", "Football", "Basketball", "Ice Hockey", 4),
                ("What is the national sport of Japan?", "Karate", "Sumo Wrestling", "Judo", "Kendo", 2),
                ("Which female tennis player has won the most Grand Slam titles?", "Serena Williams", "Steffi Graf", "Martina Navratilova", "Margaret Court", 4),
                ("How many holes are there in a standard round of golf?", "9", "12", "18", "24", 3),
                ("Which soccer player is known as 'The Hand of God'?", "Zinedine Zidane", "Diego Maradona", "Lionel Messi", "Cristiano Ronaldo", 2)
                '''
                
                cursor.execute(query)

        #movies QUESTIONS TABLE
        query = '''CREATE TABLE IF NOT EXISTS movies (
        id INT AUTO_INCREMENT PRIMARY KEY,
        question TEXT NOT NULL,
        option1 VARCHAR(255) NOT NULL,
        option2 VARCHAR(255) NOT NULL,
        option3 VARCHAR(255) NOT NULL,
        option4 VARCHAR(255) NOT NULL,
        correct_option TINYINT NOT NULL
        )'''
        cursor.execute(query)
        
        
        query = "SELECT question FROM movies WHERE id = 1"
        cursor.execute(query)
        result = cursor.fetchone()
        print (result)
        
        if result is None:
                query='''INSERT INTO movies (question, option1, option2, option3, option4, correct_option) VALUES
("Which movie features the journey to destroy the One Ring?", "The Hobbit", "The Chronicles of Narnia", "The Lord of the Rings: The Fellowship of the Ring", "Harry Potter and the Philosopher's Stone", 3),
("Who directed the movie 'Inception'?", "Steven Spielberg", "Christopher Nolan", "James Cameron", "Quentin Tarantino", 2),
("What is the name of the school of witchcraft and wizardry that Harry Potter attends?", "Ilvermorny", "Durmstrang", "Beauxbatons", "Hogwarts", 4),
("Which actor played Batman in 'The Dark Knight' trilogy?", "Ben Affleck", "Christian Bale", "Michael Keaton", "Robert Pattinson", 2),
("In the Marvel Cinematic Universe, who is the Norse god of thunder?", "Iron Man", "Thor", "Loki", "Hawkeye", 2),
("Which movie series is set in a dystopian future where humans are trapped in a simulated reality?", "The Matrix", "Terminator", "Blade Runner", "Mad Max", 1),
("Who played Jack Dawson in the movie 'Titanic'?", "Brad Pitt", "Tom Cruise", "Leonardo DiCaprio", "Johnny Depp", 3),
("Which movie features a group of superheroes including Iron Man, Captain America, and Thor?", "Justice League", "X-Men", "The Avengers", "Guardians of the Galaxy", 3),
("What is the name of the fictional African country in 'Black Panther'?", "Zamunda", "Wakanda", "Genovia", "Elbonia", 2),
("Who directed the 'Harry Potter' film series?", "David Yates", "Peter Jackson", "J.K. Rowling", "Alfonso Cuarón", 1),
("In 'Star Wars', who is the father of Luke Skywalker?", "Obi-Wan Kenobi", "Yoda", "Darth Vader", "Han Solo", 3),
("Which movie is based on the life of mathematician John Nash?", "A Beautiful Mind", "Good Will Hunting", "The Imitation Game", "The Theory of Everything", 1),
("Who played the character of Tony Stark in the Marvel Cinematic Universe?", "Chris Evans", "Chris Hemsworth", "Robert Downey Jr.", "Mark Ruffalo", 3),
("What is the title of the second 'Pirates of the Caribbean' movie?", "Dead Man's Chest", "On Stranger Tides", "At World's End", "The Curse of the Black Pearl", 1),
("Which actor voiced Woody in the 'Toy Story' series?", "Tom Hanks", "Tim Allen", "Billy Crystal", "John Goodman", 1),
("In 'The Matrix', what is Neo's real name?", "Thomas Anderson", "John Wick", "Peter Parker", "Bruce Wayne", 1),
("Which movie features the quote, 'I'll be back'?", "Terminator", "Predator", "Total Recall", "Commando", 1),
("Who directed the 'Jurassic Park' movie?", "George Lucas", "Steven Spielberg", "James Cameron", "Ridley Scott", 2),
("In 'The Lion King', what is the name of Simba's father?", "Mufasa", "Scar", "Timon", "Pumbaa", 1),
("Which movie is about a cowboy doll who feels threatened by a new spaceman action figure?", "Toy Story", "Small Soldiers", "Shrek", "Monsters, Inc.", 1);
                '''
                
                cursor.execute(query)
                
                
                
        query = '''CREATE TABLE IF NOT EXISTS Users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(225) NOT NULL,
        password VARCHAR(255) NOT NULL,
        exp INTEGER DEFAULT 0,
        name VARCHAR(255) NOT NULL,
        high_score INTEGER DEFAULT 0,
        no_of_quizzes INTEGER DEFAULT 0
        )'''
        cursor.execute(query)
        result = cursor.fetchone()
        print (result)
        
        self.intropage()
        
       
    def intropage(self):
        self.backimg=ctk.CTkImage(Image.open("back2c.png"), size=(900, 600)) 
        
        self.mainsf = ctk.CTkFrame(master=self.root, width=200, height=200, fg_color="#000001") #dashboard window
        self.mainsf.grid(row=0, column=0, sticky='nsew')
        self.mainimg=ctk.CTkLabel(master=self.mainsf, image=self.backimg, text=None)
        self.mainimg.place(x=0, y=0)
        pw.set_opacity(self.mainimg, value=0.8)
         
        self.mainframe=ctk.CTkFrame(master=self.mainsf, fg_color="#000001")
        self.mainframe.pack(fill='both', expand=True)
        
        self.backimg=ctk.CTkImage(Image.open("back2c.png"), size=(900, 600)) 
        
        self.text=ctk.CTkLabel(master=self.mainframe, text="Quizzipedia", font=("Showcard Gothic", 90), fg_color="#000001"  )
        self.text.pack(anchor='n', pady=(150, 10))
        
        self.animtxt=ctk.CTkLabel(master=self.mainframe, text="", font=("Serif", 20))
        self.animtxt.pack(pady=(0,40))
        
        self.enter=ctk.CTkButton(master=self.mainframe, text="Enter App", font=("Ariaf bold", 20), width=50, height=50, corner_radius=20, fg_color="#000001", 
                                 bg_color="#000001", border_color="white", border_width=2, text_color="white", command=self.method)
        self.enter.pack(anchor='n')
        
        global t1
        t1=threading.Thread(target=self.textchanger)
        
        t1.start()

        
    def method(self):
        global k
        self.animtxt.configure(state="disabled")
        str=self.animtxt.cget("text")
        self.animtxt.configure(text=str)
        self.createmore()

                

     
    # def textchanger(self):
    #     words=[" Test your knowledge ", " Test your iq ", " Sharpen your brain ", " Learn something new ", " Have fun while learning "]
    #     self.mainsf.after(600)
    #     global k
    #     k=0
    #     while k<100:
    #         #i=words[random.randint(0, len(words)-1)]
    #         i=words[k]
            
    #         #adding letters
    #         for j in range(0, len(i)):
    #             self.root.after(80, self.animtxt.configure(text=i[0:j]+"|"))
    #             self.animtxt.update()
            
    #         self.animtxt.configure(text=i[0:j]+" ")  
            
    #         #cursor blink
    #         for p in range(0, 2): 
    #             for op in range (0, 6):
    #                 self.mainsf.after(80, self.animtxt.configure(text=i[0:j]+" "))
    #                 if k>=100:
    #                     break

    #             if k>=100:
    #                 break
                
    #             for op in range (0, 6):
    #                 self.mainsf.after(80, self.animtxt.configure(text=i[0:j]+"|"))
    #                 if k>=100:
    #                     break
                    
    #             if k>=100:
    #                 break
    #         #removing letters
    #         if k>=100:
    #             break
    #         for j in range(0, len(i)):
    #             self.root.after(35, self.animtxt.configure(text=i[0:len(i)-j-1]+"|"))
    #             self.animtxt.update()
    #         self.mainsf.after(100)
    #         if k==len(words)-1:
    #             k=0
    #         else:
    #             k=k+1
        
        
 
    def textchanger(self):
        try:
            
            words=[" Test your knowledge ", " Test your iq ", " Sharpen your brain ", " Learn something new ", " Have fun while learning "]
            self.mainsf.after(600)
            global k
            k=0
            while k<100:
                #i=words[random.randint(0, len(words)-1)]
                i=words[k]
            
                #adding letters
                for j in range(0, len(i)):
                    self.root.after(50, self.animtxt.configure(text=i[0:j]+"|"))
                    self.animtxt.update()

                self.animtxt.configure(text=i[0:j]+" ")  

                #cursor blink
                for p in range(0, 3): 
                    for op in range (0, 6):
                        self.mainsf.after(70, self.animtxt.configure(text=i[0:j]+" "))
                        if k>=100:
                            break

                    if k>=100:
                        break
                
                    for op in range (0, 6):
                        self.mainsf.after(70, self.animtxt.configure(text=i[0:j]+"|"))
                        if k>=100:
                            break
                    
                    if k>=100:
                        break
                #removing letters
                if k>=100:
                    break
                for j in range(0, len(i)):
                    self.root.after(10, self.animtxt.configure(text=i[0:len(i)-j-1]+"|"))
                    self.animtxt.update()
                self.mainsf.after(100)
                if k==len(words)-1:
                    k=0
                else:
                    k=k+1
        except:
            pass
        
    def createmore(self):

        self.remover(self.mainframe)

        self.mainframe.destroy()
        global k
        k=900
            
        self.mainee=ctk.CTkFrame(master=self.mainsf, fg_color="#000001", bg_color="#000001")
        self.mainee.pack(fill='both', expand=True)
        
        self.mainee.grid_columnconfigure(0, weight=1)
        self.mainee.grid_columnconfigure(1, weight=1)
        
        pw.set_opacity(self.mainee, color="#000001")
        self.mainimg=ctk.CTkLabel(master=self.mainee, image=self.backimg, text=None)
        self.mainimg.place(x=0, y=0)
        pw.set_opacity(self.mainimg, value=0.8)


        self.frame = ctk.CTkFrame(master=self.mainee, fg_color="#000001")
        #self.frame.pack(pady=100, padx=300, fill='both', expand=True, side="left")#ui holder
        self.frame.grid(row=1, column=0, sticky='nsew', pady=120)
         
        pw.set_opacity(self.frame, color="#000001")
        
        self.label = ctk.CTkLabel(master=self.frame, text='Welcome back!', font=("Segoe UI Black", 35))
        self.label.pack(pady=0, padx=10)
        self.label = ctk.CTkLabel(master=self.frame, text='Sign in to continue', font=("Arial", 15))
        self.label.pack(pady=(0,12), padx=10)

        self.user_entry = ctk.CTkEntry(master=self.frame, 
                                       width=150, height=30, 
                                       placeholder_text="Username", placeholder_text_color="white", 
                                       corner_radius=12, border_width=1, border_color="white", bg_color="#000001", fg_color="#000001")
        self.user_entry.pack(pady=12, padx=10)

        self.user_pass = ctk.CTkEntry(master=self.frame, 
                                      width=150, height=30,
                                      placeholder_text="Password", show="*", placeholder_text_color="white",
                                      corner_radius=12, border_width=1, border_color="white", bg_color="#000001", fg_color="#000001")
        self.user_pass.pack(pady=12, padx=10)

        self.button = ctk.CTkButton(master=self.frame, text='Login', fg_color="#e44204", command=self.login)
        self.button.pack(pady=12, padx=10)
        self.button2 = ctk.CTkButton(master=self.frame, text='Not a user? Sign up!', fg_color="#000001", text_color="#e44204",  
                                     width=120, height=20, command=self.signup)
        self.button2.pack(padx=10)
        
        self.checkbox = ctk.CTkCheckBox(master=self.frame, text='Remember Me', checkbox_height=15, checkbox_width=15, border_width=1)
        self.checkbox.pack(pady=12, padx=10)
        
        
        self.adder(self.mainee)

    def remover(self, widg):
        global i
        i=20
        while True:
            widg.after(1, self.meth(widg, 'r'))
            if i<=0:
                break 
        widg.destroy()
        
    def adder(self, widg):
        global i
        i=0
        while True:
            widg.after(10, self.meth(widg, 'a'))
            if i>=20:
                break
            
    def meth(self, widg, ch):
        global i
        pw.set_opacity(widg, value=(i/20))
        if ch=='r':
            i=i-1
        else:
            i=i+1
        widg.update()
        return
    
    def signup(self):
        if 1==1:
            global user
            user=self.user_entry.get()
            global name
            name=ctk.CTkInputDialog(text="Type in a name", title="create Name").get_input()
            print(name)
            global exp
            exp=0
            
            #adding new to database:
            cursor = self.mydb.cursor()
            sql_insert_query = f"INSERT INTO Users (username,password,exp,Name) VALUES (%s, %s, %s, %s)"
            vals=(user,self.user_pass.get(),exp,name)
            
            # Execute the insert statement
            cursor.execute(sql_insert_query, vals)
            self.mydb.commit()
            
            
            self.remover(self.mainee) 

               
            self.mainee=ctk.CTkFrame(master=self.mainsf, fg_color="#000001", bg_color="#000001")
            self.mainee.pack(fill='both', expand=True)
            pw.set_opacity(self.mainee, color="#000001") 
            self.mainimg=ctk.CTkLabel(master=self.mainee, image=self.backimg, text=None)
            self.mainimg.place(x=0, y=0)
            pw.set_opacity(self.mainimg, value=0.8)
               
            self.textbox1=ctk.CTkLabel(master=self.mainee, text="Signing you up", font=("Arial bold", 30), bg_color="#000001")
            self.textbox1.pack(anchor='n',pady=(200,0))
            pw.set_opacity(self.textbox1, color="#000001")
            self.textbox2=ctk.CTkLabel(master=self.mainee, text="Please Wait", font=("Arial bold", 15), bg_color="#000001")
            self.textbox2.pack(anchor='n',pady=(20,0))
            pw.set_opacity(self.textbox2, color="#000001") 
            self.progress=ctk.CTkProgressBar(master=self.mainee, width=300, fg_color="purple")
            

            
            
            self.adder(self.mainee)
            
            for i in range(0,6):
                self.mainee.after(800, self.textbox2.configure(text=(self.textbox2.cget("text")+"."))) 
                self.textbox1.update()  
            self.open_dashboard()
        

    
    def login(self):
        username = self.user_entry.get()
        password=self.user_pass.get()
        cursor = self.mydb.cursor(buffered=True)
        query = "SELECT password FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        
        result = cursor.fetchone()

        if result:
            stored_password = result[0]
            if stored_password == password:
                print("Login successful!")
                global user
                user=username
                print(user)
                
                global name
                global exp
                global highscore
                global no_of_quiz
                cursor = self.mydb.cursor()
                query = "SELECT Name, exp, high_score, no_of_quizzes FROM users WHERE username = %s"
                cursor.execute(query, (username,))
                result = cursor.fetchone()
                name=result[0]
                print(name)
                exp=result[1]
                print(exp) 
                highscore=result[2]
                print(highscore)
                no_of_quiz=result[3]
                print(no_of_quiz)               
                
                
                
                self.confirm_action(0)
            else:
                print("Invalid password.")
                self.confirm_action(1)

    def confirm_action(self, k):
        if k == 0:
            #CTkMessagebox(message="Login successful",icon="check", option_1="Okay!")
            self.remover(self.mainee)
                
            self.mainee=ctk.CTkFrame(master=self.mainsf, fg_color="#000001", bg_color="#000001")
            self.mainee.pack(fill='both', expand=True)
            pw.set_opacity(self.mainee, color="#000001") 
            self.mainimg=ctk.CTkLabel(master=self.mainee, image=self.backimg, text=None)
            self.mainimg.place(x=0, y=0)
            pw.set_opacity(self.mainimg, value=0.8)
               
            self.textbox1=ctk.CTkLabel(master=self.mainee, text="LOGGING YOU IN", font=("Segoe UI Black", 30), bg_color="#000001")
            self.textbox1.pack(anchor='n',pady=(200,0))
            pw.set_opacity(self.textbox1, color="#000001")
            self.textboxwait=ctk.CTkLabel(master=self.mainee, text="Please Wait", font=("Helvetica", 15), bg_color="#000001")
            self.textboxwait.pack(anchor='n',pady=(10,0))
            pw.set_opacity(self.textboxwait, color="#000001")
            self.textbox2=ctk.CTkLabel(master=self.mainee, text="", font=("Segoe UI Black", 30), bg_color="#000001", text_color="red")
            self.textbox2.pack(anchor='n',pady=(200,0))
            pw.set_opacity(self.textbox2, color="#000001")
             
            
            self.adder(self.mainee)
            
            # def tocontinue1():
            #     print("cont1")
            #     self.textbox1.configure(text="Loading GUI")
            #     print("txt1")
            #     self.textbox2.destroy()
            #     print("txt2")
            #     self.progress.pack(anchor='n', pady=20)
            #     self.progress.set(0)
            #     for k in range(1,14):
            #         self.mainee.after(100, self.progress.set(k/10))
            #         self.progress.update()
            #         print(k/10)
                    
            #     self.textbox1.configure(text="Done!")    
            #     self.open_dashboard()
            
            for i in range(0,6):
                self.mainee.after(800, self.textbox2.configure(text=(self.textbox2.cget("text")+"."))) 
                self.textbox1.update()  
            # self.mainee.after(1500, tocontinue1)  
            self.mainee.after(200, self.textbox1.configure(text="Done!"))
            self.textbox1.update() 
            
            def delayfunc():
                self.mainee.after(3300)
                self.open_dashboard()
                
            delayfunc()
            
            
         


        elif k==1:
            CTkMessagebox(title="Error", message="Wrong username/password", icon="cancel")     

    def clear_options(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            
    def open_dashboard(self):
        
        self.remover(self.mainee)
        self.clear_options()
        DashPage(self.root)
        
    def open_dashboarddev(self):
        self.clear_options()
        DashPage(self.root)
            
            

class DashPage:
    def __init__(self, root):
        self.root = root
        self.btnState = False
        self.btnStateprof = False
        self.clr = 0
        self.wdth = 400
        self.root.configure(title="Welcome!")
        
        self.root.grid_rowconfigure(0, weight=0)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=0)

        ctk.set_appearance_mode("dark")
        
        #quiz window variables:
        self.current_question=0
        self.questions = []
        self.score = 0
        self.asked_questions = set()  # Track asked questions
        
        #Database connection:
        self.mydb=cord.connect(
        host="localhost",
        user="root",
        password="password",
        database="oracle"
        )
        
        print(self.mydb)


        self.label1 = ctk.CTkLabel(master=self.root, text="", image=ctk.CTkImage(Image.open("back1.jpg"), size=(900,600)), width=900, height=600) 
        self.label1.place(x=0, y=0)
        
        self.frame = ctk.CTkFrame(self.root, height=15, corner_radius=0, fg_color="transparent", bg_color="#000001")
        self.frame.grid(row=0, column=0, sticky='ew')#top label/bar
        
        self.mainsf = ctk.CTkFrame(master=self.root, width=200, height=200, fg_color="#000001") #dashboard window
        self.mainsf.grid(row=1, column=0, sticky='nsew')
        
        self.immage = ctk.CTkImage(Image.open("menu1.png"), size=(26, 26)) #collapsible sidebar image
        self.button1 = ctk.CTkButton(self.frame, image=self.immage, fg_color="transparent", bg_color="#000001", width=8, height=8, text=None, hover_color="#999999", 
                                     command=self.switchsidebar)
        self.button1.pack(side="left", padx=5, pady=5) #collapsible sidebar button
        
        self.image2 = ctk.CTkImage(Image.open("prof2.png"), size=(24, 24))
        self.theme = ctk.CTkButton(self.frame, image=self.image2, fg_color="transparent",  bg_color="#000001", width=8, height=8, text=None, hover_color="#999999", 
                                   command=lambda: self.launcher(self.sf, self.createprofilewidgets))
        self.theme.pack(side="right", pady=5, padx=5) #theme change button--->profile view button
        
        self.createdashwidgets()
        
        
    def quiz_initialize(self):
        self.current_question=0
        self.questions = []
        self.score = 0
        self.asked_questions = set()
        
    def createdashwidgets(self): 
        self.quiz_initialize  
        

        
        self.labelidek = ctk.CTkLabel(master=self.mainsf, text="", image=ctk.CTkImage(Image.open("back1.jpg"), size=(900,600)), width=900, height=600) 
        self.labelidek.place(x=0, y=-45)
        # pw.set_opacity(self.label1, value=1)
        
        self.sf=ctk.CTkFrame(master=self.mainsf)
        self.sf.pack(fill='both', expand=True)
        
        pw.set_opacity(self.frame, color="#000001")
        
        #designing the sidebar:
        self.nav_frame = ctk.CTkFrame(master=self.root, width=300, height=1000)
        self.nav_frame.place(x=-300, y=0) #collapsible sidebar
        self.nav_frame.grid_rowconfigure(0, weight=0)
        self.nav_frame.grid_rowconfigure(1, weight=1)
        self.nav_frame.grid_columnconfigure(0, weight=1)
        
        self.label0 = ctk.CTkLabel(master=self.nav_frame, text="", image=ctk.CTkImage(Image.open("sidebar4.jpg"), size=(300,600)), width=300, height=600) 
        self.label0.place(x=0, y=0)
        
        self.nav_framebar = ctk.CTkFrame(self.nav_frame, height=15, border_width=1, border_color="dark red", bg_color="#000001")
        self.nav_framebar.grid(row=0, column=0, sticky='ew')#top bar of collapsible side bar
        pw.set_opacity(self.nav_frame, color="#000001")
        self.labelm = ctk.CTkLabel(master=self.nav_framebar, text="", image=ctk.CTkImage(Image.open("sidebar4.jpg"), size=(300,600)), width=300) 
        self.labelm.place(x=0, y=0)
        pw.set_opacity(self.labelm, value=0.5)

        self.button2 = ctk.CTkButton(self.nav_framebar, image=self.immage, fg_color="transparent", bg_color="#000001", width=10, text=None, command=self.switchsidebar)
        self.button2.pack(side="left", pady=5, padx=5)#close btn of collapsible side bar
        pw.set_opacity(self.button2, color="#000001")
        
        self.barpg = ctk.CTkFrame(master=self.nav_frame, width=300, border_color="white", bg_color="#000001", height=900)
        self.barpg.grid(row=1, column=0, sticky='nsew')
        pw.set_opacity(self.barpg, color="#000001")
        self.label2 = ctk.CTkLabel(master=self.barpg, text="", image=ctk.CTkImage(Image.open("sidebar4.jpg"), size=(300,600)), width=300) 
        self.label2.place(x=0, y=0)
        pw.set_opacity(self.label2, value=1.5)

        
        self.imgprof = ctk.CTkImage(Image.open("avatars/avatar.png"), size=(100, 100))
        
        #buttons for sidebar:
        self.imgprofile = ctk.CTkImage(Image.open("prof2.png"), size=(20, 20))
        self.imgeye=ctk.CTkImage(Image.open("eye.png"), size=(20, 20))
        self.imgrank=ctk.CTkImage(Image.open("rank.png"), size=(20, 20))
        self.btn1=ctk.CTkButton(master=self.barpg, image=self.imgprofile, text="View Profile", font=("Helvetica", 20), width=300, height=60, fg_color="#000001"
                                , text_color="white", border_color="black", border_width=1 , compound="left", corner_radius=0
                                , hover_color="dark red", command=lambda: self.launcher(self.sf, self.createprofilewidgets))
        self.btn1.place(x=0, y=0)
        self.btn2=ctk.CTkButton(master=self.barpg, image=self.imgrank, text="Leaderboard", font=("Helvetica", 20), width=300, height=60, fg_color="#000001"
                                , text_color="white", border_color="black", border_width=1 , compound="left",corner_radius=0
                                , hover_color="dark red", command=lambda: self.launcher(self.sf, self.createleaderboard))
        self.btn2.place(x=0, y=60)
        self.btn3=ctk.CTkButton(master=self.barpg, text="Exit", font=("Helvetica", 20), width=300, height=60, fg_color="#000001"
                                , text_color="white", border_color="black", border_width=1 , compound="left", corner_radius=0
                                , hover_color="dark red", command=lambda: self.launcher(self.sf, sys.exit()))
        self.btn3.place(x=0, y=120)
        pw.set_opacity(self.btn1, color="#000001")  
        pw.set_opacity(self.btn2, color="#000001")  
        pw.set_opacity(self.btn3, color="#000001")   
        
        
        #=====================================================================================================================
        
        #designing dashboard: #self.sf declared above
        self.label1 = ctk.CTkLabel(master=self.sf, text="", image=ctk.CTkImage(Image.open("back1.jpg"), size=(900,600)), width=900, height=600) 
        self.label1.place(x=0, y=-45)
        pw.set_opacity(self.label1, value=1)
        
        # pw.set_opacity(self.sf, value=0.5, color="#000001")
        
        self.yourstats=ctk.CTkLabel(master=self.sf, text="Your Stats", font=("Arial Bold", 20), justify="left", text_color="white", bg_color="#000001")
        self.yourstats.pack(anchor="w", pady=(20, 18), padx=(56,0))
        pw.set_opacity(self.yourstats, color="#000001")
        
        self.stats_frame = ctk.CTkFrame(master=self.sf, fg_color="transparent", bg_color="#000001")
        self.stats_frame.pack(padx=(50, 0), pady=(18, 0), anchor="nw")
        pw.set_opacity(self.stats_frame, color="#000001")

        self.quizzes_taken_frame = ctk.CTkFrame(master=self.stats_frame, fg_color="#70179A", width=250, height=100, corner_radius=12, bg_color="#000001")
        self.quizzes_taken_frame.pack_propagate(0)
        self.quizzes_taken_frame.pack(anchor="w", side="left", padx=(0, 25))
        pw.set_opacity(self.quizzes_taken_frame, color="#000001")

        ctk.CTkLabel(master=self.quizzes_taken_frame, text="Quizzes Taken", font=("Arial Bold", 10), text_color="#F3D9FF").pack(anchor="nw", padx=(14,0))
        ctk.CTkLabel(master=self.quizzes_taken_frame, text=f"{no_of_quiz}", justify="left",  font=("Arial Bold", 25), text_color="#F3D9FF").pack(anchor="nw", padx=(14, 0))

        self.total_exp_frame = ctk.CTkFrame(master=self.stats_frame, fg_color="#146C63", width=250, height=100, corner_radius=8, bg_color="#000001")
        self.total_exp_frame.pack_propagate(0)
        self.total_exp_frame.pack(anchor="w", side="left", padx=(0, 25))
        pw.set_opacity(self.total_exp_frame, color="#000001")

        ctk.CTkLabel(master=self.total_exp_frame, text="Total EXP", font=("Arial Bold", 10), text_color="#D5FFFB").pack(anchor="nw", padx=(14,0))
        ctk.CTkLabel(master=self.total_exp_frame, text=f"{exp}", justify="left",  font=("Arial Bold", 25), text_color="#D5FFFB").pack(anchor="nw", padx=(14, 0))

        self.highest_score_frame = ctk.CTkFrame(master=self.stats_frame, fg_color="#9A1717", width=250, height=100, corner_radius=8, bg_color="#000001")
        self.highest_score_frame.pack_propagate(0)
        self.highest_score_frame.pack(anchor="w", side="left", padx=(0, 20))
        pw.set_opacity(self.highest_score_frame, color="#000001")

        ctk.CTkLabel(master=self.highest_score_frame, text="Highest Score", font=("Arial Bold", 10), text_color="#FFCFCF").pack(anchor="nw", padx=(14,0))
        ctk.CTkLabel(master=self.highest_score_frame, text=f"{highscore}", justify="left",  font=("Arial Bold", 25), text_color="#FFCFCF").pack(anchor="nw", padx=(14, 0))

        self.takeaquiz=ctk.CTkLabel(master=self.sf, text="Take A Quiz", font=("Arial Bold", 20), bg_color="#000001")
        self.takeaquiz.pack(anchor='w', side="top", padx=(56,0), pady=(43, 0))
        pw.set_opacity(self.takeaquiz, color="#000001")

        self.quizzes_frame = ctk.CTkFrame(master=self.sf, fg_color="transparent",bg_color="#000001")
        self.quizzes_frame.pack(anchor='w', side="left", pady=(0, 0), padx=(50, 50), fill='both', expand=True)
        pw.set_opacity(self.quizzes_frame, color="#000001")
        self.quizzes_frame.grid_rowconfigure(0, weight=1)
        self.quizzes_frame.grid_rowconfigure(1, weight=1)
        self.quizzes_frame.grid_columnconfigure(0, weight=1)
        self.quizzes_frame.grid_columnconfigure(1, weight=1)
        self.quizzes_frame.grid_columnconfigure(2, weight=1)

        self.movies_img_data = Image.open("movies-quiz-bg.png")
        self.movies_img = ctk.CTkImage(light_image=self.movies_img_data, dark_image=self.movies_img_data, size=(234,91))
        self.moviebtn=ctk.CTkButton(master=self.quizzes_frame, image=self.movies_img, text=None, corner_radius=12, fg_color="transparent", 
                                    hover_color="#000001",bg_color="#000001", command=lambda: self.launcher(self.sf, self.countdown_page("movies")))
        self.moviebtn.grid(row=0, column=0, padx=(0,0), pady=(0,0))

        # pw.set_opacity(self.moviebtn, color="#000001")


        self.sports_img_data = Image.open("sports-quiz-bg.png")
        self.sports_img = ctk.CTkImage(light_image=self.sports_img_data, dark_image=self.sports_img_data, size=(234,91))
        self.sportsbtn=ctk.CTkButton(master=self.quizzes_frame, text=None, image=self.sports_img, fg_color="transparent", hover_color="#000001",bg_color="#000001",
                                     command=lambda: self.launcher(self.sf,lambda: self.countdown_page("sports")))
        self.sportsbtn.grid(row=0, column=1, padx=(10,0), pady=(0,0), sticky='w')
        
        
        self.geography_img_data = Image.open("geography-quiz-bg.png")
        self.geography_img = ctk.CTkImage(light_image=self.geography_img_data, dark_image=self.geography_img_data, size=(175,210))
        self.geographybtn=ctk.CTkButton(master=self.quizzes_frame, text=None, image=self.geography_img, fg_color="transparent", hover_color="#000001",
                                        bg_color="#000001", command=lambda: self.launcher(self.sf,lambda: self.countdown_page("geography")))
        self.geographybtn.grid(row=0, rowspan=2, column=2, padx=(10,0), pady=30, sticky='nw')
        
        self.leaderboardbtn=ctk.CTkButton(master=self.quizzes_frame, text="Show Leaderboard", font=("Arial Bold", 20), corner_radius=14, border_color="blue", 
                                       height=70, width=520, bg_color="#000001", text_color="white", fg_color="#C8ACD6", 
                                       command=lambda: self.launcher(self.sf, self.createleaderboard))
        self.leaderboardbtn.grid(row=1, column=0, columnspan=2, padx=(30,0), pady=(10,0), sticky='wn')
        self.adder(self.mainsf)

        return self.sf
    
    def createquizselection(self):
        
        self.quizselwind = ctk.CTkFrame(master=self.mainsf, width=200, height=200)
        self.quizselwind.grid(row=1, column=0, sticky='nsew')
        self.label1 = ctk.CTkLabel(master=self.quizselwind, text="", image=ctk.CTkImage(Image.open("back1.jpg"), size=(900,600)), width=900, height=600) 
        self.label1.place(x=0, y=-45)
        
        
        self.selectquiz=ctk.CTkLabel(master=self.quizselwind, text="Select a Quiz", font=("Arial Bold", 20), justify="left", text_color="white", bg_color="#000001")
        self.selectquiz.pack(anchor="w", pady=(20, 0), padx=56)
        pw.set_opacity(self.selectquiz, color="#000001")
        
        self.opt=ctk.CTkFrame(master=self.quizselwind, fg_color="#000001")
        self.opt.pack(anchor='n', fill='both', padx=30, pady=20, expand=True)
        pw.set_opacity(self.opt, color="#000001")
        self.opt.grid_columnconfigure(0, weight=1)
        self.opt.grid_columnconfigure(1, weight=1)
        
        self.movies=ctk.CTkButton(master=self.opt, text="Movies", font=("Arial Bold", 18), height=80, text_color="black", fg_color="#efc1db")
        self.movies.grid(row=0, column=0, sticky='nsew', padx=(20,10), pady=20)
        
        self.geography=ctk.CTkButton(master=self.opt, text="Geography", font=("Arial Bold", 18), height=80, fg_color="#85c64b", 
                                     command=lambda: self.launcher(self.quizselwind, self.createdashwidgets ))
        self.geography.grid(row=0, column=1, sticky='nsew', padx=(10,20), pady=20)
        
        self.theme.configure(command=lambda: self.launcher(self.quizselwind, self.createprofilewidgets))
        
        self.adder(self.quizselwind)


                
    def createprofilewidgets(self):
        
        self.profwind=ctk.CTkFrame(master=self.mainsf)
        self.profwind.pack(fill='both', expand=True)
        self.label5 = ctk.CTkLabel(master=self.profwind, text="", image=ctk.CTkImage(Image.open("back1.jpg"), size=(900,600)), width=900, height=600) 
        self.label5.place(x=0, y=-45)
        pw.set_opacity(self.label5, value=1)
        self.profwind.grid_rowconfigure(0, weight=0)
        self.profwind.grid_rowconfigure(1, weight=1)
        self.profwind.grid_columnconfigure(0, weight=1)

        
        self.holder=ctk.CTkFrame(master=self.profwind, border_width=0, border_color="black", fg_color="#000001", bg_color="#000001")
        self.holder.pack(anchor='n', padx=30, pady=10, fill='x')
        pw.set_opacity(self.holder, color="#000001")
        
        
        self.imgprof = ctk.CTkImage(Image.open("avatars/avatar.png"), size=(90, 90))
        self.pic = ctk.CTkLabel(master=self.holder, image=self.imgprof, height=50, width=50, fg_color="transparent", text=None, bg_color="#000001")
        self.pic.pack(side="left", pady=20, padx=20)
        pw.set_opacity(self.pic, color="#000001")
        
        global user
        global name
        global exp
        
        # self.userinfo=ctk.CTkFrame(self.holder, bg_color="transparent", fg_color="transparent")
        # self.userinfo.pack(side="left", fill='y',expand=True )
        
        self.username = ctk.CTkLabel(master=self.holder, text=f"Name: {name}", font=("Arial bold", 17), bg_color="#000001")
        self.username.pack(anchor='w', side="top", padx=20, pady=(30,0))
        pw.set_opacity(self.username, color="#000001")
        
        self.name = ctk.CTkLabel(master=self.holder, text=f"Username: {user}", font=("Arial bold", 12), bg_color="#000001")
        self.name.pack(anchor='w', side="top", padx=20, pady=0)
        pw.set_opacity(self.name, color="#000001")
        
        self.exp = ctk.CTkLabel(master=self.holder, text=f"Level: {exp//500}    Total EXP: {exp}", font=("Arial bold", 12), text_color="#f56dff", bg_color="#000001")
        self.exp.pack(anchor='w', side="top", padx=20, pady=0)
        pw.set_opacity(self.name, color="#000001")
        
        self.progressbar = ctk.CTkProgressBar(master=self.holder, orientation="horizontal", width=250, progress_color="#f56dff")
        self.progressbar.set((exp%500)/500)
        self.progressbar.pack(anchor='w', side="top", padx=20, pady=0)
        self.history=ctk.CTkLabel(master=self.profwind, text="History: ", font=("Arial bold", 20), justify="left", bg_color="#000001")
        self.history.pack(anchor='nw', padx=56, pady=10)
        pw.set_opacity(self.history, color="#000001")
   
        self.mainpframe = ctk.CTkFrame(master=self.profwind, width=360, height=1000, border_width=0, border_color="black", fg_color="#000001", bg_color="#000001")
        self.mainpframe.pack(anchor='nw', side="top", padx=30, pady=10, fill='both', expand=True)
        pw.set_opacity(self.mainpframe, color="#000001")
        
        self.btn=ctk.CTkButton(master=self.holder, text="Back", height=20, width=60, fg_color="red", bg_color="#000001", 
                               command=lambda: self.launcher(self.profwind, self.createdashwidgets))
        self.btn.pack(anchor='s', side="right", pady=10, padx=30)
        self.adder(self.mainsf)
        
        return self.profwind
    
    
    def createleaderboard(self):
        self.leaderwind=ctk.CTkFrame(master=self.mainsf)
        self.leaderwind.pack(fill='both', expand=True)
        self.label69 = ctk.CTkLabel(master=self.leaderwind, text="", image=ctk.CTkImage(Image.open("back1.jpg"), size=(900,600)), width=900, height=600) 
        self.label69.place(x=0, y=-45)
        
        
        self.ld=ctk.CTkLabel(master=self.leaderwind, text="Leaderboard", font=("Arial bold", 30), bg_color="#000001")
        self.ld.pack(padx=60, pady=(20,0))
        pw.set_opacity(self.ld, color="#000001")
        
        self.leaderboard=ctk.CTkFrame(master=self.leaderwind, border_width=2, fg_color="#000001")
        self.leaderboard.grid_columnconfigure(0, weight=1)
        self.leaderboard.grid_columnconfigure(1, weight=1)
        self.leaderboard.grid_columnconfigure(2, weight=1)
        self.leaderboard.grid_columnconfigure(3, weight=1)
        self.leaderboard.pack(padx=130, pady=20, side="top", fill='both', expand=True)
        pw.set_opacity(self.leaderboard, color="#000001")
        
        self.wtf=ctk.CTkFrame(master=self.leaderboard, width=640, height=3300, fg_color="red")
        self.wtf.place(x=0, y=0)
        pw.set_opacity(self.wtf, value=0.5)
        

        
        self.usernames=ctk.CTkLabel(master=self.leaderboard, text="Usernames", font=("Arial bold", 20), bg_color="#000001")
        self.usernames.grid(row=1, column=0, padx=20, pady=(30,0))
        pw.set_opacity(self.usernames, color="#000001")
        print("ok")
        
        self.EXP=ctk.CTkLabel(master=self.leaderboard, text="User EXP", font=("Arial bold", 20), bg_color="#000001")
        self.EXP.grid(row=1, column=1, padx=20, pady=(30,0))
        pw.set_opacity(self.EXP, color="#000001")
        
        self.high_score=ctk.CTkLabel(master=self.leaderboard, text="High Scores", font=("Arial bold", 20), bg_color="#000001")
        self.high_score.grid(row=1, column=2, padx=20 , pady=(30,0))
        pw.set_opacity(self.high_score, color="#000001")
        
        self.noofq=ctk.CTkLabel(master=self.leaderboard, text="No. of Quizzes", font=("Arial bold", 20), bg_color="#000001")
        self.noofq.grid(row=1, column=3, padx=20, pady=(30,0))
        pw.set_opacity(self.noofq, color="#000001")
        

        
        # #chatgpt:
        
        cursor = self.mydb.cursor()
        cursor.execute("SELECT username, exp, high_score, no_of_quizzes FROM Users ORDER BY exp DESC")
        rows = cursor.fetchall()

        row_num = 2  # Starting row for the data

        for row in rows:
            username_label = ctk.CTkLabel(master=self.leaderboard, text=row[0], font=("Arial", 16), bg_color="#000001")
            username_label.grid(row=row_num, column=0, pady=(20, 20),padx=(20, 20))
            pw.set_opacity(username_label, color="#000001")

            exp_label = ctk.CTkLabel(master=self.leaderboard, text=row[1], font=("Arial", 16), bg_color="#000001")
            exp_label.grid(row=row_num, column=1, pady=(20, 20),padx=(20, 20))
            pw.set_opacity(exp_label, color="#000001")

            profileimage_label = ctk.CTkLabel(master=self.leaderboard, text=row[2], font=("Arial", 16), bg_color="#000001")
            profileimage_label.grid(row=row_num, column=2, pady=(20, 20),padx=(20, 20))
            pw.set_opacity(profileimage_label, color="#000001")

            name_label = ctk.CTkLabel(master=self.leaderboard, text=row[3], font=("Arial", 16), bg_color="#000001")
            name_label.grid(row=row_num, column=3, pady=(20, 20),padx=(20, 20))
            pw.set_opacity(name_label, color="#000001")

            row_num += 1
            
        self.btn=ctk.CTkButton(master=self.leaderwind, text="Back", height=50, width=50, fg_color="red", bg_color="#000001", 
                               command=lambda: self.launcher(self.leaderwind, self.createdashwidgets))
        self.btn.pack(side="right", pady=10, padx=30)
        pw.set_opacity(self.btn, color="#000001")

        
        self.adder(self.leaderwind)
        
    def switchsidebar(self):
        self.nav_frame.lift()
        if self.btnState is True:
            self.btnState = False
            for i in range(0, 401, 2):
                self.nav_frame.place(x=-i, y=0)
                self.root.update()
        else:
            for i in range(-400, 0):
                self.nav_frame.place(x=i, y=0)
                self.root.update()
            self.btnState = True


    def countdown_page(self, topic):
        self.quiz_initialize()
        self.cdpage = ctk.CTkFrame(master=self.mainsf)
        self.cdpage.pack(fill='both', expand=True)
    
        # Background image
        background_image = ctk.CTkImage(Image.open("back1.jpg"), size=(900,600))
        self.label1 = ctk.CTkLabel(master=self.cdpage, text="", image=background_image, width=900, height=600)
        self.label1.place(x=0, y=-45)
    
        # Countdown label
        self.count = ctk.CTkLabel(master=self.cdpage, text="", font=("Arial bold", 90), wraplength=800, bg_color="#000001")
        self.count.pack(pady=(200,20))
        pw.set_opacity(self.count, color="#000001")
    
        # Function to update countdown
        def update_countdown(count):
            self.count.configure(text=str(count))
    
        # Countdown sequence

    
        # Start the countdown
        self.start_countdown(topic)
        self.theme.configure(command=lambda: self.launcher(self.cdpage, self.createprofilewidgets))

    def start_countdown(self, topic):
        self.adder(self.cdpage)
        self.cdpage.after(2000, lambda: self.count.configure(text=str(3)))
        self.cdpage.after(3000, lambda: self.count.configure(text=str(2)))
        self.cdpage.after(4000, lambda: self.count.configure(text=str(1)))
        self.cdpage.after(5000, lambda: self.count.configure(text=str("GO")))
        self.cdpage.after(6000, self.create_quizwidgets, topic)

    def create_quizwidgets(self, topic):
        try:
            self.cdpage.destroy()
        except:
            print('hmm')
        
        self.quizpage=ctk.CTkFrame(master=self.mainsf)
        self.quizpage.pack(fill='both', expand=True)
        self.label1 = ctk.CTkLabel(master=self.quizpage, text="", image=ctk.CTkImage(Image.open("back1.jpg"), size=(900,600)), width=900, height=600) 
        self.label1.place(x=0, y=-45)
        
        self.qnprogress=ctk.CTkProgressBar(master=self.quizpage, width=600, progress_color="yellow")
        self.qnprogress.pack(pady=(20,0))
        self.qnprogress.set(0)
        
        self.questions_label = ctk.CTkLabel(master=self.quizpage, text="", font=("Arial bold", 20), wraplength=800, bg_color="#000001")
        self.questions_label.pack(pady=(30,20))
        pw.set_opacity(self.questions_label, color="#000001")
        
        self.adder(self.mainsf)
        
        self.get_questions(topic)
        self.theme.configure(command=lambda: self.launcher(self.quizpage, self.createprofilewidgets))
        
        

    def get_questions(self, topic, amount=10):
        self.cursor = self.mydb.cursor(dictionary=True)
        self.cursor.execute(f"SELECT * FROM {topic} WHERE id NOT IN (%s) ORDER BY RAND() LIMIT %s",
                                (",".join(map(str, self.asked_questions)), amount))
        self.questions = self.cursor.fetchall()
        self.display_question()

    def display_question(self):
        self.qnprogress.set((self.current_question+1)/10)
        self.qnprogress.update()
        
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.questions_label.configure(text=f"Q.{self.current_question+1}:{html.unescape(question['question'])}")

            options = [question['option1'], question['option2'], question['option3'], question['option4']]
            options = [html.unescape(option) for option in options]
            correct_answer = html.unescape(options[question['correct_option'] - 1])

            for i in options:
                option_button = ctk.CTkButton(master=self.quizpage, text=i, font=("Arial bold", 15), fg_color="#efc1db", bg_color="#000001", text_color="black", width=300, height=40)
                option_button.configure(command=lambda ans=i: self.check_answer(ans, correct_answer))
                option_button.pack(pady=10)
        else:
            self.end_quiz()
            
        self.adder(self.quizpage)

    def check_answer(self, selected_answer, correct_answer):
        for widget in self.quizpage.winfo_children():
            if isinstance(widget, ctk.CTkButton):
                if widget.cget("text") == selected_answer:
                    if selected_answer == correct_answer:
                        widget.configure(fg_color="#7FFF7F")  # Green for correct answer
                    else:
                        widget.configure(fg_color="#FF7F7F")  # Red for wrong answer
                elif widget.cget("text") == correct_answer:
                    widget.configure(fg_color="#7FFF7F")
                widget.configure(state="disabled")
        if selected_answer == correct_answer:
            self.score += 1
        self.next_button = ctk.CTkButton(self.quizpage, text="Next", font=("Arial", 10), fg_color="yellow", text_color="black", command=self.next_question)
        self.next_button.pack(pady=(20, 20))

    def next_question(self):
        self.remover(self.quizpage)
        self.current_question += 1
        self.clearoptions()
        self.display_question()

    def clearoptions(self):
        for widget in self.quizpage.winfo_children():
            if isinstance(widget, ctk.CTkButton):
                widget.destroy()

    def end_quiz(self):

        self.questions_label.configure(text=f"Quiz over! Your score is: {self.score}\n{self.score*10} EXP has been added to your account!")
        global exp
        global user
        print(self.score)
        
        global highscore
        if highscore<self.score:
            highscore=self.score
            
        global no_of_quiz
        no_of_quiz+=1
        
        exp=exp+(self.score*10)
        for widget in self.quizpage.winfo_children():
            if isinstance(widget, ctk.CTkButton):
                widget.destroy()
        self.qnprogress.destroy()
        self.backbtn=ctk.CTkButton(self.quizpage, text="Go back", font=("Arial bold", 16), width=120, height=60, corner_radius=8, 
                                   fg_color="#efc1db", text_color="black", command=lambda: self.launcher(self.quizpage, self.createdashwidgets))
        self.backbtn.pack(pady=20)
        if self.cursor:
            sql = "UPDATE Users SET exp = %s, high_score= %s, no_of_quizzes= %s WHERE username = %s"
            values = (exp,highscore, no_of_quiz,user)
            self.cursor.execute(sql, values)
            self.mydb.commit()
            print(f"Updated user {user} with new exp {exp}")


#============================================================================================================================================ 
 
        
        
#Animations:
 
    def launcher(self, prevw, funct):
        self.remover(prevw)
        prevw.update()
        for widget in prevw.winfo_children():
            widget.destroy()
        # if prevw !=self.mainsf: 
        #     prevw.destroy()
        prevw.destroy()
        try:
            funct()
            print("opt1")
        except:
            funct
            print("opt2")
            
        # newwidg=funct()
        # print("profile created, starting new func")
        # pw.set_opacity(newwidg, value=0)
        # newwidg.after(101, self.newmeth(newwidg, funct))  
        
    # def newmeth(self, newwidg, funct):
    #     self.adder(newwidg)
    #     print("function ends")
    #     if newwidg!=self.sf:
    #         funct()
                   
    def meth(self, widg, ch):
        global i
        pw.set_opacity(widg, value=(i/10))
        if ch=='r':
            i=i-1
        else:
            i=i+1
        widg.update()
        return

    def adder(self, widg):
        global i
        i=0
        while True:
            widg.after(10, self.meth(widg, 'a'))

            if i>=10:
                break
        
    def remover(self, widg):
        global i
        i=10
        while True:
            widg.after(10, self.meth(widg, 'r'))

            if i<=0:
                break  
            
#=============================================================================================================================================== 

    def updateinfo(self):
        global user
        
        update_query = """
        UPDATE Users
        SET high_score = %s, no_of_quizzes = %s
        WHERE username = %s;
        """
        values = (highscore, no_of_quiz, user)
        self.cursor.execute(update_query, values)
        self.mydb.commit()
        print("User stats updated successfully.")
    
    

if __name__ == "__main__":
    app = ctk.CTk()
    LoginPage(app)
    app.mainloop()

