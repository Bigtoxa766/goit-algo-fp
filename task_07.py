import random
import matplotlib.pyplot as plt

num_throws = 100000
sum_counts = {i: 0 for i in range(2,13)}

for _ in range(num_throws):
    dice1 =  random.randint(1,6)
    dice2 =  random.randint(1,6)
    roll_sum = dice1 + dice2
    sum_counts[roll_sum] += 1

    sum_probabilities = {sum_: count / num_throws for sum_, count in sum_counts.items()}

print("Сума | Імовірність")
for sum_, prob in sum_probabilities.items():
    print(f" {sum_:>4} | {prob:.4f}")

sums = list(sum_probabilities.keys())
probabilities = list(sum_probabilities.values())

plt.bar(sums, probabilities, color='skyblue')
plt.xlabel('Сума на двох кубиках')
plt.ylabel('Ймовірність')
plt.title('Ймовірність кожної суми на основі методу Монте-Карло')
plt.xticks(range(2, 13))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()