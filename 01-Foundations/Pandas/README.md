# Pandas - Data Manipulation

> [!blue] 💙 **What is Pandas?**
> Python's data analysis library. Think Excel but in code - work with tables (DataFrames), clean data, analyze, and visualize!

---

## 📚 Topics

### Basics
- [ ] [[series-dataframe|Series & DataFrame]] - Core data structures
- [ ] [[reading-data|Reading Data]] - CSV, Excel, JSON, SQL
- [ ] [[data-inspection|Data Inspection]] - head, info, describe
- [ ] [[selection-indexing|Selection & Indexing]] - loc, iloc, at, iat

### Data Cleaning
- [ ] [[missing-data|Missing Data]] - Handling NaN, dropna, fillna
- [ ] [[data-types|Data Types]] - astype, category
- [ ] [[duplicates|Duplicates]] - Finding and removing
- [ ] [[string-operations|String Operations]] - Working with text

### Data Transformation
- [ ] [[filtering|Filtering]] - Boolean indexing
- [ ] [[sorting|Sorting]] - sort_values, sort_index
- [ ] [[groupby|GroupBy]] - Split-Apply-Combine
- [ ] [[pivot-tables|Pivot Tables]] - Reshaping data
- [ ] [[merging-joining|Merging & Joining]] - Combining datasets

### Advanced
- [ ] [[time-series|Time Series]] - Working with dates
- [ ] [[apply-map|Apply & Map]] - Custom functions
- [ ] [[performance|Performance]] - Speed optimization

---

## 💚 Quick Examples

> [!green] Creating DataFrames
> ```python
> import pandas as pd
> 
> # From dictionary
> data = {
>     'name': ['Raj', 'Priya', 'Amit'],
>     'age': [25, 28, 23],
>     'city': ['Mumbai', 'Delhi', 'Bangalore']
> }
> df = pd.DataFrame(data)
> 
> # From CSV
> df = pd.read_csv('data.csv')
> 
> # Basic info
> print(df.head())
> print(df.info())
> print(df.describe())
> ```

> [!green] Common Operations
> ```python
> # Filtering
> young_people = df[df['age'] < 26]
> 
> # GroupBy
> avg_age_by_city = df.groupby('city')['age'].mean()
> 
> # Adding column
> df['age_category'] = df['age'].apply(
>     lambda x: 'young' if x < 25 else 'adult'
> )
> 
> # Sorting
> df_sorted = df.sort_values('age', ascending=False)
> ```

---

## 🚨 Common Pitfalls

> [!red] SettingWithCopyWarning
> ```python
> # ❌ WRONG - Chain indexing
> df[df['age'] > 25]['name'] = 'Updated'  # Warning!
> 
> # ✅ CORRECT - Use loc
> df.loc[df['age'] > 25, 'name'] = 'Updated'
> ```

> [!red] Modifying Copy vs Original
> ```python
> # ❌ Creates a view sometimes!
> subset = df[df['age'] > 25]
> subset['name'] = 'Changed'  # May or may not affect df!
> 
> # ✅ CORRECT - Explicit copy
> subset = df[df['age'] > 25].copy()
> ```

---

## 🎓 Interview Prep

- [ ] Explain difference between loc and iloc
- [ ] What is groupby? Give example
- [ ] How to handle missing data?
- [ ] Merge vs Join vs Concat - when to use what?
- [ ] How to optimize pandas for large datasets?

See: [[../../09-Interview-Prep/ML-Theory/pandas-questions|Pandas Interview Questions]]

---

## 🔗 Related
- [[../NumPy/README|NumPy]] (prerequisite)
- [[../Python/README|Python]] (prerequisite)
- [[../../02-Statistics-and-Data/EDA/README|EDA]] (applications)

---

**Tags:** #pandas #data-analysis #foundations  
**Status:** 🔴 Not Started  
**Prerequisites:** Python, NumPy basics
