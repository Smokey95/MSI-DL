# MNIST Datensatz

Der MNSIT Datensatz besteht aus handgeschriebenen Ziffern von 0 bis 9. Er enthält insgesamt 70.000 Bilder, die in 60.000 Trainingsbilder und 10.000 Testbilder aufgeteilt sind. Jedes Bild ist ein Graustufenbild mit einer Auflösung von 28x28 Pixeln.

## Download
Der MNIST Datensatz kann von der offiziellen Webseite [http://yann.lecun.com/exdb/mnist/](http://yann.lecun.com/exdb/mnist/) heruntergeladen werden. Alternativ kann der Datensatz auch über [https://www.kaggle.com/datasets/hojjatk/mnist-dataset](https://www.kaggle.com/datasets/hojjatk/mnist-dataset) bezogen werden.

## Verzeichnisstruktur
Nach dem Herunterladen und Entpacken des MNIST Datensatzes sollte dieses Verzeichnis folgende Struktur aufweisen:

```
data/MNIST/
├── train-images-idx3-ubyte
├── train-labels-idx1-ubyte
├── t10k-images-idx3-ubyte
└── t10k-labels-idx1-ubyte
```
- `train-images-idx3-ubyte`: Enthält die Trainingsbilder.
- `train-labels-idx1-ubyte`: Enthält die Labels (Ziffern) für die Trainingsbilder.
- `t10k-images-idx3-ubyte`: Enthält die Testbilder.
- `t10k-labels-idx1-ubyte`: Enthält die Labels (Ziffern) für die Testbilder.
