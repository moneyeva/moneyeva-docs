# Decisions/Expectations (7 Types)

Decisions and expectations are definitions evaluated against **Year 0**, the starting point of your scenario. They help you set up financial actions or anticipate future events, creating variables that can be used throughout the rest of calculation. Below are the seven types, each with its unique fields and output.

---

## 1. **Buy Asset**
- **Fields**:
    1. **Purchase Price**: An expression defining the cost of acquiring the asset.
    2. **Annual Appreciation Rate**: The expected yearly growth rate of the asset's value.
    3. **Cost Basis**: The total acquisition cost, calculated as the purchase price plus any associated costs.  
- **Use Case**: Useful for modeling investments in real estate, commodities, or other assets.
- **Output**: Produces an **Asset variable symbol** providing access to its fair market value and cost basis.

---

## 2. **Take Installment Loan**
- **Fields**:
    1. **Loan Amount**: An expression defining the total loan principal.
    2. **Interest Rate**: The annual interest rate as an expression.
    3. **Interest Compounding**: A dropdown to select the compounding frequency (daily, monthly, quarterly, semi-annually, annually).
    4. **Amortized Over**: The number of years the loan is amortized, displayed with a **years** suffix.
    5. **After Interest-Only Period**: The duration of the interest-only period in years (optional, defaults to **0**), before amortization starts.

- **Use Case**: Ideal for modeling loans such as mortgages, student loans, or car loans.  
- **Output**: Produces an **Installment Loan variable symbol** providing access to principal, interest payment cash flows, and balance over time.

---

## 3. **Invest**
- **Fields**:
    - **Lump Sum of Cash**: An expression defining a one-time cash inflow or outflow at the starting point.
- **Use Case**: Represents scenarios where a lump sum of money is moved, such as investing into liquid assets, receiving a payout, or making an initial payment. 
- **Output**: Produces a **Cash Flow variable symbol**, representing the one-time cash inflow or outflow at **Year 0**.


---

## 4. **Expect to Invest**
- **Fields**:
    1. **Cash Amount**: An expression defining a one-time cash inflow or outflow expected in the future.
    2. **At**: Specifies when the cash movement will occur, displayed with a **years from now** suffix.
    3. **Adjust the Amount for Inflation?**: A dropdown to select **Yes** or **No**, indicating whether the cash amount should account for inflation over time.

- **Use Case**: Ideal for modeling future financial events, such as planned purchases, contributions, or payouts.  
- **Output**: Produces a **Cash Flow variable symbol**, representing the one-time cash inflow or outflow at the specified future point.

---

## 5. **Expect Monthly Cash Flow**
- **Fields**:
    1. **Monthly Amount**: An expression specifying the recurring amount per month.
    2. **From**: Defines when the cash flow starts, displayed with a **years from now** suffix (optional, defaults to **Now**).
    3. **To**: Specifies when the cash flow ends, displayed with a **years from now** suffix (defaults to an **infinity symbol** to represent no end date).
    4. **Annual Increase (Starting Now)**: The rate at which the cash flow amount increases annually. This can be an expression or set to **Follow Inflation** (optional, defaults to **Follow Inflation**).  

        !!! info
            - **Note**: The increase starts from **Year 0**, even if the cash flow begins later.  
            - **Note**: The annual increase always applies at whole-year intervals, regardless of when the cash flow starts. For example, even if the cash flow starts midway through a year, the first adjustment will align with the next whole-year point from Year 0.

- **Use Case**: Ideal for modeling recurring cash flows like rent, salary, or subscription expenses.  
- **Output**: Produces a **Cash Flow variable symbol**, representing the recurring monthly cash flows over time.

---

## 6. **Expect Yearly Cash Flow**
- **Fields**: Similar to **Expect Monthly Cash Flow**, but tailored for annual cash flows:
    1. **Yearly Amount**: An expression specifying the recurring amount per year.
    2. **From**: Defines when the yearly cash flow starts, displayed with a **years from now** suffix (optional, defaults to **Now**).
    3. **To**: Specifies when the yearly cash flow ends, displayed with a **years from now** suffix (defaults to an **infinity symbol** to represent no end date).
    4. **Annual Increase (Starting Now)**: The rate at which the yearly cash flow amount increases. This can be an expression or set to **Follow Inflation** (optional, defaults to **Follow Inflation**). 

        !!! info 
            - **Note**: The increase starts from **Year 0**, even if the cash flow begins later. 
            - **Note**: Yearly cash flows are always counted at whole-year points. If the **From** value is a floating number (e.g., 1.5 years), the first cash flow will align with the next whole-year point (e.g., Year 2), ensuring simple and consistent annual intervals.

- **Use Case**: Suitable for modeling annual cash flows, such as insurance premiums, yearly bonus payments, or lump-sum contributions.  
- **Output**: Produces a **Cash Flow variable symbol**, representing recurring yearly cash flows.

---

## 7. **Define Variable (Numerical)**
- **Fields**:
    - **Numerical Expression**: A calculation producing a numeric value.  
- **Use Case**: Allows you to define reusable constants or calculated values, such as specific percentages, adjustments, or intermediate results.  
- **Output**: Produces a **Numerical variable symbol**, representing the result of the calculation.

---

These seven types of decisions and expectations provide powerful tools to define key variables and actions in your Eva. By combining these definitions with inputs and calculations, you can create detailed, flexible scenarios tailored to your financial questions.
