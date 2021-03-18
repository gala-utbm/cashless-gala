#!/usr/bin/python
from GUI import *

# TODO: ENSURE BALANCE CAN'T HAVE ABSURDS VALUES (eg: 16.33333...)       [OK Money class + string]
# TODO: FIX MULTI-USER PANEL
# TODO: UNIFY KEY NAME BITWEEN THE SERVER AND THE CLIENT                 [OK GRPC]
# TODO: MAKE AUTOMATIC GRAPH
# TODO: FIND A EASIER WAY TO HANDLE TREEMODELS AND STUFF...              [OK QATOMS]
# TODO: ADD WARNING WHEN ADD HUGE AMOUNT ON CARDS
# TODO: HANDLE TRANSLATION
# TODO: ADD A TOOLBAR STATUS SINGLETON HANDLER                          [OK VIA QCONNECTOR]
# TODO: HANDLE CARD READER PLUG/UNPLUG                                  [OK]
# TODO: ADD TRADUCTION

if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    # translation
    locale = QLocale.system().name()
    qtTranslator = QTranslator()
    print(QLibraryInfo.location(QLibraryInfo.TranslationsPath))
    frenchLocale = QLocale(QLocale.French, QLocale.France)
    if qtTranslator.load(locale, "qt_" + locale):
        print("qtTranslator installed")
        app.installTranslator(qtTranslator)

    MainWindow = QMainMenu()
    VirtualCard = QVirtualCard()

    # la fenêtre est rendue visible
    #    MainWindow.showMaximized()
    MainWindow.show()
    # VirtualCard.show()
    app.exec_()
