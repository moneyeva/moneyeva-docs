# Inputs

Money Eva supports six primary types of input, allowing you to define key variables for your financial scenarios with precision and clarity. Each input type produces a unique variable symbol that can be used in your calculations, making scenarios both flexible and intuitive.

---

## Primary Types

### 1. **Amount**
- **Description**: A single input box for entering a currency value.  
- **Use Case**: Ideal for defining any monetary amount.  
- **Output**: Produces an **Amount variable symbol** for use in calculations.

---

### 2. **Cash Flow**
- **Description**: Two input boxes:
     1. **Amount**: Enter the cash flow amount, with a toggle for **monthly** or **yearly** values.
     2. **Annual Increase Rate**: Specify the rate at which the cash flow increases annually. Optionally, empty it out and select **"Follow Inflation"** to tie this to the global inflation rate.  
- **Use Case**: Designed for recurring cash flows like rent, insurance premiums, or salary.  
- **Output**: Produces a **Cash Flow variable symbol** for use in calculations.

---

### 3. **Current Asset**
- **Description**: Three input boxes:
     1. **Fair Market Value**: The current value of the asset.
     2. **Annual Appreciation Rate**: The expected rate of appreciation.
     3. **Purchase Price**: The original purchase price of the asset.  
- **Use Case**: Perfect for assets like real estate, commodities, bonds, or other investments that you already own.  
- **Output**: Produces an **Asset variable symbol** providing access to its fair market value and cost basis.

---

### 4. **Installment Loan**
- **Description**: Three input boxes:
     1. **Loan Balance**: The remaining balance of the loan.
     2. **Interest Rate**: The annual interest rate on the loan.
     3. **Remaining Amortization**: The remaining time to pay off the loan.  

    !!! info
        Additionally, the details dialog through the **"?" button** provides an option to select the **Interest Compounding** frequency:
        
        - Daily, Monthly, Quarterly, Semi-Annually, or Annually.  

- **Use Case**: Best for loans like mortgages, car loans, or personal loans.  
- **Output**: Produces an **Installment Loan variable symbol** providing access to principal, interest payment cash flows, and balance over time.

---

### 5. **Percentage**
- **Description**: A single input box for entering a percentage value (**%**).
- **Use Case**: Useful for defining any rates.  
- **Output**: Produces a **Percentage variable symbol**.

---

### 6. **Years/Months**
- **Description**: A single input box with a toggle to switch between **years** or **months**.  
- **Use Case**: Useful for defining a time horizon, such as the duration of a project or investment.
- **Output**: Produces a **Years variable symbol**.

---

## Additional Types

These specialized input types are designed to enhance scenarios that require an age-based perspective or retirement planning. 

### 1. **Age**
- **Description**: Accepts a whole number in years. This enables the chart to display **"Age"** instead of **"# Years from Now"**.  
- **Rules**: Limited to **1 occurrence** per Eva.  
- **Output**: Produces a **Years variable symbol**.

---

### 2. **Retirement Age**
- **Description**: Enables a global input for **"Investment Return After Retirement"** (a percentage value).  
- **Rules**: Limited to **1 occurrence** per scenario and requires an **Age input** to function.  
- **Use Case**: Essential for scenarios that transition from working years to retirement, allowing for distinct returns before and after retirement.  
- **Output**: Produces a **Years variable symbol**.

---

These input types provide the foundation for creating flexible, data-driven scenarios in Money Eva. By combining these inputs, you can build highly personalized financial models that reflect real-life situations with precision.
