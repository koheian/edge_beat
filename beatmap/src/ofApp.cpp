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
}

//--------------------------------------------------------------
void ofApp::update(){

}

//--------------------------------------------------------------
void ofApp::draw(){
    color_image.draw(0,0);
    gray_image.draw(100, 100);
    canny_image.draw(200, 200);
    ofDrawBitmapStringHighlight("Everything works!", 20, 20);
    
    ofDrawCircle(circle_x, circle_y, 10);
    
    canny_pixels = canny_image.getPixels();
    
    for (int i=0; i<image_width; i++) {
        pixel_array[i] = canny_pixels[image_width*row_number + i];
    }

    img.setFromPixels(canny_pixels);
    
    circle_x = (circle_x + 5) % 1024;
    circle_y = (circle_y + 2) % 768;
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
