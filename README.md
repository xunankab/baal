# Ba’al

> Cosa, objeto. Thing, object.

## Links

- [XunanKab Google Drive](https://drive.google.com/drive/folders/10E7w4uWseHjPriCD1uFH_HESddpgBeF2?usp=sharing)
- [XunanKab Architecture Device](https://docs.google.com/document/d/1KC5pMvnQGR6Q5Isv04f09mMQqSTflUg_0u5NQQDns00/edit?usp=sharing)

## REST API

```
curl -H "Content-Type: application/json" -X POST -d '{"address":"127.0.0.1","port":"5600"}' http://127.0.0.1:5000/api/server
curl http://127.0.0.1:5000/api/server

curl -H "Content-Type: application/json" -X POST -d '{"enable":"True"}' http://127.0.0.1:5000/api/stream
curl http://127.0.0.1:5000/api/stream

curl -H "Content-Type: application/json" -X POST -d '{"enable":"False"}' http://127.0.0.1:5000/api/stream
curl http://127.0.0.1:5000/api/stream
```
