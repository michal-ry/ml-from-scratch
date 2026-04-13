# Median

### Definition

The median is the middle value of a sorted in ascending order dataset.

It devides the dataset into two equal halves.

### Formula

#### Median for odd number of observations:

$$\tilde{x} = x_{\left(\frac{n+1}{2}\right)}$$

#### Median for even number of observation:

$$\tilde{x} = \frac{x_{\left(\frac{n}{2}\right)} + x_{\left(\frac{n}{2}+1\right)}}{2}$$

### Interpretation

- Median represent central tendency even when data is skewed
- Comparing with mean:
    - mean ≈ median → data is roughly symmetric
    - mean > median → right-skewed (outliers on high side)
    - mean < median → left-skewed (outliers on low side)

### When to use  it

- When data is numerical and continuous
- When datasets have outliers
- When the distribution is skewed

### When not to use it

- When the full distribution of values matters
- When you want a measure sensitive to all observations
- When data is symmetric and free of outliers (mean may provide more information)

### Example

```
Even:
incomes_k_1 = [3, 3, 4, 50]
incomes_k_1_median = (4 + 3) / 2 = 3.5

Odd:
incomes_k_2 = [2, 3, 3, 4, 50]
incomes_k_2_median = 3
```