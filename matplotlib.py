1) Calculating Frequency of each number
import matplotlib.pyplot as plt
import random

rolls = [random.randint(1, 6) for _ in range(100)]

plt.hist(rolls, bins=6, color='plum', edgecolor='black')
plt.title('How many times did each number appear?')
plt.xlabel('Dice Face Value')
plt.ylabel('Frequency')
plt.show()

2) x-y axis plotting

heights = [150, 160, 170, 180, 190]
weights = [50, 62, 75, 85, 95]

plt.scatter(heights, weights, marker='o', color='teal')
plt.title('Relationship between Height and Weight')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()

3)Plotting Outlier Boxplot

import seaborn as sns

# Most people stay for 30-60 mins, but one person stayed for 500.
gym_times = [30, 45, 50, 40, 55, 60, 45, 500] 

sns.boxplot(x=gym_times, color='coral')
plt.title('Identifying Outliers in Gym Session Times')
plt.show()

4) Graph plotting

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
temps = [28, 30, 25, 22, 27]

plt.plot(days, temps, color='green', marker='s') # 's' for square points
plt.title('Weather Trends over the Week')
plt.ylabel('Temperature in Celsius')
plt.show()

5) Correlation Heatmap

# Imagine a 3x3 grid of 'Heat' levels
heat_data = [
    [10, 20, 30],
    [20, 50, 80],
    [30, 80, 100]
]

sns.heatmap(heat_data, annot=True, cmap='YlOrRd') # Yellow to Orange to Red , Yl for Yellow , Or for Orange , Rd for Red
plt.title('A Simple Heatmap of Values')
plt.show()
