This is a flask checkpoint project made for the code bullet discord servers 2020 puzzle hunt.
Done in python flask, bootstrap, and jquery.

I used a dockerfile to setup my dev env to use simply build the docker file

docker build -t cbsite .

And then run it with

docker run -d -p 80:80 cbsite