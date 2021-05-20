BEGIN{
t=0
read_flag=0
}

{
if(read_flag==2){
 if($1>0){
  t=t+$2
 }
 if($1==2000){
  read_flag=0  
 }
}
if($2=="Temp"){
 read_flag=read_flag+1
}
}
END{
t=t/5
print t
}

