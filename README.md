# Data Science with Python Study Note

## 准备知识

### Pandas Lib

Pandas支持`Data Frames`和`Series`等对象，提供对数据行列的截取或调换等操作。
Pandas操作的对象多是`Numpy`类型的Array，后者也是一个Python的库
从Numpy Array创建Pandas DataFrame，或者从后者转化为前者都很容易。

Scikit Learn是一个机器学习的Python库，使用Numpy Array作为输入。一般操作流程是：
* 用Pandas加载、清理和处理数据
* Pandas DataFrame -> Numpy Array
* 将Numpy Array导入Scikit Learn函数

### Matplotlib Lib

一个专注绘图的库，提供：
* plot()函数用于绘图
* show()函数用于显示绘图
* Norm.pdf()方法用户绘制标准分布的概率密度函数
* 支持多个图形交叠绘制
* savefit()函数导出绘制图形到图像文件
* axes()函数支持自定义标尺的比例，方格，注释等
* 支持自定义图线颜色和线型

图形类型：
* XKCD()函数提供手绘图形样式
* 饼图
* 柱形图
* 点图
* 直方图
* 箱型图

参考
* https://matplotlib.org
* 7_Matplotlib.py中的示例

### Types of Data

Different techniques could be applied on different types of data.
Think about the data type before processing them.

Major types
* Numerical
* Categorical
* Ordinal

Numerical data
* Quantitative measurement
    * Heights of people
    * Page load times
    * Stock prices
* Integer based discrete numbers
    * Annual purchase times
    * Annual rain fall times
* Continuous infinite possible values
    * Time taken to check out
    * Rain fall volume per day

Categorical data
* Qualitative without Math meaning
    * Gender, Race
    * Yes/No, Binary data
    * Product Category
* Even numbers could be used for representing categories without math meanings

Ordinal data
* Mix numerical and categorical data
* Could be categorical with Math meaning
* For example, rating on a 1 to 5 scale 

### Mean, Median, and Mode

Mean
* Is Average
* Sum / number of samples

Median
* Sort the values
* Take the value at midpoint

Mode
* The most common value
* Not relevant to continuous data

### Variation and Standard Deviation

Variance
* How spread out the data is
* Is the average of diffs**2 from the mean
* Find the mean
* Find the differences from the mean
* Find the squared differences
* Find the average of the squared differences

Standard Deviation
* Is the square root of the Variance
* Identifies outlier with the # of SDs
* One SD from the mean is unusual

Population and Samples
* Usually work with a sample of data
* Calculate the variance of N samples:
    * The same steps as calculating SD
    * Except dividing with N-1 but not N

### Probability Density

Probability Density Function
* Gives the probability of a data point falling within some range of a values

Probability Mass Function
* Same with PDF but for discrete data

### Percentiles and Moments

Percentile
* The value on the X percent point of the dataset

Moments
* Measures the shape of a PDF
* The first moment is the mean
* The second moment is the variance
* The third moment is skew
    * skewed left - a longer tail on the left
    * skewed right - a longer tail on the right
* The fourth moment is kurtosis
    * Higher peaks have higher kurtosis

### Covariance and Correlation

Covariance
* Measure how two variables are related
* Vector two vars of each sample elements
* Convert vectors to variances from mean
* Take dot product of the two vectors
* Divide the product by the sample size

A covariance close to zero means there is no much correlation, 
but it is hard to say how large means there is much correlation.

Correlation
* Is covariance divided by the SD of both vars
* Is normalized measurement of correlation
* Valued between -1 and 1
    * -1 means perfect inverse correlation
    * 1 means perfect correlation
    * 0 means no correlation

Pay attention to the causation of the two vars.
No matter their correlation is they may or may not cause each other.

### Conditional Probability

For two events that depend on each other, conditional probability is the 
probability that both will occur.

Notation:
* P(A,B): the probability of both A and B occurring
* P(B|A): the probability of B given that A has occurred
* P(B|A) = P(A,B) / P(A)

Example:
* 60% students passed both of two tests
* 80% students passed the 1st one
* ?% passed the 1st also passed the 2nd
Solution:
* P(A,B) = 60%
* P(A) = 80%
* P(B|A) = 60%/80% = 75%

### Bayes Theorem

Notation
* P(A|B) = P(A)P(B|A)/P(B) = P(A,B)/P(B)
* The P of A given B, is the P of B given A, times P of A, over the P of B.
* The P of A depends on B, depends very much on the base P of B and A.

Example of a drug test
* Has a positive test accuracy of 99%
* Has a negative test accuracy of 99%
* 0.3% of the overall population use this drug

P of real drug user from positive test results
* Set A as users of the drug
* Set B as users with positive test result
* We know that
    * P(A)=0.003
    * P(B|A) = 0.99
    * P(B) = 0.003*0.99+0.997*0.01=0.013
* We can find:
    * P(A|B) = P(A)P(B|A)/P(B)=0.228

Conclusion
* Only 22.8% positive results are real drug users.
* A P(B|A) of 99% does not mean a high P(A|B)
* The key cause of this bias is the low P(A)
