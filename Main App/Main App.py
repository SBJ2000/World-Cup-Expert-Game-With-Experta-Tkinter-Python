from experta import *
from tkinter import *

window= Tk()
# Create Canvas
canvas1 = Canvas( window, width = 400,
                 height = 400)
  
canvas1.pack(fill = "both", expand = True)
# Add image file
imgang = PhotoImage(file = "Angleterre.png")
# Add image file
imgesp = PhotoImage(file = "Espagne.png")
# Add image file
imgfr = PhotoImage(file = "France.png")
# Add image file
imgall = PhotoImage(file = "Allemagne.png")
# Add image file
imgpbas = PhotoImage(file = "paysbas.png")
# Add image file
imgcroitie = PhotoImage(file = "Croitie.png")
# Add image file
imgpaysgales = PhotoImage(file = "paysgales.png")
# Add image file
imgport = PhotoImage(file = "portugale.png")
# Add image file
imgpoland = PhotoImage(file = "poland.png")
# Add image file
imgdanemark = PhotoImage(file = "danemark.png")
# Add image file
imgsuisse = PhotoImage(file = "suisse.png")
# Add image file
imgserbie = PhotoImage(file = "serbie.png")
# Add image file
imgbelgique = PhotoImage(file = "belgique.png")
# Add image file
imgmaroc = PhotoImage(file = "maroc.png")
# Add image file
imgtunisie = PhotoImage(file = "tunisie.png")
# Add image file
imgcam = PhotoImage(file = "cameroun.png")
# Add image file
imgsen = PhotoImage(file = "senegale.png")
# Add image file
imgghana = PhotoImage(file = "ghana.png")
# Add image file
imgqatar = PhotoImage(file = "qatar.png")
# Add image file
imgjapon = PhotoImage(file = "japon.png")
# Add image file
imgcorree = PhotoImage(file = "corree.png")
# Add image file
imgarabie = PhotoImage(file = "arabie.png")
# Add image file
imgaust = PhotoImage(file = "australie.png")
# Add image file
imgiran = PhotoImage(file = "iran.png")
# Add image file
imgusa = PhotoImage(file = "usa.png")
# Add image file
imgmexique = PhotoImage(file = "mexique.png")
# Add image file
imgcanada = PhotoImage(file = "canada.png")
# Add image file
imgcosta = PhotoImage(file = "costa.png")
# Add image file
imgbresil = PhotoImage(file = "bresil.png")
# Add image file
imgarg = PhotoImage(file = "argentine.png")
# Add image file
imgurug = PhotoImage(file = "uruguay.png")
# Add image file
imgequateur = PhotoImage(file = "equateur.png")
# Add image file
imgno = PhotoImage(file = "noimage.png")
# Add image file
imgallphotos = PhotoImage(file = "All.png")
class Pays(Fact):
    """Information sur le pays"""
    pass

class DetectionPays(KnowledgeEngine):
    
    @Rule(Pays(Europe=True),Pays(RemporteCM=True),Pays(MeilleurChampionnatEurope=True))
    def Angleterre(self):
        # Display image
        canvas1.create_image( 50, 300, image = imgang, anchor = "nw")
        canvas1.create_text( 250, 270 ,fill="Black",font="Arial 15 ", text = "Angleterre")
    @Rule(Pays(Europe=True),Pays(RemporteCM=True),Pays(RemporteCMenAfrique=True))
    def Espagne(self):
        # Display image
        canvas1.create_image( 50, 300, image = imgesp, anchor = "nw")
        canvas1.create_text( 210, 270 ,fill="Black",font="Arial 15 ", text = "Espagne")
    @Rule(Pays(Europe=True),Pays(RemporteCM=True),Pays(RemporteCM2fois=True))
    def France(self):
        # Display image
        canvas1.create_image( 50, 300, image = imgfr, anchor = "nw")
        canvas1.create_text( 210, 270 ,fill="Black",font="Arial 15 ", text = "France")
    @Rule(Pays(Europe=True),Pays(RemporteCM=True),Pays(MeilleurChampionnatEurope=False))
    def Allemagne(self):
        # Display image
        canvas1.create_image( 50, 300, image = imgall, anchor = "nw")
        canvas1.create_text( 210, 270 ,fill="Black",font="Arial 15 ", text = "Allemagne")
    @Rule(Pays(Europe=True),Pays(FinalisteCM=True),Pays(Roisanscouronne=True))
    def Paysbas(self):
        # Display image
        canvas1.create_image( 50, 300, image = imgpbas, anchor = "nw")
        canvas1.create_text( 210, 270 ,fill="Black",font="Arial 15 ", text = "Pays-Bas")
    @Rule(Pays(Europe=True),Pays(FinalisteCM=True),Pays(Roisanscouronne=False))
    def Croitie(self):
        # Display image
        canvas1.create_image( 50, 300, image = imgcroitie, anchor = "nw")
        canvas1.create_text( 210, 270 ,fill="Black",font="Arial 15 ", text = "Croitia")
    @Rule(Pays(Europe=True),Pays(appartientUK=True))
    def paysgales(self):
        # Display image
        canvas1.create_image( 50, 300, image = imgpaysgales, anchor = "nw")
        canvas1.create_text( 210, 270 ,fill="Black",font="Arial 15 ", text = "Pays de gales")
    @Rule(Pays(Europe=True),Pays(commenceparP=True),Pays(joueurcelebre=True))
    def portugal(self):
        # Display image
        canvas1.create_image( 50, 300, image = imgport, anchor = "nw")
        canvas1.create_text( 210, 270 ,fill="Black",font="Arial 15 ", text = "Portugale")
    @Rule(Pays(Europe=True),Pays(commenceparP=True),Pays(joueurcelebre=False))
    def pologne(self):
        # Display image
        canvas1.create_image( 50, 300, image = imgpoland, anchor = "nw")
        canvas1.create_text( 210, 270 ,fill="Black",font="Arial 15 ", text = "Pologne")
    @Rule(Pays(Europe=True),Pays(viking=True))
    def Danemark(self):
        # Display image
        canvas1.create_image( 50, 300, image = imgdanemark, anchor = "nw")
        canvas1.create_text( 210, 270 ,fill="Black",font="Arial 15 ", text = "Danemark")
    @Rule(Pays(Europe=True),Pays(commencepars=True),Pays(paysriche=True))
    def Suisse(self):
        # Display image
        canvas1.create_image( 50, 300, image = imgsuisse, anchor = "nw")
        canvas1.create_text( 210, 270 ,fill="Black",font="Arial 15 ", text = "Suisse")
    @Rule(Pays(Europe=True),Pays(commencepars=True),Pays(paysriche=False))
    def Serbie(self):
        # Display image
        canvas1.create_image( 50, 300, image = imgserbie, anchor = "nw")
        canvas1.create_text( 210, 270 ,fill="Black",font="Arial 15 ", text = "Serbia")
    @Rule(Pays(Europe=True,RemporteCM=False,MeilleurChampionnatEurope=False))
    def Belgique(self):
        # Display image
        canvas1.create_image( 50, 300, image = imgbelgique, anchor = "nw")
        canvas1.create_text( 210, 270 ,fill="Black",font="Arial 15 ", text = "Belgique")
    @Rule(Pays(Afrique=True),Pays(Arabe=True),Pays(Tour1=True))
    def Maroc(self):
        # Display image
        canvas1.create_image( 50, 300, image = imgmaroc, anchor = "nw")
        canvas1.create_text( 210, 270 ,fill="Black",font="Arial 15 ", text = "Maroc")
    @Rule(Pays(Afrique=True),Pays(Arabe=True),Pays(Tour1=False))
    def Tunisie(self):
        # Display image
        canvas1.create_image( 50, 300, image = imgtunisie, anchor = "nw")
        canvas1.create_text( 210, 270 ,fill="Black",font="Arial 15 ", text = "Tunisie")
    @Rule(Pays(Afrique=True),Pays(Lions=True),Pays(BattreBresil=True))
    def Cameroun(self):
        # Display image
        canvas1.create_image( 50, 300, image = imgcam, anchor = "nw")
        canvas1.create_text( 210, 270 ,fill="Black",font="Arial 15 ", text = "Cameroun")
    @Rule(Pays(Afrique=True),Pays(Lions=True),Pays(BattreBresil=False))
    def Senegale(self):
        # Display image
        canvas1.create_image( 50, 300, image = imgsen, anchor = "nw")
        canvas1.create_text( 210, 270 ,fill="Black",font="Arial 15 ", text = "Sengale")
    @Rule(Pays(Afrique=True,Lions=False))
    def Ghana(self):
        # Display image
        canvas1.create_image( 50, 300, image = imgghana, anchor = "nw")
        canvas1.create_text( 210, 270 ,fill="Black",font="Arial 15 ", text = "Ghana")
    @Rule(Pays(Asie=True),Pays(organiseCM=True),Pays(Arabe=True))
    def Qatar(self):
        # Display image
        canvas1.create_image( 50, 300, image = imgqatar, anchor = "nw")
        canvas1.create_text( 210, 270 ,fill="Black",font="Arial 15 ", text = "Qatar")
    @Rule(Pays(Asie=True),Pays(organiseCM=True),Pays(battue2europe=True))
    def Japon(self):
        # Display image
        canvas1.create_image( 50, 300, image = imgjapon, anchor = "nw")
        canvas1.create_text( 210, 270 ,fill="Black",font="Arial 15 ", text = "Japon")
    @Rule(Pays(Asie=True),Pays(organiseCM=True),Pays(Arabe=False))
    def Coree(self):
        # Display image
        canvas1.create_image( 50, 300, image = imgcorree, anchor = "nw")
        canvas1.create_text( 210, 270 ,fill="Black",font="Arial 15 ", text = "Corré du sud")
    @Rule(Pays(Asie=True),Pays(Arabe=True),Pays(organiseCM=False))
    def KSA(self):
        # Display image
        canvas1.create_image( 50, 300, image = imgarabie, anchor = "nw")
        canvas1.create_text( 210, 270 ,fill="Black",font="Arial 15 ", text = "Arabie Saoudie")
    @Rule(Pays(Asie=True),Pays(continent=True))
    def australie(self):
        # Display image
        canvas1.create_image( 50, 300, image = imgaust, anchor = "nw")
        canvas1.create_text( 210, 270 ,fill="Black",font="Arial 15 ", text = "Australie")
    @Rule(Pays(Asie=True,Arabe=False,organiseCM=False))
    def Iran(self):
        # Display image
        canvas1.create_image( 50, 300, image = imgiran, anchor = "nw")
        canvas1.create_text( 210, 270 ,fill="Black",font="Arial 15 ", text = "Iran")
    @Rule(Pays(AmeriqueNord=True),Pays(organiseCM=True),Pays(Soccer=True))
    def usa(self):
        # Display image
        canvas1.create_image( 50, 300, image = imgusa, anchor = "nw")
        canvas1.create_text( 210, 270 ,fill="Black",font="Arial 15 ", text = "USA")
    @Rule(Pays(AmeriqueNord=True),Pays(organiseCM=True),Pays(Soccer=False))
    def Mexique(self):
        # Display image
        canvas1.create_image( 50, 300, image = imgmexique, anchor = "nw")
        canvas1.create_text( 210, 270 ,fill="Black",font="Arial 15 ", text = "Mexique")
    @Rule(Pays(AmeriqueNord=True),Pays(PremiereCM=True))
    def Canada(self):
        # Display image
        canvas1.create_image( 50, 300, image = imgcanada, anchor = "nw")
        canvas1.create_text( 210, 270 ,fill="Black",font="Arial 15 ", text = "Canada")
    @Rule(Pays(AmeriqueNord=True,organiseCM=False,Soccer=False,PremiereCM=False))
    def CostaRica(self):
        # Display image
        canvas1.create_image( 50, 300, image = imgcosta, anchor = "nw")
        canvas1.create_text( 210, 270 ,fill="Black",font="Arial 15 ", text = "Costa Rica")
    @Rule(Pays(AmeriqueSud=True,RemporteCM=False ,meilleur2joueurs=False,Plustitree=False))
    def Equateur(self):
        # Display image
        canvas1.create_image( 50, 300, image = imgequateur, anchor = "nw")
        canvas1.create_text( 210, 270 ,fill="Black",font="Arial 15 ", text = "Equateur")
    @Rule(Pays(AmeriqueSud=True , RemporteCM=True,meilleur2joueurs=False, Plustitree=False))
    def Uruguay(self):
        # Display image
        canvas1.create_image( 50, 300, image = imgurug, anchor = "nw")
        canvas1.create_text( 210, 270 ,fill="Black",font="Arial 15 ", text = "Uruguay")
    @Rule(Pays(AmeriqueSud=True , RemporteCM=True , Plustitree=True))
    def Bresil(self):
        # Display image
        canvas1.create_image( 50, 300, image = imgbresil, anchor = "nw")
        canvas1.create_text( 210, 270 ,fill="Black",font="Arial 15 ", text = "Brésil")
    @Rule(Pays(AmeriqueSud=True , RemporteCM=True ,meilleur2joueurs=True))
    def Argentine(self):
        # Display image
        canvas1.create_image( 50, 300, image = imgarg, anchor = "nw")
        canvas1.create_text( 210, 270 ,fill="Black",font="Arial 15 ", text = "Argentine")

    
pays=DetectionPays()
pays.reset()

m0=False
m1=False
m2=False
m3=False
m4=False
m5=False
m6=False
m7=False
m8=False
m82=False
m9=False
m10=False
m11=False
m12=False
m13=False
m14=False
m15=False
m16=False
m17=False
m18=False
m19=False
m20=False
m21=False
m22=False
m23=False
m24=False
m25=False
m26=False
m27=False
m28=False
m29=False
m30=False

window.title("Fifa World Cup Qatar 2022")
window.geometry("1080x720")
window.iconbitmap("petitlogocm.ico")

# Add image file
bg = PhotoImage(file = "logocm.png")
# Add image file
imgcm = PhotoImage(file = "cm.png")

  
# Display image
canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")
# Display image
canvas1.create_image( 1425, 20, image = imgcm, 
                     anchor = "nw")
# Add Text
canvas1.create_text( 1000, 40,fill="#811d36",font="Arial 20 ", text = "Bienvenue dans le Jeu de la Coupe du Monde Fifa Qatar 2022")

def fnEurope():
    def fnRemporteCM(): 
        btn1.configure(bg="#BDECB6",state= DISABLED)
        def fnMeilleurChampionnatEurope():
            btn2.configure(bg="#BDECB6",state= DISABLED)
            m2=True
            pays.declare(Pays(Europe=m0,RemporteCM=m1,MeilleurChampionnatEurope=m2))
            pays.run()
        def fnPasMeilleurChampionnatEurope():
            btn21x.configure(bg="#ff6961",state= DISABLED)
            def gagnecmafrique():
              btn3.configure(bg="#BDECB6",state= DISABLED)      
              m3=True
              pays.declare(Pays(Europe=m0,RemporteCM=m1,RemporteCMenAfrique=m3))
              pays.run()
            def pasgagnecmafrqiue():
                btn31x.configure(bg="#ff6961",state= DISABLED)
                def gagne2foiscm():
                    btn4.configure(bg="#BDECB6",state= DISABLED)
                    m4=True
                    pays.declare(Pays(Europe=m0,RemporteCM=m1,RemporteCM2fois=m4))
                    pays.run()
                def pasgagne2foiscm():
                    btn41.configure(bg="#ff6961",state= DISABLED)
                    m2=False
                    pays.declare(Pays(Europe=m0,RemporteCM=m1,MeilleurChampionnatEurope=m2))
                    pays.run()
                canvas1.create_text( 860, 335 ,fill="Black",font="Arial 15 ", text = "Est ce que le pays a gagné 2 fois la coupe du monde?\n")
                btn4 = Button(window, text='Oui', width=10,height=0, bd='1',command=gagne2foiscm)
                btn4.place(x=1200, y=310)
                btn41 = Button(window, text='Non', width=10,height=0, bd='1',command=pasgagne2foiscm)
                btn41.place(x=1300, y=310)   
            canvas1.create_text( 856, 275 ,fill="Black",font="Arial 15 ", text = "Est ce que le pays a gagné la coupe du monde dans \nun pays Africain?")
            btn3 = Button(window, text='Oui', width=10,height=0, bd='1',command=gagnecmafrique)
            btn3.place(x=1200, y=265)
            btn31x = Button(window, text='Non', width=10,height=0, bd='1',command=pasgagnecmafrqiue)
            btn31x.place(x=1300, y=265)  
        m1=True   
        canvas1.create_text( 870, 235 ,fill="Black",font="Arial 15 ", text = "Est ce que le pays a le meilleur championnat en Europe?\n")
        btn2 = Button(window, text='Oui', width=10,height=0, bd='1',command=fnMeilleurChampionnatEurope)
        btn2.place(x=1200, y=210)
        btn21x = Button(window, text='Non', width=10,height=0, bd='1',command=fnPasMeilleurChampionnatEurope)
        btn21x.place(x=1300, y=210)
    def pasremportecm():
        btn11.configure(bg="#ff6961",state= DISABLED)
        def jouefinale():
            btn5.configure(bg="#BDECB6",state= DISABLED)
            def roisanscour():
               btn6.configure(bg="#BDECB6",state= DISABLED) 
               m6=True
               pays.declare(Pays(Europe=m0,FinalisteCM=m5,Roisanscouronne=m6))
               pays.run()
            def nonroisanscour():
                btn61.configure(bg="#ff6961",state= DISABLED)
                m6=False
                pays.declare(Pays(Europe=m0,FinalisteCM=m5,Roisanscouronne=m6))
                pays.run() 
            m5=True
            canvas1.create_text( 865, 270 ,fill="Black",font="Arial 15 ", text = "Est ce que le pays est surnomé 'Le roi sans couronne'?\n")
            btn6 = Button(window, text='Oui', width=10,height=0, bd='1',command=roisanscour)
            btn6.place(x=1200, y=250)
            btn61 = Button(window, text='Non', width=10,height=0, bd='1',command=nonroisanscour)
            btn61.place(x=1300, y=250)
        def pasjouefinale():
            btn51.configure(bg="#ff6961",state= DISABLED)
            def grandebret():
               btn7.configure(bg="#BDECB6",state= DISABLED) 
               m7=True
               pays.declare(Pays(Europe=m0,appartientUK=m7))
               pays.run()
            def pasgrandebret():
                btn71.configure(bg="#ff6961",state= DISABLED)
                def commencep():
                    btn8.configure(bg="#BDECB6",state= DISABLED)
                    def joucelebre():
                       btn9.configure(bg="#BDECB6",state= DISABLED)
                       m82=True
                       pays.declare(Pays(Europe=m0,commenceparP=m8,joueurcelebre=m82))
                       pays.run()
                    def nonjouecelbre():
                       btn91.configure(bg="#ff6961",state= DISABLED) 
                       m82=False
                       pays.declare(Pays(Europe=m0,commenceparP=m8,joueurcelebre=m82))
                       pays.run()
                    m8=True
                    canvas1.create_text( 900, 500 ,fill="Black",font="Arial 15 ", text = "Est ce que je suis le pays du joueur le plus celere du monde entier?\n")
                    btn9 = Button(window, text='Oui', width=10,height=0, bd='1',command=joucelebre)
                    btn9.place(x=1200, y=477)
                    btn91 = Button(window, text='Non', width=10,height=0, bd='1',command=nonjouecelbre)
                    btn91.place(x=1300, y=477) 
                def commencepasp():
                    btn81.configure(bg="#ff6961",state= DISABLED)
                    def vikings():
                        btn88.configure(bg="#BDECB6",state= DISABLED)
                        m9=True
                        pays.declare(Pays(Europe=m0,viking=m9))
                        pays.run()
                    def pasvikings():
                        btn881.configure(bg="#ff6961",state= DISABLED)
                        def pasavecs():
                            btn101.configure(bg="#ff6961",state= DISABLED)
                            m2=False 
                            m1=False
                            pays.declare(Pays(Europe=m0,RemporteCM=m1,MeilleurChampionnatEurope=m2))
                            pays.run()
                        def avecs():
                            btn10.configure(bg="#BDECB6",state= DISABLED)
                            def riche():
                              btn11.configure(bg="#BDECB6",state= DISABLED)  
                              m11=True
                              pays.declare(Pays(Europe=m0,commencepars=m10,paysriche=m11))
                              pays.run()  
                            def pasriche():
                              btn111.configure(bg="#ff6961",state= DISABLED)  
                              m11=False  
                              pays.declare(Pays(Europe=m0,commencepars=m10,paysriche=m11))
                              pays.run()
                            m10=True
                            canvas1.create_text( 910, 758 ,fill="Black",font="Arial 15 ", text = "Est ce que le pays est parmi les pays les plus riches au monde?\n")
                            btn11 = Button(window, text='Oui', width=10,height=0, bd='1',command=riche)
                            btn11.place(x=1200, y=735)
                            btn111 = Button(window, text='Non', width=10,height=0, bd='1',command=pasriche)
                            btn111.place(x=1300, y=735)
                        canvas1.create_text( 870, 720 ,fill="Black",font="Arial 15 ", text = "Est ce que le nom du pays commence avec la lettre S?\n")
                        btn10 = Button(window, text='Oui', width=10,height=0, bd='1',command=avecs)
                        btn10.place(x=1200, y=697)
                        btn101 = Button(window, text='Non', width=10,height=0, bd='1',command=pasavecs)
                        btn101.place(x=1300, y=697)
                    canvas1.create_text( 820, 498 ,fill="Black",font="Arial 15 ", text = "Est ce que le pays est surnomée 'Le viking'?\n")
                    btn88 = Button(window, text='Oui', width=10,height=0, bd='1',command=vikings)
                    btn88.place(x=1200, y=475)
                    btn881 = Button(window, text='Non', width=10,height=0, bd='1',command=pasvikings)
                    btn881.place(x=1300, y=475) 
                canvas1.create_text( 862, 310 ,fill="Black",font="Arial 15 ", text = "Est ce que le nom du pays commence avec la lettre P?\n")
                btn8 = Button(window, text='Oui', width=10,height=0, bd='1',command=commencep)
                btn8.place(x=1200, y=290)
                btn81 = Button(window, text='Non', width=10,height=0, bd='1',command=commencepasp)
                btn81.place(x=1300, y=290)  
            canvas1.create_text( 855, 275 ,fill="Black",font="Arial 15 ", text = "Est ce que le pays fait partie de la Grande-Bretagne?\n")
            btn7 = Button(window, text='Oui', width=10,height=0, bd='1',command=grandebret)
            btn7.place(x=1200, y=250)
            btn71 = Button(window, text='Non', width=10,height=0, bd='1',command=pasgrandebret)
            btn71.place(x=1300, y=250)
        canvas1.create_text( 873, 235 ,fill="Black",font="Arial 15 ", text = "Est ce que le pays a joué la finale de la coupe du monde?\n")
        btn5 = Button(window, text='Oui', width=10,height=0, bd='1',command=jouefinale)
        btn5.place(x=1200, y=210)
        btn51 = Button(window, text='Non', width=10,height=0, bd='1',command=pasjouefinale)
        btn51.place(x=1300, y=210) 
    btn0.configure(bg="#BDECB6",state= DISABLED)
    m0=True
    canvas1.create_text( 868, 196,fill="Black",font="Arial 15 ", text = "Est ce que le pays a deja remporté la coupe du monde?\n")
    btn1 = Button(window, text='Oui', width=10,height=0, bd='1',command=fnRemporteCM)
    btn1.place(x=1200, y=170)
    btn11 = Button(window, text='Non', width=10,height=0, bd='1',command=pasremportecm)
    btn11.place(x=1300, y=170)
def paseurope():
    def fnafrique():
        btn12.configure(bg="#BDECB6",state= DISABLED)
        def fnarabe():
           btn13.configure(bg="#BDECB6",state= DISABLED)
           def fntour1():
                btn15.configure(bg="#BDECB6",state= DISABLED)
                m14=True
                pays.declare(Pays(Afrique=m12,Arabe=m13,Tour1=m14))
                pays.run()
           def fnpastour1():
                btn151.configure(bg="#ff6961",state= DISABLED)
                m14=False
                pays.declare(Pays(Afrique=m12,Arabe=m13,Tour1=m14))
                pays.run() 
           m13=True
           canvas1.create_text( 912, 275 ,fill="Black",font="Arial 15 ", text = "Est ce que le pays a deja passé le 1er tour à la coupe du monde?\n")
           btn15 = Button(window, text='Oui', width=10,height=0, bd='1',command=fntour1)
           btn15.place(x=1200, y=250)
           btn151 = Button(window, text='Non', width=10,height=0, bd='1',command=fnpastour1)
           btn151.place(x=1300, y=250)
        def fnpasarabe():
            btn131.configure(bg="#ff6961",state= DISABLED)
            def fnlions():
                btn14.configure(bg="#BDECB6",state= DISABLED)
                def battubres():
                    btn16.configure(bg="#BDECB6",state= DISABLED)
                    m16=True
                    pays.declare(Pays(Afrique=m12,Lions=m15,BattreBresil=m16))
                    pays.run()
                def nonbattubresil():
                    btn161.configure(bg="#ff6961",state= DISABLED)
                    m16=False
                    pays.declare(Pays(Afrique=m12,Lions=m15,BattreBresil=m16))
                    pays.run()
                m15=True
                canvas1.create_text( 907, 320 ,fill="Black",font="Arial 15 ", text = "Est ce que c'est le seul pays africain qui a battu le Bresil pendant\n la coupe du monde?")
                btn16 = Button(window, text='Oui', width=10,height=0, bd='1',command=battubres)
                btn16.place(x=1200, y=300)
                btn161 = Button(window, text='Non', width=10,height=0, bd='1',command=nonbattubresil)
                btn161.place(x=1300, y=300)
            def fnpaslions():
                btn141.configure(bg="#ff6961",state= DISABLED)
                m15=False
                pays.declare(Pays(Afrique=m12,Lions=m15))
                pays.run()
            canvas1.create_text( 825, 275 ,fill="Black",font="Arial 15 ", text = "Est ce que le pays 'Les lions ' comme surnon?\n")
            btn14 = Button(window, text='Oui', width=10,height=0, bd='1',command=fnlions)
            btn14.place(x=1200, y=250)
            btn141 = Button(window, text='Non', width=10,height=0, bd='1',command=fnpaslions)
            btn141.place(x=1300, y=250)   
        m12=True
        canvas1.create_text( 765, 235 ,fill="Black",font="Arial 15 ", text = "Est ce que c'est un pays Arabe?\n")
        btn13 = Button(window, text='Oui', width=10,height=0, bd='1',command=fnarabe)
        btn13.place(x=1200, y=210)
        btn131 = Button(window, text='Non', width=10,height=0, bd='1',command=fnpasarabe)
        btn131.place(x=1300, y=210)
    def fnpasafrique():
            btn121.configure(bg="#ff6961",state= DISABLED)
            def fnasie():
                btn17.configure(bg="#BDECB6",state= DISABLED)
                def fnorganisecm():
                    btn18.configure(bg="#BDECB6",state= DISABLED)
                    def fnasiearabe():
                        btn19.configure(bg="#BDECB6",state= DISABLED)
                        m19=True
                        pays.declare(Pays(Asie=m17,organiseCM=m18,Arabe=m19))
                        pays.run() 
                    def fnasiepasrabe():
                        btn191.configure(bg="#ff6961",state= DISABLED)
                        def fnbattre2europe():
                            btn20.configure(bg="#BDECB6",state= DISABLED)
                            m20=True
                            pays.declare(Pays(Asie=m17,organiseCM=m18,battue2europe=m20))
                            pays.run()
                        def fnpasbattre2europe():
                            btn201.configure(bg="#ff6961",state= DISABLED)
                            m19=False
                            pays.declare(Pays(Asie=m17,organiseCM=m18,Arabe=m19))
                            pays.run()
                        canvas1.create_text( 900, 500 ,fill="Black",font="Arial 15 ", text = "Est ce que le pays a battu 2 équipes européenne durant la coupe\n                                                             du monde Qatar 2022?")
                        btn20 = Button(window, text='Oui', width=10,height=0, bd='1',command=fnbattre2europe)
                        btn20.place(x=1200, y=477)
                        btn201 = Button(window, text='Non', width=10,height=0, bd='1',command=fnpasbattre2europe)
                        btn201.place(x=1300, y=477) 
                    m18=True 
                    canvas1.create_text(765, 316 ,fill="Black",font="Arial 15 ", text = "Est ce que c'est un pays Arabe?\n")
                    btn19 = Button(window, text='Oui', width=10,height=0, bd='1',command=fnasiearabe)
                    btn19.place(x=1200, y=290)
                    btn191 = Button(window, text='Non', width=10,height=0, bd='1',command=fnasiepasrabe)
                    btn191.place(x=1300, y=290)
                def fnpasorganisecm():
                    btn181.configure(bg="#ff6961",state= DISABLED)
                    def fnarabepascm():
                        btn22.configure(bg="#BDECB6",state= DISABLED)
                        m21=True
                        m18=False
                        pays.declare(Pays(Asie=m17,Arabe=m21,organiseCM=m18))
                        pays.run()
                    def fnpasarabepascm():
                        btn221.configure(bg="#ff6961",state= DISABLED)
                        def fncontinent():
                            btn23.configure(bg="#BDECB6",state= DISABLED)
                            m22=True
                            pays.declare(Pays(Asie=m17,continent=m22))
                            pays.run()
                        def fnpascontinent():
                            btn231.configure(bg="#ff6961",state= DISABLED)
                            m19=False
                            m18=False
                            pays.declare(Pays(Asie=m17,Arabe=m19,organiseCM=m18))
                            pays.run()
                        canvas1.create_text( 830, 500 ,fill="Black",font="Arial 15 ", text = "Est ce que le pays représente tout un continent?\n")
                        btn23 = Button(window, text='Oui', width=10,height=0, bd='1',command=fncontinent)
                        btn23.place(x=1200, y=477)
                        btn231 = Button(window, text='Non', width=10,height=0, bd='1',command=fnpascontinent)
                        btn231.place(x=1300, y=477) 
                    canvas1.create_text(765, 316 ,fill="Black",font="Arial 15 ", text = "Est ce que c'est un pays Arabe?\n")
                    btn22 = Button(window, text='Oui', width=10,height=0, bd='1',command=fnarabepascm)
                    btn22.place(x=1200, y=290)
                    btn221 = Button(window, text='Non', width=10,height=0, bd='1',command=fnpasarabepascm)
                    btn221.place(x=1300, y=290)
                m17=True
                canvas1.create_text(865, 272 ,fill="Black",font="Arial 15 ", text = "Est ce que le pays a deja organisé la coupe du monde?\n")
                btn18 = Button(window, text='Oui', width=10,height=0, bd='1',command=fnorganisecm)
                btn18.place(x=1200, y=250)
                btn181 = Button(window, text='Non', width=10,height=0, bd='1',command=fnpasorganisecm)
                btn181.place(x=1300, y=250)
            def fnpasasie():
                btn171.configure(bg="#ff6961",state= DISABLED)
                def fnameriquenord():
                    btn24.configure(bg="#BDECB6",state= DISABLED)
                    def fnameriquenordcm():
                        btn25.configure(bg="#BDECB6",state= DISABLED)
                        def fnsoccer():
                            btn26.configure(bg="#BDECB6",state= DISABLED)
                            m25=True
                            pays.declare(Pays(AmeriqueNord=m23,organiseCM=m24,Soccer=m25))
                            pays.run() 
                        def fnnosoccer():
                            btn261.configure(bg="#ff6961",state= DISABLED)
                            m25=False
                            pays.declare(Pays(AmeriqueNord=m23,organiseCM=m24,Soccer=m25))
                            pays.run()
                        m24=True
                        canvas1.create_text( 897, 500 ,fill="Black",font="Arial 15 ", text = "Est ce que le 'Football' dans ce pays est indiqué par le mot 'Soccer'?\n")
                        btn26 = Button(window, text='Oui', width=10,height=0, bd='1',command=fnsoccer)
                        btn26.place(x=1200, y=477)
                        btn261 = Button(window, text='Non', width=10,height=0, bd='1',command=fnnosoccer)
                        btn261.place(x=1300, y=477)
                    def fnameriquenordpascm():
                        btn251.configure(bg="#ff6961",state= DISABLED)
                        def fnpremierefois():
                            btn27.configure(bg="#BDECB6",state= DISABLED)
                            m26=True
                            pays.declare(Pays(AmeriqueNord=m23,PremiereCM=m26))
                            pays.run()
                        def fnpaspremierefois():
                              btn271.configure(bg="#ff6961",state= DISABLED)  
                              m24=False
                              m25=False
                              m26=False
                              pays.declare(Pays(AmeriqueNord=m23,organiseCM=m24,Soccer=m25,PremiereCM=m26))
                              pays.run() 
                        canvas1.create_text( 978, 500 ,fill="Black",font="Arial 15 ", text = "Est ce que la coupe du monde FIFA Qatar 2022, est la première\n                                                   coupe du monde dans l'histoire de ce pays?")
                        btn27 = Button(window, text='Oui', width=10,height=0, bd='1',command=fnpremierefois)
                        btn27.place(x=1200, y=477)
                        btn271 = Button(window, text='Non', width=10,height=0, bd='1',command=fnpaspremierefois)
                        btn271.place(x=1300, y=477)
                    m23=True
                    canvas1.create_text(865, 314 ,fill="Black",font="Arial 15 ", text = "Est ce que le pays a deja organisé la coupe du monde?\n")
                    btn25 = Button(window, text='Oui', width=10,height=0, bd='1',command=fnameriquenordcm)
                    btn25.place(x=1200, y=290)
                    btn251 = Button(window, text='Non', width=10,height=0, bd='1',command=fnameriquenordpascm)
                    btn251.place(x=1300, y=290)
                def fnpasameriquenord():
                    btn241.configure(bg="#ff6961",state= DISABLED)
                    def fnameriquesud():
                        btn28.configure(bg="#BDECB6",state= DISABLED)
                        def fnameriquesudcm():
                            btn29.configure(bg="#BDECB6",state= DISABLED)
                            def fnplustitree():
                                btn30.configure(bg="#BDECB6",state= DISABLED)
                                m29=True
                                pays.declare(Pays(AmeriqueSud=m27,RemporteCM=m28,Plustitree=m29))
                                pays.run()
                            def fnpasplustitree():
                                btn301.configure(bg="#ff6961",state= DISABLED)
                                def fn2meilleur():
                                    btn31.configure(bg="#BDECB6",state= DISABLED)
                                    m30=True
                                    pays.declare(Pays(AmeriqueSud=m27,RemporteCM=m28,meilleur2joueurs=m30))
                                    pays.run()
                                def fnpas2meilleur():
                                    btn311.configure(bg="#ff6961",state= DISABLED)
                                    m29=False
                                    m30=False         
                                    pays.declare(Pays(AmeriqueSud=m27,RemporteCM=m28,meilleur2joueurs=m30,Plustitree=m29))
                                    pays.run()
                                canvas1.create_text(828, 760 ,fill="Black",font="Arial 15 ", text = "Est ce que ce pays contient les deux meilleurs \njoueurs de l'histoire du football ?")
                                btn31 = Button(window, text='Oui', width=10,height=0, bd='1',command=fn2meilleur)
                                btn31.place(x=1200, y=740)
                                btn311 = Button(window, text='Non', width=10,height=0, bd='1',command=fnpas2meilleur)
                                btn311.place(x=1300, y=740)
                            m28=True
                            canvas1.create_text(860, 710 ,fill="Black",font="Arial 15 ", text = "Est ce que ce pays a le plus de coupe du monde dans \nl'histoire des nations ?")
                            btn30 = Button(window, text='Oui', width=10,height=0, bd='1',command=fnplustitree)
                            btn30.place(x=1200, y=690)
                            btn301 = Button(window, text='Non', width=10,height=0, bd='1',command=fnpasplustitree)
                            btn301.place(x=1300, y=690)
                        def fnameriquesudpascm():
                            btn291.configure(bg="#ff6961",state= DISABLED)
                            m28=False
                            m29=False
                            m30=False  
                            pays.declare(Pays(AmeriqueSud=m27,RemporteCM=m28,Plustitree=m29,meilleur2joueurs=m30))
                            pays.run()
                        m27=True
                        canvas1.create_text( 870, 500 ,fill="Black",font="Arial 15 ", text = "Est ce que ce pays a deja remporté la coupe du monde ?\n")
                        btn29 = Button(window, text='Oui', width=10,height=0, bd='1',command=fnameriquesudcm)
                        btn29.place(x=1200, y=477)
                        btn291 = Button(window, text='Non', width=10,height=0, bd='1',command=fnameriquesudpascm)
                        btn291.place(x=1300, y=477)
                    def fnpasameriquesud():
                        btn281.configure(bg="#ff6961",state= DISABLED)
                        # Display image
                        canvas1.create_image( 50, 300, image = imgno, anchor = "nw")
                        canvas1.create_text( 220, 270 ,fill="Black",font="Arial 15 ", text = "Pas d'équipe de coupe du monde\n     qui n'a pas de cantinent")
                    canvas1.create_text(843, 314 ,fill="Black",font="Arial 15 ", text = "Est ce que le pays se trouve en Amérique du sud?\n")
                    btn28 = Button(window, text='Oui', width=10,height=0, bd='1',command=fnameriquesud)
                    btn28.place(x=1200, y=290)
                    btn281 = Button(window, text='Non', width=10,height=0, bd='1',command=fnpasameriquesud)
                    btn281.place(x=1300, y=290)
                canvas1.create_text( 847, 272 ,fill="Black",font="Arial 15 ", text = "Est ce que le pays se trouve en Amérique du nord?\n")
                btn24 = Button(window, text='Oui', width=10,height=0, bd='1',command=fnameriquenord)
                btn24.place(x=1200, y=250)
                btn241 = Button(window, text='Non', width=10,height=0, bd='1',command=fnpasameriquenord)
                btn241.place(x=1300, y=250)
            canvas1.create_text( 788, 235 ,fill="Black",font="Arial 15 ", text = "Est ce que le pays se trouve en Asie?\n")
            btn17 = Button(window, text='Oui', width=10,height=0, bd='1',command=fnasie)
            btn17.place(x=1200, y=210)
            btn171 = Button(window, text='Non', width=10,height=0, bd='1',command=fnpasasie)
            btn171.place(x=1300, y=210)
    btn01.configure(bg="#ff6961",state= DISABLED)
    canvas1.create_text( 800, 196,fill="Black",font="Arial 15 ", text = "Est ce que le pays se trouve en Afrique?\n")
    btn12 = Button(window, text='Oui', width=10,height=0, bd='1',command=fnafrique)
    btn12.place(x=1200, y=171)
    btn121 = Button(window, text='Non', width=10,height=0, bd='1',command=fnpasafrique)
    btn121.place(x=1300, y=171)
canvas1.create_text( 800, 158,fill="Black",font="Arial 15 ", text = "Est ce que le pays se trouve en Europe?\n")
btn0 = Button(window, text='Oui', width=10,height=0, bd='1',command=fnEurope)
btn0.place(x=1200, y=130)
btn01 = Button(window, text='Non', width=10,height=0, bd='1',command=paseurope)
btn01.place(x=1300, y=130)
canvas1.create_image( 10, 20, image = imgallphotos, anchor = "nw")
window.mainloop()