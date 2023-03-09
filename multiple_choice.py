#Create a multiple choices quiz for programming related questions where the question asked will not be in the same order when run again.
#There will be 5 question in the programs, calculate the correct answer that user enter and determine the total grade after the quiz and compare with the class average.
#Display the message indicated whether the user has passed the quiz or not and how many percent they are higher or lower than class average.
#Whenever a user has enter something that not correct such as continue with the program or their quiz answer, allow the user to keep entering until it matched the options.
#The class average can be made up in a list by inputting any number that you wish from 0 to 100. Each quiz question will be weight 20%.
#If the user does not wish to continue with the quiz, exit the program and display a message indicated so.

#The import function here is used in order to apply various Python built-in functions
#random is for using producing random number, list, integer
import random
#String is used here to convert letter to upper or lowercase and various other use cases.
import string
#sys is used for function related to the computer system, can exit the program if needed to
import sys
#math function is imported to utilized the abs function if it is not already in used.
import math
#Initializing the list for questions, could be used for any question that want to be asked and alter
quiz_question = ["What is CPS109 course called ? ", "Can list be immutable ? ", 
"What is HTML stands for ? ", "What would be the best way to find cube root using Python ? ", 
"What is the data type for this ? -> ['Alice',2,('Wonderland',3),['temp',3]]"]
#Create a list to display the quiz answer to the question asked, the answer must match the question that is asksed above
quiz_answer = ["(a)Computer Science I (b)Introduction to Multimedia Computation (c)Digital Computation and Programming",
"(a)Yes (b)No (c)In some cases","(a)How To Make Lasagna (b)Hyper Text Markup Language (c)Hi There Mark Louise",
"(a)Exhaustive Enumeration (b)Counting by hand (c)Bisection Search","(a)Tuple (b)String (c)List"]
#Creat a separate list that can be track whether it is correct answer or not,
quiz_results = ["a","b","b","c","c"]
user_score = []
#The classes score list here is randomized in any number enter, could also used random function for this.
classes_score= [95,80,65,50,72,99,87,66,64,68,75,46]

#First part will be creating a function to welcome user to the quiz and display the quiz question.
def multiple_choice_quiz():
    print("Welcome to your multiple choice quiz for CPS109 2022 Class!!\n")
    print("Please identify if you are a student in CPS109 to continue: ")
    #The counter is created here in order to use the while loop and ask for user input validation
    counter_1 = 0
    while counter_1 < 1 :
        user_input = input("(Y)es or (N)o  ")
        #String built in fuction is used here to convert all input to uppercase.
        user_input = user_input.upper()
        print("\n")
        #If and elif was used here to let user enter either y or yes in which both is acceptable even when it asked to enter y
        if user_input == "Y" or user_input == "YES":
            print("Your Quiz will now be begin!")
            print("\n")
            #For these case increase the counter by 1 in order to exit the while loop if input is valid
            counter_1 += 1
        elif user_input== "N" or user_input == "NO":
            print("You have fail the quiz since it worth more than 50 percent of your final mark !")
            counter_1 += 1
            #Built in sys function in order to exit the whole program if user does not wish to continue
            sys.exit()
        #This message will keep printing if the response is not one of the four cases mentioned above.
        else:
            print ("Please enter a valid respons such as Y or N")
    #A second counter is used for another while loop as user answer's input  
    counter_2 = 0
    #Create an index list of possible quiz_question to sort through (0 to 4 since ther 5 questions).
    version_list = [0,1,2,3,4]
    #Quiz version now been initialized a random list from the input above, 5 -> indicated 5 number taken from version_list
    #Quiz will be randomized for 120 different combinations using permutations of 5
    quiz_version= random.sample(version_list, 5)
    #version index and question number is initialized here to index from 0 and up to range in quiz, 1 indicated the first question
    version_index = 0
    question_number = 1
    #For loop used here to go through the quiz_question which is 5 times
    for i in quiz_question:
        #f string used here for better formatting and print out the quiz question from index used above.
        print(f"{question_number}. {quiz_question[quiz_version[version_index]]}")
        print(quiz_answer[quiz_version[version_index]])
        #Initialized the while loop for input validation and keep printing error message if not match.
        while counter_2 < 1:
            answer = input("Enter your answer: ")
            #Convert using string built in function for everything to convert back to lower case.
            answer = answer.lower()
            print("\n")
            #As long as the input is A,a,B,b,C,c the program will exit the loop
            if answer == "a" or answer == "b" or answer == "c":
                break
            #This message will keep printing in console to let user know that it is invalid and required a proper one.
            else:
                print("Invalid response! Please Try again !")
        #Comparing the user input whether it matched the results or not and add 20% to their score
        if answer == quiz_results[quiz_version[version_index]]:
            user_score.append(20)
        else:
            user_score.append(0)
        #Increasing both version index and question number by 1 so it keep going to the next index and question
        version_index += 1
        question_number += 1  

#Create a separate function to calculated the total score and compared with class average      
def user_score_compare():
    #Asking for user name and student number to record in results
    user_name = input("Enter your full name: ")
    user_student_number = input("Enter your student number: ")
    print("\n")
    #Initialized the user final score and class average by adding list index and add to 0
    user_final_score = 0
    classes_average = 0
    for i in range(len(user_score)):
        user_final_score += user_score[i]
    #Use for loop here to loop through classes score and add from index 0 to the end of len of list and add it to classes_average
    for j in range(len(classes_score)):
        classes_average += classes_score[j]
    #Calculate the class average from list above according to it length of input in lists.
    classes_average = classes_average/len(classes_score)
    score_difference = classes_average - float(user_final_score)
    #Score difference is later converted into absolute number to display when they have passed or fail.
    score_difference = abs(score_difference)
    print(f"Thank you for your submissions of the quiz {user_name}, Student Number: {user_student_number}\n")
    #If user scored 4/5 question above they will pass and message will be display.
    if user_final_score >= 80:
        print("You have passed the QUIZ! Congratulations on your achievement !\n")
    #F string is used once again here for clearer format on what will display in the console.
        print(f"Your final score is {user_final_score}% which is {score_difference}% more than the class average.")
    #If the user fail this is what will be printed and showing their score compared to class average
    else:
        print ("Sorry, you have failed, please try harder next time!\n")
        print(f"Your final score is {user_final_score}% which is {score_difference}% less than the class average.")

#This code below here is to initialized the program even if we import other py file into assignment 1
if __name__ == "__main__":
    #Run the two function below when the code is run         
    multiple_choice_quiz()
    user_score_compare()









            



    




