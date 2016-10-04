import numpy as np

print("ingrese l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,m122,tB")

l1=0.8
l2=0.25
l3=0.011
l4=-0.5
l5=0.5
l6=0
l7=0
l8=0
l9=0
l10=0
m122=100000
tB=1

print("l1=",l1,"l2=",l2,"l3",l3,"l4",l4,"l5",l5,"l6",l6,"l7",l7,"l8",l8,"l9",l9,"l10",l10,"m122",m122,"tB",tB)

B=np.arctan(tB)
arctB=np.arctan(B)
sB2=np.sin(B)*np.sin(B)
cB2=np.cos(B)*np.cos(B)
s2B=np.sin(2*B)
c2B=np.cos(2*B)


#masa del h con la formula de 2HDMC
#Mh2=m122/np.sqrt(sB2*cB2)-246*0.5*(2*l5+l6*(1/tB)+l7*tB)+246*0.5*(l5-l4) 

#print("Mh2=",np.sqrt(Mh2))

m112=m122*tB-246*0.5*(l1*cB2+(l3+l4+l5)*sB2+3*l6*np.sqrt(sB2*cB2)+l7*sB2*tB)

m222=m122*arctB-246*0.5*(l2*sB2+(l3+l4+l5)*cB2+l6*cB2*arctB+3*l7*np.sqrt(sB2*cB2))

M222 = m112*sB2+m222*cB2+m122*s2B

L3=0.25*s2B*s2B*(l1+l2-2*(l3+l4+l5))+l3-s2B*c2B*(l6-l7)

#masa del h con la formula de aritizabal
MH2=M222+0.5*246*L3

print("MH2=",np.sqrt(MH2))  



mA2=m122*(tB*sB2+arctB*cB2+s2B)-246/2*(2*l5+l6*(np.sqrt(sB2*cB2)*sB2+cB2*arctB*cB2)+l7*(sB2*tB*sB2+np.sqrt(sB2*cB2)*cB2))

mH2=mA2+246/2*(l5-l4)

print("mH2",np.sqrt(mH2))
