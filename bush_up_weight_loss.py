class Exercises:
    def __init__(self, weight):
        self.weight = weight
        self.exercise_dic = {
            'Pushup': 0.2,
            'Jogging': 0.4,
            'Walking': 0.04
        }

    def add_exercise(self,exercise_name,lossing_weight):
        self.exercise_dic[exercise_name]= lossing_weight

    def print_exercises_name(self): 
        for i, k in enumerate(self.exercise_dic, start=1):
            print(i,".", k)

    def weightloss(self,exercise_name):
        self.weight=self.weight-self.exercise_dic[exercise_name]

    def try_do_exercise(self, exercise_num):

        exercise_list=list(self.exercise_dic.keys())

        if exercise_num == 0:
            exercise_name=input("Enter your exercise name: ")
            lossing_weight=float(input("How much weight the exercise loss: "))
            self.exercise_dic[exercise_name] = lossing_weight
            print("New exercise add")
        else:
            exercise_name = exercise_list[exercise_num-1]
            self.weightloss(exercise_name)


weight = float(input("Enter your weigth in kg: "))
exercise = Exercises(weight)
while exercise.weight>0:
    exercise.print_exercises_name()
    choose_input = int(
        input("Choose exercise number or Press 0 for adding new exercise: "))
    exercise.try_do_exercise(choose_input)
    print(exercise.weight)

print("Congratulation you died by exercise")
