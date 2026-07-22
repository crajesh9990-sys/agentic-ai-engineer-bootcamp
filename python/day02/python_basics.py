numbers = [1,2,3,4,5]

squares = [i**2 for i in numbers]

print(squares)

# Dictionary comprehension
profile = {
    "Java":20,
    "React":4,
    "Python":1
}

for key, value in profile.items():
    print(f"{key}:{value}")

# Dictionary comprehension

role = input("Role:")
task = input("Task:")
format = input("Output format:")

prompt = f"""
You are an expert {role}.

Perform the following task:

{task}

Return the answer in {format}.
"""

print(prompt)