activity 3:
    different roles get different ability.
    ** tutor
        give the command
    ** student
        do the math and print it out
    ** assistant
        verity the input is legal or not
ability is present with a method. 

*** week3 activity 2:
    currency diagram: https://docs.google.com/drawings/d/1IAIKmG0tCV2STHiC97D_rUXO9NdBUnIKsZGNTFafAuw/edit
    Relationship Types (1:1 / 1:N / M:N)
User ↔ UserWallet
1:N
One User can have many Wallets; One Wallet belongs to only one User
Currency ↔ UserWallet
1:N
One Currency can be used in many Wallets; One Wallet uses only one Currency
User ↔ ExchangeTransaction
1:N
One User can place many Exchange Transactions; One Transaction belongs to one User
Currency ↔ ExchangeTransaction
1:N (twice)
One Currency can be from currency in many transactions
One Currency can be to currency in many transactions
AdminStaff ↔ RateUpdateLog
1:N
One Admin can update many currency rates (many logs); One log created by one Admin
Currency ↔ RateUpdateLog
1:N
One Currency has many rate update logs; One log for one Currency


week4 activity 1
---
Total Database Tables Created: 6
All tables are normalized with clear PK/FK constraints. Below is a concise justification for each table:

---
1. Table: User
Core Purpose: Store registered user account and login details.
Justification: Uniquely identifies users, links to their wallets/transactions, and enables account management. Indispensable for user identity verification.
2. Table: Currency
Core Purpose: Manage supported global currencies and real-time exchange rates.
Justification: Provides standardized currency data for exchange calculations, fee deduction, and rate displays. Critical for core exchange functionality.
3. Table: UserWallet
Core Purpose: Track user balances for each currency.
Justification: Serves as the digital asset carrier for users, links to User and Currency, and enables fund settlement for exchanges.
4. Table: ExchangeTransaction
Core Purpose: Record all user exchange orders and details.
Justification: Ensures transaction traceability, supports compliance/auditing, and provides a basis for user inquiries and dispute resolution.
5. Table: AdminStaff
Core Purpose: Manage backend administrator accounts and roles.
Justification: Separates user/administrator permissions, enables rate management and system maintenance, and ensures backend security.
6. Table: RateUpdateLog
Core Purpose: Log all exchange rate modification operations.
Justification: Ensures compliance via audit trails, tracks rate changes, and enables responsibility traceability for administrators.


week4 activity 1
---
2 files. run week4aitivity2.py and will get pic:week4activity2.png
---