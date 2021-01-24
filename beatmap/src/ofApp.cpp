#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup(){
    color_image.allocate(image_width, image_height);
    canny_image.allocate(image_width, image_height);
//    img.load("input.jpg");
    ofLoadImage(input_pixels,"input.jpg");
    color_image.setFromPixels(input_pixels);
    color_image.resize(image_width, image_height);
    gray_image = color_image;
    cvCanny(color_image.getCvImage(), canny_image.getCvImage(), min_th, max_th);
    
    output_img.allocate(image_width, image_height,OF_IMAGE_GRAYSCALE);
    
    osc_sender.setup(HOST, PORT);
    
    pixel_x = CANNY_IMG_X;
    pixel_y = CANNY_IMG_Y + row_number;
}

//--------------------------------------------------------------
void ofApp::update(){

}

//--------------------------------------------------------------
void ofApp::draw(){
    
    ofSetColor(255);
    color_image.draw(0,0);
    gray_image.draw(100, 100);
    canny_image.draw(CANNY_IMG_X, CANNY_IMG_Y);
    
    ofDrawBitmapStringHighlight("Everything works!", 20, 20);
    
    circle_x = pixel_x;
    circle_y = pixel_y;
    ofSetColor(255, 0, 0);
    ofDrawCircle(circle_x, circle_y, 5);
    
    canny_pixels = canny_image.getPixels();
    
    // 定期的にoscSendOnePixel()を呼ぶ
    elasped_time = ofGetElapsedTimeMicros();
    if (elasped_time >= interval) {
        oscSendOnePixel();
        ofResetElapsedTimeCounter();
    }
    
    img.setFromPixels(canny_pixels);
    
//    circle_x = (circle_x + 5) % 1024;
//    circle_y = (circle_y + 2) % 768;
}

//--------------------------------------------------------------
void ofApp::keyPressed(int key){

}

//--------------------------------------------------------------
void ofApp::keyReleased(int key){

}

//--------------------------------------------------------------
void ofApp::mouseMoved(int x, int y ){

}

//--------------------------------------------------------------
void ofApp::mouseDragged(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mousePressed(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mouseReleased(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mouseEntered(int x, int y){

}

//--------------------------------------------------------------
void ofApp::mouseExited(int x, int y){

}

//--------------------------------------------------------------
void ofApp::windowResized(int w, int h){

}

//--------------------------------------------------------------
void ofApp::gotMessage(ofMessage msg){

}

//--------------------------------------------------------------
void ofApp::dragEvent(ofDragInfo dragInfo){ 

}

void ofApp::oscSendOnePixel(){
    const int TH_ONOFF = 200;
    const int STAT_ON = 144;
    const int STAT_OFF = 128;
    const int VELO_ON = 80;
    const int VELO_OFF = 0;
    ofxOscMessage m_velocity, m_status;
    m_velocity.setAddress("/velo");
    m_status.setAddress("/stat");
    
    static int i = 0;
    pixel_x = CANNY_IMG_X + i;
    pixel_array[i] = canny_pixels[image_width*row_number + i];
    i++;
    if (i >= image_width) {
        i = 0;
        row_number = (row_number + 1) % image_height;
    }
    
    /// ピクセルの値取得を確認 ///
    std::cout << std::to_string(pixel_array[i]) + ",";
    std::cout << std::to_string(i) << std::endl;
    
    /// OSC送信 ///
    if (pixel_array[i] >= TH_ONOFF) { // 200はnote on/off判定のしきい値。いまは適当。
        m_status.addIntArg(STAT_ON);
        m_velocity.addIntArg(VELO_ON);
    } else {
        m_status.addIntArg(STAT_OFF);
        m_velocity.addIntArg(VELO_OFF);
    }
    
    osc_sender.sendMessage(m_velocity);
    osc_sender.sendMessage(m_status);
    
//    m_velocity.addStringArg(std::to_string(pixel_array[i]));
//    osc_sender.sendMessage(m_velocity);
}
