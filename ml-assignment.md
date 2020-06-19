Your ML assignment consists of 3 parts.

## Part I

Here's a link to the dataset you'll be working on.

http://academictorrents.com/details/99811ba62918f8e73791d21be29dcc372d660305

This is a dataset of `Fundus' images.

A fundus image is an image of the back of the eye (the retina) that is
taken with a specialized device known as a fundus camera.

Fundus images are key to the ophthalmology related AI
work we do here at Radical.

In all but the most high-end cameras, fundus images which
are manually taken by trained optometrists often have flaws
caused due to poor illumination, shot angles, and head movement.
These factors result in poor quality images which are not
useful.

The dataset we've linked to is a dataset of fundus images of different quality levels.

Your task in this section:

1. Read about fundus images from various sources (Wikipedia, aao.org, etc)
   in order to develop some domain knowledge about the subject.
2. Download the dataset and perform an Exploratory Data Analysis (EDA)
3. Try to identify, intuitively, by looking at the images, which factors
   contribute to an image being of "good" or "bad" quality.

## Part II

In this section, your aim will be to train a convolutional
network to classify an arbitrary fundus image as being of good
or bad quality. You must keep in mind the following guidelines:

1. You can use any framework (TF/Keras/PyTorch/etc).

   - We prefer PyTorch, but using TF/Keras will not count against you.

2. You must write the dataloader for your framework of choice, and implement
   appropriate pre-processing steps such as splitting, standardization,
   augmentation, etc.

3. You can use any classification architecture (VGG, ResNet, etc...)
   but you must write code implementing that architecture from scratch.
   You can use a standard model architecture such as ResNet, you're also
   free to use any variant that you wish (but you must code it yourself.)

   - For extra marks, if time permits, you can also implement certain tricks
     that aid model performance (cyclic LR scheduling, MixUp training, etc.)

4. The aim is not to maximize predictive power, but to present **well structured,
   modular, clearly written and well-documented code**.

5. Your training scripts must log metrics, losses, etc at regular intervals,
   possibly in the form of a graph. These will comprise part of the final
   submission.

6. For extra marks, you can implement hyperparameter tuning using any library
   of choice.

> Note: The dataset we've linked above is more of a toy than full fledged dataset.
> It is small enough to train on a laptop or on free resources such as
> Google Colab or Kaggle Notebooks.

## Part III

In the final section, you will be analyzing the model trained in the previous
part. Model explainability is of critical importance, especially in the
medical domain. It is very important to understand the failure modes of a
trained model.

In the section, you must:

1. Extract images from the test set on which your model gives incorrect results.
   These are the false positives and false negatives.

2. Use a technique such as (CAM, GradCAM, SIDU, etc...) to understand why
   the model gives incorrect results. The techniques mentioned above can
   often serve as a debugging aid -- given a model, an input and an output,
   these techniques identify which parts of the input most greatly contributed
   to the output.

   - For this task, you can use a library. For example, you will find GradCAM
     implementations for all popular frameworks.

   - For many extra marks, implement one such technique from scratch by
     following the paper and using it on the model you trained in Part II.

3. Run the explainability technique on some images which the model has predicted
   correctly. Does the output match your intuition (Part I, question 2)?

4. What factors lead to the model classifying some images incorrectly?

   - How would you attempt to improve your model to handle such cases?

5. This assignment has to be completed within a certain time-frame.

   - How would you improve the performance of your model given more time?

Your final submission will comprise any notebooks you've used for EDA, containing
any insights gleaned. Also included must by notebooks/scripts you've used to define
the model architecture, utility functions, training code, model weights etc.
For the analysis questions in Part III, a notebook is preferred but not mandatory.
