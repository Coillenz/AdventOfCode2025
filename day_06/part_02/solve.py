from problem import Problem

def find_problem_ranges(line: str) -> list[tuple[int, int]]:
  problem_ranges: list[tuple[int, int]] = []
  
  problen_start_idx = 0
  curr_idx = 1
  while curr_idx < len(line) - 1:
    if line[curr_idx] != ' ':
      problem_ranges.append((problen_start_idx, curr_idx - 1))
      problen_start_idx = curr_idx

    curr_idx += 1

  problem_ranges.append((problen_start_idx,  curr_idx + 1))
  return problem_ranges
  

def load_input(env: str) -> list[Problem]:
  with open(f'day_06/{env}-input.txt') as input:
    lines = input.readlines()
    problem_ranges = find_problem_ranges(lines[-1])
    problems: list[Problem] = [{ 'numbers': [], 'operator': None } for _ in problem_ranges]

    for problem_idx, problem_range in enumerate(problem_ranges):
      for idx in range(problem_range[0], problem_range[1]):
        curr_number: list[str] = []
        for line in lines[:len(lines) - 1]:
          if line[idx].isnumeric():
            curr_number.append(line[idx])

        if curr_number == []:
          continue
        
        problems[problem_idx]['numbers'].append(int(''.join(curr_number)))

    for idx, problem_range in enumerate(problem_ranges):
      problems[idx]['operator'] = lines[-1][problem_range[0]]

    return problems

def calculate_problem(env: str) -> int:
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