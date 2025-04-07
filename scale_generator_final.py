import random 

class ScaleGenerator:
    chromatic_scale = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    scale_patterns = { "major": [2, 2, 1, 2, 2, 2, 1], "minor": [2, 1, 2, 2, 1, 2, 2], "major_arpeggio": [4, 3], "minor_arpeggio" : [3, 4], 
                      "major_seventh_arpeggio" : [4, 3, 4], "minor_seventh_arpeggio" : [3, 4, 3], "dominant_seventh_arpeggio" : [4, 3, 3],
                      "half_diminished_arpeggio" : [3, 3, 4], "diminished_arpeggio" : [3, 3, 3], "major_ninth_arpeggio" : [4, 3, 4, 3], 
                      "dominant_ninth_arpeggio" : [4, 3, 3, 4], "minor_ninth_arpeggio": [3, 4, 3, 4], "major_thirteenth_arpeggio" : [4, 3, 4, 3, 7], 
                      "minor_thirteenth_arpeggio" : [3, 4, 3, 4, 6], "dominant_thirteenth_arpeggio" : [4, 3, 3, 4, 7], "major_sixth_arpeggio" : [4, 3, 2, 3] ,
                        "minor_sixth_arpeggio" : [3, 4, 1, 4]}
    easy_keys = ['C', 'D', 'E', 'G', 'A']
    medium_keys = ['C', 'C#','D', 'E','F', 'G', 'A', 'B']
    hard_keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    advanced_keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    scale_types = ['major', 'minor']
    easy_arpeggios_types = ['major_arpeggio', 'minor_arpeggio', "major_seventh_arpeggio", "minor_seventh_arpeggio", "dominant_seventh_arpeggio"]
    medium_arpeggio_types = ['major_arpeggio', 'minor_arpeggio', "major_seventh_arpeggio", "minor_seventh_arpeggio", "dominant_seventh_arpeggio",
                             "half_diminished_arpeggio", "diminished_arpeggio", "major_ninth_arpeggio", "dominant_ninth_arpeggio", "minor_ninth_arpeggio",
                             "major_sixth_arpeggio", "minor_sixth_arpeggio"]
    hard_arpeggio_types = ['major_arpeggio', 'minor_arpeggio', "major_seventh_arpeggio", "minor_seventh_arpeggio", "dominant_seventh_arpeggio",
                             "half_diminished_arpeggio", "diminished_arpeggio", "major_ninth_arpeggio", "dominant_ninth_arpeggio", "minor_ninth_arpeggio",
                             "major_sixth_arpeggio", "minor_sixth_arpeggio", "major_thirteenth_arpeggio", "minor_thirteenth_arpeggio", "dominant_thirteenth_arpeggio" ]
    scale_degrees = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
    arpeggio_degrees = ['I', 'III', 'V', 'VII', 'IX', 'XIII']
    sixth_arpeggio_degrees = ['I', 'III', 'V', 'VI']

    def __init__(self, root, scale_type):
        self.root = root
        self.scale_type = scale_type

    def generate_scale(self):
        pattern = self.scale_patterns[self.scale_type]
        start_index = self.chromatic_scale.index(self.root)
        notes = [self.root]
        for interval in pattern:
            start_index = (start_index + interval) % len(self.chromatic_scale)
            notes.append(self.chromatic_scale[start_index])
        return notes



def easy_scale_practice():
    random_key = random.choice(ScaleGenerator.easy_keys)
    random_scale = random.choice(ScaleGenerator.scale_types)
    operating_scale = ScaleGenerator(random_key, random_scale)
    scale_tones = operating_scale.generate_scale()
    scale_dictionary = dict(zip(ScaleGenerator.scale_degrees, scale_tones))
    print(f"Complete the {random_key} {random_scale} scale: ")
    omit_indices = random.sample(range(len(scale_tones)), 3)
    user_notes = {}
    for index in omit_indices:
        user_note = input(f"Enter the note for position {index + 1}: ")
        user_notes[index] = user_note
    is_correct = all(user_notes[i] == scale_tones[i] for i in omit_indices)
    if is_correct:
        print("Correct, good job!")
        print(scale_dictionary)
    else:
        print("Incorrect. Try again!")
        print(scale_dictionary)
  

def medium_scale_practice():
    random_key = random.choice(ScaleGenerator.medium_keys)
    random_scale = random.choice(ScaleGenerator.scale_types)
    operating_scale = ScaleGenerator(random_key, random_scale)
    scale_tones = operating_scale.generate_scale()
    scale_dictionary = dict(zip(ScaleGenerator.scale_degrees, scale_tones))
    print(f"Complete the {random_key} {random_scale} scale: ")
    omit_indices = random.sample(range(len(scale_tones)), 4)
    user_notes = {}
    for index in omit_indices:
        user_note = input(f"Enter the note for position {index + 1}: ")
        user_notes[index] = user_note
    is_correct = all(user_notes[i] == scale_tones[i] for i in omit_indices)
    if is_correct:
        print("Correct, good job!")
        print(scale_dictionary)
    else:
        print("Incorrect. Try again!")
        print(scale_dictionary)

def hard_scale_practice():
    random_key = random.choice(ScaleGenerator.hard_keys)
    random_scale = random.choice(ScaleGenerator.scale_types)
    operating_scale = ScaleGenerator(random_key, random_scale)
    scale_tones = operating_scale.generate_scale()
    scale_dictionary = dict(zip(ScaleGenerator.scale_degrees, scale_tones))
    print(f"Complete the {random_key} {random_scale} scale: ")
    omit_indices = random.sample(range(len(scale_tones)), 6)
    user_notes = {}
    for index in omit_indices:
        user_note = input(f"Enter the note for position {index + 1}: ")
        user_notes[index] = user_note
    is_correct = all(user_notes[i] == scale_tones[i] for i in omit_indices)
    if is_correct:
        print("Correct, good job!")
        print(scale_dictionary)
    else:
        print("Incorrect. Try again!")
        print(scale_dictionary)

def advanced_scale_practice():
    random_key = random.choice(ScaleGenerator.advanced_keys)
    random_scale = random.choice(ScaleGenerator.scale_types)
    operating_scale = ScaleGenerator(random_key, random_scale)
    scale_tones = operating_scale.generate_scale()
    scale_dictionary = dict(zip(ScaleGenerator.scale_degrees, scale_tones))
    print(f"Complete the {random_key} {random_scale} scale: ")
    omit_indices = random.sample(range(len(scale_tones)), 7)
    user_notes = {}
    for index in omit_indices:
        user_note = input(f"Enter the note for position {index + 1}: ")
        user_notes[index] = user_note
    is_correct = all(user_notes[i] == scale_tones[i] for i in omit_indices)
    if is_correct:
        print("Correct, good job!")
        print(scale_dictionary)
    else:
        print("Incorrect. Try again!")
        print(scale_dictionary)

advanced_scale_practice()