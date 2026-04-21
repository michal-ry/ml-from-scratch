# Mode

### Definition

The mode is the most frequent value in a dataset.

It shows the most common value or values if two or more values appear the same number of times.

### Formula

$$\mathrm{Mode} = x_i \text{ such that } f(x_i) = \max(f(x))$$

### Interpretation

- Mode represents the most common value or values
- A dataset may have one mode, multiple modes, or no mode.

### When to use  it

- When data is categorical
- When we want to know which value is dominant
- To fill missing values

### When not to use it

- When most values are unique
- When numerical data is continuous with few repeated values
- When you need a true average value

### Example

```
names = ["Michael", "Natalia", "Agata", "Michael"]

mode = "Michael"
```