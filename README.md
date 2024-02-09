# Sales Point Predict Service
THIS IS ENGLISH VERSION OF [THIS PORJECT](https://github.com/Won-Been/ai06project3?tab=readme-ov-file#sales-point%ED%8C%90%EB%A7%A4%EC%A7%80%EC%88%98-%EC%98%88%EC%B8%A1-%EC%84%9C%EB%B9%84%EC%8A%A4).

Information about folders and files
- flask_app: Flask app related file
- getdata: Data scrapping and building database
- Project3_model.ipynb: Train the model and save it
- point_predict.pickle: Sales point predict model

## What is this service for?
- To preidict the sales point by using rank of book, rating and genre.
  - Sales point information from Aladin(online bookstore in South Korea):

    ![스크린샷 2022-03-10 오전 11 29 07](https://user-images.githubusercontent.com/86759423/157576511-c6ba0f13-7926-4087-9734-7817770d64d0.png)
    - SalesPoint is Aladdin's unique sales index method that calculates the sales performance of a particular product based on sales quantity and sales duration.
    - Applied a weight to recent sales, with the score increasing as more units are sold and decreasing when sales are lower.
    - As a result, recent bestsellers receive high scores, and steady sellers maintain a certain level of points.
    - 'SalesPoint' is updated daily.

## Pipeline
![스크린샷 2022-03-10 오전 11 43 28](https://user-images.githubusercontent.com/86759423/157577987-c6939a37-3b70-4c86-8bc1-a31e2f9e2422.png)
1. Scrap the ranking, rating, genre data of bestsellers from Aladin
2. Build relational database
3. Train the Multi Linear Regression Model that predict the sales point
4. Create a local host by using Flask app and display a page that predicts sales point when entering book informations.

## Detailed process
1. Scrap the bestseller data

  ![스크린샷 2022-03-10 오후 1 24 02](https://user-images.githubusercontent.com/86759423/157589142-5d84d599-02b2-490a-a960-25dc17c646c7.png)
- Scrap the data with {Book id: [Ranking, Rating, Genre]} form.

1. Save data to DBeaver

  ![스크린샷 2022-03-10 오후 1 25 48](https://user-images.githubusercontent.com/86759423/157589298-a169525e-cad9-4c55-a057-8f3474c0a8aa.png)

3. Create Machin Learning model and deploy

  ![스크린샷 2022-03-10 오후 1 26 39](https://user-images.githubusercontent.com/86759423/157589393-f8614851-8643-49ec-9816-f3d5badacb0a.png)
- Build a model to predict Sales Point using a multiple linear regression model.
- Connect the model to a local host and displaying a page where entering rankings, ratings, and genres predicts the Sales Point.


## Results

https://user-images.githubusercontent.com/86759423/157589016-0c67aa9f-9412-4bd2-a989-6504312d1747.mov

------------------------------------------------------
## Additional
## Analytical dashboards using Metabase
- Used Docker

  ![스크린샷 2022-03-10 오후 1 30 45](https://user-images.githubusercontent.com/86759423/157589819-f8d15cde-3501-42b0-ba2a-44c0feff75be.png)
  ![스크린샷 2022-03-10 오후 1 33 33](https://user-images.githubusercontent.com/86759423/157590128-0ad642c0-b40e-4f17-a584-705f9b2d3a39.png)



