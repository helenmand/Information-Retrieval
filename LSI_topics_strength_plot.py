import matplotlib.pyplot as plt

vals = [82.19786454591414,
38.901631402972626,
30.047122802991673,
27.867943713230265,
27.24125052656836,
25.562012906983387,
24.477869910491798,
23.242171597641725,
22.467740626593834,
20.690043557806554,
20.101118231220703,
19.544783527385313,
19.14427010496348,
18.921238652611894,
18.41455271489775,
18.181197474201024,
18.13320007437854,
17.92164519143437,
17.699876343226737,
17.215907596760907,
16.867633237182396,
16.556412409686576,
16.489414733006065,
16.21487975053442,
15.711402017987707,
15.626201859494333,
15.538729179952202,
15.376028027170586,
15.14167195621263,
15.035214802324564,
14.873398033493824,
14.836283153944052,
14.61701925060958,
14.486537373364964,
14.393516525449096,
14.170019678886725,
13.970007910983577,
13.908291226588775,
13.809546644845932,
13.752249635620846,
13.657594460833629,
13.54319084485332,
13.459160525981043,
13.40742717132386,
13.363239403661629,
13.269498696969428,
13.139846808747217,
13.097664662789384,
13.07012153555888,
12.966994607446996,
12.9523555796327,
12.894964743451172,
12.807340217833886,
12.768245583837826,
12.72892788334801,
12.64180076241534,
12.556575297102679,
12.503997693114911,
12.464473710170356,
12.443016189032612,
12.39195163266971,
12.316766873200901,
12.231375089257886,
12.224258079149944,
12.161361780020796,
12.081744909825604,
12.07444157493249,
12.051003180371042,
11.963715601180784,
11.956939680605316,
11.93595750814519,
11.865813298435286,
11.795579713404628,
11.77786068561145,
11.703476174888285,
11.662032499388719,
11.620185766236398,
11.57181225820066,
11.525425676636328,
11.507609707434746,
11.47400304399278,
11.437001771096106,
11.386967201697992,
11.359060275982271,
11.342455928864998,
11.322562273776496,
11.3033433359963,
11.24556715464279,
11.235974700401485,
11.211670355301392,
11.18552461309846,
11.137281670719805,
11.126140336418578,
11.106555001701071,
11.077376776801541,
11.043561196787273,
11.012673234863263,
10.992359389874297,
10.951150056163932,
10.92489680886742 ]

X = [i for i in range(0,100)]

plt.plot(X, vals, 'ro', markersize=0.9)
plt.xlabel('number of topics')
plt.ylabel('topic strenght')
plt.show()