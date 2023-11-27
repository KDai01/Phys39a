data = readmatrix("Initial sine test.txt");
data = data';

baseTemp = data(1, :);
pwm = data(2, :);
time = data(3, :);
setTemp = data(4, :);

%Set bounds on x-axis for plots
xStart = 22; % 
xEnd = 1133; % 

hold on;

%Plot the base temperature
plot(time(xStart:end),baseTemp(xStart:end),'DisplayName','Base Temp');

%Plot the set temperature
plot(time(xStart:end),setTemp(xStart:end),'DisplayName','Set Temp');


%Plot all the temperatures along the rod
%for i = 5:9
%    plot(time(xStart:end),data(i,xStart:end),'DisplayName',replace('Temp REPLACE','REPLACE',int2str(i-4)));
%end

xlabel('Time (s)');
ylabel('Temp (C)');
title('Base Temp Response vs Time');
%legend('Set Temp','Temp1','Temp2','Temp3','Temp4','Temp5','Location','best');
legend('Base Temp', 'Set Temp','Location','best');

hold off;
