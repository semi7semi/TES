from app_2.models import Companies

BTC_DATA = (
    ('2021-7-16', 31745.52),
    ('2021-7-15', 31730.85),
    ('2021-7-14', 32861.26),
    ('2021-7-13', 32583.88),
    ('2021-7-12', 32868.73),
    ('2021-7-11', 34473.46),
    ('2021-7-10', 33431.63)
)

GOLD_DATA = (
    ('2021-7-16', 1811.01),
    ('2021-7-15', 1829.49),
    ('2021-7-14', 1827.41),
    ('2021-7-13', 1806.18),
    ('2021-7-12', 1808.33),
    ('2021-7-9', 1802.71),
    ('2021-7-8', 1803.65)
)



# yyy-mm-dd
for btc in BTC_DATA:
    Companies.objects.create(
        name = "Bitcoin",
        price = btc[1],
        date = btc[0],
    )

for gold in GOLD_DATA:
    Companies.objects.create(
        name="Złoto",
        price=gold[1],
        date=gold[0],
    )