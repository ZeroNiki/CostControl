# Test (via curl)

```sh
curl -X {GET/POST/PUT/DELETE} http://127.0.0.1:8000/api/{transaction/categories} \
-H "Authorization: Bearer JWT_TOKEN"
```

# Test (via swagger ui)
go to `http://127.0.0.1:8000/api/docs`

go to `Authentication` `/api/register`. Register new user

```json 
{
  "Message": "User registered successfully!",
  "Refresh": "smth",
  "Access": "smth"
}
```

copy `Access` token. Click on the button `Authorize` and paste token into `value`

