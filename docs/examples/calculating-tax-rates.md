# Calculating Tax Rates

## Tax Rate Library

This page provides a library of equations to calculate various tax rates, designed to be used in Money Eva's "[Define Variable (Numerical)](../calculation-breakdown/decisions-expectations.md#7-define-variable-numerical)" calculations. These examples cover tiered rate systems, deductions, and adjustments for different jurisdictions.

Want to contribute? Visit our <a href="https://github.com/moneyeva/moneyeva-docs" target="_blank" rel="noopener">:material-github:{ .github } **GitHub repository**</a>. Whether you want to refine existing examples, add new equations, or expand coverage for specific jurisdictions, your input can make this resource even more valuable!

{{ tax_rates_table }}

---

## Example 1: Canada Federal Tax (2024)

**Equation**:  

- (((min(max(A, 0), 55867) - 0) * 0.15 + (min(max(A, 55867), 111733) - 55867) * 0.205 + (min(max(A, 111733), 173205) - 111733) * 0.26 + (min(max(A, 173205), 246752) - 173205) * 0.29 + (max(A, 246752) - 246752) * 0.33) - min(15705, A) * 0.15)

**Explanation**:

- This formula calculates federal tax in Canada for 2024 using tiered rates for different income brackets.
- The **basic personal amount** of $15,705 is deducted at the lowest tax rate (15%).
- **Income Brackets**:
    - $0–$55,867 taxed at 15%.
    - $55,868–$111,733 taxed at 20.5%.
    - $111,734–$173,205 taxed at 26%.
    - $173,206–$246,752 taxed at 29%.
    - Over $246,752 taxed at 33%.

---

## Example 2: U.S. Federal Tax (2024, Single Filer)

**Equation**:  

- ((min(max(A, 0), 11600) - 0) * 0.1 + (min(max(A, 11600), 47150) - 11600) * 0.12 + (min(max(A, 47150), 100525) - 47150) * 0.22 + (min(max(A, 100525), 191950) - 100525) * 0.24 + (min(max(A, 191950), 243725) - 191950) * 0.32 + (min(max(A, 243725), 609350) - 243725) * 0.35 + (max(A, 609350) - 609350) * 0.37)

**Explanation**:

- Calculates U.S. federal income tax for single filers in 2024.
- **Income Brackets**:
    - $0–$11,600 taxed at 10%.
    - $11,601–$47,150 taxed at 12%.
    - $47,151–$100,525 taxed at 22%.
    - $100,526–$191,950 taxed at 24%.
    - $191,951–$243,725 taxed at 32%.
    - $243,726–$609,350 taxed at 35%.
    - Over $609,350 taxed at 37%.
