#pragma once

#include "ofMain.h"
#include "ofxOpenCv.h"
#include "ofxOsc.h"

#define HOST "127.0.0.1"
#define PORT 12345


class ofApp : public ofBaseApp{

	public:
		void setup();
		void update();
		void draw();

		void keyPressed(int key);
		void keyReleased(int key);
		void mouseMoved(int x, int y );
		void mouseDragged(int x, int y, int button);
		void mousePressed(int x, int y, int button);
		void mouseReleased(int x, int y, int button);
		void mouseEntered(int x, int y);
		void mouseExited(int x, int y);
		void windowResized(int w, int h);
		void dragEvent(ofDragInfo dragInfo);
		void gotMessage(ofMessage msg);
    void oscSendOnePixel();
		
    ofImage img;
    ofPixels input_pixels;
    ofxCvColorImage color_image;
    ofxCvGrayscaleImage gray_image;
    ofxCvGrayscaleImage canny_image;
    ofPixels canny_pixels;
    ofPixels output_img;
    ofxOscSender osc_sender;

    const int image_width = 512;
    const int image_height = 512;
    double min_th = 60.0;
    double max_th = 150.0;
    
    unsigned int pixel_array[512];
    int row_number = 100; // tekitou
    
    // テストとして円を飛ばすときの座標
    int circle_x = 0;
    int circle_y = 0;
    
    // 定期的に関数を呼ぶための変数
    unsigned int elasped_time = 0;
    unsigned const int interval = 20000;
    
    // OSCで送っているピクセルを描画するための座標
    const int CANNY_IMG_X = 200;
    const int CANNY_IMG_Y = 200;
    int pixel_x = 0;
    int pixel_y = 0;
};
