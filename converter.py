import pandas as pd
import os
import numpy as np
type1_list=["Bug","Dark","Dragon","Electric","Fairy","Fighting","Fire","Flying","Ghost","Grass","Ground","Ice","Normal","Poison","Psychic","Rock","Steel","Water"]
type2_list=["Bug","Dark","Dragon","Electric","Fairy","Fighting","Fire","Flying","Ghost","Grass","Ground","Ice","Normal","Poison","Psychic","Rock","Steel","Water","No-type2"]
#data = pd.read_csv('./pokemon.csv', enoding='utf-8')
type1_path="./type1/"
type2_path="./type2/"
with open('./pokemon.csv', encoding='utf-8') as file:
	lines = file.readlines()
	lines.pop(0);
	for line in lines :
		line=line[:len(line)-1]
		temp=line.split(",");
		if len(temp)==2:
			temp.append("")
		print(temp)

		#type1
		type1=type1_list.index(temp[1])
		print(type1)
		output=str(type1)+" 0 1 0 1"
		print(output)
		newf=open(type1_path+temp[0]+'.txt',"w")
		newf.write(output)

		#type2
		if temp[2]=='':
			temp[2]="No-type2"
		type2=type2_list.index(temp[2])
		print(type2)
		output2=str(type2)+" 0 1 0 1"
		print(output2)
		newf=open(type2_path+temp[0]+'.txt',"w")
		newf.write(output2)