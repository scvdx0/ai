```
conda create --name py11 python=3.11
conda create --clone py11 --name mlops
conda activate mlops
conda install 'mlflow[pipelines]'
```