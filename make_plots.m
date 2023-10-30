dataLow = readmatrix("Kp=14.5_Ki=0.06started_high_T_Tset=35.txt");
dataLow = dataLow';

dataMed = readmatrix("Kp=15_Ki=0.23_second_data.txt");
dataMed = dataMed';

dataMed2 = readmatrix("Kp=15_Ki=1.14_thirdTrial.txt");
dataMed2 = dataMed2';

dataHigh = readmatrix("Kp=15.1_Ki=2.00_fourth_trial.txt");
dataHigh = dataHigh';

t = linspace(0,180,100);
y = zeros(length(t),1) + 35;

hold on;

plot(dataLow(3, 20:end), dataLow(1, 20:end),'DisplayName','Ki=0.06');
plot(dataMed(3, 20:end), dataMed(1, 20:end),'DisplayName','Ki=0.23');
plot(dataMed2(3, 20:end), dataMed(1, 20:end),'DisplayName','Ki=1.14');
plot(dataHigh(3, 20:end), dataHigh(1, 20:end),'DisplayName','Ki=2.00');
plot(t,y,'DisplayName','Set T');

xlabel('Time (s)');
ylabel('Temp (C)');
title('Temp vs Time, Kp ~ 15');
legend('Ki=0.06', 'Ki=0.23', 'Ki=1.14','Ki=2.00', 'Set T');

hold off;
