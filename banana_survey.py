import tkinter as tk
root = tk.Tk()
# 제목
root.title('Banana interest survey')
#루트 윈도우 크기
root.geometry('640x480+300+300')
root.resizable(False, False)

title = tk.Label(root, text= 'Please take the survey', font=('Arial 16 bold'), bg='brown', fg='#FF0')

name_label = tk.Label(root, text='what is your name')
name_inp = tk.Entry(root)

eater_inp = tk.Checkbutton(root, text='Check this box if you eat bananas')

num_label = tk.Label(root, text='How many bananas do you eat per day?')
num_inp = tk.Spinbox(root, from_=0, to=1000, increment=1)

color_label = tk.Label(root, text='what is the best color for a banana?')
color_inp = tk.Listbox(root, height=1)  # 선택한 아이템만 보여주기
# 선택 사항 추가
color_choices = ( 'Any', 'Green', 'Green-Yellow', 'Yellow', 'Brown Spotted', 'Black')
for choise in color_choices:
    color_inp.insert(tk.END, choise)

plantain_lable = tk.Label(root, text='Do you eat plantains?')
plantain_frame = tk.Frame(root)
plantain_yes_inp = tk.Radiobutton(plantain_frame, text='Yes')
plantain_no_inp = tk.Radiobutton(plantain_frame, text='No!')

banana_haiku_label = tk.Label(root, text='Write a haiku about bananas')
banana_haiku_inp = tk.Text(root, height=3)

submit_btn = tk.Button(root, text='submit Survey')

output_line = tk.Label(root, text='', anchor='w', justify='left')

title.grid(columnspan=2)
name_label.grid(row=1, column=0)
name_inp.grid(row=1, column=1)


root.mainloop()
