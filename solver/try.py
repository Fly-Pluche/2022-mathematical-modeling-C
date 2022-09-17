F_list=[]
F1_list =[]
F2_list =[]
F3_list =[]
F4_list =[]
F5_list =[]
F6_list =[]
F7_list =[]
for i in range(length):
    # 铅钡
    F1=0.215*data2.iloc[i,0]+0.073*data2.iloc[i,1]+0.091*data2.iloc[i,2]-0.029*data2.iloc[i,3]+0.134*data2.iloc[i,4]+0.18*data2.iloc[i,5]+0.111*data2.iloc[i,6]-0.161*data2.iloc[i,7]-0.137*data2.iloc[i,8]-0.178*data2.iloc[i,9]-0.098*data2.iloc[i,10]-0.133*data2.iloc[i,11]+0.13*data2.iloc[i,12]-0.144*data2.iloc[i,13]
    F2=-0.164*data2.iloc[i,0]-0.161*data2.iloc[i,1]+0.117*data2.iloc[i,2]+0.28*data2.iloc[i,3]+0.194*data2.iloc[i,4]+0.061*data2.iloc[i,5]+0.166*data2.iloc[i,6]-0.093*data2.iloc[i,7]+0.178*data2.iloc[i,8]-0.122*data2.iloc[i,9]+0.228*data2.iloc[i,10]+0.102*data2.iloc[i,11]+0.065*data2.iloc[i,12]-0.029*data2.iloc[i,13]
    F3=-0.036*data2.iloc[i,0]+0.004*data2.iloc[i,1]+0.259*data2.iloc[i,2]+0.142*data2.iloc[i,3]+0.031*data2.iloc[i,4]+0.214*data2.iloc[i,5]+0.153*data2.iloc[i,6]+0.235*data2.iloc[i,7]-0.349*data2.iloc[i,8]+0.372*data2.iloc[i,9]+0.05*data2.iloc[i,10]-0.065*data2.iloc[i,11]+0.215*data2.iloc[i,12]+0.328*data2.iloc[i,13]
    F4=-0.07*data2.iloc[i,0]+0.415*data2.iloc[i,1]-0.404*data2.iloc[i,2]+0.029*data2.iloc[i,3]+0.305*data2.iloc[i,4]+0.277*data2.iloc[i,5]-0.343*data2.iloc[i,6]+0.011*data2.iloc[i,7]-0.033*data2.iloc[i,8]-0.001*data2.iloc[i,9]+0.083*data2.iloc[i,10]+0.433*data2.iloc[i,11]+0.323*data2.iloc[i,12]+0.066*data2.iloc[i,13]
    F5=-0.106*data2.iloc[i,0]+0.306*data2.iloc[i,1]+0.342*data2.iloc[i,2]-0.082*data2.iloc[i,3]-0.134*data2.iloc[i,4]-0.232*data2.iloc[i,5]+0.069*data2.iloc[i,6]-0.607*data2.iloc[i,7]+0.244*data2.iloc[i,8]+0.005*data2.iloc[i,9]-0.312*data2.iloc[i,10]+0.179*data2.iloc[i,11]+0.194*data2.iloc[i,12]+0.527*data2.iloc[i,13]
    F6=0.018*data2.iloc[i,0]+0.588*data2.iloc[i,1]+0.4*data2.iloc[i,2]-0.05*data2.iloc[i,3]+0.287*data2.iloc[i,4]-0.122*data2.iloc[i,5]+0.22*data2.iloc[i,6]+0.224*data2.iloc[i,7]-0.097*data2.iloc[i,8]-0.021*data2.iloc[i,9]+0.084*data2.iloc[i,10]+0.307*data2.iloc[i,11]-0.602*data2.iloc[i,12]-0.145*data2.iloc[i,13]
    F7=-0.086*data2.iloc[i,0]-0.186*data2.iloc[i,1]+0.245*data2.iloc[i,2]-0.195*data2.iloc[i,3]-0.147*data2.iloc[i,4]+0.075*data2.iloc[i,5]+0.21*data2.iloc[i,6]+0.322*data2.iloc[i,7]+0.228*data2.iloc[i,8]+0.152*data2.iloc[i,9]-0.497*data2.iloc[i,10]+0.524*data2.iloc[i,11]+0.378*data2.iloc[i,12]-0.478*data2.iloc[i,13]

    F=(0.269/0.846)*F1+(0.212/0.846)*F2+(0.113/0.846)*F3+(0.077/0.846)*F4+(0.061/0.846)*F5+(0.06/0.846)*F6+(0.056/0.846)*F7

    F_list.append(F)
    F1_list.append(F1)
    F2_list.append(F2)
    F3_list.append(F3)
    F4_list.append(F4)
    F5_list.append(F5)
    F6_list.append(F6)
    F7_list.append(F7)



F_list=[]
F1_list =[]
F2_list =[]
F3_list =[]
F4_list =[]

for i in range(length):
    # 高钾
    F1=-0.15*data2.iloc[i,0]+0.092*data2.iloc[i,1]+0.132*data2.iloc[i,2]+0.112*data2.iloc[i,3]+0.112*data2.iloc[i,4]+0.134*data2.iloc[i,5]+0.118*data2.iloc[i,6]+0.074*data2.iloc[i,7]+0.072*data2.iloc[i,8]+0.105*data2.iloc[i,9]+0.09*data2.iloc[i,10]+0.121*data2.iloc[i,11]+0.023*data2.iloc[i,12]+0.062*data2.iloc[i,13]
    F2=0.063*data2.iloc[i,0]-0.255*data2.iloc[i,1]-0.142*data2.iloc[i,2]-0.216*data2.iloc[i,3]+0.154*data2.iloc[i,4]+0.022*data2.iloc[i,5]+0.138*data2.iloc[i,6]+0.04*data2.iloc[i,7]-0.087*data2.iloc[i,8]+0.117*data2.iloc[i,9]+0.243*data2.iloc[i,10]+0.183*data2.iloc[i,11]+0.07*data2.iloc[i,12]-0.246*data2.iloc[i,13]
    F3=0.013*data2.iloc[i,0]-0.014*data2.iloc[i,1]+0.093*data2.iloc[i,2]-0.119*data2.iloc[i,3]+0.21*data2.iloc[i,4]+0.039*data2.iloc[i,5]-0.159*data2.iloc[i,6]-0.432*data2.iloc[i,7]+0.153*data2.iloc[i,8]-0.188*data2.iloc[i,9]+0.021*data2.iloc[i,10]+0.109*data2.iloc[i,11]+0.479*data2.iloc[i,12]+0.138*data2.iloc[i,13]
    F4=0.027*data2.iloc[i,0]+0.004*data2.iloc[i,1]+0.074*data2.iloc[i,2]-0.072*data2.iloc[i,3]-0.09*data2.iloc[i,4]-0.229*data2.iloc[i,5]-0.187*data2.iloc[i,6]+0.221*data2.iloc[i,7]+0.507*data2.iloc[i,8]+0.385*data2.iloc[i,9]-0.237*data2.iloc[i,10]+0.034*data2.iloc[i,11]+0.231*data2.iloc[i,12]-0.261*data2.iloc[i,13]
    F=(0.464/0.878)*F1+(0.198/0.878)*F2+(0.119/0.878)*F3+(0.097/0.878)*F4


    F_list.append(F)
    F1_list.append(F1)
    F2_list.append(F2)
    F3_list.append(F3)
    F4_list.append(F4)