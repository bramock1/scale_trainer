import tkinter as tk
from scale_generator import ScaleGenerator, easy_scale_practice, medium_scale_practice, hard_scale_practice, advanced_scale_practice
import random
chromatic_scale = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
scale_patterns = { "major": [2, 2, 1, 2, 2, 2, 1], "minor": [2, 1, 2, 2, 1, 2, 2], "major_arpeggio": [4, 3, 5], "minor_arpeggio" : [3, 4, 5], 
                      "major_seventh_arpeggio" : [4, 3, 4, 1], "minor_seventh_arpeggio" : [3, 4, 3, 2], "dominant_seventh_arpeggio" : [4, 3, 3, 2],
                      "half_diminished_arpeggio" : [3, 3, 4, 2], "diminished_arpeggio" : [3, 3, 3, 3], "major_ninth_arpeggio" : [4, 3, 4, 3], 
                      "dominant_ninth_arpeggio" : [4, 3, 3, 4], "minor_ninth_arpeggio": [3, 4, 3, 4], "major_thirteenth_arpeggio" : [4, 3, 4, 3, 7], 
                      "minor_thirteenth_arpeggio" : [3, 4, 3, 4, 6], "dominant_thirteenth_arpeggio" : [4, 3, 3, 4, 7], "major_sixth_arpeggio" : [4, 3, 2, 3] ,
                        "minor_sixth_arpeggio" : [3, 4, 1, 4]}
scale_types = ['Major', "Minor"]
scale_degrees = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
arpeggio_degrees = ['I', 'III', 'V', 'VII', 'IX', 'XIII']
sixth_arpeggio_degrees = ['I', 'III', 'V', 'VI']
root = tk.Tk()
root.geometry("400x300")

label = tk.Label(root, text="Music Theory Trainer")
label.pack()

feedback_label = tk.Label(root, text="", fg="red")
feedback_label.pack_forget()

message = tk.StringVar()  # A variable to hold the message displayed in the label
message.set("Select a difficulty: \n Option 1: Easy \n Option 2: Medium \n Option 3: Hard \n Option 4: Advanced")
message_label = tk.Label(root, textvariable=message)  # A label to display text
message_label.pack()  # Adds the label to the window
difficulty_entry = tk.Entry(root)
difficulty_entry.pack()
difficulty_button = tk.Button(root, text="Submit", command=lambda: select_difficulty(difficulty_entry.get()))
difficulty_button.pack()
submit_button = tk.Button(root, text="Submit")
# submit_button.pack()

# selection_entry = tk.Entry(root)
# selection_entry.pack()

reset_button = tk.Button(root, text="New Scale", command=easy_scale_practice)
reset_button.pack_forget()

def reset_GUI():
    global note_entry, feedback_label
    note_entry.pack_forget()
    feedback_label.config(text="")
    reset_button.pack_forget()
    message.set("Select a difficulty:\n Option 1: Easy \n Option 2: Medium \n Option 3: Hard \n Option 4: Advanced")
    difficulty_entry.pack()
    difficulty_button.pack()

def combined_reset():
    global feedback_label
    reset_GUI()
    feedback_label.pack_forget()

reset_button.config(command=combined_reset)



def select_difficulty(difficulty):
    if difficulty in ["1", "easy"]:
        feedback_label.pack_forget()
        difficulty_entry.pack_forget()
        difficulty_button.pack_forget()
        easy_scale_practice()
    elif difficulty in ["2", "medium"]:
        difficulty_entry.pack_forget()
        difficulty_button.pack_forget()
        message.set("Medium")
        medium_scale_practice()
    elif difficulty in ["3", "hard"]:
        difficulty_entry.pack_forget()
        difficulty_button.pack_forget()
        message.set("Hard")
        medium_scale_practice()
    elif difficulty in ["4", "advanced"]:
        difficulty_entry.pack_forget()
        difficulty_button.pack_forget()
        message.set("Jazz Cat Mode")
        advanced_scale_practice()

def check_notes():
    global omit_indices, scale_tones, scale_dictionary, note_entry, entries, feedback_label
    entries = note_entry.get().split()
    feedback_label.pack()
    entries = [entry.upper() for entry in entries]
    if len(entries) != len(omit_indices):
        feedback_label.config(text="Please enter all tones")
        return
    is_correct = all(entries[i] == scale_tones[omit_indices[i]] for i in range(len(omit_indices)))
    if is_correct:
        feedback_label.config(text=f"Correct, good job! \nScale:{scale_dictionary}")
        note_entry.pack_forget()
        submit_button.pack_forget()
        reset_button.config(command=reset_GUI)
        reset_button.pack()
    else:
        feedback_label.config(text="Try again.")

def easy_scale_practice():
    global omit_indices, scale_tones, scale_dictionary, note_entry, entries, feedback_label
    global omit_indices, entries, scale_tones
    feedback_label = tk.Label(root, text="", fg="red")
    feedback_label.pack()
    submit_button.pack_forget()
    random_key = random.choice(ScaleGenerator.easy_keys)
    random_scale = random.choice(ScaleGenerator.scale_types)
    operating_scale = ScaleGenerator(random_key, random_scale)
    scale_tones = operating_scale.generate_scale()
    scale_dictionary = dict(zip(ScaleGenerator.scale_degrees, scale_tones))
    message.set(f"Complete the {random_key} {random_scale} scale: ")
    omit_indices = random.sample(range(len(scale_tones)), 3)
    missing_positions = ', '.join(str(i + 1) for i in omit_indices)
    message.set(f"Enter the following {random_key} {random_scale} scale degrees: {missing_positions}")
    note_entry =tk.Entry(root)
    note_entry.pack()
    submit_button.config(command=check_notes)
    submit_button.pack()

def medium_scale_practice():
    global omit_indices, scale_tones, scale_dictionary, note_entry, entries
    global omit_indices, entries, scale_tones
    feedback_label = tk.Label(root, text="", fg="red")
    feedback_label.pack()
    submit_button.pack_forget()
    random_key = random.choice(ScaleGenerator.medium_keys)
    random_scale = random.choice(ScaleGenerator.scale_types)
    operating_scale = ScaleGenerator(random_key, random_scale)
    scale_tones = operating_scale.generate_scale()
    scale_dictionary = dict(zip(ScaleGenerator.scale_degrees, scale_tones))
    message.set(f"Complete the {random_key} {random_scale} scale: ")
    omit_indices = random.sample(range(len(scale_tones)), 5)
    missing_positions = ', '.join(str(i + 1) for i in omit_indices)
    message.set(f"Enter the following {random_key} {random_scale} scale degrees: {missing_positions}")
    note_entry =tk.Entry(root)
    note_entry.pack()
    submit_button.config(command=check_notes)
    submit_button.pack()

def hard_scale_practice():
    global omit_indices, scale_tones, scale_dictionary, note_entry, entries
    global omit_indices, entries, scale_tones
    feedback_label = tk.Label(root, text="", fg="red")
    feedback_label.pack()
    submit_button.pack_forget()
    random_key = random.choice(ScaleGenerator.hard_keys)
    random_scale = random.choice(ScaleGenerator.scale_types)
    operating_scale = ScaleGenerator(random_key, random_scale)
    scale_tones = operating_scale.generate_scale()
    scale_dictionary = dict(zip(ScaleGenerator.scale_degrees, scale_tones))
    message.set(f"Complete the {random_key} {random_scale} scale: ")
    omit_indices = random.sample(range(len(scale_tones)), 6)
    missing_positions = ', '.join(str(i + 1) for i in omit_indices)
    message.set(f"Enter the following {random_key} {random_scale} scale degrees: {missing_positions}")
    note_entry =tk.Entry(root)
    note_entry.pack()
    submit_button.config(command=check_notes)
    submit_button.pack()

def advanced_scale_practice():
    global omit_indices, scale_tones, scale_dictionary, note_entry, entries
    global omit_indices, entries, scale_tones
    feedback_label = tk.Label(root, text="", fg="red")
    feedback_label.pack()
    submit_button.pack_forget()
    random_key = random.choice(ScaleGenerator.advanced_keys)
    random_scale = random.choice(ScaleGenerator.scale_types)
    operating_scale = ScaleGenerator(random_key, random_scale)
    scale_tones = operating_scale.generate_scale()
    scale_dictionary = dict(zip(ScaleGenerator.scale_degrees, scale_tones))
    message.set(f"Complete the {random_key} {random_scale} scale: ")
    omit_indices = random.sample(range(len(scale_tones)), 8)
    missing_positions = ', '.join(str(i + 1) for i in omit_indices)
    message.set(f"Enter the following {random_key} {random_scale} scale degrees: {missing_positions}")
    note_entry =tk.Entry(root)
    note_entry.pack()
    submit_button.config(command=check_notes)
    submit_button.pack()


root.mainloop()




# def navigate(selection):
#     if selection in ["1", "option 1", "scales"]:
#         selection_entry.pack_forget()
#         submit_button.pack_forget()
#         message.set("Select a difficulty: \n Option 1: Easy \n Option 2: Medium \n Option 3: Hard \n Option 4: Advanced")
#         difficulty_entry.pack()
#         difficulty_button.pack()
#     elif selection in ["2", "option 2", "arpeggios"]:
#         message.set("Select a difficulty: \n Option 1: Easy \n Option 2: Medium \n Option 3: Hard \n Option 4: Advanced")
#         selection_entry.pack_forget()
#         submit_button.pack_forget()
#         difficulty_entry.pack()
#         difficulty_button.pack()
#     elif selection in ["3", "option 3", "diatonic chords"]:
#         message.set("Select a difficulty: \n Option 1: Easy \n Option 2: Medium \n Option 3: Hard \n Option 4: Advanced")
#         selection_entry.pack_forget()
#         submit_button.pack_forget()
#         difficulty_entry.pack()
#         difficulty_button.pack()
#     elif selection in ["4", "option 4", "modal intervals"]:
#         message.set("Select a difficulty: \n Option 1: Easy \n Option 2: Medium \n Option 3: Hard \n Option 4: Advanced")
#         selection_entry.pack_forget()
#         submit_button.pack_forget()
#         difficulty_entry.pack()
#         difficulty_button.pack()
#     print("User entries:", entries)
#     expected_notes = [scale_tones[i] for i in omit_indices]
#     print("Expected notes:", expected_notes)


# def check_notes():
#     global omit_indices, scale_tones, scale_dictionary, note_entry
#     entries = note_entry.get().strip().split()

#     # Debugging: print entries and the expected scale tones
#     print("User entries:", entries)
#     expected_notes = [scale_tones[i] for i in omit_indices]
#     print("Expected notes:", expected_notes)

#     if len(entries) != len(omit_indices):
#         print("Please enter the notes.")
#         return

#     is_correct = all(entries[i] == scale_tones[omit_indices[i]] for i in range(len(omit_indices)))
#     if is_correct:
#         print("Correct, good job!")
#         print(scale_dictionary)
#     else:
#         print("Try again.")

# def easy_scale_practice():
#     global omit_indices, scale_tones, scale_dictionary, note_entry
#     submit_button.pack_forget()
#     random_key =  random.choice(ScaleGenerator.easy_keys)
#     random_scale = random.choice(ScaleGenerator.scale_types)
#     operating_scale = ScaleGenerator(random_key, random_scale)
#     scale_tones = operating_scale.generate_scale()
#     scale_dictionary = dict(zip(ScaleGenerator.scale_degrees, scale_tones))
#     message.set(f"Complete the {random_key} {random_scale} scale: ")
#     omit_indices = random.sample(range(len(scale_tones)), 3)
#     missing_positions = ', '.join(str(i + 1) for i in omit_indices)
#     message.set(f"Complete the {random_key} {random_scale} scale at positions: {missing_positions}")
#     note_entry = tk.Entry(root)
#     note_entry.pack()
#     submit_button.config(command=check_notes)
#     submit_button.pack()
#         # submit_button = tk.Button(root, text="Submit", command =lambda: navigate(selection_entry.get()))
    # omit_indices = random.sample(range(len(scale_tones)), 3)
    # user_notes = {}
    # for index in omit_indices:
    #     user_note = input(f"Enter the note for position {index + 1}: ")
    #     user_notes[index] = user_note
    # is_correct = all(user_notes[i] == scale_tones[i] for i in omit_indices)
    # if is_correct:
    #     print("Correct, good job!")
    #     print(scale_dictionary)
    # else:
    #     print("Incorrect. Try again!")
    #     print(scale_dictionary)
  
# def scale_study():
#     generic_scale = Scale()
#     random_key = random.choice(chromatic_scale)
#     random_scale = random.choice(scale_types)
#     return generic_scale
# scale_study()


# scale_study()
# random_key = random.choice(chromatic_scale)
# random_scale = random.choice(scale_types)
# print(f"{random_key} {random_scale}")

# difficulty_entry = tk.Entry(root)
# difficulty_entry.pack()

# submit_button = tk.Button(root, text="Submit", command =lambda: select_difficulty(difficulty_entry.get()))
# submit_button.pack()


# c_major = Scale('C', 'major')

# def show_scale():
#     c_major_scale = c_major.generate_scale()
#     message.set(c_major_scale)

# scale_button = tk.Button(root, text="Show C Major Scale", command= show_scale)  # A button to trigger a function
# scale_button.pack()  # Adds the button to the window

# label2 = tk.Label(root, text = "Choose a key")
# label2.pack()
# key_entry = tk.Entry(root)
# key_entry.pack()
# key_input = key_entry.get()

# label3 = tk.Label(root, text = "major or minor")
# label3.pack()
# scale_entry =tk.Entry(root)
# scale_entry.pack()
# scale_input = scale_entry.get()

# user_scale = Scale(key_input, scale_input)
# def show_new_scale():
#     auto_generate_scale = user_scale.generate_scale()
#     message.set(auto_generate_scale)

# generate_scale_button = tk.Button(root, text="Generate Scale", command= show_new_scale)  # A button to trigger a function
# generate_scale_button.pack()  # Adds the button to the window



