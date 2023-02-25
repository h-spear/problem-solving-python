# https://www.acmicpc.net/problem/1918

# 중위 표기법을 후위 표기법으로 바꾸는 과정
# 1. 피연산자가 들어오면 바로 출력한다.
# 2. 연산자가 들어오면 자기보다 우선순위가 높거나 같은 것들을 빼고 자신을 스택에 담는다.
# 3. 여는 괄호를 만나면 무조건 스택에 담는다.
# 4. 닫는 괄호를 만나면 여는 괄호를 만날때 까지 스택에서 출력한다.
# 참고 : https://kyun2da.github.io/2021/05/13/postfix_notation/

expr = input()
stack = []
answer = ""
for char in expr:
    if char.isalpha():
        answer += char
    else:
        if char == "(":
            stack.append(char)
        elif char == "*" or char == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                answer += stack.pop()
            stack.append(char)
        elif char == "+" or char == "-":
            while stack and stack[-1] != "(":
                answer += stack.pop()
            stack.append(char)
        elif char == ")":
            while stack and stack[-1] != "(":
                answer += stack.pop()
            stack.pop()
        else:
            print("unknown operator")
            exit(1)

while stack:
    answer += stack.pop()

print(answer)
