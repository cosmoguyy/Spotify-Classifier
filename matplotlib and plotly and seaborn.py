1)Plotting graph

import matplotlib.pyplot as plt

x=[2,3,4,5,8,9,12]
y=[1,2,3,4,5,6,7]

plt.plot(x,y)
plt.show()

2)Plotting graph and adding label

import matplotlib.pyplot as plt

x=[2,3,4,5,8,9,12]
y=[1,2,3,4,5,6,7]

fig, ax = plt.subplots()
ax.plot(x,y marker='o' , lable="Data points")

ax.set_title("Basic Components of matplotlib figure")
ax.set_xlable("X-Axis")
ax.set_ylable("Y-Axis")

ax.legend()
plt.show()

3)bar plotting

import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[13,34,56,15,25]

plt.title('bar plot')
plt.bar(x,y, color='blue', width=.5)
plt.show()


4)pie chart

import matplotlib.pyplot as plt

x = [35, 20, 30, 40, 50, 40]
y=['iron man','thor','spiderman','daredevil','punisher','superman']
plt.title('pie chart')
plt.pie(x, labels=y)
plt.show()

5)line plot
#iris being the default dataset

import seaborn as sns
import matplotlib.pyplot as plt

data=sns.load_dataset("iris")

sns.lineplot(x="sepal_length", y="sepal_width", data=data)

plt.show()

6)scatter plot

import seaborn as sns
import matplotlib.pyplot as plt
data = sns.load_dataset("iris")
sns.scatterplot(data=data)
plt.show()

7)box plot

import plotly.express as px

df= px.data.iris()
fig= px.box(df, x="sepal_width", y="sepal_length", color="species")
fig.show()

8)histogram

import plotly.express as px

df = px.data.iris()
fig = px.histogram(df, x="sepal_width", y="sepal_length")
fig.show()
