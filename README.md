# Python_OpenCV
Python OpenCV learning

Learning OpenCV in Python by the official tutorials.

- - -
### Sublime Text3 设置Python3为默认编译系统
`Tools -> Build System -> New Build System`

    {
     "cmd": ["usr/bin/python3", "$file"], 
     "selector": "source.python", 
      "file_regex": "file \"(...*?)\", line ([0-9]+)"
    }
    
Saved As Python3.sublime-build.

## Tutorials Notes      
---
2017-02-24      

#### Erode & Dilate
**Erode**:      `erosion = cv2.erode(img,kernel,iterations = 1)`        
就像土壤侵蚀一样，这个操作会把前景物体的边界腐蚀掉（但是前景仍然是白色）.       
前景物体会变小，整幅图像的白色区域会减少。       
这对于去除白噪声很有用，也可以用来断开两个连在一块的物体等。

**Dilate**:     `dilation = cv2.dilate(img,kernel,iterations = 1)`      
与腐蚀相反，这个操作会增加图像中的白色区域（前景）。      
一般在去噪声时先用腐蚀再用膨胀。因为腐蚀在去掉白噪声的同时，也会使前景对象变小。        
所以我们再对他进行膨胀。这时噪声已经被去除了，不会再回来了，但是前景还在并会增加。       
膨胀也可以用来连接两个分开的物体。

#### Morph Open & Close
**Morph Open**:      `opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)`      
先进性腐蚀再进行膨胀就叫做开运算。就像我们上面介绍的那样，它被用来去除噪声。

**Morph Close**:    `closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)`      
先膨胀再腐蚀。它经常被用来填充前景物体中的小洞，或者前景物体上的小黑点。        

#### Gradient, Tophat & Blackhat
**Gradient**:       `gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)`      
是一幅图像膨胀与腐蚀的差。结果看上去就像前景物体的轮廓。        

**Tophat**:         `tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)`      
原始图像与进行开运算之后得到的图像的差。

**Blackhat**        `blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)`          
进行闭运算之后得到的图像与原始图像的差。


*The whole relationship is*:            
**Opening**:        `dst = open(src, kernel) = dilate(erode(src, kernel), kernel)`      
**Closing**:        `dst = close(src, kernel) = erode(dilate(src, kernel), kernel)`         
**Gradient**:       `dst = gradient(src, kernel) = dilate(src, kernel) - erode(src, kernel)`      
**Tophat**:         `dst = tophat(src, kernel) = src - open(src, kernel)`           
**Blackhat**        `dst = blackhat(src, kernel) = close(src, kernel) - src`        

