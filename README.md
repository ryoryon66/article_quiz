英文を入力すると，spacyを用いて自動で冠詞クイズ，時制クイズを作成するflask製web app.
以前はheroku上で動かしていたが，現在は無料枠の消失で止まっているので気が向いたら別のクラウドにデプロイしなおしたい．

EC2で動かしています． http://54.147.147.151:5000/

# 入出力例
## 入力
> The iMac G4 is an all-in-one personal computer produced by Apple Computer from January 2002 to August 2004. It comprises a hemispheric base that holds the computer components and a flatscreen liquid-crystal display (LCD) mounted above. The iMac G3, first released in 1998, helped save Apple from bankruptcy. Development of the iMac G4 took roughly two years, with Apple's designers exploring multiple ways of marrying the display screen with the computer components. Its shape was inspired by a sunflower, with the display connected to the base via an adjustable stainless-steel arm that allows the monitor to be freely tilted and swiveled. The product was a critical and commercial success for Apple, selling more than 1.3 million units in its first year, and it was updated with faster components and larger displays before being replaced by the iMac G5 in September 2004. The machine is held in the collections of multiple museums, including the Museum of Modern Art and Museums Victoria.



 ## 出力（冠詞クイズ）
> (Q1) iMac G4 is  (Q2) all-in-one personal computer produced by  (Q3) Apple Computer from  (Q4) January 2002 to  (Q5) August 2004. It comprises  (Q6) hemispheric base that holds  (Q7) computer components and  (Q8) flatscreen liquid-crystal display ( (Q9) LCD) mounted above.  (Q10) iMac G3, first released in 1998, helped save  (Q11) Apple from  (Q12) bankruptcy.  (Q13) Development of  (Q14) iMac G4 took  (Q15) roughly two years, with  (Q16) Apple's designers exploring  (Q17) multiple ways of marrying  (Q18) display screen with  (Q19) computer components. Its shape was inspired by  (Q20) sunflower, with  (Q21) display connected to  (Q22) base via  (Q23) adjustable stainless-steel arm that allows  (Q24) monitor to be freely tilted and swiveled.  (Q25) product was  (Q26) critical and commercial success for  (Q27) Apple, selling  (Q28) more than 1.3 million units in its first year, and it was updated with  (Q29) faster components and  (Q30) larger displays before being replaced by  (Q31) iMac G5 in  (Q32) September 2004.  (Q33) machine is held in  (Q34) collections of  (Q35) multiple museums, including  (Q36) Museum of  (Q37) Modern Art and Museums Victoria.
 


## 出力（時制クイズ）
> The iMac G4 (Q1  is) an all - in - one personal computer (Q2  produce) by Apple Computer from January 2002 to August 2004 . It (Q3  comprise) a hemispheric base that (Q4  hold) the computer components and a flatscreen liquid - crystal display ( LCD ) (Q5  mount) above . The iMac G3 , first (Q6  release) in 1998 , (Q7  help) (Q8  save) Apple from bankruptcy . Development of the iMac G4 (Q9  take) roughly two years , with Apple 's designers (Q10  explore) multiple ways of (Q11  marry) the display screen with the computer components . Its shape (Q12  was) (Q13  inspire) by a sunflower , with the display (Q14  connect) to the base via an adjustable stainless - steel arm that (Q15  allow) the monitor to (Q16  be) freely (Q17  tilt) and (Q18  swivel) . The product (Q19  was) a critical and commercial success for Apple , (Q20  sell) more than 1.3 million units in its first year , and it (Q21  was) (Q22  update) with faster components and larger displays before (Q23  being) (Q24  replace) by the iMac G5 in September 2004 . The machine (Q25  is) (Q26  hold) in the collections of multiple museums , (Q27  include) the Museum of Modern Art and Museums Victoria . 
