biler = 100 #integer
plads_i_en_bil = 4.0 #Float værdi
førere = 30 #integer
passagerer = 90 #integer
biler_ude_af_drift = biler - førere #Int biler trækkes fra int førere
biler_i_kørsel = førere #biler_i_kørsel defineres som førere
samlet_bil_kapacitet = biler_i_kørsel * plads_i_en_bil #ganger biler_i_kørsel og plads_i_en_bil
#som definere som samlet_bil_kapacitet
gennemsnit_af_passagerer_per_bil = passagerer / biler_i_kørsel #passagerer divideres med biler_i_kørsel og definere
#gennemsnit_af_passagerer_per_bil

print("Der er", biler, " biler til rådighed. ")
print("Der er kun", førere, "førere til rådghed. ")
print("Der vil være", biler_ude_af_drift, "tomme biler i dag.")
print("Vi kan transportere", samlet_bil_kapacitet, "personer i dag. ")
print("Vi har", passagerer, "passagerer i dag.")
print("Vi skal cirka putte", gennemsnit_af_passagerer_per_bil, "i hver bil.")
