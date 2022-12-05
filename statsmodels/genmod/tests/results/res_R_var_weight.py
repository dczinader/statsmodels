# This file auto-generated by test_get_R_tweedie_var_weight.R
# Using: R version 3.5.1 (2018-07-02)
import numpy as np
import pandas as pd
import os

from statsmodels.tools.tools import Bunch

path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)


res = dict()
res['params'] = np.array([
    0.74699331283637337986, -0.031592165334818379796, -0.021959412079720488226
])
res['bse'] = np.array([
    0.25438368514036091561, 0.011629899831763365614, 0.011034604276375996681
])
res['deviance'] = 45399.238887
res['ll'] = -8669.17968  # regression number, not from R
res['resids_colnames'] = [
    'resid_response', 'resid_pearson', 'resid_deviance', 'resid_working']
csv_path = os.path.join(dir_path, 'results_tweedie_aweights_nonrobust.csv')
resids = np.array(pd.read_csv(csv_path))
res['resids'] = resids
results_tweedie_aweights_nonrobust = Bunch(**res)

res = dict()
res['params'] = np.array([
    4.3171222692811204169, -0.038835175525200764379, 0.54097404989168318412,
    1.0560051456310013407])
res['bse'] = np.array([
    0.80693035378427380166, 0.013827354415809251648, 0.18432033392178892584,
    0.186384917449112536])
res['deviance'] = 28.440959
res['ll'] = -301.601118
res['resids_colnames'] = [
    'resid_response', 'resid_pearson', 'resid_deviance', 'resid_working']
res['resids'] = np.array([
    -6.0158828841102272023, -5.0064618225897614678, -5.5825299715106844189,
    -6.9511999508118442748, -4.5194555811187591132, -1.557595268795654242,
    -1.4915816790031248829, -2.8827914717229985442, -0.51945558111875911322,
    0.11720852827700145582, -1.9511999508118442748, -3.1808072343012465666,
    0.24507818532437042336, 2.1431814907569695094, 0.81919276569875343341,
    5.2513574111143244139, 4.6547413066088410005, 5.8191927656987534334,
    13.805056937442099496, 13.048800049188155725, -3.5461655328997796488,
    -4.3171742547402551793, -6.5401065768334341044, -5.6336912448773173168,
    -9.2050394978136971247, -1.0510357685093119073, 1.4079973153855167567,
    -3.4735049910420947583, 6.4538344671002203512, 0.52649500895790524169,
    4.7868274865566906584, 8.4598934231665658956, 2.2438400124908675082,
    14.907031299164781757, -19.462143004837859195, -16.470421414020314899,
    -3.9684071475551156993, -13.14329303600413823, 1.3380516354871438978,
    -5.9189306482160155554, -0.46214300483785919482, 4.4406584647078979344,
    -5.4161390946438174865, 7.5077293157326110418, 12.031592852444884301,
    14.598574701805357989, 1.5838609053561825135, 10.391659888606849194,
    -1.4851751347306552109, -0.83351263530235220056, -0.73623579365799252106,
    -0.69852881915459330564, -0.5304864305103017541, -0.62668991425384801275,
    -0.22977168781956672228, -0.36570693035127138648, -0.060972861020603522086,
    0.014868911437965813202, -0.4384411678265578427, -0.2844881561451974572,
    0.022787537608125515293, 0.41912332605193491908, 0.07326776578220378644,
    1.7399635542616316286, 0.44993957566111131285, 0.52046266819145536875,
    1.6845824104033622071, 1.3112790531481182121, -0.83064421664412402269,
    -0.41844541423313824646, -0.48301736324758975938, -0.38498087397118291308,
    -0.4793033359218865086, -0.19501953776552996556, 0.21037977246201788883,
    -0.18802631080168147326, 0.67606563544889408668, 0.028500006317870137801,
    0.70357919408636093728, 0.62480257265043215309, 0.10810477534578602499,
    0.87211481867607798524, -0.76435604815902624676, -1.3913258623193209829,
    -0.18925649047299358818, -0.40889690490896990482, 0.059043980418843691749,
    -0.33157319461752626788, -0.040585082486855973694, 0.1884882248536425553,
    -0.16208153429406677026, 0.30653463749913562042, 0.57379622437595356743,
    1.6825261498124608472, 0.047398082132416530232, 0.36323882644517407892,
    -2.5581754807831980081, -1.3851521395433199491, -1.0922123777693948377,
    -1.0005518818611833787, -0.67167201555474287389, -0.69718647545513146024,
    -0.25018637428846979276, -0.42317194149448128515, -0.062258126689424299338,
    0.014795849256191397764, -0.47090072427136225874, -0.31707718530745676588,
    0.022616711999637318514, 0.38940961248878158685, 0.071551164078391196743,
    1.4232712112275127669, 0.39602447412952324068, 0.45043976885155773138,
    1.1807262353227552243, 0.97311662116074171269, -0.96387085778973813355,
    -0.4972022256055589895, -0.59452271009315738048, -0.449713327474644875,
    -0.58870075509045161066, -0.20099628504835270748, 0.20241883427909049264,
    -0.20130092403600013951, 0.56500703038717148274, 0.028233670119025004036,
    0.64093348203300071209, 0.52804594118935443969, 0.10443781791098502576,
    0.70006586509944224161, -1.1671137422196677935, -1.8740944537491481814,
    -0.20271679195797467909, -0.48346236689503357953, 0.057920368116502723987,
    -0.35546257706309924984, -0.040833257924115747006, 0.1777983388792870878,
    -0.17177278732799597383, 0.27984395723434191128, 0.4905212458386473684,
    1.3835988461755979184, 0.046669269235505038418, 0.32672761718963955202,
    -0.85746626383048263342, -0.83351263530235220056, -0.73623579365799252106,
    -0.69852881915459330564, -0.5304864305103017541, -0.28026424981702369177,
    -0.22977168781956672228, -0.36570693035127138648, -0.060972861020603522086,
    0.014868911437965813202, -0.19607685107891539844, -0.2844881561451974572,
    0.022787537608125515293, 0.2419809651197359357, 0.07326776578220378644,
    0.77813535714023041034, 0.44993957566111131285, 0.52046266819145536875,
    1.6845824104033622071, 1.3112790531481182121, -0.37147538670666468974,
    -0.41844541423313824646, -0.48301736324758975938, -0.38498087397118291308,
    -0.4793033359218865086, -0.087215388676862487527, 0.12146281826299824835,
    -0.18802631080168147326, 0.67606563544889408668, 0.028500006317870137801,
    0.31465018110632420045, 0.62480257265043215309, 0.10810477534578602499,
    0.87211481867607798524, -0.76435604815902624676, -0.62221984139990293983,
    -0.18925649047299358818, -0.40889690490896990482, 0.059043980418843691749,
    -0.19143387316849300173, -0.018150200662609233121, 0.1884882248536425553,
    -0.16208153429406677026, 0.30653463749913562042, 0.57379622437595356743,
    0.75244856898033141146, 0.047398082132416530232, 0.36323882644517407892
]).reshape((48, 4), order="F")
results_gamma_aweights_nonrobust = Bunch(**res)

res = dict()
res['params'] = np.array([
    0.019083886775238277644, 0.93993818789790006818
])
res['bse'] = np.array([
    0.021677622811348211396, 0.82525357389082676374
])
res['deviance'] = 1248.273065
res['ll'] = -52.674985
res['resids_colnames'] = [
    'resid_response', 'resid_pearson', 'resid_deviance', 'resid_working']
res['resids'] = np.array([
    32.059654149533187706, 3.3448403477511448045, 4.0197139294873869275,
    -0.28159357985674304814, -1.6667828494180003673, 0.13880513444962283565,
    -0.18150652396610489347, -2.9789626432480238449, -1.2529678442364695634,
    -3.7054159544565843376, -1.0424256120017099114, -0.88813363987303950431,
    -3.7241309801112230105, -1.3985915365753158746, -0.9406665144733470374,
    -0.76290530967944270024, -1.0174777728628758844, 32.059654149533187706,
    4.7303185837624086574, 6.9623487577644933566, -0.56318715971348609628,
    -3.7270397550294447342, 0.27761026889924567129, -0.31437852141451172461,
    -4.2128893718841595728, -1.2529678442364695634, -5.2402494970261486174,
    -1.8055341230980426204, -1.7762672797460790086, -8.3274100286416121719,
    -2.7971830731506317491, -1.6292821960465615483, -1.0789110357551139341,
    -1.0174777728628758844, 32.059654149533187706, 4.7303185837624086574,
    6.9623487577644942448, -0.56318715971348609628, -3.7270397550294447342,
    0.27761026889924567129, -0.31437852141451178012, -4.2128893718841595728,
    -1.2529678442364695634, -5.2402494970261477292, -1.8055341230980428424,
    -1.7762672797460790086, -8.3274100286416121719, -2.7971830731506317491,
    -1.6292821960465617703, -1.0789110357551139341, -1.0174777728628758844,
    6.4893542112044375614, 0.59146700596171875031, 2.0298652751957457774,
    -0.065768404825141027481, -0.35715886151117287595, 0.07457850707565569226,
    -0.083202375043149326417, -0.5983099004142555799, -0.55614102413481192322,
    -0.78747893710589345062, -0.5103860849943342437, -0.47037647183319014621,
    -0.78832085642628468847, -0.58308866484712540412, -0.48471311658027066427,
    -0.43275455890377079182, -0.50433158994313831425
]).reshape((17, 4), order="F")
results_gaussian_aweights_nonrobust = Bunch(**res)
