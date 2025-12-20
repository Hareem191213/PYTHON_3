#window making
import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import json
import os
import matplotlib.pyplot as plt

screen= tk.Tk()
screen.title("Average Calculator!")
screen.geometry("10500x10500")
screen.config(bg= "lightblue")
#label top main title
txt=tk.Label(screen, text="AVERAGE CALCULATOR!!!🧮" , font=("Poor Richard" , 17 , "bold"), fg="navy" , bg="lightblue")
txt.pack(pady=5)

#another sentence
txt=tk.Label(screen, text="Let's Calculate Your Amazing Grades!" , font=("Courier New" , 14  , "italic", "bold"), fg="darkblue" , bg="lightblue")
txt.pack(pady=3)

#INPUT MAKING:
#input_1:subject:!!
input_frame=tk.Frame(screen, bg="lightcyan" , relief="solid", borderwidth=3 )
input_frame.pack(pady=5)
subject_intro= tk.Label(input_frame , text= "Enter your subject!📕", bg="lightblue" , font=("Courier New" , 12 ), fg="navy")
subject_intro.pack(pady=5)
subject_entry=tk.Entry(input_frame , bg="White" , font=("Courier New" , 10 ), width=15)
subject_entry.pack(pady=3)
#input_2:marks:!!
input_frame2=tk.Frame(screen, bg="lightcyan" , relief="solid" , borderwidth=3 )
input_frame2.pack(pady=5)
marks_intro=tk.Label(input_frame2 , text= "Enter your marks!🔢" , bg="lightblue" , font=("Courier New" , 14), fg="navy")
marks_intro.pack(pady=5)
marks_entry=tk.Entry(input_frame2 , bg="white" , font=("Courier New" , 10 ), width=15)
marks_entry.pack(pady=3)

#scroller
display=scrolledtext.ScrolledText(screen , bg="lightcyan" ,font=("Gabriola" , 12) , fg="black" , borderwidth=3 , relief="solid", height=5, width=32)
display.pack(pady=5,padx=5, fill=tk.BOTH , expand=False)
def update_display(text):#helper
    display.config(state="normal")
    display.delete("1.0" , tk.END)
    display.insert(tk.END , text)
    display.config(state="disabled")

#important
grades_file= "grades_history.json"

#FUNCTIONS:
#saving the grades
def save_grades():
    try:
        with open(grades_file, "w")as f:
            json.dump(grades_list , f , indent=2)
        update_display("Grades saved Successfully!")
    except Exception as e:
        update_display(f"❌ Error saving grades: {str(e)}")
#loading the grades
def load_grades():
    global grades_list
    try:
        if os.path.exists(grades_file):
            with open (grades_file , "r") as f:
                grades_list=json.load(f)
            show_grade()
            update_display(f"✅ Loaded {len(grades_list)} grades successfully!")
        else:
            update_display("📝 No saved grades found. Start by adding new grades!")
    except Exception as e:
        update_display(f"❌ Error loading grades: {str(e)}")
 #deleting(clearing the grades):       
def clear_all_grades():
    global grades_list
    if os.path.exists(grades_file):
        os.remove(grades_file)
    update_display("All grades removed!🗑️")
    subject_entry.delete(0 , tk.END)
#calculating average
grades_list=[]
def add_grades():
    subject=subject_entry.get().strip()
    marks=marks_entry.get().strip()
    if subject and marks:
        try:
            mark_number=float(marks)
            if 0 <= mark_number <= 100:
                # e.g[(subject, marks )(subject_2 , marks_2)] list of tupples
                grades_list.append((subject , mark_number))
                show_grade()
                subject_entry.delete(0 , tk.END)
                marks_entry.delete(0 , tk.END)
            else:
                update_display("Plese enter the grades between zero and hundred1️⃣")
        except ValueError:
            update_display("Please enter an integer!, WE can't recognise what the text you've written📗")
    else:
        update_display("Please provide information of subject and marks both!!✌🏼")
#showing the graph
def show_graph():
    if not grades_list:
        update_display("No grades to graph it on screen!, please add some grades!🅰")
        return
    subject = [item[0] for item in grades_list]
    mark_number = [item[1] for item in grades_list]
    plt.figure(figsize=(10, 6))
    plt.bar(subject , mark_number , color="navy" , linewidth=2)
    plt.title("RESULT PROGRESS!" , fontsize=16 , color="black")
    plt.xlabel("Subjects!" , fontsize=14 ,color="#151617")
    plt.ylabel("Marks!" , fontsize=12 , color="#1B1C1D")
    plt.show()
    update_display("Graph displayed!📊")
#showing the highest marks:
def show_highest_marks():
    if not grades_list:
        update_display("PLease add grades to verify your highest marks!")
        return 
    highest=max(grades_list , key=lambda x: x[1])
    text = f"🏆 HIGHEST SUBJECT\n"
    text += f"Subject: {highest[0]}\n"
    text += f"Mark: {highest[1]}%\n"
    update_display(text)
#showing the lowest marks:
def show_lowest_marks():
    if not grades_list:
        update_display("PLease add grades to verify your lowest marks!")
        return 
    lowest=min(grades_list , key=lambda x: x[1])
    text = f" 📍LOWEST SUBJECT\n"
    text += f"Subject: {lowest[0]}\n"
    text += f"Mark: {lowest[1]}%\n"
    update_display(text)
#deleting the last grades:
def delete_last_grade():
    if not grades_list:
        update_display("PLease add grades to delete!")
        return 
    deleted=grades_list.pop()
    update_display(f"❌ Deleted: {deleted[0]} ({deleted[1]}%)")
    show_grade()
#showing the grades   
def show_grade():
    if len(grades_list) > 0:
        total = 0
        for subject, mark_number in grades_list:
            total += mark_number
        average = total / len(grades_list)
        grade_letter = ABCD_grades(average)
        
        text = f"📊 YOUR RESULTS\n"
        text += f"{'='*40}\n"
        text += f"Average: {average:.1f}%\n"
        text += f"Grade: {grade_letter}\n"
        text += f"{'='*40}\n"
        text += f"📚 Your Grades:\n"
        
        for subject, mark in grades_list:
            text += f"  • {subject}: {mark}%\n"
        
        display.config(state="normal")
        display.delete("1.0", tk.END)
        display.insert(tk.END, text)
        display.config(state="disabled")
    else:
        update_display("Stay ready for the !!📄")
#
def ABCD_grades(average):
    if average >= 95:
        return "A* Magnaficient!" 
    elif average >= 90:
        return "A Well done!"
    elif  90 >= average >= 50:
        return "B Nice Atempt!"
    elif 50 >= average >=30:
        return "C Good!"
    else :
        return "F!! You can do Better!"
    
    

#BUTTON MAKING:
# making a separator:
separator1=tk.Frame(screen , height=2 , bg="navy" ,relief=tk.SUNKEN , borderwidth=1 )
separator1.pack(pady=10 , padx=10 , fill=tk.X)
# button section label:
button_label = tk.Label(screen, text="🎮 CONTROLS", font=("Papyrus", 14, "italic", "bold"),fg="darkblue", bg="lightblue") 
button_label.pack(pady=5)
# action buttons:
action_frame=tk.Frame(screen , bg="lightblue" , relief=tk.RAISED , borderwidth=2)
action_frame.pack(pady=8 , padx=15 , fill=tk.X)
action_label= tk.Label(action_frame ,text="Analysis!💹" ,font=("Courier New" , 11 , "bold"), fg="darkblue" , bg="lightblue"  )
action_label.pack(pady=5, padx=5)
action_buttons=tk.Frame(action_frame , bg="lavender")
action_buttons.pack(pady=5 , padx=10 , fill=tk.X)
tk.Button(action_buttons , text="➕ADD GRADES" , command=add_grades , font=("papyrus" , 10 , "bold"), height=1 , width=12, fg="white" , bg= "#053F09", relief=tk.RAISED ).pack(padx=3 , side=tk.LEFT , expand=True , fill=tk.BOTH)
tk.Button(action_buttons, text="📊 SHOW GRAPH", command=show_graph, bg="#040B54", fg="white", font=("papyrus", 10, "bold"), width=12, height=1, relief=tk.RAISED, bd=2).pack(side=tk.LEFT, padx=3, expand=True, fill=tk.BOTH)
tk.Button(action_buttons, text="🏆 HIGHEST YET", command=show_highest_marks, bg="#87B9F2", fg="white", font=("papyrus", 10, "bold"), width=12, height=1, relief=tk.RAISED, bd=2).pack(side=tk.LEFT, padx=3, expand=True, fill=tk.BOTH)
tk.Button(action_buttons, text="📍 LOWEST YET", command=show_lowest_marks, bg="#2f506c", fg="white", font=("papyrus", 10, "bold"), width=12, height=1, relief=tk.RAISED, bd=2).pack(side=tk.LEFT, padx=3, expand=True, fill=tk.BOTH)
#making a data frame
data_frame = tk.Frame(screen, bg="lightblue", relief=tk.RAISED, borderwidth=2)
data_frame.pack(pady=8, padx=15, fill=tk.X)
#making a data label:
data_label = tk.Label(data_frame, text="💾 Data Management", font=("Courier New", 11, "bold"), fg="darkblue" ,bg="lightblue" )
data_label.pack(pady=5)
# first row of data buttons:
data_buttons_row1 = tk.Frame(data_frame, bg="lightblue")
data_buttons_row1.pack(pady=3, fill=tk.X, padx=10)
tk.Button(data_buttons_row1, text="💾 SAVE", command=save_grades, bg="#070F7A", fg="white", font=("papyrus", 10, "bold"),  width=12, height=1, relief=tk.RAISED, bd=2).pack(side=tk.LEFT, padx=3, expand=True, fill=tk.BOTH)
tk.Button(data_buttons_row1, text="📂 LOAD", command=load_grades, bg="#00BCD4", fg="white", font=("papyrus", 10, "bold"),  width=12, height=1, relief=tk.RAISED, bd=2).pack(side=tk.LEFT, padx=3, expand=True, fill=tk.BOTH)
tk.Button(data_buttons_row1, text="❌ DELETE LAST", command=delete_last_grade, bg="#6999C1", fg="white", font=("papyrus", 10, "bold"), width=12, height=1, relief=tk.RAISED, bd=2).pack(side=tk.LEFT, padx=3, expand=True, fill=tk.BOTH)
tk.Button(data_buttons_row1, text="🗑️ CLEAR ALL", command=clear_all_grades, bg="#023BF6", fg="white", font=("papyrus", 10, "bold"), width=12, height=1, relief=tk.RAISED, bd=2).pack(side=tk.LEFT, padx=3, expand=True, fill=tk.BOTH)
# bottom separator
separator2 = tk.Frame(screen, height=2, bg="#9370DB", relief=tk.SUNKEN, borderwidth=1)
separator2.pack(pady=10, fill=tk.X, padx=10)

#finish(done)
screen.mainloop()











