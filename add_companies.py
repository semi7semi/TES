from app_2.models import Companies

BTC_DATA = (
    ('2021-7-6', 31745.52),
    ('2021-7-5', 31730.85),
    ('2021-7-4', 32861.26),
    ('2021-7-3', 32583.88),
    ('2021-7-2', 32868.73),
    ('2021-7-1', 34473.46),
    ('2021-6-30', 33431.63)
)

GOLD_DATA = (
    ('2021-7-6', 1811.01),
    ('2021-7-5', 1829.49),
    ('2021-7-4', 1827.41),
    ('2021-7-3', 1806.18),
    ('2021-7-2', 1808.33),
    ('2021-7-1', 1802.71),
    ('2021-6-30', 1803.65)
)

SILVER_DATA = (
    ('2021-7-14', 811.01),
    ('2021-7-13', 829.49),
    ('2021-7-12', 827.41),
    ('2021-7-11', 806.18),
    ('2021-7-10', 808.33),
    ('2021-7-9', 802.71),
    ('2021-7-8', 803.65)
)



# yyy-mm-dd
for btc in BTC_DATA:
    company = Companies()
    company.name = 'Bitcoin'
    company.price = btc[1]
    company.date = btc[0]
    company.save(using='tes')

for gold in GOLD_DATA:
    company = Companies()
    company.name = 'Gold'
    company.price = gold[1]
    company.date = gold[0]
    company.save(using='tes')

for silv in SILVER_DATA:
    company = Companies()
    company.name = 'Srebro'
    company.price = silv[1]
    company.date = silv[0]
    company.save(using='tes')