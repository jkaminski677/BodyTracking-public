import cv2
import time
import datetime
import re
import pose_module as pm
import pandas as pd
from tkinter import filedialog
import os
import create_datas as crd
from PIL import Image, ImageOps


#The code was written by someone who had no contact with python before the project started. Good luck!

print('Witaj!')
print('Jeśli chcesz analizować film z kamery (na żywo) to napisz "tak" i potwierdź przyciskiem Enter.\n'
      'Jeśli nie, to napisz "nie", wtedy będziesz mógł wybrać film z pamięci koputera :D')
potw = input()
consi = ""
while potw != "tak" and potw != "nie":
    print("Napisz jeszcze raz (tak/nie) ;)")
    potw = input()

if potw == "tak":
    print('Wybierz źródło nagrania, czyli albo wbudowaną kamerkę internetową ("k"), albo podłączony zewnęrzny sprzęt ("i").')
    devic = input()
    while devic != "k" and devic != "i":
        print("Ktoś tu nie chodził do szkoły? ;) Napisz jeszcze raz (k/i).")
        devic = input()

    if devic == "k":
        cap = cv2.VideoCapture(0)
    elif devic == "i":
        cap = cv2.VideoCapture(1)

    if (cap.isOpened() == False):
      print("!!!!!!!!!!!!!!Nie można otworzyć kamery.!!!!!!!!!!!!!!!!")

    print('Jeśli chcesz, aby film był nagrywany napisz "chce", jeśli nie to napisz "nie":')
    consi = input()
    while consi != "chce" and consi != "nie":
        print("Nie potrafisz pisać! Napisz jeszcze raz czego chcesz(chce/nie) ;)")
        consi = input()

one_more = "chce"

while one_more == "chce":

    if potw == "nie":
        print('Wybierz film z pamięci komputera :)')
        file_path_up = filedialog.askopenfilename()
        cap = cv2.VideoCapture('{}'.format(file_path_up))

    #########################################################################################
    # cap = cv2.VideoCapture('PoseVideos/videoplayback.mp4')
    # cap = cv2.VideoCapture('PoseVideos/autoprez360.mp4')
    # cap = cv2.VideoCapture('PoseVideos/autoprez720.mp4')
    # cap = cv2.VideoCapture('PoseVideos/rozgrzewka.mp4')
    # cap = cv2.VideoCapture(0)
    # consi = "chce"
    #########################################################################################

    chosetimephoto = 0

    print('Wybierz folder, w którym zostanie zapisany film oraz zebrane dane')
    print('\n')

    time.sleep(1)
    os.chdir(filedialog.askdirectory())
    print(os.getcwd())
    print('Folder został wybrany! Jego adres w komputerze widzisz tutaj nade mną :D')
    print('\n')
    print('Na koniec wybierz moment, w którym ma zostać zapisana klatka filmu do wykresów z tłem.')
    print('Prędkość to około 26 klatek na sekunde ( w trakcie filmu wyświetla się na niebiesko)')
    chosetimephoto = input('Podaj numer klatki (np. 50 czyli około 2 sekunda, 100 czyli 4 sekunda, 500 czyli 20 sekunda): ')
    print('\n')
    print('Jeśli będziesz chciał zakończyć nagrywanie i analizowanie filmu naciśnij klawisz "q".')
    print('To zaczynamy!')
    time.sleep(2)


    pTime = 0
    # zer_arr = []
    el_arr = []
    twe_arr = []
    # thi_arr = []
    # fou_arr = []
    ni_arr = []
    tw_arr = []
    tw3_arr = []
    tw4_arr = []
    # tw5_arr = []
    # tw6_arr = []
    # tw7_arr = []
    # tw8_arr = []
    barki_list = []
    centr_11_12 = []
    centr_23_24 = []
    centr_body = []

    all_arr = []
    img_array = []
    pose_array = []
    time_array = []
    detector = pm.poseDetector()
    datass = crd.createDatas()

    # szer: str = input('Podaj szerokość wykresu (oś x): ')
    # wys = input('Podaj wysokość wykresu (oś y): ')
    # perm_all = input('Chcesz widzieć wszystkie wykresy? "tak" lub "nie" ')

    szer = 10
    wys = 7
    perm_all = 'tak'

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # width = int(cap.get(3))
    # height = int(cap.get(4))
    fpsy = 23
    video_cod = cv2.VideoWriter_fourcc(*'mp4v')
    if consi == "chce":
        writer = cv2.VideoWriter('MyVideo_Recorded.mp4', video_cod, fpsy, (width, height))
    # cv2.VideoWriter_fourcc(*'DIVX')

    obrazek = 0
    zdj = 0

    cap.read()
    start = datetime.datetime.now()
    while True:
        success, img = cap.read()
        if success == True:
            if consi == 'chce':
                writer.write(img)
        else:
            break
        if obrazek == int(chosetimephoto):
            cv2.imwrite("feamefromvid.jpg", img)
        else:
            obrazek += 1
        # obrazek += 1
        img = detector.findPose(img)
        lmList = detector.findPosition(img, draw=False)
        elap = datetime.datetime.now() - start

        if len(lmList) != 0:
            # # 0 środek głowy
            # zer_arr.append(lmList[0])
            # cv2.circle(img, (lmList[0][1], lmList[0][2]), 10, (0, 0, 255), cv2.FILLED)
            # 11 lewe ramię
            el_arr.append(lmList[11])
            # cv2.circle(img, (lmList[11][1], lmList[11][2]), 10, (0, 0, 255), cv2.FILLED)
            # 12 prawe ramię
            twe_arr.append(lmList[12])
            # cv2.circle(img, (lmList[12][1], lmList[12][2]), 10, (0, 0, 255), cv2.FILLED)

            barki_x = int((abs(lmList[11][1] + lmList[12][1]))/2)
            barki_y = int((abs(lmList[11][2] + lmList[12][2]))/2)
            # barki_list.append(lmList[11][0], barki_x, barki_y, lmList[11][3])
            centr_11_12.append([lmList[11][0], barki_x, barki_y, lmList[11][3], elap])
            cv2.circle(img, (barki_x, barki_y), 10, (0, 0, 255), cv2.FILLED)

            # # 13 lewy łokieć
            # thi_arr.append(lmList[13])
            # cv2.circle(img, (lmList[13][1], lmList[13][2]), 10, (0, 0, 255), cv2.FILLED)
            # # 14 prawy łokieć
            # fou_arr.append(lmList[14])
            # cv2.circle(img, (lmList[14][1], lmList[14][2]), 10, (0, 0, 255), cv2.FILLED)
            # 19 lewa dłoń
            ni_arr.append(lmList[19])
            cv2.circle(img, (lmList[19][1], lmList[19][2]), 10, (0, 0, 255), cv2.FILLED)
            # 20 prawa dłoń
            tw_arr.append(lmList[20])
            cv2.circle(img, (lmList[20][1], lmList[20][2]), 10, (0, 0, 255), cv2.FILLED)
            # 23 lewe biodro
            tw3_arr.append(lmList[23])
            # cv2.circle(img, (lmList[23][1], lmList[23][2]), 10, (0, 0, 255), cv2.FILLED)
            # 24 prawe biodro
            tw4_arr.append(lmList[24])
            # cv2.circle(img, (lmList[24][1], lmList[24][2]), 10, (0, 0, 255), cv2.FILLED)

            biodra_x = int((abs(lmList[23][1] + lmList[24][1])) / 2)
            biodra_y = int((abs(lmList[23][2] + lmList[24][2])) / 2)
            # barki_list.append(lmList[11][0], barki_x, barki_y, lmList[11][3])
            centr_23_24.append([lmList[23][0], biodra_x, biodra_y, lmList[23][3], elap])
            cv2.circle(img, (biodra_x, biodra_y), 10, (0, 0, 255), cv2.FILLED)

            korpus_x = int((abs(barki_x + biodra_x)) / 2)
            korpus_y = int((abs(barki_y + biodra_y)) / 2)
            centr_body.append(["body-center", korpus_x, korpus_y, lmList[23][3], elap])
            cv2.circle(img, (korpus_x, korpus_y), 10, (0, 0, 255), cv2.FILLED)
            # # 25 lewe kolano
            # tw5_arr.append(lmList[25])
            # cv2.circle(img, (lmList[25][1], lmList[25][2]), 10, (0, 0, 255), cv2.FILLED)
            # # 26 prawe kolano
            # tw6_arr.append(lmList[26])
            # cv2.circle(img, (lmList[26][1], lmList[26][2]), 10, (0, 0, 255), cv2.FILLED)
            # # 27 lewa kostka
            # tw7_arr.append(lmList[27])
            # cv2.circle(img, (lmList[27][1], lmList[27][2]), 10, (0, 0, 255), cv2.FILLED)
            # # 28 prawa kostka
            # tw8_arr.append(lmList[28])
            # cv2.circle(img, (lmList[28][1], lmList[28][2]), 10, (0, 0, 255), cv2.FILLED)
            lmList[20].append(elap)
            lmList[19].append(elap)
            # lmList[0].append(elap)
            # lmList[11].append(elap)
            # lmList[12].append(elap)
            # lmList[13].append(elap)
            # lmList[14].append(elap)
            # lmList[23].append(elap)
            # lmList[24].append(elap)
            # lmList[25].append(elap)
            # lmList[26].append(elap)
            # lmList[27].append(elap)
            # lmList[28].append(elap)
            # centr_11_12.append(elap)

        cTime = time.time()
        # if potw == "nie":
        fps = 1 / (cTime - pTime)
        # else:
        #     fps = fpsy
        pTime = cTime
        cv2.putText(img, str(elap), (79, 100), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        cv2.putText(img, str(int(fps)), (79, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 0), 3)
        cv2.imshow("Video", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    if consi == "chce":
        writer.release()
    cv2.destroyAllWindows()
    datafile_org = Image.open('feamefromvid.jpg')
    datafile = ImageOps.flip(datafile_org)
    datafile.save('feamefromvid1.jpg', quality=95)

    #####################################################################################################################

    # all_arr.extend([zer_arr, el_arr, twe_arr, thi_arr, fou_arr, ni_arr, tw_arr,
    #                 tw3_arr, tw4_arr, tw5_arr, tw6_arr, tw7_arr, tw8_arr])
    all_arr.extend([ni_arr, tw_arr, centr_11_12, centr_23_24, centr_body])

    begi = []
    begg = 0
    ende = []
    endd = 0
    rasti = 0
    big_rasti = 0
    rasted = []
    print('\n')
    print('Czy chcesz "wykroić" konkretne dane z wykresów oraz z plików csv z całęgo filmu? (tak/nie) ')
    cutter = input()
    while cutter != "tak" and cutter != "nie":
        print("Napisz jeszcze raz czego chcesz (tak/nie) ;)")
        cutter = input()
    if cutter == "tak":
        perform = "tak"
        while perform == "tak":
            print(f'\nNapisz przedział czasu jaki chcesz wyciąć z wykresów. \nCałe nagranie trwa {elap} - Godziny:Minuty:Sekundy.Mikrosekundy '
                  f'\nMusisz napisać odpowiedni format czasu(tak jak poniżej pokazano, czyli z ":" pomiędzy), ponieważ inaczej program się wysypie :D '
                  f'\n Podawaj koniec przedziału większy od początku, bo nie wiem co się stanie, nie testowałem tego.')

            begg = (input('Tutaj podaj POCZĄTEK swojego przedziału \nczasowego(np. 00:01:20, słownie to jedna minuta i dwadzieścia sekund):'))
            beggi = begg[0:8]
            matchedb = re.match("[0-9][0-9]+:+[0-9][0-9]+:+[0-9][0-9]", beggi)
            isb_mat = bool(matchedb)
            while isb_mat == False:
                begg = input('Zły format. Wpisz jeszcze raz czas początkowy:')
                beggi = begg[0:8]
                matchedb = re.match("[0-9][0-9]+:+[0-9][0-9]+:+[0-9][0-9]", beggi)
                isb_mat = bool(matchedb)
            begi.append(beggi)

            endd = (input('Tutaj podaj KONIEC przedziału(np. 00:05:12):'))
            enddi = endd[0:8]
            matchede = re.match("[0-9][0-9]+:+[0-9][0-9]+:+[0-9][0-9]", enddi)
            ise_mat = bool(matchede)
            while ise_mat == False:
                endd = input('Zły format. Wpisz jeszcze raz czas końcowy:')
                enddi = endd[0:8]
                matchede = re.match("[0-9][0-9]+:+[0-9][0-9]+:+[0-9][0-9]", enddi)
                ise_mat = bool(matchede)
                print(ise_mat)
                # if ise_mat:
                #     check_itbe = int(begg[6:8])
                #     print(check_itbe)
                #     input()
                #     check_iten = int(endd[6:8])
                #     print(check_iten)
                #     input()
                #     if check_itbe > check_iten:
                #         print('Jeszcze raz wprowadź drugi czas większy od pierwszego.')
                #         ise_mat = False
            ende.append(enddi)
            rasti = input('Podaj dowolną częstotliwość danych czasowych widocznych na wykresie. Przykłady co do minuty oraz 15 sekund:'
                          '\n80 - 19pom/min'
                          '\n60 - 25pom/min'
                          '\n40 - 37pom/min'
                          '\n35 - 42pom/min'
                          '\n80 - 5pom/15sek'
                          '\n60 - 7pom/15sek'
                          '\n40 - 10pom/15sek'
                          '\n20 - 19pom/15sek '
                          '\nPodaj wartość:')
            rasted.append(int(rasti))
            perform = input('Czy chcesz wprowadzić kolejny przedział?(tak/nie)')
            while perform != "tak" and perform != "nie":
                print("Napisz jeszcze raz czego chcesz (tak/nie) ;)")
                perform = input()

    big_freq = int(input('Na końcu podaj dowolną częstotliwość danych czasowych widocznych na wykresie wszystkich pomiarów z nagrania.\n'
                          'Im większa liczba, tym szybciej wykres się załaduje, ponieważ będzie miał mniej pomiarów.'
                          '\nPrzykłady co do minuty oraz 15 sekund:'
                          '\n80 - 19pom/min'
                          '\n60 - 25pom/min'
                          '\n40 - 37pom/min'
                          '\n35 - 42pom/min'
                          '\n80 - 5pom/15sek'
                          '\n60 - 7pom/15sek'
                          '\n40 - 10pom/15sek'
                          '\n20 - 19pom/15sek '
                          '\nPodaj wartość:'))

    # begi = ["00:00:02", "00:00:06", "00:00:09"]
    # ende = ["00:00:03", "00:00:07", "00:00:10"]
    # begi = ["00:00:22", "00:00:33", "00:00:39"]
    # ende = ["00:00:30", "00:00:35", "00:00:39"]
    # rasted = [10, 5, 2]
    # begi = ["00:00:25", "00:00:50", "00:01:39", "00:03:50"]
    # ende = ["00:00:40", "00:01:20", "00:02:39", "00:04:05"]
    # rasted = [8, 25, 30, 5]
    # big_freq = 70
    second_start = datetime.datetime.now()
    lenn = len(begi)
    print(lenn)
    iterations = len(all_arr)
    iters = 1
    dk = pd.DataFrame()

    for number in all_arr:
        iterations -= 1
        df = pd.DataFrame(number, columns=['body part', 'x', 'y', 'actual time', 'timer'])
        dk = dk.append(df)
        if number == ni_arr:
            riko = "19-lewa-dłoń"
        elif number == tw_arr:
            riko = "20-prawa-dłoń"
        elif number == centr_11_12:
            riko = "-barki-środek"
        elif number == centr_23_24:
            riko = "-biodra-środek"
        elif number == centr_body:
            riko = "-body-center"
            # all_arr.extend([el_arr, twe_arr, ni_arr, tw_arr, tw3_arr, tw4_arr])
        # elif number == el_arr:
        #     riko = "11-lewe-ramie"
        # elif number == twe_arr:
        #     riko = "12-prawe-ramie"
        # elif number == tw3_arr:
        #     riko = "23-lewe-biodro"
        # elif number == tw4_arr:
        #     riko = "24-prawe-biodro"
        # elif number == tw5_arr:
        #     riko = "25-lewe-kolano"
        # elif number == tw6_arr:
        #     riko = "26-prawe-kolano"
        # elif number == tw7_arr:
        #     riko = "27-lewa-kostka"
        # elif number == tw8_arr:
        #     riko = "28-prawa-kostka"
        # if number == zer_arr:
        #     riko = "0-środek-głowy"
        # elif number == fou_arr:
        #     riko = "14-prawy-łokieć"
        # elif number == thi_arr:
        #     riko = "13-lewy-łokieć"

        dk.to_json('Wszystkie-zapisane-dane.json', orient='values')
        dk.to_csv('Wszystkie-zapisane-dane.csv')
        df.to_csv(f'Wszystkie-dane-{riko}.csv')

        print(f'{iters}. Teraz wykonuję pliki ze wszystkimi danymi {riko}...')
        print(f'Zostało {iterations} plików do zrobienia...')

        datass.alldatas_figs(riko, szer, wys, big_freq, width, height)

        print(f'{iters}. Teraz wykonuję pliki wycięte {riko}...')
        print(f'Zostało {iterations} plików do zrobienia...')

        dr = datass.cutdatas_figs(lenn, riko, begi, ende, rasted, szer, wys, width, height)
        dcut = pd.DataFrame(dr, columns=['body part', 'y', 'x', 'actual time', 'timer'])
        dcut.to_csv(f'Dane-wszystkich-fragmentów-{riko}.csv')

        iters += 1
        cv2.destroyAllWindows()

    second_elaps = datetime.datetime.now() - second_start
    cv2.destroyAllWindows()
    print('\n')
    print('\n')
    print("Program zakończył działanie.")
    print(f'Jego męczarnie trwały {second_elaps}!')
    one_more = input('Wpisz "nie" oraz naciśnij "Enter" aby zakończyć działanie programu. \n'
          ' Jeśli chcesz analizować kolejne pliki napisz "chce" :D')
    while one_more != "chce" and one_more != "nie":
        print("Napisz jeszcze raz czego chcesz (chce/nie) ;)")
        one_more = input()
print('Zamykanie programu...')
time.sleep(2)
