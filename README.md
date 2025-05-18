# mldeployment-cpe393

## Important!!!
Model training can found in [`model experiments.ipynb`](<model experiments.ipynb>)\
step 1-4 files are at [`step-4` branch](https://github.com/RONLUG/mldeployment-cpe393/tree/step-4#) \
Sorry for late submission ˙◠˙

---

## Installation
```bash
git clone https://github.com/RONLUG/mldeployment-cpe393.git
cd mldeployment-cpe393/app
```

### Install with Docker
```bash
docker build -t ml-model .
```
```bash
docker run -p 9000:9000 ml-model
# Or the command below to run and mount local directory
docker run -p 9000:9000 -v $(pwd):/app ml-model
```

## Test the API in new terminal
run:
```bash
curl -X POST http://localhost:9000/predict \
     -H "Content-Type: application/json" \
     -d '{"area": [300, 200], "stories": [2, 2], "bathrooms": [3, 1]}'
```

expected output:
```json
[{"predict_price":5373324.557230508},{"predict_price":2612353.46388657}]
```




