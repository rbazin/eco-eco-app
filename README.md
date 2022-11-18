# Eco Eco, the gamified environmental app

This project is about creating a mobile application engaging people to reduce their daily carbon emissions. This happens in the context of the human-computer interraction course at McGill University.

## How to use

To install the depencies for the frontend of the app, clone the repository and use the following commands (this requires to have the yarn packet manager installed) :
```bash
cd eco-eco-app
cd frontend
yarn install
```

Then to see the app in your browser (press f12 to resize to a mobile screen size), use the command :
```bash
yarn serve
```

To install the depedencies for the backend :
```bash
cd eco-eco-app
cd backend
pip install -r requirements.txt
```

Then to serve the backend locally, go back to the root folder and do :
```bash
flask --app backend run
```
