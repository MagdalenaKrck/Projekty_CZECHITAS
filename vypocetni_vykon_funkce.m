% Měření výkonu a času
numIterations = 10; % Počet iterací pro výpočet průměru
timeArray = zeros(1, numIterations);
memUsageArray = zeros(1, numIterations);

for i = 1:numIterations
    beforeMem = memory; % Celková paměť před voláním funkce
    tic; % Zahájení měření času

    % Volání funkce 
    radar(inputs);

    elapsedTime = toc; % Konec měření času
    afterMem = memory; % Celková paměť po volání funkce

    % Výpočet a uložení paměti
    usedMem = afterMem.MemUsedMATLAB - beforeMem.MemUsedMATLAB;
    if usedMem < 0
        usedMem = 0; % Nastavení na nulu, pokud je hodnota záporná
    end
    memUsageArray(i) = usedMem;

    % Uložení času
    timeArray(i) = elapsedTime;
end % Konec smyčky for


% Výpočet průměrných a maximálních hodnot
averageTime = mean(timeArray);
averageMemUsage = mean(memUsageArray);
maxTime = max(timeArray);
maxMemUsage = max(memUsageArray);

% Výpis výsledků
fprintf('Average elapsed time over %d iterations: %.2f seconds\n', numIterations, averageTime);
fprintf('Average memory used by MATLAB over %d iterations: %.2f MB\n', numIterations, averageMemUsage / (1024^2));
fprintf('Max elapsed time over %d iterations: %.2f seconds\n', numIterations, maxTime);
fprintf('Max memory used by MATLAB over %d iterations: %.2f MB\n', numIterations, maxMemUsage / (1024^2));

% Vykreslení grafu pro paměť na iteraci
figure;
plot(1:numIterations, memUsageArray / (1024^2), '-o'); % Převod na MB a vykreslení
xlabel('Iteration');
ylabel('Memory Used (MB)');
title('Memory Usage per Iteration');
grid on;

% Vykreslení grafu pro čas na iteraci
figure;
plot(1:numIterations, timeArray, '-o'); % Vykreslení doby trvání v sekundách
xlabel('Iteration');
ylabel('Elapsed Time (seconds)');
title('Elapsed Time per Iteration');
grid on;

%Heat map
ranVelMat = rvMatStruct.ranVelMat; % Načtení matice z pole struktury

% Definování os
rangeVals = linspace(0, 50, size(ranVelMat, 1)); % Osa X - vzdálenost od 0 do 50
velocityVals = linspace(6, -6, size(ranVelMat, 2)); % Osa Y - rychlost od 0 do -6

% Vykreslení heat mapy
figure;
imagesc(rangeVals, velocityVals, ranVelMat'); % Transpozice matice pro správné zobrazení
set(gca, 'YDir', 'normal'); % Upraví orientaci osy Y
xlabel('Range (Distance)');
ylabel('Velocity');
title('Heat Map of Radar Data (ranVelMat)');
colorbar; % Zobrazení barevné škály pro intenzitu

% Nastavení barevné mapy na 'jet' pro požadovaný přechod barev
colormap('jet');

% Nastavení rozsahu intenzity, pokud je to relevantní
caxis([2000, 6000]);

ranVelMat = rvMatStruct.ranVelMat; % Načtení matice z pole struktury

% Definování os
rangeVals = linspace(0, 50, size(ranVelMat, 1)); % Osa X - vzdálenost od 0 do 50
velocityVals = linspace(0, -6, size(ranVelMat, 2)); % Osa Y - rychlost od 0 do -6

% Najdi maximální intenzitu a její indexy
[maxIntensity, linearIndex] = max(ranVelMat(:));
[row, col] = ind2sub(size(ranVelMat), linearIndex);

% Převeď indexy na skutečné hodnoty vzdálenosti a rychlosti
detectedRange = rangeVals(row);
detectedVelocity = velocityVals(col);