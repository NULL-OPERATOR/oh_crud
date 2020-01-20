## crud
quick Github OAuth CRUD


### install steps
```
git clone https://github.com/NULL-OPERATOR/crud.git
cd crud
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```



setup app    

https://developer.github.com/apps/building-oauth-apps/creating-an-oauth-app/


export OAUTHLIB_INSECURE_TRANSPORT=1

flask db init

flask db migrate
flask db upgrade
