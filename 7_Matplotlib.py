from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 3, 0.01)
plt.plot(x, norm.pdf(x))
plt.show()

# plot two graphs together
plt.plot(x, norm.pdf(x))
plt.plot(x, norm.pdf(x, 1.0, 0.5))
plt.show()

# plot and save img to file
plt.plot(x, norm.pdf(x))
plt.plot(x, norm.pdf(x, 1.0, 0.5))
plt.savefig('/Users/jiangling/Workspace/DSWP/7_MyPlot.png', format='png')

# adjust the axes
axes = plt.axes()
axes.set_xlim([-5,5])
axes.set_ylim([0, 1.0])
axes.set_xticks([-5,-4,-3,-2,-1,0,1,2,3,4,5])
axes.set_yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
# add grid lines
axes.grid()
# add some labels
plt.xlabel('Greebles')
plt.ylabel('Probability')
# customize the line style and color
plt.plot(x, norm.pdf(x), 'b--')
plt.plot(x, norm.pdf(x, 1.0, 0.5), 'r:')
# add legend
plt.legend(['Sneetches', 'Gacks'], loc=1)
plt.show()

# plot in XKCD style
plt.xkcd()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.xticks([])
plt.yticks([])
ax.set_ylim([-30,10])

data = np.ones(100)
data[70:] -= np.arange(30)

plt.annotate(
    'THE DAY I REALIZED\nI COULD COOK BACON\nWHENEVER I WANT',
    xy=(70,1), arrowprops=dict(arrowstyle='->'), xytext=(15,-10))

plt.plot(data)
plt.xlabel('time')
plt.ylabel('my overall health')

# plot pie chart
plt.rcdefaults() # clear XKCD mode

values = [12,55,4,32,14]
colors = ['r','g','b','c','m']
explode = [0,0,0.2,0,0]
labels = ['India','United States','Russia','China','Europe']
plt.pie(values,colors=colors,labels=labels,explode=explode)
plt.title('Student Locations')
plt.show()

# bar chart
values = [12,55,4,32,14]
colors = ['r','g','b','c','m']
tick_label = ['India','United States','Russia','China','Europe']
plt.bar(range(0,5), values, color=colors, tick_label=tick_label)
plt.title('Student Locations')
plt.show()

# scatter plot
X = randn(500)
Y = randn(500)
plt.scatter(X,Y)
plt.show()

# histogram
incomes = np.random.normal(27000, 15000, 10000)
plt.hist(incomes, 50)
plt.show()

# box and whisker plot
# good for visualizing the spread and skew of data
# box in the middle represents the 1st and 3rd quartiles
# hotizontal line in the box represents the median
# vertical line of whiskers indicate the range of data
# dots outside of the whiskers are outliers
uniformSkewed = np.random.rand(100)*100-40
high_outliers = np.random.rand(10)*50+100
low_outliers = np.random.rand(10)*50-100
data = np.concatenate((uniformSkewed, high_outliers, low_outliers))
plt.boxplot(data)
plt.show()