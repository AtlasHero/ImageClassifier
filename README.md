# sgi_2020_classifier
## Data Labeling 

Data is stored in the folder ```assets/```. Labels for each file are stored in ```fire_data_csv```.
## Requirements for new Data
+ put the new data into a new folder in ```assets/```. 
+ make sure there is no text annotation visible. Otherwise skip the label. 
+ extend the existing csv with your new labeled data. 
+ We do binary classification please label your data with ```fire``` and ```no_fire```

# Scrapping the ```fire_database```
 + Run the Jupyter Notepook ScrapeDatabase
 
# Setting up GAN from Zalando Research
+ follow installation instructions of lasagne and Theano on: https://lasagne.readthedocs.io/en/latest/user/installation.html#bleeding-edge-version
+ Make sure OpenBLAS is installed: Try installing it vie ```conda install -c menpo openblas```
+ add ````conda install numpy scipy mkl-service libpython m2w64-toolchain````