# Marketing Funnel & Conversion Performance Analysis
**Future Interns | Data Science & Analytics | Task 3 (2026)**

## Problem
Bank ke telemarketing campaign mein customers kahan drop hote hain, kaunse segments best convert karte hain, aur conversion kaise badhaye?

## Dataset
UCI Bank Marketing (`bank-full.csv`), 45,211 customers, 17 columns. Target `y` = term deposit subscribe kiya ya nahi. No missing values, no duplicates.

## Tools
Python (pandas, matplotlib), Power BI, Jupyter, VS Code.

## Funnel (strictly nested)
| Stage | Customers | % of previous | % of start |
|---|---|---|---|
| Contacted | 45,211 | - | 100% |
| Engaged (call >= 3 min) | 22,674 | 50.15% | 50.15% |
| Converted (engaged and subscribed) | 4,588 | 20.23% | 10.15% |

Overall conversion (all "yes"): **5,289 / 45,211 = 11.70%**. 701 customers ne 3 min se kam call mein bhi subscribe kiya (isliye 5,289 > 4,588).

## Key Insights
1. **Biggest drop-off:** Engaged se Converted mein 79.8% drop. 18,086 customers ne 3+ min baat ki par subscribe nahi kiya, yahan pitch/offer improve karna sabse bada opportunity hai.
2. **Previous campaign success** wale customers 64.7% convert hote hain (vs 9.2% unknown). Inhe pehle target karo.
3. **Students (28.7%) aur retired (22.8%)** best jobs hain. Blue-collar sabse kam (7.3%). Age 65+ = 42.1%, <25 = 25.6%.
4. **Cellular (14.9%)** telephone (13.4%) se behtar; **"unknown" contact sirf 4.1%**, jo 13,020 customers hain. Contact data capture sudharo.
5. **Seasonality:** Mar (52%), Sep (46%), Oct (44%), Dec (47%) mein conversion bahut high hai par volume bahut kam (<750 customers). **May mein 13,766 calls par sirf 6.7%**, yani zyada calls, kam result.
6. **Contact fatigue:** 1 call = 14.6%, 6+ calls = 5.8%. 3 se zyada baar call karna wasteful hai.
7. **Financial profile:** Housing loan wale 7.7% vs bina loan ke 16.7%; personal loan wale 6.7% vs 12.7%. Balance 1000+ wale 15%+, negative balance 6.9%.

## Recommendations
- Previous success, students, retired aur 65+ ko priority list mein rakho.
- Calls ko max 2-3 attempts tak limit karo.
- Volume ko May se shift karke Mar/Sep/Oct/Dec jaise high-conversion months mein badhao (test karke).
- Cellular channel prefer karo, aur "unknown" contact type ka data fix karo.
- Engaged customers ke liye follow-up (email/SMS offer) banao, kyunki 18K warm leads waste ho rahe hain.
- Housing/personal loan wale customers ko alag product ya message do.

## Limitations
- `duration` call ke baad hi pata chalta hai, isliye engagement ek **post-call** metric hai, pre-call targeting ke liye nahi.
- Dataset mein sirf month hai (year/date nahi), isliye time trend month-level hai.
- Ye observational data hai; segments ke beech difference ka matlab causation nahi.
- `poutcome = unknown` (82% rows) mein previous history nahi hai.

## Files
- `bank_marketing_analysis.ipynb`: poora code
- `powerbi_ready/`: Power BI ke liye clean CSVs
- `charts/dashboard.png`: dashboard screenshot
- `POWERBI_GUIDE.md`: Power BI step by step
