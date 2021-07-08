
# Wiki Degrees

Wiki° is a site written in python/Flask to try and find how many clicks it would take you to get from one Wikipedia page to another only clicking the first link in the body. I hope to show how connected Wikipedia is.


## Demo

![Alt Text](https://media.giphy.com/media/AhcQfI0fUspwhtM3ht/giphy.gif)

  
## Run Locally

Clone the project

```bash
  git clone https://github.com/shaunnnorton/Degrees-Of-Wiki.git
```

Go to the project directory

```bash
  cd Degrees-Of-Wiki
```

Install dependencies

```bash
  pip install requirements.txt
```

Set Environment Variables 

```
touch .env
echo "SECRET_KEY={YOURSECRETKEY}" >> .env
echo "SQLALCHEMY_DATABASE_URI=sqlite:///database.db" >> .env
```

Start the server

```bash
  python3 app.py
```

  
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY`

`SQLALCHEMY_DATABASE_URI`

  
## FAQ

#### Why is my query not in the recent queries

If a query results in a deadend or goes longer than 1000 links it will not save to the database so it can try again the next time it is queried.

#### Why did it skip a link

A link will be skipped if it redirects to another Wiki or if it is a link to one of Wikipedia's own urls.

  
## Authors

- [@shaunnorton](https://www.github.com/shaunnnorton)

  
## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://snorton.dev/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shaun-norton-2731b8162/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/Shaunnorton72)

  