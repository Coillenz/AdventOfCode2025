def find_highest_voltage(voltages: list[int]):
  largest_number = [0, 0]
  for idx, voltage in enumerate(voltages):
    if voltage > largest_number[0] and idx < len(voltages) - 1:
      largest_number[0] = voltage
      largest_number[1] = 0
      continue

    if voltage > largest_number[1]:
      largest_number[1] = voltage
  
  return ((largest_number[0] << 3) + (largest_number[0] << 1)) + largest_number[1]
      


with open('day_03/real-input.txt') as input:
  battery_voltages: list[list[int]] = []
  for line in input.readlines():
    voltages = []
    for num in line.replace('\n', ''):
      voltages.append(int(num))

    battery_voltages.append(voltages)

  largest_voltages: list[int] = []
  for battery_line in battery_voltages:
    largest_voltage = find_highest_voltage(battery_line)
    largest_voltages.append(largest_voltage)

  print(largest_voltages)
  print(sum(largest_voltages))