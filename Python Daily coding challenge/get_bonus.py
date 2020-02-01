# You are the manager of a number of employees who all sit in a row. The CEO would like to give bonuses to all of your employees, but since the company did not perform so well this year the CEO would like to keep the bonuses to a minimum.

# The rules of giving bonuses is that:
# - Each employee begins with a bonus factor of 1x.
# - For each employee, if they perform better than the person sitting next to them,
#  the employee is given +1 higher bonus (and up to +2 if they perform better than both people to their sides).

# Given a list of employee's performance, find the bonuses each employee should get.

# Example:
# Input: [1, 2, 3, 2, 3, 5, 1]
# Output: [1, 2, 3, 1, 2, 3, 1]
# Here's your starting point:

def getBonuses(performance):
  # Fill this in.
  bonus_list = []
  emp_len = len(performance)
  bonus_list.append(2) if performance[0] > performance[1] else bonus_list.append(1)
  for val in range(1,emp_len-1):

    bonus = 1
    emp_perf = performance[val]
    if emp_perf > performance[val-1]:
        bonus+=1
    if emp_perf > performance[val+1]:
        bonus+=1
    bonus_list.append(bonus)
  bonus_list.append(2) if performance[emp_len-1] > performance[emp_len-2] else bonus_list.append(1)
  return bonus_list
       
    
    

print(getBonuses([1, 2, 3, 2, 3, 5, 1]))
# [1, 2, 3, 1, 2, 3, 1]