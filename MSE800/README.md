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

