from fastai.vision.all import (
    load_learner,
    PILImage,
    Resize,
)
from fastai.vision.all import *
from fastai.vision.widgets import *
import glob
from random import shuffle
import urllib.request
import streamlit as st

# set app title
st.title("cactus")
# load model
path = Path()
learn_inf = load_learner(path/'resnet50.pkl', cpu=True)


def predict(img, learn):
    # make prediction
    pred, pred_idx, pred_prob = learn_inf.predict(img)
    # Display the prediction
    st.success(f"This is {pred}  with the probability of {pred_prob[pred_idx]*100:.02f}%")
    # Display the test image
    st.image(img, use_column_width=True)


##################################
# sidebar
##################################
# sidebar title
st.sidebar.write('### Enter cactus to classify')

# image source selection
option = st.sidebar.radio('', ['Use a validation image', 'Use your own image'])
valid_images = glob.glob('images/valid/*/*')
shuffle(valid_images)

if option == 'Use a validation image':
    st.sidebar.write('### Select a validation image')
    fname = st.sidebar.selectbox('',
                                 valid_images)

else:
    st.sidebar.write('### Select an image to upload')
    fname = st.sidebar.file_uploader('',
                                     type=['png', 'jpg', 'jpeg'],
                                     accept_multiple_files=False)
    if fname is None:
        fname = valid_images[0]

# open image
img = PILImage.create(fname)
# infer
predict(img, learn_inf)
