# Logistic regression model deployed with Flask

If you are using anaconda you can just run `debug.bat` or `debug.sh`.

Alternatively just run this command in the terminal:

```
flask run
```

Goto `http://localhost:5000` in the browser.

## Deployment

The app is deployed [here](https://the-logistic-regression-app.herokuapp.com/obesity).

The API is here:

```
https://the-logistic-regression-app.herokuapp.com/api/obesity?height=170&weight=60
```

## Useful links:

* https://www.jcchouinard.com/deploy-a-flask-app-on-heroku/

Deploy commands:

```
conda create --name logic-regression-with-flask python=3.9.7
conda activate logic-regression-with-flask
```

