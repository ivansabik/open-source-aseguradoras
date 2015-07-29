Toolkit para CUSF y LISF de aseguradoras
=======================

Python para cálculos actuariales y estadísticas

### Notebooks Python

- [Análisis control médico](http://nbviewer.ipython.org/github/mandroslabs/toolkit-aseguradoras/blob/master/ipython%20notebooks/An%C3%A1lisis%20control%20m%C3%A9dico.ipynb)
- [Cálculo PNNx con vectores](http://nbviewer.ipython.org/github/mandroslabs/toolkit-aseguradoras/blob/master/ipython%20notebooks/C%C3%A1lculo%20PNNx%20con%20vectores.ipynb)
- [Cálculo PNNx](http://nbviewer.ipython.org/github/mandroslabs/toolkit-aseguradoras/blob/master/ipython%20notebooks/C%C3%A1lculo%20PNNx.ipynb)
- [Preguntas de exploración ramo Salud](http://nbviewer.ipython.org/github/mandroslabs/toolkit-aseguradoras/blob/master/ipython%20notebooks/Preguntas%20de%20exploraci%C3%B3n%20ramo%20Salud.ipynb)
- [Cálculo de triángulos SONR](http://nbviewer.ipython.org/github/mandroslabs/toolkit-aseguradoras/blob/master/ipython%20notebooks/Tri%C3%A1ngulos%20SONR.ipynb)

### MapReduce

En consola

```cat deudores.txt | ./mapper_deudores_prima.py | sort | ./reducer_deudores_prima.py```

En pig modo local

```pig -x local deudores.pig```




