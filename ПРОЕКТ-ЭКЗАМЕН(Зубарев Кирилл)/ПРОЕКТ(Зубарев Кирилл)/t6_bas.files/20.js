<!--íà÷àëî ñöåíàðèÿ
function test(){
answ="";
with(document){
answ+=control(res.charAt(0), forms[0].q1[0], forms[0].q1[1], forms[0].q1[2], forms[0].q1[3]) ?"1":"0";
answ+=control(res.charAt(1), forms[0].q2[0], forms[0].q2[1], forms[0].q2[2], forms[0].q2[3]) ?"1":"0";
answ+=control(res.charAt(2), forms[0].q3[0], forms[0].q3[1], forms[0].q3[2], forms[0].q3[3]) ?"1":"0";
answ+=control(res.charAt(3), forms[0].q4[0], forms[0].q4[1], forms[0].q4[2], forms[0].q4[3]) ?"1":"0";


showResult();
}
}
function control(k,f1,f2,f3,f4){
if(k==1&&f1.checked)return true;
if(k==2&&f2.checked)return true;
if(k==3&&f3.checked)return true;
if(k==4&&f4.checked)return true;
return false;
}
function showResult(){
    var nok=0;
    var i; var s;
for(i=0; i<answ.length; i++)
   nok+=answ.charAt(i)=='1'?1:0;

document.forms[0].S1.value="Количество правильных ответов "+nok+" из "+answ.length+".";
with(document.forms[0]){
     if (answ.charAt(0)=="1") {T1.value="  :-))"}
        else {T1.value="  :-(("};
     if (answ.charAt(1)=="1") {T2 .value="  :-))"}
        else {T2.value="  :-(("};
     if (answ.charAt(2)=="1") {T3.value="  :-))"}
        else {T3.value="  :-(("};
     if (answ.charAt(3)=="1") {T4.value="  :-))"}
        else {T4.value="  :-(("};
     
     


}
}
<!--êîíåö ñöåíàðèÿ-->
