## oh crud
quick Github OAuth CRUD


### install steps
```
git clone https://github.com/NULL-OPERATOR/oh_crud.git
cd oh_crud
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

follow this guide to setup your github ouath app    

https://developer.github.com/apps/building-oauth-apps/creating-an-oauth-app/

update these in example_config.py
```
GITHUB_OAUTH_CLIENT_ID = 'your id'   
GITHUB_OAUTH_CLIENT_SECRET = 'your key'   
```

then rename it to config.py (ignored by git)

```
mv example_config.py config.py
```

export this for running github oauth on localhost:
```
export OAUTHLIB_INSECURE_TRANSPORT=1
```

then run the app
```
python run.py
```


```
open http://127.0.0.1:5000/
```

to run tests
```
python tests.py
```


### other bits

#### how it looks


![alt text](app_in_use.png)

#### editing models

flask db init # once   
flask db migrate   
flask db upgrade   
