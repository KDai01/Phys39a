dataLow = readmatrix("Kp=14.7_Ki=0.07_trial1.txt");
dataLow = dataLow';

dataMed = readmatrix("Kp=15_Ki=0.23_second_data.txt");
dataMed = dataMed';

dataMed2 = readmatrix("Kp=15_Ki=1.14_thirdTrial.txt");
dataMed2 = dataMed2';

dataHigh = readmatrix("Kp=15.1_Ki=2.00_fourth_trial.txt");
dataHigh = dataHigh';

dataZMOpen = readmatrix("manual_test.txt");
dataZMOpen = dataZMOpen';

dataZNClosed = readmatrix("dataZNClosed.txt");
dataZNClosed = dataZNClosed';

t = linspace(0,1000,1000);
y = zeros(length(t),1) + 35;

t2 = linspace(550,1000,100);
y2 = zeros(length(t2),1) + 28.1;
y3 = zeros(length(t2),1) + 30.7;

hold on;

% plot(dataLow(3, 20:end), dataLow(1, 20:end),'DisplayName','Ki=0.07');
% plot(dataMed(3, 20:end), dataMed(1, 20:end),'DisplayName','Ki=0.23');
% plot(dataMed2(3, 20:end), dataMed2(1, 20:end),'DisplayName','Ki=1.14');
% plot(dataHigh(3, 20:end), dataHigh(1, 20:end),'DisplayName','Ki=2.00');
% plot(t,y,'DisplayName','Set T');

plot(dataZNClosed(3, 650:end), dataZNClosed(1, 650:end));

xlabel('Time (s)');
ylabel('Temp (C)');
title('Temp vs Time, Kp ~ 172');

% ylabel('Temp (C)');
% title('Temp vs Time, Kp ~ 15');
% legend('Ki=0.06', 'Ki=0.23', 'Ki=1.14','Ki=2.00', 'Set T');

hold off;
