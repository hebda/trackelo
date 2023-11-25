# trackelo

Thanks Matt for inspiration: https://mattmazzola.medium.com/implementing-the-elo-rating-system-a085f178e065

Current dataset:
- 2023
- men's 1500m, mile, 2000m, 3000m, 3000mSC, 2 mile, 5000m, 10,000m
- women's 1500m, mile, 3000m, 3000mSC, 5000m, 10,000m
- Diamond League and World Championships (excluding prelims and semis)

Elo settings:
- k-factor: 32
- Exponent denominator: 400
- Exponent base: 10
- Everyone starts with 1000 points
- Points cannot go below 1000

# Results - Men

```
Jakob INGEBRIGTSEN             1633
Soufiane EL BAKKALI            1549
Yared NUGUSE                   1466
Yomif KEJELCHA                 1456
Lamecha GIRMA                  1433
Samuel FIREWU                  1419
Joshua CHEPTEGEI               1411
Simon Kiprop KOECH             1386
Daniel Simiu EBENYO            1386
Josh KERR                      1375
Jacob KROP                     1349
George BEAMISH                 1338
Telahun Haile BEKELE           1330
Hagos GEBRHIWET                1323
Selemon BAREGA                 1322
```

# Results - Women

```
Faith KIPYEGON                 1650
Beatrice CHEBET                1501
Diribe WELTEJI                 1494
Winfred Mutile YAVI            1468
Beatrice CHEPKOECH             1457
Laura MUIR                     1455
Freweyni HAILU                 1437
Sifan HASSAN                   1409
Letesenbet GIDEY               1380
Ejgayehu TAYE                  1377
Nelly CHEPCHIRCHIR             1356
Medina EISA                    1355
Faith CHEROTICH                1352
Margaret Chelimo KIPKEMBOI     1337
Lilian Kasait RENGERUK         1308
```
