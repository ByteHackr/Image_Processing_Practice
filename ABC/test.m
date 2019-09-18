clc;
clearvars;
close all;
workspace;
fontSize = 16;
folder = fullfile(matlabroot, 'parrotsec.png');
if ~exist(folder, 'dir')
  folder = [];
end
baseFileName = 'beach_wood_orig.jpg';
fullFileName = fullfile(folder, baseFileName);
grayImage = imread(fullFileName);
[rows columns numberOfColorBands] = size(grayImage)
subplot(2, 2, 1);
imshow(grayImage, []);
title('Original Grayscale Image', 'FontSize', fontSize);
set(gcf, 'Position', get(0,'Screensize')); 
set(gcf,'name','Image Analysis Demo','numbertitle','off') 
medianFilterFunction = @(theBlockStructure) median(theBlockStructure.data(:)) * ones(size(theBlockStructure.data), class(theBlockStructure.data));
blockSize = [8 8];
blockyImage8 = blockproc(single(grayImage), blockSize, medianFilterFunction); % Works.
[rows columns] = size(blockyImage8);
subplot(2, 2, 2);
imshow(blockyImage8, []);
caption = sprintf('Block Median Image\n32 blocks. Input block size = 8, output block size = 8\n%d rows by %d columns', rows, columns);
title(caption, 'FontSize', fontSize);
meanFilterFunction = @(theBlockStructure) mean2(theBlockStructure.data(:)) * ones(2,2, class(theBlockStructure.data));
blockSize = [4 4];
blockyImage64 = blockproc(grayImage, blockSize, meanFilterFunction);
[rows columns] = size(blockyImage64);
subplot(2, 2, 3);
imshow(blockyImage64, []);
caption = sprintf('Block Mean Image\n64 blocks. Input block size = 4, output block size = 2\n%d rows by %d columns', rows, columns);
title(caption, 'FontSize', fontSize);
blockSize = [8 8];
StDevFilterFunction = @(theBlockStructure) std(double(theBlockStructure.data(:)));
blockyImageSD = blockproc(grayImage, blockSize, StDevFilterFunction);
[rows columns] = size(blockyImageSD);
subplot(2, 2, 4);
imshow(blockyImageSD, []);
title('Standard Deviation Filtered Image', 'FontSize', fontSize);
caption = sprintf('Block Standard Deviation Filtered Image\n32 blocks. Input block size = 8, output block size = 1\n%d rows by %d columns', rows, columns);
title(caption, 'FontSize', fontSize);