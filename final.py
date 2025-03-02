from tkinter import *
import tkinter as tk

# define question dictionary
question = {
	"What country has the highest life expectancy? ": ["India", "Hong kong", "Pakistan", "Russia"],
	"What is team name of SIH ?" : ["Meta", "Meta-cubes", "Target","Target-cubes"],
	
        "Lakshya is from " :["Bharatpur","alwar","Jaipur","None of These"],
        "Amit Mittal sir is teaching ":["DSA","C++","oops","All of these"],
}
# define answer list
ans = ["Hong-kong", "Target-cubes","Bharatpur","oops"]

current_question = 0


def start_quiz():
        
	 start_button.forget()
	 next_button.pack()
	 next_question()


def next_question():

                
                
                global current_question
                if current_question < len(question):
                    # get key or question that need to be printed
                    check_ans()
                    user_ans.set('None')
                    c_question = list(question.keys())[current_question]
                    # clear frame to update its content
                    clear_frame()
                    # printing question
                    Label(f1, text=f"Question : {c_question}", padx=22,pady=10,
                            font="ChunkFive 25 normal",background="#856ff8").pack(anchor=NW,fill=tk.X)
                    # printing options
                    for option in question[c_question]:
                            Radiobutton(f1, text=option, variable=user_ans,font="Rubik ",
                                                    value=option, pady=10,padx=28,background="#856ff8").pack(anchor=NW,fill=tk.X)
                    current_question += 1
                else:
                    next_button.forget()
                    check_ans()
                    clear_frame()
                    output = f"Your Score is {user_score.get()} out of {len(question)}"
                    Label(f1, text=output, font="calibre 30 bold",pady=20).pack()
                    Label(f1, text="Thanks for Participating",
                            font="calibre 25 bold",pady=20).pack()


def check_ans():
	temp_ans = user_ans.get()
	if temp_ans != 'None' and temp_ans == ans[current_question-1]:
		user_score.set(user_score.get()+1)


def clear_frame():
	for widget in f1.winfo_children():
		widget.destroy()


if __name__ == "__main__":
	root = Tk()
	# setup basic window
	root.title("SIH Hackthon")
	root.geometry("950x620")
	root.minsize(800, 400)
	root.configure(bg="#1e31bd")

	user_ans = StringVar()
	user_ans.set('None')
	user_score = IntVar()
	user_score.set(0)
	Label(root, text="", font="calibre 50 bold",background="#1e31bd").pack()

	Label(root, text="Mental Health Checkup",fg="#E86498",
		font="calibre 30 bold",
		relief=FLAT, background="#E4AFCC",
		padx=17, pady=20).pack()
	Label(root, text="", font="calibre 80 bold",background="#1e31bd").pack()
	start_button = Button(root,
						text="Start Quiz",
						command=start_quiz,
						font="calibre 19 bold",
                                                background="#A5A5BA",
                                                fg="#000000"
                                                )
	start_button.pack()
	
    
	f1 = Frame(root)
	f1.pack(side=TOP, fill=X)
        
        #Label(root, text="", font="calibre 10 bold",background="#856ff8").pack()
	next_button = Button(root, text="Next Question",
						command=next_question,
						font="calibre 20 bold",
                                                background="#234E70",
                                                fg="#FBF8BE"
                                                )
	

	root.mainloop()
