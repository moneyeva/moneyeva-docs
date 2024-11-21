# Common Use Cases

Money Eva’s flexibility allows users to model a wide range of financial scenarios. Below are some common use cases to help you understand how the app can be applied to real-world financial questions.

!!! info
    Also check the other pages under "Examples" section for detailed math equations.

---

## 1. **Rent vs. Buy Analysis**

<a href="https://moneyeva.com/?search=Rent+Buy+Home" target="_blank" rel="noopener">Search this topic on Money Eva</a>

- **Objective**: Compare the financial impact of renting versus buying a home over time.
  
- **What to Compare**: Focus on **Net Worth**. To ensure a fair comparison, align cash inputs for both scenarios. This can be done by:
    - Using the same income level and subtracting renting or homeownership expenses (assuming identical spending habits); or
    - Treating the costs from one scenario as investments in the other scenario to balance the analysis.

- **Key Steps**:
    1. Define monthly rent as a **Cash Flow** with an annual increase tied to inflation.
    2. Define the purchase price and expected appreciation of the home as an **Asset**.
    3. Set up the financing (mortgage) as an **Installment Loan**.
    4. Add related homeownership costs, including property tax, maintenance, and closing fees.
    5. Incorporate any tax-sheltered accounts to capture the investment value of cost savings.
    6. Account for primary residence tax exemptions when evaluating the net worth of the home (i.e., assuming a hypothetical sale for cash).

- **Insights**: Identify which option—renting or buying—offers better long-term value based on your financial situation and assumptions.


---

## 2. **Estimating Retirement Savings**

<a href="https://moneyeva.com/?search=Retirement+Spending" target="_blank" rel="noopener">Search this topic on Money Eva</a>

- **Objective**: Determine whether your current savings, contributions, and expected returns are sufficient to meet your retirement goals.

- **What to Compare**: Focus on your **Retirement Account Balance**:
    - Before retirement, contributions and investment returns increase the balance.
    - After retirement, spending decreases the balance until falling below zero.

- **Key Steps**:
    1. Define monthly or yearly contributions as a **Cash Flow** to model pre-retirement savings growth.
    2. Define the spending level after retirement as a negative **Cash Flow**.
    3. Add a **Retirement Age** input to enable distinct market investment returns after retirement.
    4. Exclude pension plans or external income sources outside personal retirement savings from the post-retirement spending.
    5. Allocate savings and withdrawals across tax-advantaged and non-tax-sheltered accounts based on their capacity and rules.
    6. When [modeling withdrawals from non-tax-sheltered accounts](../calculation-breakdown/cash-flow-and-investment-basics.md#withdrawals-from-non-tax-sheltered-accounts), account for the capital gains tax portion, which reduces the investment value (`iv`) growth.

    !!! info
        **Note**: Money Eva doesn’t model mandatory withdrawals from tax-advantaged accounts (e.g., US RMD, Canada RRIF, or Australian Superannuation) as they typically reduce account value by less than 5%. Market fluctuations over a lifetime far outweigh this impact.

- **Insights**: Visualize the growth of your savings over time and evaluate whether they will last through your retirement years.

---

## 3. **Budgeting for a Big Purchase**


<a href="https://moneyeva.com/?search=Lease+Finance+Budget" target="_blank" rel="noopener">Search this topic on Money Eva</a>


- **Objective**: Plan for a major expense, such as buying a car, by comparing savings and financing options.

- **What to Compare**: Choose an approach based on your financial situation:
    - **Option A**: If you have the full amount for a cash purchase, treat both the purchase and financing plans as lost investment opportunities. Compare to see which option results in the smallest lost opportunity.
    - **Option B**: If financing is your only option (e.g., via installment payments), the concept of lost investment opportunity doesn’t apply. Instead, use the [Inflation-Adjusted Cost Basis (cb)](../calculation-breakdown/cash-flow-and-investment-basics.md#key-uses-of-inflation-adjusted-cost-basis) to evaluate the total purchasing power required.

- **Key Steps**:
    1. Define the one-time expense as **Invest** for upfront costs.
    2. Define recurring payments as a **Cash Flow**.
    3. Define any future-dated payments, such as deferred costs, as **Expect to Invest**.
    4. If financing through a bank instead of using vendor-provided terms, model the loan as an **Installment Loan** to calculate payments and interest.
    5. Depending on your comparison approach, sum up expenses using either:
        - Investment Value (`iv`) to measure lost opportunity.
        - Inflation-Adjusted Cost Basis (`cb`) to determine total purchasing power spent.

- **Insights**: Analyze the impact of financing versus upfront payment on your financial goals to identify the option that is most cost-effective in the long run.


---

## 4. **Annuity Plan vs. Self-Managed Savings**

<a href="https://moneyeva.com/?search=Pension+Plan+PP" target="_blank" rel="noopener">Search this topic on Money Eva</a>


- **Objective**: Compare the financial benefits of purchasing an annuity plan versus managing your own savings, based on your life expectancy.

- **What to Compare**: Focus on the **Net Benefit** of each approach:
    - For the annuity plan, consider the guaranteed payouts over your expected lifespan and compare them to the upfront cost.
    - For self-managed savings, factor in the investment growth before and after retirement and evaluate whether withdrawals can sustain the same payouts over your expected lifespan.

- **Key Steps**:
    1. Define the **Age** input to reflect your current age, providing a timeline for calculations.
    2. Set a **Retirement Age** to enable separate market investment return rates for pre- and post-retirement growth.
    3. For the annuity plan:
        - Define the upfront cost as **Invest**.
        - Define the annuity payouts as a **Cash Flow**, starting at your retirement age and continuing for your expected lifespan.
    4. For self-managed savings:
        - Define the initial savings as **Invest**.
        - Define withdrawals as a negative **Cash Flow**, adjusted to match the annuity payouts.
        - Apply the appropriate market investment return rates to project growth pre- and post-retirement.
    5. Compare the total value provided by the annuity payouts to the net value of your self-managed savings after accounting for withdrawals and investment growth.

- **Insights**: Determine whether the guaranteed payouts of the annuity plan outweigh the potential growth and flexibility of managing your own savings, based on your expected lifespan and financial assumptions.

---

## 5. **Early Retirement Feasibility**

<a href="https://moneyeva.com/?search=Retirement+Feasibility" target="_blank" rel="noopener">Search this topic on Money Eva</a>

- **Objective**: Assess whether retiring earlier than planned is financially viable, given your current savings, expected contributions, and spending levels.

- **What to Compare**: Focus on the **Sustainability of Savings**:
    - Determine how long your savings can last under an early retirement scenario.
    - Compare different retirement ages to evaluate the trade-offs between retiring early and allowing additional time for savings to grow.

- **Key Steps**:
    1. Define your current savings as **Invest**.
    2. Set up **Cash Flows**:
        - Monthly or yearly contributions until the chosen retirement age.
        - Post-retirement spending levels as negative cash flows.
    3. Use the **Age** input to represent your current age.
    4. Enable the separate post-retirement **Market Investment Return** rate by defining a **Retirement Age** input to reflect more conservative investment growth after retirement.
    5. If you have non-tax-sheltered accounts, [include the dynamic scaling factor for withdrawals to account for capital gains tax](../calculation-breakdown/cash-flow-and-investment-basics.md#withdrawals-from-non-tax-sheltered-accounts).
    6. Consider incorporating additional income sources, such as rental income or part-time work, as **Cash Flows**.

- **Insights**: Identify the earliest feasible retirement age by comparing how long your savings will last under each scenario. Explore how adjustments to spending, contributions, or expected returns can impact the feasibility of early retirement.

---

## 6. **Saving for a Child’s Education**


<a href="https://moneyeva.com/?search=Child+Education" target="_blank" rel="noopener">Search this topic on Money Eva</a>

- **Objective**: Plan and evaluate whether your savings and contributions will cover future education expenses, such as college or university tuition.

- **What to Compare**: Focus on the **Education Fund Balance**:
    - Assess if your savings, contributions, and investment growth will meet the estimated cost of education.
    - Evaluate the impact of starting early or late on the fund’s growth and sufficiency.

- **Key Steps**:
    1. Define the **Age** of your child to establish the timeline for savings and withdrawals.
    2. Set up **Cash Flows**:
        - Monthly or yearly contributions to the education fund.
        - Future education expenses as negative cash flows, starting when your child begins college and ending when the program completes.
    3. If using a tax-advantaged education savings account (e.g., RESP in Canada):
        - Omit the capital gains tax calculation to reflect its tax-free status.
        - Model any government contributions, grants, or matching programs as additional positive cash flows.
    4. Define the global market investment return rate to reflect the growth of the education fund.
    5. Compare scenarios with different contribution levels or timelines to see how adjustments impact the fund’s ability to cover expenses.

- **Insights**: Determine whether your savings plan is sufficient to cover expected education costs. Explore how starting contributions earlier or increasing them can improve the likelihood of meeting your goal.


---

## 7. **Pay Off Debt vs. Invest**

<a href="https://moneyeva.com/?search=Payoff+Debt" target="_blank" rel="noopener">Search this topic on Money Eva</a>

- **Objective**: Evaluate whether it’s more beneficial to use extra cash to pay off debt early or invest it for potential growth.

- **What to Compare**: Focus on the **Account Value Minus Debt**:
    - Subtract the debt balance from the account value to calculate net worth.
    - Include potential investment returns by matching the cash input (invest the equivalent of what would be used for debt payments).
    - Consider the after-tax cost of debt and the after-tax returns on investment for an accurate comparison.

- **Key Steps**:
    1. Define the debt as an **Installment Loan** with its current balance, interest rate, and remaining term.
    2. Define the potential investment as **Invest**, using the global market investment return rate.
    3. If applicable, account for the after-tax cost of the loan, including any deductible interest.
    4. Model cash flow scenarios:
        - **Scenario A**: Use extra cash as a lump-sum payment to reduce or eliminate the loan balance, then gradually rebuild the investment using the savings from reduced debt payments.
        - **Scenario B**: Invest the extra cash immediately while continuing to make regular debt payments.
    5. Compare the account value minus debt balance of each scenario.

- **Insights**: Identify which option provides greater value over time, based on your financial situation. This example helps clarify when paying off debt is more advantageous than investing and vice versa.

---

## Conclusion
These examples demonstrate just a few of the ways Money Eva can be used to model financial scenarios. Tailor them to your unique situation or create entirely new scenarios to explore your financial questions with precision and clarity.
