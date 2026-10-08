import pandas as pd, matplotlib.pyplot as plt, matplotlib.gridspec as gs
P="powerbi_ready/"
df=pd.read_csv(P+"bank_clean.csv"); fn=pd.read_csv(P+"funnel.csv")
job=pd.read_csv(P+"seg_job.csv").sort_values("conversion_pct")
mon=pd.read_csv(P+"seg_month.csv"); con=pd.read_csv(P+"seg_contact.csv")
pout=pd.read_csv(P+"seg_poutcome.csv"); age=pd.read_csv(P+"seg_age_group.csv")
camp=pd.read_csv(P+"seg_campaign_band.csv")
BLUE,GREEN,ORG,RED,GREY="#1f6feb","#2da44e","#f59e0b","#d1242f","#6e7781"
overall=df.converted.mean()*100
fig=plt.figure(figsize=(22,14),facecolor="#f6f8fa")
fig.suptitle("Bank Marketing Campaign: Funnel & Conversion Performance",fontsize=26,fontweight="bold",y=0.975)
g=gs.GridSpec(4,4,figure=fig,height_ratios=[0.55,2,2,2],hspace=0.55,wspace=0.35,left=0.085,right=0.97,top=0.92,bottom=0.05)
kp=[("Customers Contacted",f"{len(df):,}"),("Engaged (3+ min)",f"{fn.customers[1]:,}  ({fn.conv_from_start_pct[1]:.1f}%)"),
    ("Subscribed (Yes)",f"{int(df.converted.sum()):,}"),("Overall Conversion",f"{overall:.2f}%")]
for i,(t,v) in enumerate(kp):
    a=fig.add_subplot(g[0,i]); a.axis("off")
    a.add_patch(plt.Rectangle((0,0),1,1,transform=a.transAxes,color="white",ec="#d0d7de",lw=1.5))
    a.text(.5,.68,v,ha="center",va="center",fontsize=22,fontweight="bold",color=BLUE,transform=a.transAxes)
    a.text(.5,.25,t,ha="center",va="center",fontsize=13,color=GREY,transform=a.transAxes)
def style(a,t):
    a.set_title(t,fontsize=14,fontweight="bold",loc="left"); a.set_facecolor("white")
    for s in ["top","right"]: a.spines[s].set_visible(False)
# funnel
a=fig.add_subplot(g[1,0:2]); style(a,"Conversion Funnel (strict: each stage is a subset of previous)")
st=["Contacted","Engaged\n(3+ min)","Converted"]; v=fn.customers.tolist()
a.barh(st[::-1],v[::-1],color=[GREEN,ORG,BLUE]); a.set_xlim(0,max(v)*1.45)
for i,(n,p) in enumerate(zip(v[::-1],fn.conv_from_prev_pct.tolist()[::-1])):
    lab=f"{n:,}" if i==2 else f"{n:,}  ({p:.1f}% of previous)"
    a.text(n+400,i,lab,va="center",fontsize=12,fontweight="bold")
a.text(0.99,0.05,f"Drop-off: Contacted→Engaged {fn.dropoff_from_prev_pct[1]:.1f}% | Engaged→Converted {fn.dropoff_from_prev_pct[2]:.1f}%",
       transform=a.transAxes,ha="right",fontsize=11,color=RED)
# job
a=fig.add_subplot(g[1,2:4]); style(a,"Conversion % by Job")
cl=[GREEN if x>overall else GREY for x in job.conversion_pct]
a.barh(job.job,job.conversion_pct,color=cl); a.axvline(overall,color=RED,ls="--",lw=1.5)
a.text(overall+.3,0,f"avg {overall:.1f}%",color=RED,fontsize=10)
for i,x in enumerate(job.conversion_pct): a.text(x+.3,i,f"{x:.1f}%",va="center",fontsize=10)
# month
a=fig.add_subplot(g[2,0:2]); style(a,"Monthly: Volume (bars) vs Conversion % (line)")
a.bar(mon.month,mon.customers,color="#b6d4fe"); a.set_ylabel("Customers")
b=a.twinx(); b.plot(mon.month,mon.conversion_pct,color=RED,marker="o",lw=2.5); b.set_ylabel("Conversion %",color=RED)
b.spines["top"].set_visible(False)
# poutcome
a=fig.add_subplot(g[2,2]); style(a,"Previous Campaign Outcome")
p=pout.sort_values("conversion_pct",ascending=False)
a.bar(p.poutcome,p.conversion_pct,color=[GREEN,ORG,GREY,GREY][:len(p)])
a.set_ylim(0,75)
for i,x in enumerate(p.conversion_pct): a.text(i,x+1,f"{x:.1f}%",ha="center",fontsize=11,fontweight="bold")
# contact
a=fig.add_subplot(g[2,3]); style(a,"Contact Channel")
a.bar(con.contact,con.conversion_pct,color=[BLUE,BLUE,RED] if False else [BLUE if c!="unknown" else RED for c in con.contact])
a.set_ylim(0,18)
for i,x in enumerate(con.conversion_pct): a.text(i,x+.3,f"{x:.1f}%",ha="center",fontsize=11,fontweight="bold")
# age
a=fig.add_subplot(g[3,0:2]); style(a,"Conversion % by Age Group")
ao=["<25","25-34","35-44","45-54","55-64","65+"]; age=age.set_index("age_group").loc[ao].reset_index()
a.bar(age.age_group,age.conversion_pct,color=[GREEN if x>overall else GREY for x in age.conversion_pct]); a.axhline(overall,color=RED,ls="--"); a.set_ylim(0,48)
for i,x in enumerate(age.conversion_pct): a.text(i,x+.7,f"{x:.1f}%",ha="center",fontsize=11,fontweight="bold")
# campaign
a=fig.add_subplot(g[3,2:4]); style(a,"Fatigue: Conversion % by No. of Contacts in Campaign")
co=["1","2","3","4-5","6+"]; camp["campaign_band"]=camp.campaign_band.astype(str); camp=camp.set_index("campaign_band").loc[co].reset_index()
a.plot(camp.campaign_band,camp.conversion_pct,marker="o",color=RED,lw=3)
for i,x in enumerate(camp.conversion_pct): a.text(i,x+.5,f"{x:.1f}%",ha="center",fontsize=11,fontweight="bold")
a.set_ylim(0,18)
fig.text(.5,.012,"Source: UCI Bank Marketing (bank-full, 45,211 rows). Engaged = call duration >= 180 sec.",ha="center",fontsize=11,color=GREY)
plt.savefig("charts/dashboard.png",dpi=130,facecolor=fig.get_facecolor()); print("ok")
