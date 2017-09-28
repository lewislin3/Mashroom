[response, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22 ]=textread('Mushroom.txt','%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s','delimiter',',');
attribute = table (a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22);
att = table (a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22);
len = 1;
label1 = [a1(len:len+1623), a2(len:len+1623), a3(len:len+1623), a4(len:len+1623), a5(len:len+1623), a6(len:len+1623), a7(len:len+1623), a8(len:len+1623), a9(len:len+1623), a10(len:len+1623), a11(len:len+1623), a12(len:len+1623), a13(len:len+1623), a14(len:len+1623), a15(len:len+1623), a16(len:len+1623), a17(len:len+1623), a18(len:len+1623), a19(len:len+1623), a20(len:len+1623), a21(len:len+1623), a22(len:len+1623)];
len = len + 1624;
label2 = [a1(len:len+1623), a2(len:len+1623), a3(len:len+1623), a4(len:len+1623), a5(len:len+1623), a6(len:len+1623), a7(len:len+1623), a8(len:len+1623), a9(len:len+1623), a10(len:len+1623), a11(len:len+1623), a12(len:len+1623), a13(len:len+1623), a14(len:len+1623), a15(len:len+1623), a16(len:len+1623), a17(len:len+1623), a18(len:len+1623), a19(len:len+1623), a20(len:len+1623), a21(len:len+1623), a22(len:len+1623)];
len = len + 1624;
label3 = [a1(len:len+1623), a2(len:len+1623), a3(len:len+1623), a4(len:len+1623), a5(len:len+1623), a6(len:len+1623), a7(len:len+1623), a8(len:len+1623), a9(len:len+1623), a10(len:len+1623), a11(len:len+1623), a12(len:len+1623), a13(len:len+1623), a14(len:len+1623), a15(len:len+1623), a16(len:len+1623), a17(len:len+1623), a18(len:len+1623), a19(len:len+1623), a20(len:len+1623), a21(len:len+1623), a22(len:len+1623)];
len = len + 1624;
label4 = [a1(len:len+1623), a2(len:len+1623), a3(len:len+1623), a4(len:len+1623), a5(len:len+1623), a6(len:len+1623), a7(len:len+1623), a8(len:len+1623), a9(len:len+1623), a10(len:len+1623), a11(len:len+1623), a12(len:len+1623), a13(len:len+1623), a14(len:len+1623), a15(len:len+1623), a16(len:len+1623), a17(len:len+1623), a18(len:len+1623), a19(len:len+1623), a20(len:len+1623), a21(len:len+1623), a22(len:len+1623)];
len = len + 1624;
label5 = [a1(len:len+1623), a2(len:len+1623), a3(len:len+1623), a4(len:len+1623), a5(len:len+1623), a6(len:len+1623), a7(len:len+1623), a8(len:len+1623), a9(len:len+1623), a10(len:len+1623), a11(len:len+1623), a12(len:len+1623), a13(len:len+1623), a14(len:len+1623), a15(len:len+1623), a16(len:len+1623), a17(len:len+1623), a18(len:len+1623), a19(len:len+1623), a20(len:len+1623), a21(len:len+1623), a22(len:len+1623)];
atable = table (response, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22);
vector = [response, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22];
attribute1 = table (a1(1625:8120), a2(1625:8120), a3(1625:8120), a4(1625:8120), a5(1625:8120), a6(1625:8120), a7(1625:8120), a8(1625:8120), a9(1625:8120), a10(1625:8120), a11(1625:8120), a12(1625:8120), a13(1625:8120), a14(1625:8120), a15(1625:8120), a16(1625:8120), a17(1625:8120), a18(1625:8120), a19(1625:8120), a20(1625:8120), a21(1625:8120), a22(1625:8120));
attribute2 = table ([a1(1:1624);a1(3249:8120)], [a1(1:1624);a1(3249:8120)], [a1(1:1624);a1(3249:8120)], [a1(1:1624);a1(3249:8120)], [a1(1:1624);a1(3249:8120)], [a1(1:1624);a1(3249:8120)], [a1(1:1624);a1(3249:8120)], a8(1625:8120), a9(1625:8120), a10(1625:8120), a11(1625:8120), a12(1625:8120), a13(1625:8120), a14(1625:8120), a15(1625:8120), a16(1625:8120), a17(1625:8120), a18(1625:8120), a19(1625:8120), a20(1625:8120), a21(1625:8120), a22(1625:8120));

%k-fold
att = table (a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22);
att(1:1624,:) = [];
SVM1 = fitcsvm(att,response(1625:8120));
label = predict(SVM1,label1);
c1 = confusionmat(response(1:1624),label);

att = table (a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22);
att(1625:3248,:) = [];
SVM2 = fitcsvm(att,[response(1:1624);response(3249:8120)]);
label = predict(SVM2,label2);
c2 = confusionmat(response(1625:3248),label);

att = table (a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22);
att(3249:4872,:) = [];
SVM3 = fitcsvm(att,[response(1:3248);response(4873:8120)]);
label = predict(SVM3,label3);
c3 = confusionmat(response(3249:4872),label);

att = table (a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22);
att(4873:6496,:) = [];
SVM4 = fitcsvm(att,[response(1:4872);response(6497:8120)]);
label = predict(SVM4,label4);
c4 = confusionmat(response(4873:6496),label);

att = table (a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22);
att(6497:8120,:) = [];
SVM5 = fitcsvm(att,response(1:6496));
label = predict(SVM5,label5);
c5 = confusionmat(response(6497:8120),label);

confusion = c1 + c2 + c3 + c4 + c5;
disp(confusion);
% 0.991625