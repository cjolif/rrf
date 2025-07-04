from rff import rff

def test_default():
    rankings = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
    ]

    expected = [
        (1, 0.04918032786885246),
        (2, 0.04838709677419355),
        (3, 0.047619047619047616),
        (4, 0.046875),
        (5, 0.046153846153846156)
    ]

    computed = rff(rankings=rankings)

    assert computed == expected

def test_k1():
    rankings = [
        [1, 2],
        [1, 2],
    ]

    expected = [
        (1, 1.0), (2, 0.6666666666666666)
    ]

    computed = rff(rankings=rankings, k=1)

    assert computed == expected

def test_k10():
    rankings = [
        [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16, 17, 20,
            23, 32, 24, 21, 13, 14, 18, 19, 22, 36, 38, 26, 27,
            28, 29, 30, 31, 33, 34, 35, 37, 38, 39,
        ],
        [
            3, 1, 6, 7, 2, 4, 9, 13, 12, 21, 17, 14, 18, 16, 35,
            31, 25, 26, 5, 28, 37, 34, 29, 33, 8, 19, 10, 11,
            15, 32, 30, 20, 22, 39, 23, 24, 27, 36, 38,
        ],
        [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
            16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
            28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
        ],
    ]

    expected = [
         (1, 0.26515151515151514),
         (3, 0.24475524475524477),
         (2, 0.23333333333333334),
         (4, 0.20535714285714285),
         (6, 0.20192307692307693),
         (7, 0.18907563025210083),
         (5, 0.16781609195402297),
         (9, 0.16408668730650156),
         (12, 0.14354066985645933),
         (8, 0.13968253968253969),
         (13, 0.1312918809412498),
         (10, 0.12702702702702703),
         (17, 0.12465608465608466),
         (16, 0.12179487179487179),
         (11, 0.12155388471177944),
         (14, 0.11837121212121213),
         (21, 0.11559139784946237),
         (18, 0.10949557688688123),
         (15, 0.10911928651059086),
         (20, 0.0956043956043956),
         (19, 0.09167230110434979),
         (26, 0.0898078529657477),
         (23, 0.08956228956228957),
         (38, 0.0891018569589998),
         (31, 0.08610759631746587),
         (24, 0.08563365376135462),
         (28, 0.08464912280701754),
         (32, 0.08452380952380953),
         (35, 0.08396135265700483),
         (22, 0.08307724252491694),
         (29, 0.08033429984649497),
         (34, 0.07619949494949496),
         (33, 0.07539485138664345),
         (37, 0.07481125600549074),
         (27, 0.07394464841273352),
         (30, 0.07319976771196283),
         (36, 0.07035024154589371),
         (25, 0.0656084656084656),
         (39, 0.06354359925788497)
    ]

    computed = rff(rankings=rankings, k=10)

    assert computed == expected
