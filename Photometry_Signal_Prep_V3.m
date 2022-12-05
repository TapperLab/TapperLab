%Run this section first to create dat variable.%
clear all
dat = []; %Col1 = time, Col2 = 465nm, Col3 = 405nm
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%Calculate DF/F0
x = dat(:,2);
y = dat(:,3); 

reg = polyfit(y, x, 1);

a = reg(1);
b = reg(2);

controlFit = a.*y + b; %This is the fitted control signal

normDat = (x - controlFit)./ controlFit;%this gives dF/F using 465 channel (dat1) and fitted 405 channel (controlFit).
normDat = normDat * 100; %Scales df/f by a factor of 100 as in Doric software.

clear a b reg x y

%Create Table for Stacked Plot
output_table = table(dat(:,1),normDat,dat(:,2),dat(:,3),controlFit);
output_table.Properties.VariableNames = {'Time','DF/F0','465nm','405nm','405nm Fitted'};

%Create Stacked Plot
xaxis = output_table(:,1);

s = stackedplot(output_table,{'DF/F0','465nm','405nm'},'XVariable','Time');
s.LineProperties(1).Color = 'b';
s.LineProperties(2).Color = 'g';
s.LineProperties(3).Color = 'm';
s.XLabel = {'Time (s)'};

clear dat normDat xaxis controlFit