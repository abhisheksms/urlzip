# url-shortener

A URL Shortening service

Steps to setup


1. To setup the project, we perform the following steps, we would require docker compose for this setup
   ```shell
      $ git clone https://github.com/abhisheksms/url-shortener.git
      $ cd url-shortener
      $ docker-compose up --build
    ```

2. We will now shorten the URL by using the following command
   ```shell
      curl -X GET 'http://localhost:8000/shorten?url=https://www.formula1.com'
   ```
   Or we can visit this URL 'http://localhost:8000/shorten?url=https://www.formula1.com'

   We would get http://localhost:8000/4lEkWTr
   Clicking on the shortened URL will redirect us to the original site
   

3. To run the tests, we can use the following
    ```shell
      $ docker-compose run --rm fastapi pytest -rA
    ```

