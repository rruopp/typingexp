% % load individual data and save into a table (abanddoned given differences
% % in folder structures for now
% filenames = dir('s*');
% Thal_MRS_data = table();
% for i = 1:size(filenames,1)
%     disp(filenames(i).name)
%     sID = extractBetween(filenames(i).name, 'S', '_');
%     Tha_MRS_data.sID = sID{1};
%     load([filenames(i).name, 'Thal_L/GannetFit_output/','s*thal_1*'])
% end

%% Plot Diff spectra
f = figure;
f.Position = [56 137 600 400];

data_dir = '/Volumes/greenhouse/MRS/data/';

load(('/Volumes/greenhouse/MRS/data/Typ_s263_02272024/L_thal/GannetFit_output/s263_L_thal_1_09-May-2025.mat'))
plot(MRS_struct.spec.freq, real(MRS_struct.spec.vox1.GABAGlx.diff), ...
    'color',[0.8359, 0.1523, 0.1562], ...
    'LineWidth',2)
set(gca, 'XDir','reverse')
xlim([0 3.85]);
hold on
% 
load(fullfile('/Volumes/greenhouse/MRS/data/Typ_s263_02272024/L_thal/GannetFit_output/s263_L_thal_2_09-May-2025.mat'))
y_data_adjusted = real(MRS_struct.spec.vox1.GABAGlx.diff)-.002;
plot(MRS_struct.spec.freq, y_data_adjusted, ...
    'color',[0.8359, 0.1523, 0.1562], ...
    'LineWidth',2)
set(gca, 'XDir','reverse')
xlim([0 3.85]);
%%
load(fullfile('/Volumes/greenhouse/MRS/data/Typ_s209_11132023/L_thal/GannetFit_output/s209_L_thal_1_09-May-2025.mat'))
y_data_adjusted = real(MRS_struct.spec.vox1.GABAGlx.diff)-.004;
plot(MRS_struct.spec.freq, y_data_adjusted, ...
    'color',[0.1211, 0.4648, 0.7031], ...
    'LineWidth',2)
set(gca, 'XDir','reverse')
xlim([0 3.85]);
%
load(fullfile('/Volumes/greenhouse/MRS/data/Typ_s209_11132023/L_thal/GannetFit_output/s209_L_thal_2_09-May-2025.mat'))
y_data_adjusted = real(MRS_struct.spec.vox1.GABAGlx.diff)-.006;
plot(MRS_struct.spec.freq, y_data_adjusted, ...
    'color',[0.1211, 0.4648, 0.7031], ...
    'LineWidth',2)
set(gca, 'XDir','reverse')
xlim([0 3.85]);
%%
load(fullfile('/Volumes/greenhouse/MRS/data/Typ_s261_11202023/L_thal/GannetFit_output/s261_L_thal_1_09-May-2025.mat'))
y_data_adjusted = real(MRS_struct.spec.vox1.GABAGlx.diff)-.008;
plot(MRS_struct.spec.freq, y_data_adjusted, 'Color', '#ffd700', 'LineWidth',2)
set(gca, 'XDir','reverse')
xlim([0 3.85]);   
%
load(fullfile('/Volumes/greenhouse/MRS/data/Typ_s261_11202023/L_thal/GannetFit_output/s261_L_thal_2_09-May-2025.mat'))
y_data_adjusted = real(MRS_struct.spec.vox1.GABAGlx.diff)-.01;
plot(MRS_struct.spec.freq, y_data_adjusted, 'Color','#ffd700', 'LineWidth',2)
set(gca, 'XDir','reverse')
xlim([0 3.85]);
%%
load(fullfile('/Volumes/greenhouse/MRS/data/Typ_s262_01312024/L_thal/GannetFit_output/s262_L_thal_1_09-May-2025.mat'))
y_data_adjusted = real(MRS_struct.spec.vox1.GABAGlx.diff)-.012;
plot(MRS_struct.spec.freq, y_data_adjusted, 'k', 'LineWidth',2)
set(gca, 'XDir','reverse')
xlim([0 3.85]); 
%
load(fullfile('/Volumes/greenhouse/MRS/data/Typ_s262_01312024/L_thal/GannetFit_output/s262_L_thal_2_09-May-2025.mat'))
y_data_adjusted = real(MRS_struct.spec.vox1.GABAGlx.diff)-.014;
plot(MRS_struct.spec.freq, y_data_adjusted, 'k', 'LineWidth',2)
set(gca, 'XDir','reverse')
xlim([0 3.85]); 
%%

xlabel('ppm', 'FontSize', 20);
ylabel('A.U.', 'FontSize', 20);
ax = gca;
ax.FontSize = 25;
set(ax, 'Color', 'none');

legend('Subject 1','','Subject 2','', 'Subject 3','', 'Subject 4', 'Location','southeast')
set(legend ,'color','w', 'TextColor', 'k')

set(gca, 'Color','none', 'XColor','k', 'YColor','k')

path = '/Users/rubi/Desktop/Github/typingexp/MRS/figures/';
exportgraphics(gcf, fullfile(path, 'l_thal_rawspectra_lightposter.png'), 'Resolution', 300)