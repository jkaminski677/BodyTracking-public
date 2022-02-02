import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class createDatas():

    def alldatas_figs(self, riko, szer, wys, big_freq, width, height):
        x = []
        y = []
        z = []

        with open(f'Wszystkie-dane-{riko}.csv', 'r') as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            i = 0
            for row in lines:
                if i > 0:
                    # print(row)
                    dat = row[4]
                    dat_sec = row[5]
                    # x.append(dat[7:14])
                    x.append(dat_sec[7:18])
                    z.append(int(row[2]))
                    y.append(int(row[3]))
                    # z = np.arange(int(dat[12:20]), int(row[2]))
                    # y = np.arange(int(dat[12:20]), int(row[3]))

                i += 1

        plt.rcParams["figure.figsize"] = (szer, wys)
        plt.figure(1)
        # plt.plot(x, z, 'b', x, y, 'g')
        # plt.xticks(rotation=50, fontsize=7)
        # plt.plot(x, y, color='r', linestyle='line',
        #          marker='o', label="ruch")

        plt.subplot(211)
        # np.flipud(plt.plot(x, y, color='r', drawstyle='default', label="ruch y"))
        plt.plot(x, y, color='r', drawstyle='default', label="ruch y")
        # plt.plot(x, y, color='r', label="ruch y")
        plt.title(f'Wykres - wszystkie dane {riko}', fontsize=20)
        plt.xticks(np.arange(0, len(x) + 1, big_freq), rotation=40, fontsize=5)
        # plt.yticks(np.arange(0, len(x), 75), fontsize=5)
        plt.gca().invert_yaxis()
        plt.xlabel('Czas')
        plt.ylabel('Ruchy w osi "Y"')
        plt.grid()

        plt.subplot(212)
        plt.plot(x, z, color='b', label="ruch x")
        # plt.plot(x, z, color='b', label="ruch x")
        plt.xticks(np.arange(0, len(x) + 1, big_freq), rotation=40, fontsize=5)
        # plt.yticks(np.arange(0, len(x), 75), fontsize=5)
        plt.xlabel('Czas')
        plt.ylabel('Ruchy w osi "X"')

        plt.grid()
        plt.legend()
        plt.savefig(f"Wykres-wszystkie-dane-{riko}.pdf", dpi=1000)
        # if perm_all == 'tak':
        #     plt.show()
        plt.close()

        #////////////////  na obrazku ////////////////////////

        x = []
        y = []
        z = []

        with open(f'Wszystkie-dane-{riko}.csv', 'r') as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            i = 0
            for row in lines:
                if i > 0:
                    # print(row)
                    dat = row[4]
                    dat_sec = row[5]
                    # x.append(dat[7:14])
                    x.append(dat_sec[7:18])
                    z.append(int(row[2]))
                    y.append(int(row[3]))
                    # z = np.arange(int(dat[12:20]), int(row[2]))
                    # y = np.arange(int(dat[12:20]), int(row[3]))

                i += 1

        datafile1 = 'feamefromvid1.jpg'
        img = plt.imread(datafile1)
        fig, ax = plt.subplots()
        plt.title(f'Wykres z tłem {riko}', fontsize=20)
        plt.imshow(img, extent=[0, width, 0, height])
        ax.plot(z, y, 'b')
        ax.invert_yaxis()
        plt.xlabel('Ruchy w osi "X"')
        plt.ylabel('Ruchy w osi "Y"')
        plt.savefig(f"Wykres-z-tłem-{riko}.pdf", dpi=1000)
        plt.close()



    def cutdatas_figs(self, lenn, riko, begi, ende, rasted, szer, wys, width, height):
        dr = []
        u = 0
        while u < lenn:
            with open(f'Wszystkie-dane-{riko}.csv', 'r') as csvfile:
                lines = csv.reader(csvfile, delimiter=',')
                i = 0
                dd = []
                for row in lines:
                    tim = row[5]
                    mtime = tim[7:15]
                    if mtime >= begi[u] and mtime <= ende[u]:
                        sel_row = row[1:6]
                        # print(sel_row)
                        # input()
                        dr.append(sel_row)
                        dd.append(sel_row)
                        # input(dr)
                b_cut_name = int(begi[u][6:8])
                e_cut_name = int(ende[u][6:8])
                csvfile.close()
                d_sel_cut = pd.DataFrame(dd, columns=['body part', 'x', 'y', 'actual time', 'timer'])
                d_sel_cut.to_csv(f'Dane-fragment-{riko}-{b_cut_name}-{e_cut_name}.csv')

                x = []
                y = []
                z = []

                with open(f'Dane-fragment-{riko}-{b_cut_name}-{e_cut_name}.csv', 'r') as csv_file:
                    lines = csv.reader(csv_file, delimiter=',')
                    i = 0
                    for row in lines:
                        if i > 1:
                            dat = row[4]
                            dat_sec = row[5]
                            x.append(dat_sec[7:18])
                            # x.append(dat_sec[0:5])
                            z.append(int(row[2]))
                            y.append(int(row[3]))

                        i += 1
                csvfile.close()

                plt.rcParams["figure.figsize"] = (szer, wys)
                plt.figure(1)

                plt.subplot(211)
                plt.plot(x, y, color='r', drawstyle='default', label="ruch y")
                plt.title(f'Wykres-fragment-{riko}-{b_cut_name}-{e_cut_name}', fontsize=20)
                plt.gca().invert_yaxis()
                plt.xticks(np.arange(0, len(x) + 1, rasted[u]), rotation=40, fontsize=5)
                plt.xlabel('Czas')
                plt.ylabel('Ruchy w osi "Y"')
                plt.grid()

                plt.subplot(212)
                plt.plot(x, z, color='b', label="ruch x")
                plt.xticks(np.arange(0, len(x) + 1, rasted[u]), rotation=40, fontsize=5)
                plt.xlabel('Czas')
                plt.ylabel('Ruchy w osi "X"')

                plt.grid()
                plt.legend()
                plt.savefig(f"Wykres-fragment-{riko}-{b_cut_name}-{e_cut_name}.pdf", dpi=1000)
                # if perm_all == 'tak':
                #     plt.show()
                plt.close()

                datafile1 = 'feamefromvid1.jpg'
                img = plt.imread(datafile1)
                fig, ax = plt.subplots()
                plt.title(f'Wykres ruchu części ciała numer {riko}', fontsize=20)
                plt.imshow(img, extent=[0, width, 0, height])
                ax.plot(z, y, 'b')
                ax.invert_yaxis()
                plt.xlabel('Ruchy w osi "X"')
                plt.ylabel('Ruchy w osi "Y"')
                plt.savefig(f"Wykres-fragment-z-tłem-{riko}-{b_cut_name}-{e_cut_name}.pdf", dpi=1000)
                plt.close()
            u += 1

        return dr
