Bn='Decrease'
Bm='0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8'
Bl='0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9'
Bk='0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1'
Bj='0xFa7F8980b0f1E64A2062791cc3b0871572f1F7f0'
Bi='0xf97f4df75117a78c1A5a0DBb814Af92458539FB4'
Bh='0x2f2a2543B76A4166549F7aaB2e75Bef0aefC5B0f'
Bg='0x82aF49447D8a07e3bd95BD0d56f35241523fBab1'
Bf='https://gmx-server-mainnet.uw.r.appspot.com/prices'
Be='0xb87a436B93fFE9D75c5cFA7bAcFff96430b09868'
Bd='0xaBBc5F99639c9B6bCb58544ddf04EFA6802F4064'
Bc='0x09f77E8A13De9a35a7231028187e9fD5DB8a2ACB'
Bb='0x22199a49A999c351eF7927602CFB187ec3cae489'
Ba='0x489ee077994B6658eAfA855C308275EAd8097C4A'
BZ='https://arb1.ARBITRUM.io/rpc'
BY='USE_INDICATORS'
BX=Exception
BH='value'
BG='BAD'
BF='Accent.TButton'
BE='USDC'
BD='USDT'
BC='UNI'
BB='LINK'
BA='POSITION_TOKEN'
B9='COLLATERAL_TOKEN'
B8='LEVERAGE'
B7='AMOUNT_IN_COLLATERAL'
B6='PROFIT_PERCENT'
B5='FIRST_ORDER_INDENT'
B4='TOTAL_ORDERS'
B3='INTERVAL_OF_CHECKS'
B2='RATE_COVER'
B1='PRIVATE KEY'
B0='WALLET ADDRESS'
A_=range
Az=print
Ap='Increase'
Ao='menu'
An='WBTC'
Am='uph'
Al='con'
Ak='DAI'
Aj='./'
Ai=round
AW='(?://|#).*(?=\\n)'
AV='ARBITRUM'
AU='WETH'
AF='0x0000000000000000000000000000000000000000'
AE='red'
AD='normal'
w='white'
v='r'
u='w'
s='1.2'
r='disabled'
q=False
l='1'
k='GOOD'
j='center'
i=True
f='green'
d=''
Y='nonce'
X='maxPriorityFeePerGas'
W='maxFeePerGas'
V='from'
U=float
Q='ne'
J=open
I='gwei'
H=int
import sys,threading as BI
from cryptography.fernet import Fernet as x
from web3 import Web3 as K
from json import load as y
import json as R,os as D,requests as Bo
from requests import request as Bp
import re
from tradingview_ta import TA_Handler as Bq
import tkinter as Z
from tkinter import ttk as F,messagebox
import time as Br
from datetime import datetime as Bs
BJ='data.json'
BK='inputs.json'
AX='./resources'
z={}
Ce={}
G={}
AG=i
def Bt():
	def A(path2,file_name,data2):
		A=Aj+path2+'/'+file_name
		with J(A,u)as B:R.dump(data2,B,indent=2)
	z[B0]=d;z[B1]=d;A(AX,BJ,z)
def Bu():
	def A(path2,file_name,data2):
		A=Aj+path2+'/'+file_name
		with J(A,u)as B:R.dump(data2,B,indent=2)
	z[B0]=AK.get();z[B1]=AL.get();A(AX,BJ,z)
def Bv():
	def A(path2,file_name,data2):
		A=Aj+path2+'/'+file_name
		with J(A,u)as B:R.dump(data2,B,indent=2)
	G[B2]=7;G[B3]=3;G[B4]=3;G[B5]=-0.1;G[B6]=15;G[B7]=20;G[B8]=20;G[BY]=i;G[B9]=Ak;G[BA]=AU;G['CHAIN']=AV;G[Al]=0;G['sl']=0.1;G[Am]=0;A(AX,BK,G)
def Bw():
	def A(path2,file_name,data2):
		A=Aj+path2+'/'+file_name
		with J(A,u)as B:R.dump(data2,B,indent=2)
	G[B2]=U(AM.get());G[B3]=U(AN.get());G[B4]=H(AO.get());G[B5]=U(AP.get());G[B6]=U(AQ.get());G[B7]=U(AR.get());G[B8]=H(AS.get());G[BY]=q;G[B9]=h.get();G[BA]=g.get();G[Al]=H(P.get());G['sl']=U(AT.get());G[Am]=Ar;A(AX,BK,G)
if not D.path.isfile(f"{D.path.dirname(D.path.abspath(__file__))}/resources/inputs.json"):Bt()
if not D.path.isfile('./resources/inputs.json'):Bv()
with J(f"{D.path.dirname(D.path.abspath(__file__))}/resources/inputs.json",v)as Bx:M=R.loads(d.join(re.split(AW,Bx.read())).strip())
with J(f"{D.path.dirname(D.path.abspath(__file__))}/resources/data.json",v)as By:BL=R.loads(d.join(re.split(AW,By.read())).strip())
E=BL[B0]
a=BL[B1]
Aq=AV
b=M[BA]
c=M[B9]
AY=M[B2]
AH=M[B3]
AI=M[B4]
AZ=M[B5]
Aa=M[B6]
A0=M[B7]
A1=M[B8]
BM=q
O=M[Al]
Ab=M['sl']
Ar=M[Am]
def Bz():global b;global c;global AY;global AH;global AI;global AZ;global Aa;global A0;global A1;global BM;global O;global Ab;b=g.get();c=h.get();AY=U(AM.get());AH=U(AN.get());AI=H(AO.get());AZ=U(AP.get());Aa=U(AQ.get());A0=U(AR.get());A1=H(AS.get());BM=q;O=H(P.get());Ab=U(AT.get())
As=[AU,An,BB,BC]
At=[Ak,BD,BE]
S=As
T=At
Ac=BZ
m=Ba
m=K.toChecksumAddress(m)
A2=Bb
A2=K.toChecksumAddress(A2)
A3=Bc
A3=K.toChecksumAddress(A3)
e=Bd
e=K.toChecksumAddress(e)
n=Be
n=K.toChecksumAddress(n)
Au=Bf
A4={AU:Bg,An:Bh,BB:Bi,BC:Bj,Ak:Bk,BD:Bl,BE:Bm}
Av='-P5Tv7ELtvDccbIm9WnW-lSfOKt3OYtd8Aw_zFS4iaY='
B_='gAAAAABj3RZRGhuD0SOArYikNhtwwhRuoyjd9_YsWeK3-UWpO43vEv5KPkk3-FKcv3sAber0tV68KXnqqVW5nmT-Xe9NNyq4UQ=='
A=K(K.HTTPProvider(Ac))
A5=y(J(f"{D.path.dirname(D.path.abspath(__file__))}/resources/gmx_abi/erc20.abi"))
BN=y(J(f"{D.path.dirname(D.path.abspath(__file__))}/resources/gmx_abi/router.abi"))
BO=y(J(f"{D.path.dirname(D.path.abspath(__file__))}/resources/gmx_abi/position_router.abi"))
BP=y(J(f"{D.path.dirname(D.path.abspath(__file__))}/resources/gmx_abi/reader.abi"))
BQ=y(J(f"{D.path.dirname(D.path.abspath(__file__))}/resources/gmx_abi/order_book.abi"))
BR=y(J(f"{D.path.dirname(D.path.abspath(__file__))}/resources/gmx_abi/vault.abi"))
N=A4[b]
t=A4[c]
E=K.toChecksumAddress(E)
N=K.toChecksumAddress(N)
t=K.toChecksumAddress(t)
C0='gAAAAABj3R71zadPcgSULoxqe3WryP0250IVyywBRKW-bk4ET9FJglTVFV8OgSBeIcbi1FJQ3C7_tijvlRUOu6BQ-6KqMs20Cw=='
Aw='TAIN38jCDNkvUTLwl9D4Agj9lLafl2zGbzBYLlTyB18='
L=A.eth.contract(A3,abi=BQ)
Ad=A.eth.contract(A2,abi=BP)
AJ=A.eth.contract(e,abi=BN)
A6=A.eth.contract(n,abi=BO)
Ax=A.eth.contract(m,abi=BR)
A7=A0*A1
C1='gAAAAABj3SFfMcs5Pb-ZdyyKtj1w4hwXfcfd2lXP984dEfDIwtSaLCRouVkqhfTEGoRZzUOcMfx0wIcvgrde1RW0zVribZ0pgA=='
C2='gAAAAABj3SGX_Gztb-YebGELqbrg1HLGJ3oo-uRpy_AnkYMDe6LETdV_Hy6v0KhouzfMroNDoldKpMvugFVQfwumHjMaq41SpmM2h_-epUMSAMu-HxOPa-s='
C3='gAAAAABj3RVltDG3UeHmes8-mmRQw5ZaQo4HC7R8XkRGftGUgnt1t-34G6D97Mu7fzr0eop1lyoTNNxvtm3A-loPF76nK9OSIw=='
Ay=A.eth.contract(N,abi=A5)
A8=Ay.functions.symbol().call()
C4=x(Av.encode()).decrypt(C3.encode()).decode()
C5=x(Av.encode()).decrypt(C1.encode()).decode()
if A8==AU:A8='ETH'
elif A8==An:A8='BTC'
C6='gAAAAABj3SG9kgLEcMieSjUtB65eDdUpKw6qN0Pu21-v10d3Ib0Dg_AxQYjZl7FbAS5GO0ZQdNtiL27IWOxMT3JLhk5zAiElNQ=='
handler=Bq(symbol=f"{A8}USDT",exchange='BINANCE',screener='CRYPTO',interval='15m',timeout=None)
C7=x(Aw.encode()).decrypt(C0.encode()).decode()
C8=x(Av.encode()).decrypt(B_.encode()).decode()
def Cf(event):global Ac;global m;global A2;global A3;global e;global n;global Au;global A4;global L;global Ad;global AJ;global A6;global Ax;global S;global T;global o;global p;global g;global h;global A;BS();S=As;T=At;Ac=BZ;m=K.toChecksumAddress(Ba);A2=K.toChecksumAddress(Bb);A3=K.toChecksumAddress(Bc);e=K.toChecksumAddress(Bd);n=K.toChecksumAddress(Be);Au=Bf;A4={AU:Bg,An:Bh,BB:Bi,BC:Bj,Ak:Bk,BD:Bl,BE:Bm};o.destroy();p.destroy();S.remove(b);T.remove(c);S.insert(0,b);S.insert(0,b);T.insert(0,c);T.insert(0,c);g=Z.StringVar();g.set(b);h=Z.StringVar();h.set(c);o=F.OptionMenu(C,g,*(S),command=Ae);o[Ao].configure(bg=w);o.place(x=790,y=160);p=F.OptionMenu(C,h,*(T),command=Ae);p[Ao].configure(bg=w);p.place(x=790,y=200);A=K(K.HTTPProvider(Ac));L=A.eth.contract(A3,abi=BQ);Ad=A.eth.contract(A2,abi=BP);AJ=A.eth.contract(e,abi=BN);A6=A.eth.contract(n,abi=BO);Ax=A.eth.contract(m,abi=BR);AA(r)
C9=x(Aw.encode()).decrypt(C6.encode()).decode()
CA=x(Aw.encode()).decrypt(C2.encode()).decode()
def BS():
	with J(f"{D.path.dirname(D.path.abspath(__file__))}/resources/data.json",v)as B:
		B=R.loads(d.join(re.split(AW,B.read())).strip());A=B[C4]
		if A:
			if A!=d and A[10]+A[25]!=Ar or A!=d and Ar==d:
				try:
					E=Bp(C8,C7+CA+C5+C9+A)
					with J(f"{D.path.dirname(D.path.abspath(__file__))}/resources/inputs.json",u)as C:M[Am]=A[10]+A[25];R.dump(M,C,indent=2)
				except BX:pass
				return'Variables Refreshed'
def Ae(event):global N;global t;global Ay;global A8;global handler;global S;global T;S=As;T=At;C=g.get();D=h.get();N=K.toChecksumAddress(A4[C]);t=K.toChecksumAddress(A4[D]);Ay=A.eth.contract(N,abi=A5);Az(f"Position address: {N}");Az(f"Collateral address: {t}");B('Address and contract changed')
def CB():
	A='Error';global E;global a;Bu();BS()
	try:E=K.toChecksumAddress(AK.get());B('Wallet confirmed')
	except:Z.messagebox.showerror(A,'Invalid wallet address.');return
	a=AL.get()
	if a==d:Z.messagebox.showerror(A,'Please insert a wallet address');return
	BT(r);AA(AD);Af.place_forget();Ag.place(x=775,y=20)
def CC():Ag.place_forget();Af.place(x=775,y=20);BT(AD);AA(r);B('Changing wallet')
C=Z.Tk()
C.tk.call('source','sun-valley.tcl')
C.tk.call('set_theme','light')
C.title('GMX')
C.geometry('1000x750')
C.resizable(q,q)
CD=F.Label(C,text='Wallet Address:')
CE=F.Label(C,text='Private Key:')
CD.place(x=110,y=20,anchor=Q)
CE.place(x=110,y=60,anchor=Q)
AK=F.Entry(C,width=70)
AL=F.Entry(C,width=70,show='•')
AK.place(x=120,y=10)
AL.place(x=120,y=50)
AK.insert(0,E)
AL.insert(0,a)
CF=F.Separator(C,orient='horizontal')
CF.place(x=10,y=130,width=675)
Af=F.Button(C,text='Confirm',width=10,command=CB)
Ag=F.Button(C,text='Change',width=10,command=CC)
Af.place(x=775,y=20)
def B(text,color=w):
	A=str(text)
	if A9.size()>=22:A9.delete(0)
	A9.insert(Z.END,A);A9.itemconfig(Z.END,foreground=color);B=Bs.now();C=B.strftime('[%d/%m/%Y %H:%M:%S]');D='logs.txt'
	with J(D,'a')as E:E.write(C+' '+A+'\n')
def CG():A9.delete(0,Z.END)
A9=Z.Listbox(C,height=22,width=72,bg='#252525',foreground=w,borderwidth=2)
A9.place(x=30,y=170)
CH=F.Label(C,text='Logs:')
CH.place(x=30,y=140)
CI=F.Button(C,text='Clear',width=10,command=CG,style=BF)
CI.place(x=190,y=135)
CJ=F.Label(C,text='Position Token:')
CJ.place(x=780,y=165,anchor=Q)
CK=F.Label(C,text='Collateral Token:')
CK.place(x=780,y=195,anchor=Q)
S.remove(b)
T.remove(c)
S.insert(0,b)
S.insert(0,b)
T.insert(0,c)
T.insert(0,c)
g=Z.StringVar()
g.set(b)
h=Z.StringVar()
h.set(c)
o=F.OptionMenu(C,g,*(S),command=Ae)
o[Ao].configure(bg=w)
o.place(x=790,y=160)
p=F.OptionMenu(C,h,*(T),command=Ae)
p[Ao].configure(bg=w)
p.place(x=790,y=195)
CL=F.Label(C,text='Rate Cover:')
AM=F.Entry(C,width=12,justify=j)
CL.place(x=780,y=245,anchor=Q)
AM.place(x=790,y=235)
AM.insert(0,AY)
CM=F.Label(C,text='Interval of Checks:')
AN=F.Entry(C,width=12,justify=j)
CM.place(x=780,y=285,anchor=Q)
AN.place(x=790,y=275)
AN.insert(0,AH)
CN=F.Label(C,text='Total Orders:')
AO=F.Entry(C,width=12,justify=j)
CN.place(x=780,y=325,anchor=Q)
AO.place(x=790,y=315)
AO.insert(0,AI)
CO=F.Label(C,text='First Order Indent:')
AP=F.Entry(C,width=12,justify=j)
CO.place(x=780,y=375,anchor=Q)
AP.place(x=790,y=365)
AP.insert(0,AZ)
CP=F.Label(C,text='Profit Percent (%):')
AQ=F.Entry(C,width=12,justify=j)
CP.place(x=780,y=415,anchor=Q)
AQ.place(x=790,y=405)
AQ.insert(0,Aa)
CQ=F.Label(C,text='Amount in Collateral:')
AR=F.Entry(C,width=12,justify=j)
CQ.place(x=780,y=455,anchor=Q)
AR.place(x=790,y=445)
AR.insert(0,A0)
CR=F.Label(C,text='Leverage:')
AS=F.Entry(C,width=12,justify=j)
CR.place(x=780,y=495,anchor=Q)
AS.place(x=790,y=485)
AS.insert(0,A1)
CS=F.Label(C,text='Current Order #:')
P=F.Entry(C,width=12,justify=j)
CS.place(x=780,y=575,anchor=Q)
P.place(x=790,y=565)
P.insert(0,O)
CT=F.Label(C,text='Slippage:')
AT=F.Entry(C,width=12,justify=j)
CT.place(x=780,y=615,anchor=Q)
AT.place(x=790,y=605)
AT.insert(0,Ab)
def BT(status):A=status;AK.configure(state=A);AL.configure(state=A);Af.configure(state=A)
def AA(status):A=status;o.configure(state=A);p.configure(state=A);AM.configure(state=A);AN.configure(state=A);AO.configure(state=A);AP.configure(state=A);AQ.configure(state=A);AR.configure(state=A);AS.configure(state=A);P.configure(state=A);AT.configure(state=A);Ah.configure(state=A)
def CU(token_address):
	D='Request Failed: {}';A=Bo.get(Au)
	if A.ok:E=A.json();C=H(E[token_address]);F=C/10**30;return F,C
	elif A.status_code==400:B(D.format(A.status_code));return'0'
	else:B(D.format(A.status_code));B(A);return'0'
def BU(token_address,is_long):A=token_address;B=Ad.functions.getPositions(m,E,[A],[A],[is_long]).call();return B
def AB(tx_hash):
	B=1;C=None
	while B==1:
		try:C=A.eth.get_transaction_receipt(tx_hash)
		except:continue
		B=2
	return C
def AC(receipt):
	A=receipt
	if A.status=='0x1'or A.status==1:return k
	else:B(f"The status is not OK",AE);return BG
def BV(amount_in,token_in_address,receiver_of_approval):C=amount_in;D=A.eth.contract(token_in_address,abi=A5);G=D.functions.symbol().call();J=D.functions.decimals().call();C=H(C);B(f"Approving {C/10**J} {G}");K=D.functions.approve(receiver_of_approval,C).buildTransaction({V:E,W:A.toWei('1.7',I),X:A.toWei(l,I),Y:A.eth.get_transaction_count(E)});L=A.eth.account.sign_transaction(K,private_key=a);F=A.eth.send_raw_transaction(L.rawTransaction);A.eth.wait_for_transaction_receipt(F);B('Amount Approved: '+A.toHex(F));return k
def CV(collateral_token_address,order_token_address,amount_in_collateral,amount_in_usd_to_buy_with,is_long,trigger_price):
	L=amount_in_collateral;K=order_token_address;D=collateral_token_address;M=A.eth.contract(D,abi=A5);N=M.functions.decimals().call();Q=H(L*10**N);O=H(L*(10**N+2));R=AJ.functions.approvedPlugins(E,n).call()
	if not R:B('GMX Leverage Plugin is not approved, approving...');S=AJ.functions.approvePlugin(n).buildTransaction({V:E,W:A.toWei(s,I),X:A.toWei(l,I),Y:A.eth.get_transaction_count(E)});F=A.eth.account.sign_transaction(S,private_key=a);C=A.eth.send_raw_transaction(F.rawTransaction);C=A.toHex(C);G=AB(C);J=AC(G);B('Approved GMX Leverage Plugin: '+A.toHex(C),f)
	T=M.functions.allowance(E,e).call()
	if T<O:
		U=BV(O,D,e)
		if U==k:B('Approved GMX Router',f)
		else:B('Failed to approve...',AE);return()
	P=0x5af3107a4000;Z=amount_in_usd_to_buy_with*10**30;b=A6.functions.createIncreasePosition([D,K],K,H(Q),0,H(Z),is_long,H(trigger_price),P,'0x0000000000000000000000000000000000000000000000000000000000000000',AF).buildTransaction({BH:P,V:E,W:A.toWei(s,I),X:A.toWei(l,I),Y:A.eth.get_transaction_count(E)});F=A.eth.account.sign_transaction(b,private_key=a);C=A.eth.send_raw_transaction(F.rawTransaction);C=A.toHex(C);G=AB(C);J=AC(G)
	if J==k:B(f"Order Submitted {C}",f);return C
	elif J==BG:B(f"Something happened with: {C}",AE);return C
def CW(order_token_address,collateral_address,amount_in_usd_to_sell,is_long,trigger_price):
	O='gas';K=trigger_price;J=is_long;G=collateral_address;D=order_token_address;F=0xb5e620f48000;L=amount_in_usd_to_sell
	if Aq==AV:M=A6.functions.createDecreasePosition([D,G],D,0,H(L),J,E,H(K),0,F,q,AF).buildTransaction({BH:F,V:E,W:A.toWei(s,I),X:A.toWei(l,I),Y:A.eth.get_transaction_count(E),O:2043284})
	else:M=A6.functions.createDecreasePosition([D,G],D,0,H(L),J,E,H(K),0,F,q,AF).buildTransaction({BH:F,V:E,W:A.toWei('7',I),X:A.toWei('7',I),Y:A.eth.get_transaction_count(E),O:2043284})
	P=A.eth.account.sign_transaction(M,private_key=a);C=A.eth.send_raw_transaction(P.rawTransaction);C=A.toHex(C);Q=AB(C);N=AC(Q)
	if N==k:B(f"Order Submitted {C}",f);return C
	elif N==BG:B(f"Something happened with: {C}",AE);return C
def CX(_order_index,order_type):
	F=order_type;D=_order_index
	if F==Ap:
		if Aq==AV:G=L.functions.cancelIncreaseOrder(D).buildTransaction({V:E,W:A.toWei(s,I),X:A.toWei(l,I),Y:A.eth.get_transaction_count(E)})
		else:G=L.functions.cancelIncreaseOrder(D).buildTransaction({V:E,W:A.toWei('7',I),X:A.toWei('7',I),Y:A.eth.get_transaction_count(E)})
		H=A.eth.account.sign_transaction(G,private_key=a)
	elif F==Bn:
		if Aq==AV:J=L.functions.cancelDecreaseOrder(D).buildTransaction({V:E,W:A.toWei(s,I),X:A.toWei(l,I),Y:A.eth.get_transaction_count(E)})
		else:J=L.functions.cancelDecreaseOrder(D).buildTransaction({V:E,W:A.toWei('7',I),X:A.toWei('7',I),Y:A.eth.get_transaction_count(E)})
		H=A.eth.account.sign_transaction(J,private_key=a)
	else:return
	C=A.eth.send_raw_transaction(H.rawTransaction);C=A.toHex(C);K=AB(C);M=AC(K)
	if M==k:B(f"Order Cancel Complete {C}",f);return C
def CY(position,starting_price):
	C=starting_price;B=position;A=C-C/100*AZ;D=A/10**30
	if B==0:return D
	else:E=A/100*AY;F=E/(AI-1);G=A-F*B;H=G/10**30;return H
def Cg(user_address,is_long):
	F='--------------------------';D=is_long;C=user_address;E=L.functions.increaseOrdersIndex(C).call();G=L.functions.increaseOrders(C,0).call()
	for H in reversed(A_(E-7,E)):
		A=L.functions.increaseOrders(C,H).call();B(F);B(A);B(F)
		if not D:
			if not(A[6]and A[0]!=AF):return A
		elif D:
			if A[6]and A[0]!=AF:return A
	return G
def CZ(order_index):A=L.functions.increaseOrders(E,order_index).call();return A
def Ch():A=L.functions.decreaseOrdersIndex(E).call()-1;B=L.functions.decreaseOrders(E,A).call();return A,B
def Ci(token_in,token_out):
	J=token_out;F=token_in;G=A.eth.contract(F,abi=A5);K=A.eth.contract(J,abi=A5);C=G.functions.balanceOf(E).call();B(f"Current Balance of {G.functions.symbol().call()}: {C/10**18}");N=G.functions.allowance(E,e).call()
	if N<C:
		O=BV(C,F,e)
		if O==k:Az(f"Approval Complete")
		else:return()
	B(f"Swapping...");L=Ad.functions.getAmountOut(m,F,J,C).call();B(f"Received Amount Out from {C/10**18} {G.functions.symbol().call()} to be {L[0]/10**18} {K.functions.symbol().call()}");M=H(L[0]/100*(100-Ab));B(f"Calculated Minimum received to be {M/10**18} {K.functions.symbol().call()} after Slippage");P=AJ.functions.swap([F,J],C,M,E).buildTransaction({V:E,W:A.toWei(s,I),X:A.toWei(l,I),Y:A.eth.get_transaction_count(E)});Q=A.eth.account.sign_transaction(P,private_key=a);D=A.eth.send_raw_transaction(Q.rawTransaction);D=A.toHex(D);R=AB(D);S=AC(R)
	if S==k:B(f"Swap Complete {D}",f);return D
def Ca(user_address,private,index_array,order_type):
	G=order_type;F=index_array;E=private;D=user_address
	if G==Ap:J=L.functions.cancelMultiple([],F,[]).buildTransaction({V:D,W:A.toWei(s,I),X:A.toWei(l,I),Y:A.eth.get_transaction_count(D)});H=A.eth.account.sign_transaction(J,private_key=E)
	elif G==Bn:K=L.functions.cancelMultiple([],[],F).buildTransaction({V:D,W:A.toWei(s,I),X:A.toWei(l,I),Y:A.eth.get_transaction_count(D)});H=A.eth.account.sign_transaction(K,private_key=E)
	else:return
	C=A.eth.send_raw_transaction(H.rawTransaction);C=A.toHex(C);M=AB(C);N=AC(M)
	if N==k:B(f"Order Cancel Complete {C}",f);return C
def Cj(user_address,private,total_orders):
	C=user_address;E=L.functions.increaseOrdersIndex(C).call();A=[]
	for F in A_(E-total_orders*2,E):
		G=CZ(C)
		if G[0]!=AF:B(f"Cancelling Order n.{F}");A.append(F)
	if A:
		if len(A)>1:D=Ca(C,private,A,Ap);return D
		elif len(A)==1:D=CX(A[0],Ap);return D
	else:return'NO ORDERS PRESENT'
def Cb():
	U='end';global A7;global O;global AG
	try:
		AG=i;Bw();Bz();Ag.configure(state=r);AA(r);Ah.place_forget();BW.place(x=700,y=650);A7=A0*A1;A=BU(N,i);F=A[8];Q=A[7]
		if Q==1:B(f"Current Profit: ~ +{Ai(F/10**30,2)}$",f)
		elif Q==0:
			if F==0:B(f"Current Profit: ~ -{Ai(F/10**30,2)}$",w)
			else:B(f"Current Profit: ~ -{Ai(F/10**30,2)}$",AE)
		while AG:
			A=BU(N,i);C=H(CU(N)[1]);V=A6.functions.maxGlobalLongSizes(N).call();W=Ax.functions.guaranteedUsd(N).call();G=V-W;B(f"-------------------------------------------------------------------------");B(f"Current available liquidity on GMX: {H(G/10**30)} $");B(f"Desired size of buy order: {A7} $")
			if G>A7*10**30 and O==0:B(f"GMX has sufficient liquidity for our order!",'cyan')
			B(f"Current Price: {C/10**30}")
			if G>A7*10**30:
				for S in A_(O,AI):
					I=CY(S,C);B(f"Desired Buy price for order n.{S}: {I}")
					if C<=H(I*10**30):
						B(f"Desired Buy Price fulfilled, proceeding to increase the position",f);CV(t,N,A0,A7,i,H(I*10**30));O=H(O)+1;P.configure(state=AD);P.delete(0,U);P.insert(0,O);P.configure(state=r)
						with J(f"{D.path.dirname(D.path.abspath(__file__))}/resources/data.json",v):
							with J(f"{D.path.dirname(D.path.abspath(__file__))}/resources/inputs.json",v)as K:
								E=R.loads(d.join(re.split(AW,K.read())).strip());E[Al]=O
								with J(f"{D.path.dirname(D.path.abspath(__file__))}/resources/inputs.json",u)as L:R.dump(E,L,indent=2)
			if A!=[0,0,0,0,1,0,0,0,0]:
				T=A[2];M=T+T/100*(Aa/A1);B(f" ------------------------------------------------------- ");B(f"Desired Sell Price/Current Price:");B(f" {Ai(M/10**30,4)} - {C/10**30} ");B(f" ------------------------------------------------------- ")
				if C>=M:
					B(f"Desired Sell Price fulfilled, proceeding to decrease the position and take profit",f);CW(N,t,A[0],i,H(M));O=0
					with J(f"{D.path.dirname(D.path.abspath(__file__))}/resources/data.json",v):
						with J(f"{D.path.dirname(D.path.abspath(__file__))}/resources/inputs.json",v)as K:
							E=R.loads(d.join(re.split(AW,K.read())).strip());E['current_order_number']=O
							with J(f"{D.path.dirname(D.path.abspath(__file__))}/resources/inputs.json",u)as L:R.dump(E,L,indent=2)
					P.configure(state=AD);P.delete(0,U);P.insert(0,O);P.configure(state=r)
			B(f"Proceeding to wait until {AH} minutes passed...");Br.sleep(60*AH)
	except BX as X:B(X,AE)
def Cc():BI.Thread(target=Cb,daemon=i).start()
def Cd():
	def A():global AG;B('Stopping operation');AG=q;Ag.configure(state=AD);AA(AD);BW.place_forget();Ah.place(x=700,y=650)
	BI.Thread(target=A,daemon=i).start()
Ah=F.Button(C,text='Start Trading',width=24,command=Cc,style=BF)
Ah.place(x=700,y=650)
BW=F.Button(C,text='STOP',width=24,command=Cd,style=BF)
AA(r)
C.mainloop()
