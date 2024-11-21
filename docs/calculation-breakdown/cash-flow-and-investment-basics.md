# Cash Flow & Investment Basics

This page dives into the foundational concepts of Money Eva, focusing on cash flow, time value assumptions, and essential calculations like `iv` (Investment Value) and `cb` (Cost Basis). These tools simplify financial scenario modeling while maintaining precision and clarity.

---

## Cash Flow & Time Value Assumptions

### Cash Flow: The Core Concept
At the heart of Money Eva is [**Cash Flow**](./math-and-symbols-guide.md#1-cash-flow)—representing money moving in or out over time. Every scenario revolves around cash flows, tracked dynamically to show their impact over time.

### Assumption: Invest Free Cash
Money Eva assumes that any **free cash** is invested in a **high-liquidity market investment**:

- **Global Investment Return Rate**: All cash flows follow a single global market investment return rate for simplicity and consistency.
- **High Liquidity**: This assumption ensures cash remains accessible for withdrawals when needed.
- **"Market Investment Return After Retirement"**: When both [**Age**](./inputs.md#1-age) and [**Retirement Age**](./inputs.md#2-retirement-age) inputs are present, an additional box appears, allowing you to define a separate investment return rate specifically for post-retirement scenarios.

### Why One Global Rate?
Using a single investment return rate streamlines modeling and provides clarity across scenarios. Users should deduct any applicable **management fee percentage** when entering the global rate to ensure accurate calculations.

!!! info
    #### Typical Market Investment Return Rates

    - **All Equity Portfolio**: 6-10% annually (high risk, long-term growth).  
    - **50/50 Equity & Bonds**: 4-7% annually (balanced risk/return).  
    - **All Bonds Portfolio**: 2-4% annually (low risk, steady income).  
    - **Other Options (e.g., REITs)**: 3-8% annually (varies by asset class).

    #### Typical Management Fees

    These fees are taken from your investment returns and should be considered unless they are already included in the reported performance.

    - **ETFs**: 0.05-0.50% (low-cost, passive).  
    - **Robo-Advisors**: 0.25-0.50% (automated portfolios).  
    - **Mutual Funds**: 1-2.5% (active management). 
    - **DIY Investing**: $0-$10 per trade (platform-dependent).  

    Note: Returns and fees vary based on the specific product, provider, and market conditions. Always consider your time horizon and risk tolerance.
 
    #### Typical Inflation Rates

    - **Developed Countries**: Inflation rates usually range from **2-3% annually**, reflecting stable, mature economies. Central banks often target **2%** as an ideal rate to balance growth and price stability.

    - **Emerging Markets**: Inflation rates can range from **4-7% annually**, driven by faster economic growth, currency volatility, or supply chain challenges.

    - **High-Inflation Periods**: Inflation may spike to **10% or more** during economic crises, global disruptions, or hyperinflation scenarios. Inflation-Adjusted Cost Basis policies ([see below](./cash-flow-and-investment-basics.md#inflation-adjusted-cost-basis)) may be implemented during prolonged periods of hyperinflation.

    - **Deflationary Periods**: Occasionally, inflation may drop below **0%**, leading to deflation. This is rare and often linked to recessions or reduced consumer spending.


---

## Negative Cash Flow

### What is Negative Cash Flow?
Negative cash flow represents **required cash** and is modeled to mirror positive cash flow:

- **Simplified Modeling**: Negative cash flow behaves predictably and intuitively.
- **Write-Offs or Tax Credits**: Negative cash flow can represent deductions or credits in scenarios such as operating losses or depreciation. These scenarios often involve offsets to taxable income, allowing you to model their financial impact effectively.


### Withdrawals from Non-Tax-Sheltered Accounts
Withdrawals from non-tax-sheltered accounts require additional handling due to **capital gains tax** impacting asset growth:

- **Scaled Withdrawals**: To withdraw a specific amount, you must withdraw **more** to cover capital gains tax.
- **Dynamic Scaling**: The proportion of capital gains increases over time, requiring dynamic adjustments to the scaling factor.

    !!! info
        - **Example Formula**: **1 / (1 - B<sub>%</sub> * (Ã<sub>iv</sub> - Ã<sub>cb</sub>) / Ã<sub>iv</sub>)**  
            - **B<sub>%</sub>** is the capital gains tax rate.
            - The formula calculates the scaling factor, which must be multiplied by the desired withdrawal cash flow to account for taxes and reflect the impact on the account value.
            - See the [**Math & Symbols Guide**](./math-and-symbols-guide.md) page for more details.

- **Adjustment to `iv`**: The scaled withdrawal reduces the **Investment Value (iv)** to reflect its impact on future growth.

---

## Capital Gains: `iv` and `cb`

### The Basic Formula
Capital gains are calculated using the formula: **Ã<sub>iv</sub> - Ã<sub>cb</sub>**, where:

- **Ã<sub>iv</sub>**: Represents the value of investments, following the market investment return rate.
- **Ã<sub>cb</sub>**: Represents the cost basis, tracking the original value for tax calculation.

### Applying Capital Gains Tax
Once **Ã<sub>iv</sub> - Ã<sub>cb</sub>** is determined, the relevant tax rate can be applied to calculate the taxable amount based on your jurisdiction or a percentage input.

!!! info
    For [assets](./math-and-symbols-guide.md#5-asset), use **A<sub>fmv</sub> - A<sub>cb</sub>** to determine capital gains for tax calculations, and remember to deduct any applicable closing costs.

---

## Inflation-Adjusted Cost Basis

### What is Cost Basis (`cb`)?
Cost basis tracks the original value of cash flows. When the **"Cost Basis (cb) is Inflation-Adjusted"** toggle is enabled in edit mode, the cost basis is adjusted for inflation. Otherwise, `cb` remains fixed and does not account for inflation. 

### Key Uses of Inflation-Adjusted Cost Basis

1. **Taxation in Inflation-Indexed Jurisdictions**:
   In jurisdictions where cost basis is indexed to inflation, enabling the toggle ensures **Ã<sub>iv</sub> - Ã<sub>cb</sub>** accurately represents taxable capital gains.

    !!! warning
        **Heads Up!** These jurisdictions are rare, and Money Eva displays a warning when you toggle this option.

2. **Evaluating Purchasing Power**:
   When adjusted for inflation, `cb` reflects the **cost of purchasing power** over time. This is especially helpful for scenarios that prioritize spending analysis over investment returns or net worth, focusing on the total purchasing power used.


---

## Conditional Field Visibility

### Smart Field Behavior
To maintain a clean and intuitive interface, certain fields are hidden or greyed out unless relevant:

- **Market Investment (`iv`) Return**:
    - Hidden or greyed out in edit mode if no expression references the **`iv`** symbol.
- **Inflation-Adjusted Cost Basis (`cb`) Toggle**:
    - Hidden or greyed out in edit mode if no expression references the **`cb`** symbol.

These features ensure users focus only on fields relevant to their specific scenario, reducing clutter and enhancing usability.

---

# Conclusion

With cash flow as the foundation and tools like `iv` and `cb`, Money Eva makes it easy to model a wide range of financial scenarios. A single global market investment return rate, along with the option to adjust cost basis for inflation, provides consistent, clear, and actionable insights, empowering users to make informed decisions.
