# Tie-Point-Matching-Between-Images-using-OpenCV
This project is a fun side project that can find tie points or common points between two images using python OpenCV.

The `cv2.xfeatures2d.SIFT_create` feature from openCV is utilized to match SIFT algorithm for finding tie points. 

We also used `scipy.signal.correlate2d` to compare the performance of both scipy and opencv features. 

One can easily use the code to find features between any two images with common features even with doctored images(styled, warped, noise hindered). 

`Point_matching_diff_space.png` shows the results on two images in different space (styled images)
<div align='center'>
<img src = 'Point_matching_diff_space.png'>
</div>


`Point_matching_same_space.png` shows the results on two images in same space (same space images)
<div align='center'>
<img src = 'Point_matching_same_space.png'>
</div>



