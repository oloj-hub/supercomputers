BEGIN{
t=0
read_flag=0
N=1
}

{
if($4=="new"){
 if($5=="total"){
  N=$7
}
}
if(read_flag==2){
 if($1>0){
  t=$3/N
  print $1,t
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
}

