# Calculations (2 Types)

Calculations in Money Eva are evaluated at each **whole-year point**, allowing you to define intermediate results until deriving the final evaluation of your scenario. These calculations help you create reusable variables and calculate cash values for your scenario.

---

## Intermediate Calculations

### 1. **Define Variable (Numerical)**
- **Description**: A numerical calculation that produces a single value, based on expressions or formulas.
- **Use Case**: Useful for defining constants, derived values, or intermediate calculations needed for further steps in the scenario.
- **Output**: Produces a **Numerical variable symbol**, representing the calculated value at each whole-year point.

---

### 2. **Define Variable (Cash Flow)**
- **Description**: A calculation that combines and manipulates cash flows using expressions. This allows you to:
    - Add (`+`) one cash flow to another.
    - Subtract (`-`) one cash flow from another.
    - Scale a cash flow up or down by multiplying (`*`) or dividing (`/`) it by a factor.
- **Use Case**: Ideal for creating complex cash flow models, such as net cash flow, adjusted income, or cash flow scaling over time.
- **Output**: Produces a **Cash Flow variable symbol**, representing the combined or transformed cash flows evaluated at each whole-year point.

---

## Final Calculation

### **Cash Value**
- **Description**: A numerical calculation representing the ultimate result of the scenario at each whole-year point. All preceding variable symbols, including those from calculations and cash flows, are available for use in defining this final value.
- **Use Case**: Defines key metrics such as total net worth, cumulative savings, or other summary value for the scenario.

- **Output**: Produces the **final numerical result**, evaluated at each whole-year interval.

---

These calculation types, combined with user inputs and Year 0 decisions/expectations, give you the flexibility to craft detailed, dynamic scenarios that evolve over time. By leveraging intermediate calculations and final cash values, you can model a wide range of financial situations with accuracy and insight.

