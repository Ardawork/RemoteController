import main

kumanda = main.RemoteController("Vestel" , "T-230" , "Gri")

kumanda.showInfo()
kumanda.changeProp("Bosh" , "GR-3341" , "Siyah")
kumanda.showInfo()


