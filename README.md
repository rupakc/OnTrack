# OnTrack
Train Delay Prediction Using Python and React

## Vision

Delay of trains in the Indian Railway network is a pertinent and persistent issue, inordinate delays often cause a lot of trouble and harrassment to passengers and authorities alike. While it won't be possible for a system to predict all train delays accurately because of the multitude of covariates and latent factors involved, an attempt has been made to predict the likely delay in a train's journey using <b> Machine Learning (Extra Trees Regressor) </b> to be more rigorous.

Given the recent hoopla around data privacy and interpretable ML, we have developed the system to be self-explaning (i.e. it explains each of its predictions. We have used <b> LIME (Locally Interpretable Model Agnostic Explanations) </b> which is a local explainer with high fidelity.

## System Architecture

![architecture image][logo]

[logo]: https://github.com/rupakc/OnTrack/blob/main/Frontend/static/resources/architecture.PNG "System Data Flow"

The modular nature of the application enables one to develop the backend and frontend independently of each other. They run on different server hence can be hosted on any geographically distributed network architecture.

The backend is superpowered by <b> Django </b> and uses the best of Machine Learning in Python. <b> MongoDB </b> is our database of choice, although we could have used any other SQL or NoSQL db to store the station and train information and metadata.

The exciting part of the project is the frontend which employs one of the best frontend frameworks in existence. It consists of the following - 

- <b> React </b>
- <b> React Bootstrap </b>
- <b> Webpack </b>

