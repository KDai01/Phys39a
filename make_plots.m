dataLow = readmatrix("K=13.35_T=35.txt");
dataLow = dataLow';

dataMed = readmatrix("K=20.57_T=35.txt");
dataMed = dataMed';

dataHigh = readmatrix("K=31.15_T=35.txt");
dataHigh = dataHigh';


dataHigh2 = readmatrix("Kp=20_Ki=1_T=35.txt");
dataHigh2 = dataHigh2';

dataMed2 = readmatrix("Kp=20.41_Ki=0.3947_T=35.txt");
dataMed2 = dataMed2';

dataLow2 = readmatrix("Kp=19.92_Ki=0.04885_T=35.txt");
dataLow2 = dataLow2';


data7 = readmatrix("Kp=11.75_Ki=0.3994_T=35.txt");
data7 = data7';

data8 = readmatrix("Kp=12.23_Ki=0.2031_T=35.txt");
data8 = data8';

data9 = readmatrix("Kp=12.23_Ki=0.2872_T=35.txt");
data9 = data9';

t = linspace(0,180,100);
y = zeros(length(t),1) + 35;

choosePlot = 3; % CHANGE THIS to select plot
hold on;

%Plot Kp
if choosePlot == 1
plot(dataLow(3, 20:end), dataLow(1, 20:end),'DisplayName','Kp=13.35');
plot(dataMed(3, 20:end), dataMed(1, 20:end),'DisplayName','Kp=20.57');
plot(dataHigh(3, 20:end), dataHigh(1, 20:end),'DisplayName','Kp=31.15');
title('Temp vs Time, P control');
end

%Plot Ki, Kp=20
if choosePlot == 2
plot(dataHigh2(2, :), dataHigh2(1, :),'DisplayName','Ki=1');
plot(dataMed2(2, :), dataMed2(1, :),'DisplayName','Ki=0.4');
plot(dataLow2(2, :), dataLow2(1, :),'DisplayName','Ki=0.05');
title('Temp vs Time, PI control, Kp = 20');
end

%Plot Ki, Kp=12
if choosePlot == 3
    plot(data7(2, :), data7(1, :),'DisplayName','Ki=0.4');
    plot(data8(2, :), data8(1, :),'DisplayName','Ki=0.2');
    plot(data9(2, :), data9(1, :),'DisplayName','Ki=0.28');
    title('Temp vs Time, PI control, Kp = 12');
end


plot(t,y,'DisplayName','Set T');
xlabel('Time (s)');
ylabel('Temp (C)');
legend();

hold off;

