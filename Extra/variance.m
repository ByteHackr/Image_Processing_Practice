% grayImage = imread('img_tamp_1.bmp');
grayImage = imread('/home/sandipan/Desktop/IMG/gr.png');
subplot(1,3,1);
fontSize = 20;
set(gcf, 'Units', 'Normalized', 'Outerposition', [0, 0, 1, 1]);
stdImage = stdfilt(grayImage, true(3));
varianceImage = stdImage .^1.5;
imshow(varianceImage, []);
