%% Starting point
clear
cd /
data_dir = '/Volumes/greenhouse/MRS/data/';
cd(data_dir) % path to data folder on ION Server
d = dir();
isub = [d(:).isdir];
subject_folders = {d(isub).name}';
subject_folders(ismember(subject_folders,{'.', '..'})) = []; % makes a list containing only the subject folders
% double check GannetPreInitialise for MEGAPRESS

%% subject loop
number_of_subjects = length(subject_folders); % tells the number of subjects
topLevelFolder = pwd; % set path to /Users/actioncontrollab/Documents/MATLAB/R01_data

%% creating preallocated GABA quantification output table
sz = [number_of_subjects*5, 8];
varTypes = ["string", "string", "double", "double", "double", "double", "double", "double"];
varNames = ["sID", "voxel", "A1_GABA_Cr", "A2_GABA_Cr", "Mean_GABA_Cr", "A1_FE", "A2_FE", "Mean_FE"];
GABA_quant = table('Size',sz,'VariableTypes',varTypes,'VariableNames',varNames);

for s = 1:number_of_subjects % deleted unnecessary for-loops for entering subject folders -- RR_02152023
    subject_ID = extractBefore(subject_folders{s}(5:end), '_');
    sub_folder = fullfile(topLevelFolder, filesep, subject_folders{s});
    cd(sub_folder); % cd into subject folder

    voxel_names = {'R_thal' 'L_thal' 'L_M1' 'R_M1' 'occ'};

    for v = 1:length(voxel_names)
        voxel = voxel_names(v);
        if exist(string(fullfile(sub_folder, voxel))) == 0
            continue
        elseif exist(string(fullfile(sub_folder, voxel, 'GannetFit_output')), 'dir') == 0 % to avoid redundant analyses, don't do the following if this folder is present
            cd(fullfile(voxel_names{v}, '/'))
            dat_files = dir([pwd, '/*.dat']); % list files in current directory ending in .dat
            edit_file_index = 1;
            ref_file_index = 1;

            offset = (s-1)*5;
            row = v+offset;
            GABA_quant.sID(row) = subject_ID; % adds sID and voxel to GABA_quant
            GABA_quant.voxel(row) = voxel_names{v}; 

            for f = 1:length(dat_files)

                if find(strfind(dat_files(f).name, '68TE'))
                    MEGA_dat_files(edit_file_index) = dat_files(f);
                    edit_file_index = edit_file_index + 1;
                elseif find(strfind(dat_files(f).name, '35TE'))
                    PRESS_dat_files(ref_file_index) = dat_files(f);
                    ref_file_index = ref_file_index + 1;
                end

            end % separate out PRESS scans from MEGAPRESS scans

            n = length(MEGA_dat_files);

            if exist('PRESS_dat_files')
                PRESS_Load_files = repmat(PRESS_dat_files, n, 1);
            end % replicate PRESS files so the number matches the number of MEGAPRESS files

            % GannetLoad
            for k = 1:n % k is the scan number in each voxel
                if exist('PRESS_Load_files')==0
                    MRS_struct = GannetLoad({MEGA_dat_files(k).name}); % removed 'join' specification. In 3.3.2 it's a spec in GannetPreInitialise - RR_01312024
                else
                    MRS_struct = GannetLoad({MEGA_dat_files(k).name}, {PRESS_Load_files(k).name});
                end

                % GannetFit
                MRS_struct = GannetFit(MRS_struct);
                % Save the workspace
                cd GannetFit_output
                save([subject_ID, '_', voxel_names{v}, '_', num2str(k), '_', date]);

                % adds GABA+,Cr values to GABA_quant by scan number
                if k == 1
                    GABA_quant.("A1_GABA_Cr")(row) = MRS_struct.out.vox1.GABA.ConcCr;
                    GABA_quant.("A1_FE")(row) = MRS_struct.out.vox1.GABA.FitError_Cr;
                elseif k == 2
                    GABA_quant.("A2_GABA_Cr")(row) = MRS_struct.out.vox1.GABA.ConcCr;
                    GABA_quant.("A2_FE")(row) = MRS_struct.out.vox1.GABA.FitError_Cr;
                end

                cd ../
            end

            % code for converting T1 dicoms to nifti
            %                 if isempty(dir('s*.nii*'))
            %                     dicm2nii;
            %                     % add line to save nifti into parent subject folder
            %                 end % find the MPRAGE_MGH_P2_0002 folder and pass it to dmc_to_nii if there isn't already a nii file for that subject
            cd ../
            %                 % Anatomical CoRegistration
            %                 if ~exist(fullfile(pwd,'GannetCoRegister&Segment_output'), 'dir')
            %                     mkdir GannetCoRegister&Segment_output;
            %                 end
            %                 CoReg_nii = dir('s*.nii*');
            %                 MRS_struct = GannetCoRegister(MRS_struct, {CoReg_nii.name});
            %                 MRS_struct = GannetSegment(MRS_struct);
            %                 MRS_struct = GannetQuantify(MRS_struct);
            %                 cd GannetCoRegister&Segment_output/
            %                 save([subject_ID, '_', voxel_names{v}, '_', '_CoRegister_', date]);
            %                                       cd ..//

        end
    end
    cd(data_dir)
end

% calcuating mean values for GABA_quant
GABA_quant.("Mean_GABA_Cr") = ((GABA_quant.("A1_GABA_Cr"))+(GABA_quant.("A2_GABA_Cr")))/2;
GABA_quant.("Mean_FE") = ((GABA_quant.("A1_FE"))+(GABA_quant.("A2_FE")))/2;

% importing old GABA_quant.csv
cd(data_dir)
old_GABA_quant = readtable('Typ_GABA_quant.csv');

% adding new data to table
GABA_quant = rmmissing(GABA_quant);
all_GABA_quant = vertcat(old_GABA_quant, GABA_quant);

% exporting all_GABA_quant as .csv
writetable(all_GABA_quant,'Typ_GABA_quant.csv');