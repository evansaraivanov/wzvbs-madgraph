from ROOT import *

c = TCanvas("c","c",300,500)
h1 = TH1F("","",75,0.,750.)
h2 = TH1F("","",75,0.,750.)
h3 = TH1F("","",75,0.,750.)

f1 = TFile.Open("unweighted_events.root")
f2 = TFile.Open("~/Documents/MG5_aMC_v2_6_7/SMEFTSIM_round2_results/cw_range_tot/Events/run_03/unweighted_events.root")
f3 = TFile.Open("~/Documents/MG5_aMC_v2_6_7/SMEFTSIM_round2_results/cw_range_tot/Events/run_04/unweighted_events.root")
t1 = f1.Get("LHEF")
t2 = f2.Get("LHEF")
t3 = f3.Get("LHEF")
idlist = []

for i in t1:
    npart = i.GetLeaf("Event/Event.Nparticles").GetValue()
    print(npart)
    for j in range(1,int(npart)):
        ident = i.GetLeaf("Particle/Particle.PID").GetValue(j)
        print(ident)
        if ident not in idlist:
            idlist.append(ident)
        if(ident == 11 or ident == -11):
            pt = i.GetLeaf("Particle/Particle.PT").GetValue(j)
            if(pt != 0):
                print(pt)
                h1.Fill(pt)

for i in t2:
    npart = i.GetLeaf("Event/Event.Nparticles").GetValue()
    print(npart)
    for j in range(1,int(npart)):
        ident = i.GetLeaf("Particle/Particle.PID").GetValue(j)
        print(ident)
        if ident not in idlist:
            idlist.append(ident)
        if(ident == 11 or ident == -11):
            pt = i.GetLeaf("Particle/Particle.PT").GetValue(j)
            if(pt != 0):
                print(pt)
                h2.Fill(pt)

for i in t3:
    npart = i.GetLeaf("Event/Event.Nparticles").GetValue()
    print(npart)
    for j in range(1,int(npart)):
        ident = i.GetLeaf("Particle/Particle.PID").GetValue(j)
        print(ident)
        if ident not in idlist:
            idlist.append(ident)
        if(ident == 11 or ident == -11):
            pt = i.GetLeaf("Particle/Particle.PT").GetValue(j)
            if(pt != 0):
                print(pt)
                h3.Fill(pt)

if(h1.Integral() != 0):
    h1.Scale(0.025063/h1.Integral())
if(h2.Integral() != 0):
    h2.Scale(0.02972/h2.Integral())
if(h3.Integral() != 0):
    h3.Scale(0.02933/h3.Integral())

gStyle.SetOptStat(0)
c.SetLogx()
h1.GetXaxis().SetTitle("p_{T}^{ee}")
h1.GetYaxis().SetTitle("\frac{d \sigma}{d p_{T}^{ee}}")

h2.SetLineColor(3)
h3.SetLineColor(2)

print(idlist)
h1.Draw()
h2.Draw("same")
h3.Draw("same")
c.Print("pt-diffx.pdf")
