# Variance

### Definition

Variance is the average squared deviation of observations from the mean.

It measures how strongly the values in a dataset differ from their average value.

### Formula

Population:
$$\sigma^2 = \frac{1}{N}\sum_{i=1}^{N}(x_i - \mu)^2$$

Sample:
$$s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2$$

Where:

- $x_i$ — individual observation
- $\mu$ — population mean
- $\bar{x}$ — sample mean
- $N$ — number of observations in the population
- $n$ — number of observations in the sample

### Interpretation

- A small variance means that values are concentrated close to the mean.
- A large variance means that values are spread farther away from the mean.
- Variance cannot be negative because deviations are squared.
- Variance is expressed in squared units, which can make it harder to interpret directly.
- Standard deviation is the square root of variance and is expressed in the original unit of the data.

### Populatin vs Sample Variance

- Population variance is used when the dataset contains the entire population.
- Sample variance is used when the dataset is a sample taken from a larger population.
- Sample variance uses $n - 1$ instead of $n$ to reduce the tendency to underestimate population variance.

### When to use  it

- When working with numerical data
- To measure how strongly values are spread around the mean
- To compare variability between datasets measured on the same scale
- As a foundation for standard deviation and other statistical methods

### When not to use it

- When data is categorical
- When a dataset contains strong outliers and a robust measure of spread is needed
- When comparing datasets measured in different units or on very different scales

### Example

```
numbers = [-2, 4, 4, 6]

mean = 12 / 4 = 3

deviations = [-5, 1, 1, 3]
squared_deviations = [25, 1, 1, 9]

sum_of_squared_deviations = 36

variance_population = 36 / 4 = 9
variance_sample = 36 / (4 - 1) = 12
```