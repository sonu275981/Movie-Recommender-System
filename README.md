
# Movie Recommender System

Content Based Recommender System recommends movies similar to the movie user likes and analyses the sentiments on the reviews given by the user for that movie.

The details of the movies(title, genre, runtime, rating, poster, etc) are fetched using an API by TMDB, https://www.themoviedb.org/documentation/api, and using the IMDB id of the movie in the API, I have Download this data from kaggle to get the reviews given by the user in the IMDB site and performed sentiment analysis on those reviews.

Check out the live demo: https://movies275.herokuapp.com/

## Note

Use this URL - https://share.streamlit.io/sonu275981/movie-recommender-system/main/app.py - in case if you see application error in the above mentioned URL

## Movie Recommender System

I've developed a similar application called **Movie Recommender System** which supports all language movies. But the only thing that differs from this application is that I've used the TMDB's recommendation engine in "Movie Recommender System". The recommendation part developed by me in this application doesn't support for multi-language movies as it consumes 200% of RAM (even after deploying it to Heroku) for generating Count Vectorizer matrix for all the 5000+ movies in the TMDB.

Don't worry if the movie that you are looking for is not auto-suggested. Just type the movie name and click on "enter". You will be good to go eventhough if you made some typo errors.

## How to get the API key?

Create an account in https://www.themoviedb.org/, click on the ```API``` link from the left hand sidebar in your account settings and fill all the details to apply for API key. If you are asked for the website URL, just give "NA" if you don't have one. You will see the API key in your ```API``` sidebar once your request is approved.

## How to run the project?

- Clone or download this repository to your local machine.
- Install all the libraries mentioned in the requirements.txt file with the command ```pip install -r requirements.txt```
- Get your API key from https://www.themoviedb.org/. (Refer the above section on how to get the API key).
- Replace **YOUR_API_KEY** in both the places of **MY_KEY** and hit save.
- Open your terminal/command prompt from your project directory and run the file app.py by executing the command **streamlit run app.py**.
- Go to your browser and type http://localhost:8501/ in the address bar.
- Hurray! That's it.

## Architecture

![App Screenshot](https://github.com/sonu275981/Movie-Recommender-System/blob/dbe8dbd5a82bc815025e93b5f7759c34b04cb330/image.png?raw=true)

## Similarity Score 

How does it decide which item is most similar to the item user likes? Here we use the similarity scores.

It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the text details of both of the items. So, similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.

## How Cosine Similarity works?

Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.

![App Screenshot](https://github.com/sonu275981/Movie-Recommender-System/blob/95c0cb2990f7a1e1d03e5cf56679d9dbad35b45d/cosine.png?raw=true)

 More about Cosine Similarity [Understanding the Math behind Cosine Similarity](https://www.machinelearningplus.com/nlp/cosine-similarity/)

 ### Sources of the datasets
 - [IMDB 5000 Movie Dataset](https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset)

 




## APP Screenshots

- App UI

![App Screenshot](https://github.com/sonu275981/Movie-Recommender-System/blob/408c53c17f4089b1aee5032617187babbf0e2cca/movie_recommender/sample_1.png?raw=true)

- App working 

![App Screenshot](https://github.com/sonu275981/Movie-Recommender-System/blob/408c53c17f4089b1aee5032617187babbf0e2cca/movie_recommender/sample_2.png?raw=true)

- App working

![App Screenshot](https://github.com/sonu275981/Movie-Recommender-System/blob/408c53c17f4089b1aee5032617187babbf0e2cca/movie_recommender/sample_3.png?raw=true)










## Support

For an support, email sonu.chaurasia76@gmail.com or comment here.




