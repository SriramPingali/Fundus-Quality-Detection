# Introduction
The fundus of the eye is the interior surface of the eye opposite the lens and includes the retina, optic disc, macula, fovea, and posterior pole.
The fundus can be examined by ophthalmoscopy and/or fundus photography.

![FUNDUS](https://user-images.githubusercontent.com/43778095/85285966-6ed5c000-b4af-11ea-821d-7fd6964ada3d.png)

Medical signs that can be detected from observation of eye fundus (generally by funduscopy) include hemorrhages, exudates, cotton wool spots, 
blood vessel abnormalities (tortuosity, pulsation and new vessels) and pigmentation. Arteriolar constriction, seen as "silver wiring", and vascular 
tortuosities are seen in hypertensive retinopathy.The eye's fundus is the only part of the human body where the microcirculation can be observed directly. 

<img src="https://user-images.githubusercontent.com/43778095/85285964-6da49300-b4af-11ea-9ab8-59921b04ba63.png" width="500" height="350" tiile = "Anatomy">  <img src="https://user-images.githubusercontent.com/43778095/85285959-6c736600-b4af-11ea-9a4e-295d3daf1d61.png" width="250" height="250" title = "Blood Vessels">

In all but the most high-end cameras, fundus images which are manually taken by trained optometrists often have flaws caused due to poor illumination, shot angles,
and head movement. These factors result in poor quality images which are not useful.

## Good Image
<img src="https://user-images.githubusercontent.com/43778095/85287655-3be0fb80-b4b2-11ea-9f3f-548c954cba47.jpg" width="500" height="350">

## Bad Image
<img src="https://user-images.githubusercontent.com/43778095/85287697-469b9080-b4b2-11ea-85d9-a86728053b7d.jpg" width="500" height="350">

## Incorrect Positioning / Outliers
<img src="https://user-images.githubusercontent.com/43778095/85287721-51562580-b4b2-11ea-8e85-5b42240cd3f3.jpg" width="500" height="350">

This Repository experiments with automating the process of adjustment of the camera settings. 
We use the DRIMDB (Diabetic Retinopathy Image Database) dataset to classify fundus imagery into Good or Bad quality.

# Dependencies
  - Pytorch
  - numpy
  - sklearn
  - tqdm
  - gradcam
  - PIL
  - matplotlib
  
# Installation
  ```
  pip install torch
  pip install numpy
  pip install scikit-learn
  pip install tqdm
  pip install pytorch-gradcam
  pip install pillow
  pip install matplotlib
  ```
