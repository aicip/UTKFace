%% read face images and landmarks
% Author:   Zhifei Zhang
% Date:     Dec. 28, 2016
% Tested on MATLAB R2015a 
clc; clear; close all

%% load
imgPath = './Aligned&Cropped Faces/';
files = dir(fullfile([imgPath '/*.jpg']));
fid = fopen('./landmark_list.txt');
tline = fgets(fid);
landmark = zeros(1, 68*2);
landmark_list = [];
cnt = 1;
while ischar(tline)
    str = strsplit(tline, ' ');
    filename = str{1};
    for i = 2:137
        landmark(i-1) = str2double(str{i});
    end
    landmark_list(cnt).name = filename;
    landmark_list(cnt).landmark = reshape(landmark, 2, [])';
    cnt = cnt + 1;
    tline = fgets(fid);
end
fclose(fid);
if length(files) ~= length(landmark_list)
    warning('Dismatching of landmark list and image number!')
end

for loop = 1:length(landmark_list)
    file = landmark_list(loop).name;
    try
        img = imread([imgPath '/' file]);
        imshow(img)
        hold on
        landmark = landmark_list(loop).landmark;
        % Around Chin. Ear to Ear
        plot(landmark(1:17,1), landmark(1:17,2), 'bo-')
        % Line on top of nose
        plot(landmark(28:31,1), landmark(28:31,2), 'bo-')
        % left eyebrow
        plot(landmark(18:22,1), landmark(18:22,2), 'bo-')
        % Right eyebrow
        plot(landmark(23:27,1), landmark(23:27,2), 'bo-')
        % Bottom part of the nose
        plot(landmark(31:36,1), landmark(31:36,2), 'bo-')
        % Line from the nose to the bottom part above
        plot(landmark([31 36],1), landmark([31 36],2), 'bo-')
        % Left eye
        plot(landmark([37:42 37],1), landmark([37:42 37],2), 'bo-')
        % Right eye
        plot(landmark([43:48 43],1), landmark([43:48 43],2), 'bo-')
        % Lips outer part
        plot(landmark([49:60 49],1), landmark([49:60 49],2), 'bo-')
        % Lips inside part
        plot(landmark([61:68 61],1), landmark([61:68 61],2), 'bo-')
        hold off
        waitforbuttonpress
    catch
        warning(sprintf('Cannot find the file %s\n', [imgPath '/' file]))
    end
end