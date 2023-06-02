pip install numpy
pip install tqdm
pip install dill
pip install pandas
pip install ./torch-1.7.1+cu110-cp37-cp37m-linux_x86_64.whl
pip install nltk
conda install icu pkg-config
CFLAGS="-std=c++11" pip install ICU-Tokenizer
pip install transformers
pip install toolz
pip install cytoolz
pip install hyperopt
pip install scikit-learn
pip install prefetch_generator
pip install allrank --no-dependencies
pip install ./torchvision-0.8.2+cu110-cp37-cp37m-linux_x86_64.whl
pip install gcsfs
python run.py --config ./config/amazon/home.json --stage train