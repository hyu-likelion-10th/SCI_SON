from bwsi_grader.python.palindrome import grader

def student_func(x):
    x = x.replace(" ","")
    x = x.lower()
    str_length = len(x)
    str_half = str_length//2
    if str_length%2==0: #총 길이가 짝수일 때
        str_front = x[:str_half]
        str_back = x[str_half:]
        if str_front == str_back:
            return True
        else:
            return False
    else: #총 길이가 홀수일 때
        str_front = x[:str_half]
        str_back = x[str_half+1:]
        if str_front == str_back:
            return True
        else:
            return False

grader(student_func)