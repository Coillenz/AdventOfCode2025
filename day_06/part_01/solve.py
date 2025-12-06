from problem import Problem

def load_input(env: str) -> list[Problem]:
  with open(f'day_06/{env}-input.txt') as input:
    lines = input.readlines()
    problems: list[Problem] = [{ 'numbers': [], 'operator': None } for _ in lines[0].split()]

    for line_idx, line in enumerate(lines):
      for problem_idx, number in enumerate(line.split()):
        if line_idx == len(lines) - 1:
          problems[problem_idx]['operator'] = number.strip()
          continue

        problems[problem_idx]['numbers'].append(int(number.strip()))

    return problems

def calculate_problem(env: str):
  problems = load_input(env)

  total = 0
  for problem in problems:
    match problem['operator']:
      case '+':
        total += calculate_addition(problem)
      case '*':
        total += calculate_multiplication(problem)

  return total

def calculate_addition(problem: Problem) -> int:
  total = problem['numbers'][0]
  for number in problem['numbers'][1:]:
    total += number
  
  return total

def calculate_multiplication(problem : Problem):
  total = problem['numbers'][0]
  for number in problem['numbers'][1:]:
    total *= number
  
  return total