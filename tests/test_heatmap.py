import numpy as np
from pypage import Heatmap


test_array = np.array([[ -6.33981683,  -7.80840227,  -7.93377824,  -8.42731731,
         -7.66348485,  -7.74160932,  -1.68829856,  -1.38415529,
         -1.72963202,  -0.59207872,  -0.68019475,   2.27505674,
         2.41160259,   3.31377353,   2.52720484,   2.48713859,
         7.04231169,   7.21878915,  17.58767634],
       [ -5.63641818,  -9.98538414, -10.31019987, -12.04030142,
         -9.39142622,  -7.36706553,  -2.30541553,  -2.64805387,
         -1.42392686,  -0.54161822,  -0.69341391,   4.09540935,
         6.86661898,   3.2248728 ,   3.02722813,   3.63030434,
         2.08606853,   8.1121038 ,  20.97121979],
       [-10.17964738, -20.69401845, -16.84128145, -18.50526407,
        -20.10656082,  -9.76372304,  -4.67972201,  -3.64033145,
        -1.67151649,  -0.96963513,  -0.65154149,   4.28817315,
        10.95390065,   7.2133559 ,   5.40674828,   8.67225123,
        15.52098503,   8.27407111,  33.81813937],
       [-13.70471918, -23.71454032, -15.67615875, -21.67654803,
        -14.62871613, -10.55561644,  -3.18729958,  -3.08866304,
        -2.83031612,  -0.88533314,   0.40345618,   9.18755193,
        6.13983437,   6.9237843 ,   3.05682181,   8.29455328,
        9.96692372,  10.60970068,  51.00720584],
       [-19.26784788, -17.83982056, -16.00571655, -14.71487057,
        -13.46524463, -11.09474626,  -3.14659287,  -3.17506245,
        -1.08410197,   0.66211243,   0.94974771,   7.58319127,
        4.71869968,   7.2635771 ,   5.6092068 ,   9.69610117,
        11.17765899,  10.55066751,  38.43483079],
       [ -3.09957062,  -3.66848921,  -5.2573369 ,  -7.30220409,
         -4.71655284,  -3.3595472 ,  -3.39619333,  -2.72741753,
         -1.57284173,   0.29972683,  -1.64090743,   1.26064697,
         2.14519972,   3.18787525,   1.9122155 ,   3.08681862,
         2.9426259 ,   4.70650784,  11.78263281],
       [ -4.49376384,  -7.62716604,  -6.75451417,  -7.43296016,
         -7.30539032,  -4.51532236,  -4.06616526,  -1.74601015,
         -2.835536  ,   0.36383602,  -0.37504253,   1.42092019,
         3.36736795,   8.33203482,   4.7906404 ,   3.63298397,
         4.80177107,   3.73460274,  10.16393639],
       [ -9.17743791, -13.20756465, -14.23379399, -11.22740531,
         -13.68843186,  -6.60409238,  -4.93970236,  -4.58311175,
         -1.65486502,  -2.10027482,  -0.90576615,   7.25292564,
         5.45512748,   4.75200095,   2.2434872 ,   5.93665196,
         10.09375633,   7.97603592,  36.83997934],
       [-10.9953517 , -11.59579995, -12.43757738, -11.69278849,
        -10.58551295,  -2.09744417,  -2.40473896,  -2.53220843,
        1.26820534,   0.69839173,   1.44061551,   3.15349619,
        3.24995989,   2.12985942,   1.71296624,   2.13109738,
        1.78931889,   3.76915856,  28.16436313],
       [ -8.26214896,  -9.76156248,  -8.07130659,  -6.58219039,
         -9.16098579,  -4.78357003,  -4.05122047,  -1.65810947,
         -0.45124696,  -0.45728865,   0.97470372,   4.40532617,
         7.38096458,   3.10710335,   3.88677819,   7.03655838,
         4.340235  ,   5.41972779,  16.14712711]])

test_pathways = np.array(['MAD3', 'ARID2', 'E2F8', 'NFYA', 'SUH', 'ZN250', 'GRHL1', 'SP2',
                          'NSD2', 'SOX2'], dtype=object)

test_reg_exp = np.random.random(10) * 2 - 1


def test_heatmap():
    hm = Heatmap(test_pathways, test_array)
    hm.show()


def test_heatmap_with_reg():
    hm = Heatmap(test_pathways, test_array)
    hm.add_gene_expression(test_pathways, test_reg_exp)
    hm.show(isreg=True)

