import random

# Function to get list of names from file
def get_names(nums=2):
    with open('/workspaces/__2024_10_22__gjun_ai__/lesson8/names.txt','r',encoding='utf-8') as file:
        names = file.read().splitlines() # Read each line and remove newline characters
    random_names = random.sample(names,k=nums) # Randomly select 'nums' names, no reapeating
    return random_names

def generate_students(names):
    students = []
    for name in names:
        student = {
            'name': name,
            'chinese': random.randint(50,100), # Random score 50-100
            'english': random.randint(50,100),
            'math': random.randint(50,100),
        }
        students.append(student)
    return students

nums = int(input('請輸入學生數量(最多10位):'))
names = get_names(nums=nums) # Get random name list
students = generate_students(names) # Create student list
print(students)