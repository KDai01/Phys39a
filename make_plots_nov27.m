data = readmatrix("Initial sine test.txt");
data = data';

baseTemp = data(1, :);
pwm = data(2, :);
time = data(3, :);
setTemp = data(4, :);

%Set bounds on x-axis; steady-state occurs ~1056-1129
xStart = 22; % minimum 1, t=30 secs; control starts at 22
xEnd = 1133; % maximum 1794, t=1918 secs; control ends at 1129

hold on;

%Plot the base temperature
plot(time(xStart:end),baseTemp(xStart:end),'DisplayName','Set Temp');

%Plot all the temperatures along the rod
%for i = 5:9
%    plot(time(xStart:end),data(i,xStart:end),'DisplayName',replace('Temp REPLACE','REPLACE',int2str(i-4)));
%end

xlabel('Time (s)');
ylabel('Temp (C)');
title('Temp vs Time along rod');
legend('Set Temp','Temp1','Temp2','Temp3','Temp4','Temp5','Location','best');

hold off;
