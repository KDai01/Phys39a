dataLow = readmatrix("K=13.35_T=35.txt");
dataLow = dataLow';

dataMed = readmatrix("K=20.57_T=35.txt");
dataMed = dataMed';

dataHigh = readmatrix("K=31.15_T=35.txt");
dataHigh = dataHigh';

t = linspace(0,180,100);
y = zeros(length(t),1) + 35;

hold on;

plot(dataLow(3, 20:end), dataLow(1, 20:end),'DisplayName','Low K');
plot(dataMed(3, 20:end), dataMed(1, 20:end),'DisplayName','Medium K');
plot(dataHigh(3, 20:end), dataHigh(1, 20:end),'DisplayName','High K');
plot(t,y,'DisplayName','Set T');

xlabel('Time (s)');
ylabel('Temp (C)');
title('Temp vs Time');
legend('Low K', 'Medium K', 'High K', 'Set T');

hold off;
