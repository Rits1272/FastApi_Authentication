# FastApi_Authentication
A ready to use authentication system devekoped using FastAPI framework

This code exposes the following endpoints:
 - `/api/register/`
 - `/api/login/`
 
 To test **register** api:
 - ```bash
      curl -X POST "http://localhost:8000/api/register/?username={USERNAME}&password={PASSWORD}" -H  "accept: application/json" -d ""```
 
 To test **login** api:
 - ```bash
    curl -X POST "http://localhost:8000/api/login/?username={USERNAME}&password={PASSWORD}" -H  "accept: application/json" -d ""```
