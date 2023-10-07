import copy
import random
# Consider using the modules imported above.


class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for color, count in kwargs.items():
      self.contents.extend([color] * count)

  def draw(self, num):
    drawn = []
    if num >= len(self.contents):
      return self.contents
    for _ in range(num):
      random_index = random.randint(0, len(self.contents) - 1)
      drawn.append(self.contents.pop(random_index))
    return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success_count = 0

  for _ in range(num_experiments):
    hat_copy = copy.deepcopy(hat)

    drawn = hat_copy.draw(num_balls_drawn)

    match = all(
        drawn.count(color) >= count for color, count in expected_balls.items())

    if match:
      success_count += 1

  probability = success_count / num_experiments
  return probability

