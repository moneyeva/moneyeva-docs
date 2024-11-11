# Math & Symbols Guide

This guide covers the supported math operations and variable symbols in Money Eva. Together, these tools form the backbone of Money Eva’s flexibility, enabling you to model complex financial scenarios with precision and clarity.

---

## Part 1: Supported Math Operations

Money Eva is designed around simple math operations, enabling you to create precise calculations that are both straightforward and accessible to everyone.

### **Basic Arithmetic**
- **Addition (`+`)**: Combine values or variables.
- **Subtraction (`-`)**: Subtract one value or variable from another.
- **Multiplication (`*`)**: Scale values or variables.
- **Division (`/`)**: Divide one value or variable by another.

    !!! info
        **Important Note**: If the denominator evaluates to zero, Money Eva replaces it with a very small number to avoid undefined results. This ensures that the calculation yields an extremely large number, signaling an error in the result.  

        - You can use this behavior to test whether a number equals a specific value. For example, `1 - A / A` will result in zero if A is non-zero and one if A is zero. By multiplying this result with another value, you can implement limited conditional logic.

!!! info
    **Note**: To enter a negative number, such as negative 5, simply use `0 - 5`, as single negative signs aren’t supported.

Basic arithmetic in Money Eva follows standard mathematical precedence: **multiplication (`*`)** and **division (`/`)** are evaluated before **addition (`+`)** and **subtraction (`-`)**, unless parentheses are used to explicitly define the order of operations.

---

### **Minimum and Maximum**

- **`min(A, B)`**: Returns the smaller of the two values.  

    !!! info
        **Financial Example**: In the U.S., Social Security tax is applied to income up to a certain limit, known as the wage base (e.g., $168,600 in 2024). The formula `min(168600, A) * 0.062` calculates the Social Security tax by applying the 6.2% rate to income up to the wage base, ensuring any excess income is excluded. 

- **`max(A, B)`**: Returns the larger of the two values.  

    !!! info
        **Financial Example**: In Canada, capital gains are taxed using a tiered inclusion rate. For example, gains up to $250,000 are included at 50%, while any amount above $250,000 is included at 66.67%. The formula `min(A, 250000) * 0.5 + max(A - 250000, 0) * 0.6667` calculates the total taxable amount, ensuring that each tier is applied correctly.

Both `min()` and `max()` are versatile tools for implementing caps, floors, and tiered logic in financial scenarios. Here are some common use cases:

- **Capping Contributions**: Use `min()` to limit contributions to tax-advantaged accounts, such as retirement savings, to their annual maximum limits.
- **Ensuring Minimum Payments**: Apply `max()` to enforce a minimum required loan payment or utility bill, even if the calculated amount falls below the threshold.
- **Tiered Tax Rates**: Combine `min()` and `max()` to calculate taxes across income tiers.
- **Profit Sharing Caps**: Use `min()` to cap profit-sharing contributions to a set percentage of total earnings.
- **Expense Floors**: Apply `max()` to ensure expenses, such as maintenance costs or fixed fees, don’t fall below a base amount.
- **Adjustable Bonuses**: Combine `min()` and `max()` to calculate bonuses based on performance, ensuring they remain within predefined upper and lower limits.

These functions allow for precise handling of financial rules and constraints, making them essential for accurate scenario modeling.


---

### **Type Checking and Error Visibility**
Money Eva ensures that all expressions are logically sound by performing **type checks**. This prevents nonsensical calculations, such as dividing a percentage by a time value. Errors are immediately highlighted as you edit, making it easy to identify and correct issues in real time.

---

## Part 2: Variable Symbols

Variable symbols represent values in your scenario, each with a specific type and role. They ensure clarity and consistency in calculations.

### **1. Cash Flow**
- **Description**: The heart of Money Eva’s concept, a **Cash Flow variable** represents cash amounts over time, which are tracked monthly.  
- **Representation**: Cash flows are denoted with a tilde (`~`) above the symbol to indicate their dynamic, time-based nature.
- **Combo Symbols**:  
    - **Ã<sub>iv</sub>**: **Investment Value** — Represents the time-adjusted value of all cash flows if invested, tracking the market investment return. This gives an amount-type value.  
    - **Ã<sub>cb</sub>**: **Cost Basis** — Represents the original value of all cash flows for cost basis calculation. This also gives an amount-type value.

---

### **2. Amount**
- **Description**: A single monetary value (in the current Eva’s currency).
- **Representation**: Denoted as a standalone symbol without additional formatting. 

---

### **3. Percentage**
- **Description**: A single percentage value.  
- **Representation**: Denoted as **A<sub>%</sub>**.

!!! info
    **Note on Using Percentages in Decisions/Expectations**

    When entering a percentage value into a calculation step (e.g., the annual appreciation rate in **Buy Asset**), you must input the value in its decimal form. For example:

    - Enter `0.05` for **5%**.
    - If you input `5`, it will be interpreted as **500%**, which is typically not the intended value.

    This is slightly different from percentage inputs, where you can simply type `5` in the input box with a `%` suffix, and the system automatically interprets it as **5%**. Be mindful of this distinction when working with percentage fields in calculations.


---

### **4. Years**
- **Description**: A single value representing the number of years.  
- **Representation**: Denoted as a standalone number indicating the duration in years.

---

### **5. Asset**
- **Description**: Represents an asset such as real estate, commodities, or bonds.  
- **Direct Usage**: Cannot be used directly in calculations. Instead, access its derived combo symbols:  
    - **A<sub>fmv</sub>**: **Fair Market Value** — Tracks the asset's current value following appreciation.  
    - **A<sub>cb</sub>**: **Cost Basis** — Represents the original value of the asset, including purchase price and associated costs.

---

### **6. Installment Loan**
- **Description**: Represents a loan, such as a mortgage or car loan.  
- **Direct Usage**: Cannot be used directly in calculations. Instead, access its derived combo symbols:  
    - **<i>A</i><sub>principal~</sub>**: **Principal Cash Flow** — Represents the portion of payments allocated to reducing the loan’s principal.  
    - **<i>A</i><sub>interest~</sub>**: **Interest Cash Flow** — Represents the portion of payments covering interest charges.  
    - **<i>A</i><sub>balance</sub>**: **Loan Balance** — Tracks the remaining loan balance at each whole-year point.

---


### **Auto-Complete for Expressions**

The expression editor in Money Eva is equipped with an auto-complete feature to make writing expressions faster and easier. As you type, the editor suggests available symbols that match your input. Here’s how it works:

1. **Automatic Insertion**: If there is only one matching candidate, the editor will automatically insert it to complete your input.
2. **Candidate List**: If multiple candidates are available, they will appear in a list to the right, below the expression input box.
3. **Refined Suggestions**: If you keep typing while there are multiple candidates, your input will narrow down the list. Once it matches a single candidate, that candidate will be automatically inserted.
4. **Selecting Candidates**:  
    - Use the **Enter/Return** key to quickly insert the first candidate, which is marked with a return symbol (`↵`).
    - Alternatively, click or tap on an item in the list to select your preferred option.

This feature streamlines the process of creating expressions, reducing errors and helping you build scenarios more efficiently.

