# flask-boilerplate
Flask boilerplate using the application factory with basic authentication.

## Installation

### Clone the repository

```
git clone https://github.com/onosendi/flask-boilerplate.git
```

### Change directory into flask-boilerplate

```
cd flask-boilerplate
```

### Create your virtual environment

```
python3 -m venv venv
```

### Enter your virtual environment

```
source venv/bin/activate
```

### Install Python dependencies

```
pip install -r requirements.txt
```

### Apply migrations to database

```
flask db upgrade
```

### NPM

#### Install dependencies

```
npm install
```

#### Bundle

##### For production

```
npm run build
```

##### For development

```
npm start
```

### Run Flask

If you are running `npm start` for development, run Flask in a separate terminal so both servers are running.

```
flask run
```

Now visit `localhost:5000` in your browser.
